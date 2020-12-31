from .convert import Converter


__author__='BobDotCom'

def convert(input_string: str):
    output = Converter(input_string).convert()
    return output