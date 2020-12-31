import datetime, re


class Converter:
    """
    A converter to convert a string to a datetime.datetime object, such as returned by datetime.timedelta.

    Attributes:
        input_string: a string (usually user input) to convert to a datetime object
    """

    def __init__(self, input_string):
        """
        Initialization for the converter
        """

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
        The converter itself. Takes the string input from initialization and transforms it into a datetime.datetime object
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
