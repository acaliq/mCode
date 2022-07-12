from os import name,path
print('__name__:',__name__)
print('__address__:',path.abspath(__file__))
from .file1 import mod
print('tMain ended')