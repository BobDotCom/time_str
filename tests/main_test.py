import pytest, time_str, datetime


@pytest.fixture
def converter():
    '''Returns a converter'''
    return time_str.convert

@pytest.mark.parametrize("day,month,year,expected_days", [
    (1, 2, 3, 1158),
    (3, 2, 1, 430),
])
def test_conversions(converter, day, month, year, expected_days):
    assert expected_days == day + (31 * month) + (365 * year)
    assert converter(f'{day} d {month} months {year} yrs') == datetime.timedelta(days=expected_days)
