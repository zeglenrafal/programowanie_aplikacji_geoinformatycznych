from typing import Union, List

def zmien_wartosc(arg: Union[int, List[str]]) -> Union[int, List[str]]:
    if type(arg) is int:
        arg = 65482652

    elif type(arg) is list:
        arg[0] = 'kalafior'

    return arg
