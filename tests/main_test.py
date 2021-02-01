import pytest
import time_str
import datetime
import random


test = (random.randrange(0,61),random.randrange(0,61),random.randrange(0,25),random.randrange(0,366),random.randrange(0,5),random.randrange(0,13),random.randrange(0,100))
tests = [test for _ in range(1000)]

@pytest.fixture
def converter():
    '''Returns a converter'''
    return time_str.convert

@pytest.mark.parametrize("second,minute,hour,day,week,month,year", tests)
def test_conversions(converter, second, minute, hour, day, week, month, year,):
    assert converter(f"{second} {random.choice(['seconds', 'second', 'secs', 'sec', 's'])} {minute} {random.choice(['minutes', 'minute', 'mins', 'min', 'm'])} {hour} {random.choice(['hours', 'hour', 'hrs', 'hr', 'h'])} {day} {random.choice(['days', 'day', 'dys', 'dy', 'd'])} {week} {random.choice(['weeks', 'week', 'wks', 'wk', 'w'])} {month} {random.choice(['months', 'month', 'mons', 'mon', 'mn'])} {year} {random.choice(['years', 'year', 'yrs', 'yr', 'y'])}") == datetime.timedelta(seconds=second, minutes=minute, hours=hour, days=day + round(30.5 * month) + (365 * year) + 7 * week)