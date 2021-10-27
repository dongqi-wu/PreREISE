import os
import shutil

from prereise.gather.griddata.hifld.const import powersimdata_column_defaults
from prereise.gather.griddata.hifld.data_process.generators import build_plant
from prereise.gather.griddata.hifld.data_process.transmission import (
    build_transmission,
    create_buses,
)


def create_csvs(output_folder):
    """Process HIFLD source data to CSVs compatible with PowerSimData.

    :param str output_folder: directory to write CSVs to.
    """
    # Process grid data from original sources
    branch, substation = build_transmission()
    bus = create_buses(branch)
    plant = build_plant(bus, substation)

    outputs = {}
    outputs["branch"] = branch
    outputs["sub"] = substation
    # Separate tables as necessary to match PowerSimData format
    # bus goes to bus and bus2sub
    outputs["bus2sub"] = bus["sub_id"].to_frame()
    outputs["bus"] = bus.drop("sub_id", axis=1)
    # plant goes to plant and gencost
    outputs["gencost"] = plant[["c0", "c1", "c2"]].copy()
    outputs["plant"] = plant.drop(["c0", "c1", "c2"], axis=1)

    # Fill in missing column values
    for name, defaults in powersimdata_column_defaults.items():
        outputs[name] = outputs[name].assign(**defaults)

    # Save files
    os.makedirs(output_folder, exist_ok=True)
    for name, df in outputs.items():
        df.to_csv(os.path.join(output_folder, f"{name}.csv"))
    # The zone file gets copied directly
    zone_path = os.path.join(os.path.dirname(__file__), "data", "zone.csv")
    shutil.copyfile(zone_path, os.path.join(output_folder, "zone.csv"))
