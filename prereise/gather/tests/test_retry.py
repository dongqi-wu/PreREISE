import pytest

from prereise.gather.request_util import retry


class CustomException(Exception):
    pass


def test_max_times_reached():
    @retry(retry_count=8, allowed_exceptions=CustomException)
    def no_fail(x=[]):
        x.append(len(x))
        raise CustomException()

    counts = []
    no_fail(counts)
    assert len(counts) == 8


def test_return_value():
    @retry()
    def return_something():
        return 42

    assert 42 == return_something()


def test_must_be_called():
    @retry
    def not_fully_decorated():
        return 42

    with pytest.raises(TypeError):
        not_fully_decorated()


def test_unhandled_exception():
    @retry()
    def fail():
        raise Exception()

    with pytest.raises(Exception):
        fail()
