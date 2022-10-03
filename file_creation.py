from os import remove
from naming import naming


def file_creation(name, text, rem=False):
    name = naming(name)
    if rem:
        remove(name)
    else:
        with open(f'{name}.py', 'w') as file:
            file.write(text)


file_text = """"""
file_name = ''
file_creation(file_name, file_text)
