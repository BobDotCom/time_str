"""
time_str
====================================
A package to convert strings to datetime.timedelta objects
"""

import datetime, re


class Converter:
    """A converter to convert a string to a :class:`datetime.timedelta` object.
    The convert method returns a :class:`datetime.timedelta` object

    Attributes
    -----------
    input_string: :class:`str`
        A string (usually user input) to convert to a :class:`datetime.timedelta` object.
        This can be set during initialization.
    """

    def __init__(self, input_string):
        self.input_string = input_string
        self.converted_string = None
        self.split_string = []
        self.pattern = {
            'seconds': ['seconds', 'second', 'secs', 'sec', 's'], 
            'minutes': ['minutes', 'minute', 'mins', 'min', 'm'], 
            'hours': ['hours', 'hour', 'hrs', 'hr', 'h'], 
            'days': ['days', 'day', 'dys', 'dy', 'd'], 
            'weeks': ['weeks', 'week', 'wks', 'wk', 'w'], 
            'months': ['months', 'month', 'mons', 'mon', 'mn'], 
            'years': ['years', 'year', 'yrs', 'yr', 'y']
        }
        self.raw_output = {
            'seconds': 0,
            'minutes': 0, 
            'hours': 0, 
            'days': 0, 
            'weeks': 0, 
            'months': 0, 
            'years': 0
        }

    def convert(self):
        """
        The converter itself. Takes the string input from initialization and transforms it into a :class:`datetime.timedelta` object.

        Returns
        --------
        :class:`datetime.timedelta`
            The converted datetime.timedelta object.
        """

        self.converted_string = self.input_string
        for entry in self.pattern:
            regex_pattern = r'(?<=[0-9])\s*(' + '|'.join(self.pattern[entry]) + r')((?=\s)|$)'
            self.converted_string = re.sub(regex_pattern,entry,self.converted_string)
        self.split_string = self.converted_string.split(' ')
        for entry in self.split_string:
            for form in self.raw_output:
                if form in entry:
                    to_add = entry.replace(form,'')
                    if to_add.replace('.','').isdigit():
                        self.raw_output[form] += float(to_add)
        self.raw_output['days'] += 31 * self.raw_output['months'] # datetime.timedelta does not support months
        self.raw_output['days'] += 365 * self.raw_output['years'] # datetime.timedelta does not support years
        self.output = datetime.timedelta(seconds=self.raw_output['seconds'], minutes=self.raw_output['minutes'], hours=self.raw_output['hours'], days=self.raw_output['days'], weeks=self.raw_output['weeks'])
        return self.output

def convert(input_string: str):
    """
    A shorter way to use the :class:`Converter`. Returns the :class:`datetime.timedelta` object

    Parameters
    -----------
    input_string: :class:`str`
        A string (usually user input) to convert to a :class:`datetime.timedelta` object
    Returns
    --------
    :class:`datetime.timedelta`
        The converted datetime.timedelta object.
    """
    
    output = Converter(input_string).convert()
    return output


__author__='BobDotCom'
__version__='0.0.2'

