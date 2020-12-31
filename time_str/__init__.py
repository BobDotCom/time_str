from .convert import Converter


__author__='BobDotCom'
__version__='0.0.2.dev1'

def convert(input_string: str):
    output = Converter(input_string).convert()
    return output