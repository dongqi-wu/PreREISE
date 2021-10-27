mile_to_meter = 1609.34
meter_to_mile = 1.0 / mile_to_meter

# contiguous state
abv2state = {
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
}

abv_state_neighbor = {
    "AL": ["FL", "GA", "MS", "TN"],
    "AZ": ["CA", "CO", "NV", "NM", "UT"],
    "AR": ["LA", "MS", "MO", "OK", "TN", "TX"],
    "CA": ["AZ", "NV", "OR"],
    "CO": ["AZ", "KS", "NE", "NM", "OK", "UT", "WY"],
    "CT": ["MA", "NY", "RI"],
    "DE": ["MD", "NJ", "PA"],
    "FL": ["AL", "GA"],
    "GA": ["AL", "FL", "NC", "SC", "TN"],
    "ID": ["MT", "NV", "OR", "UT", "WA", "WY"],
    "IL": ["IN", "IA", "MI", "KY", "MO", "WI"],
    "IN": ["IL", "KY", "MI", "OH"],
    "IA": ["IL", "MN", "MO", "NE", "SD", "WI"],
    "KS": ["CO", "MO", "NE", "OK"],
    "KY": ["IL", "IN", "MO", "OH", "TN", "VA", "WV"],
    "LA": ["AR", "MS", "TX"],
    "ME": ["NH"],
    "MD": ["DE", "PA", "VA", "WV"],
    "MA": ["CT", "NH", "NY", "RI", "VT"],
    "MI": ["IL", "IN", "MN", "OH", "WI"],
    "MN": ["IA", "MI", "ND", "SD", "WI"],
    "MS": ["AL", "AR", "LA", "TN"],
    "MO": ["AR", "IL", "IA", "KS", "KY", "NE", "OK", "TN"],
    "MT": ["ID", "ND", "SD", "WY"],
    "NE": ["CO", "IA", "KS", "MO", "SD", "WY"],
    "NV": ["AZ", "CA", "ID", "OR", "UT"],
    "NH": ["ME", "MA", "VT"],
    "NJ": ["DE", "NY", "PA"],
    "NM": ["AZ", "CO", "OK", "TX", "UT"],
    "NY": ["CT", "MA", "NJ", "PA", "RI", "VT"],
    "NC": ["GA", "SC", "TN", "VA"],
    "ND": ["MN", "MT", "SD"],
    "OH": ["IN", "KY", "MI", "PA", "WV"],
    "OK": ["AR", "CO", "KS", "MO", "NM", "TX"],
    "OR": ["CA", "ID", "NV", "WA"],
    "PA": ["DE", "MD", "NJ", "NY", "OH", "WV"],
    "RI": ["CT", "MA", "NY"],
    "SC": ["GA", "NC"],
    "SD": ["IA", "MN", "MT", "NE", "ND", "WY"],
    "TN": ["AL", "AR", "GA", "KY", "MS", "MO", "NC", "VA"],
    "TX": ["AR", "LA", "NM", "OK"],
    "UT": ["AZ", "CO", "ID", "NV", "NM", "WY"],
    "VT": ["MA", "NH", "NY"],
    "VA": ["KY", "MD", "NC", "TN", "WV"],
    "WA": ["ID", "OR"],
    "WV": ["KY", "MD", "OH", "PA", "VA"],
    "WI": ["IL", "IA", "MI", "MN"],
    "WY": ["CO", "ID", "MT", "NE", "SD", "UT"],
}

blob_paths = {
    "eia_form860_2019_generator": "https://besciences.blob.core.windows.net/datasets/EIA_Form860/3_1_Generator_Y2019_Operable.csv",
    "eia_form860_2019_plant": "https://besciences.blob.core.windows.net/datasets/EIA_Form860/2___Plant_Y2019.csv",
    "epa_ampd": "https://besciences.blob.core.windows.net/datasets/EPA_AMPD/",
    "epa_needs": "https://besciences.blob.core.windows.net/datasets/EPA_NEEDS/needs-v620_06-30-21-2_active.csv",
    "substations": "https://besciences.blob.core.windows.net/datasets/hifld/Electric_Substations_Jul2020.csv",
    "transmission_lines": "https://besciences.blob.core.windows.net/datasets/hifld/Electric_Power_Transmission_Lines_Jul2020.geojson.zip",
}
eia_epa_crosswalk_path = "https://raw.githubusercontent.com/Breakthrough-Energy/camd-eia-crosswalk/master/epa_eia_crosswalk.csv"

volt_class_defaults = {
    "UNDER 100": 69,
    "220-287": 230,
    "345": 345,
    "500": 500,
}

line_reactance_per_mile = {  # per-unit
    69: 0.0096,
    100: 0.0063,
    115: 0.0039,
    138: 0.0026,
    161: 0.0021,
    230: 0.0011,
    345: 0.0005,
    500: 0.0002,
    765: 0.0001,
}
line_rating_short = {  # MVA
    69: 86,
    100: 181,
    115: 239,
    138: 382,
    161: 446,
    230: 797,
    345: 1793,
    500: 2598,
    765: 5300,
}
line_rating_short_threshold = 50  # miles
line_rating_surge_impedance_loading = {  # MVA
    69: 13,
    100: 30,
    115: 35,
    138: 50,
    161: 69,
    230: 140,
    345: 375,
    500: 1000,
    765: 2250,
}
line_rating_surge_impedance_coefficient = 43.261
line_rating_surge_impedance_exponent = -0.6678

transformer_reactance = {  # per-unit
    (69, 115): 0.14242,
    (69, 138): 0.10895,
    (69, 161): 0.14943,
    (69, 230): 0.09538,
    (69, 345): 0.08896,
    (115, 161): 0.04516,
    (115, 230): 0.04299,
    (115, 345): 0.04020,
    (115, 500): 0.06182,
    (138, 161): 0.02818,
    (138, 230): 0.03679,
    (138, 345): 0.03889,
    (138, 500): 0.03279,
    (138, 765): 0.02284,
    (161, 230): 0.06539,
    (161, 345): 0.03293,
    (161, 500): 0.06978,
    (230, 345): 0.02085,
    (230, 500): 0.01846,
    (230, 765): 0.01616,
    (345, 500): 0.01974,
    (345, 765): 0.01625,
    (500, 765): 0.00436,
}
transformer_rating = 800  # MVA

eia_storage_gen_types = {
    "Batteries",
    "Flywheels",
}

nercregion2interconnect = {
    "ASCC": "Alaska",  # Not currently used
    "HICC": "Hawaii",  # Not currently used
    "MRO": "Eastern",
    "NPCC": "Eastern",
    "RFC": "Eastern",
    "SERC": "Eastern",
    "TRE": "ERCOT",
    "WECC": "Western",
}

interconnect2state = {
    "Eastern": {
        "AL",
        "AR",
        "CT",
        "DE",
        "FL",
        "GA",
        "IA",
        "IL",
        "IN",
        "KS",
        "KY",
        "LA",
        "MA",
        "MD",
        "ME",
        "MI",
        "MN",
        "MO",
        "MS",
        "NC",
        "ND",
        "NE",
        "NH",
        "NJ",
        "NY",
        "OH",
        "OK",
        "PA",
        "RI",
        "SC",
        "TN",
        "VA",
        "VT",
        "WI",
        "WV",
    },
    "ignore": {"AK", "HI"},
    "split": {"MT", "SD", "TX"},
    "Western": {"AZ", "CA", "CO", "ID", "NM", "NV", "OR", "UT", "WA", "WY"},
}

state_county_splits = {
    "MT": {
        "default": "Western",
        "Eastern": {
            "CARTER",
            "CUSTER",
            "DANIELS",
            "DAWSON",
            "FALLON",
            "GARFIELD",
            "MCCONE",
            "PHILLIPS",
            "POWDER RIVER",
            "PRAIRIE",
            "RICHLAND",
            "ROOSEVELT",
            "ROSEBUD",
            "SHERIDAN",
            "VALLEY",
            "WIBAUX",
        },
    },
    "NM": {
        "default": "Western",
        "Eastern": {"CURRY", "LEA", "QUAY", "ROOSEVELT", "UNION"},
    },
    "SD": {"default": "Eastern", "Western": {"BUTTE", "FALL RIVER", "LAWRENCE"}},
    "TX": {
        "default": "ERCOT",
        "Eastern": {
            "BAILEY",
            "BOWIE",
            "CAMP",
            "CASS",
            "COCHRAN",
            "DALLAM",
            "DONLEY",
            "GAINES",
            "GREGG",
            "HALE",
            "HANSFORD",
            "HARDIN",
            "HARRISON",
            "HARTLEY",
            "HEMPHILL",
            "HOCKLEY",
            "HUTCHINSON",
            "JASPER",
            "JEFFERSON",
            "LAMB",
            "LIBERTY",
            "LIPSCOMB",
            "LUBBOCK",
            "LYNN",
            "MARION",
            "MOORE",
            "MORRIS",
            "NEWTON",
            "OCHLTREE",
            "ORANGE",
            "PANOLA",
            "PARMER",
            "POLK",
            "RANDALL",
            "SABINE",
            "SAN AUGUSTINE",
            "SAN JACINTO",
            "SHELBY",
            "SHERMAN",
            "TERRY",
            "TRINITY",
            "TYLER",
            "UPSHUR",
            "WALKER",
            "YOAKUM",
        },
        "Western": {"EL PASO", "HUDSPETH"},
    },
}

heat_rate_estimation_columns = [
    "ORISPL_CODE",
    "UNITID",
    "GLOAD (MW)",
    "HEAT_INPUT (mmBtu)",
]

fuel_prices = {  # EIA Annual Energy Outlook, values for 2022, $/MMBTu (2020 USD)
    "BIT": 2.02,  # BITuminous coal
    "DFO": 17.85,  # Distillate Fuel Oil
    "JF": 11.41,  # Jet Fuel
    "KER": 11.41,  # KERosene
    "LIG": 2.02,  # LIGnite coal
    "NG": 3.60,  # Natural Gas
    "NUC": 0.69,  # NUClear (uranium)
    "PC": 2.02,  # Petroleum Coke
    "PG": 15.43,  # Propane (Gaseous)
    "RC": 2.02,  # Residual Coal
    "RFO": 9.75,  # Residual Fuel Oil
    "SUB": 2.02,  # SUB-bituminous coal
    "WC": 2.02,  # Waste Coal
}

# Values from EPA's Power Sector Modeling Platform v6 - Summer 2021 Reference Case
reasonable_heat_rates_size_cutoffs = {
    ("Natural Gas Fired Combustion Turbine", "GT"): 80,
    ("Petroleum Liquids", "GT"): 80,
    ("Petroleum Liquids", "IC"): 5,
}
reasonable_heat_rates_by_type = {
    ("Conventional Steam Coal", "ST"): (8.3, 14.5),
    ("Natural Gas Fired Combined Cycle", "CA"): (5.5, 15.0),
    ("Natural Gas Fired Combined Cycle", "CS"): (5.5, 15.0),
    ("Natural Gas Fired Combined Cycle", "CT"): (5.5, 15.0),
    ("Natural Gas Internal Combustion Engine", "IC"): (8.7, 18.0),
    ("Natural Gas Steam Turbine", "ST"): (8.3, 14.5),
    ("Petroleum Coke", "ST"): (8.3, 14.5),
    ("Petroleum Liquids", "CA"): (6.0, 15.0),
    ("Petroleum Liquids", "CT"): (6.0, 15.0),
    ("Petroleum Liquids", "ST"): (8.3, 14.5),
}
reasonable_heat_rates_by_type_and_size = {
    ("Natural Gas Fired Combustion Turbine", "GT", "small"): (8.7, 36.8),
    ("Natural Gas Fired Combustion Turbine", "GT", "large"): (8.7, 18.7),
    ("Petroleum Liquids", "GT", "small"): (6.0, 36.8),
    ("Petroleum Liquids", "GT", "large"): (6.0, 25.0),
    ("Petroleum Liquids", "IC", "small"): (8.7, 42.5),
    ("Petroleum Liquids", "IC", "large"): (8.7, 20.5),
}

heat_rate_assumptions = {
    "Conventional Hydroelectric": 0,
    "Geothermal": 0,
    "Hydroelectric Pumped Storage": 0,
    "Nuclear": 10.5,  # From EIA's Electric Power Annual 2019, Table 8.1
    "Offshore Wind Turbine": 0,
    "Onshore Wind Turbine": 0,
    "Solar Photovoltaic": 0,
    "Solar Thermal with Energy Storage": 0,
    "Solar Thermal without Energy Storage": 0,
}

# These lines were manually identified based on a combination of: their 'TYPE'
# classification, their substation names, and their geographical paths. The capacities
# for each line were compiled from a variety of public sources.
dc_line_ratings = {  # MW
    108354: 500,  # Square Butte
    113313: 660,  # Neptune Cable
    131914: 2000,  # Quebec – New England Transmission (Ayer to Monroe)
    150123: 1000,  # CU
    157627: 330,  # Cross-Sound Cable
    157629: 660,  # Hudson Project
    158515: 2000,  # Quebec – New England Transmission (Quebec to Monroe)
    200823: 3100,  # Pacific DC Intertie (Path 65)
    308464: 2400,  # Intermountain Power Project (Path 27)
    310053: 400,  # Trans-Bay Cable
    311958: 5,  # Alamogordo Solar Energy Center
}

powersimdata_column_defaults = {
    "branch": {
        "rateB": 0,
        "rateC": 0,
        "angle": 0,
        "status": 1,
        "angmin": 0,
        "angmax": 0,
        "Pf": 0,
        "Qf": 0,
        "Pt": 0,
        "Qt": 0,
        "mu_Sf": 0,
        "mu_St": 0,
        "mu_angmin": 0,
        "mu_angmax": 0,
    },
    "gencost": {"type": 2, "startup": 0, "shutdown": 0, "n": 3},
    "plant": {
        "Pg": 0,
        "Qg": 0,
        "Qmax": 0,
        "Qmin": 0,
        "Vg": 1,
        "mBase": 1000,
        "status": 1,
        "Pc1": 0,
        "Pc2": 0,
        "Qc1min": 0,
        "Qc1max": 0,
        "Qc2min": 0,
        "Qc2max": 0,
        "ramp_agc": 0,
        "ramp_10": 0,
        "ramp_30": 0,
        "ramp_q": 0,
        "apf": 0,
        "mu_Pmax": 0,
        "mu_Pmin": 0,
        "mu_Qmax": 0,
        "mu_Qmin": 0,
    },
}