if __name__ == '__main__':
    print('Try module is excuted as main script'.center(80,'='))
import sys, os
'''
print(__file__)    #当前.py文件的位置
print(os.path.abspath(__file__))  #返回当前.py文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))   #当前文件的绝对路径目录，不包括当前 *.py 部分，即只到该文件目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #返回文件本身目录的上层目录    
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  #每多一层，即再上一层目录

print(os.path.realpath(__file__))   #当前文件的真实地址
print(os.path.dirname(os.path.realpath(__file__))) # 当前文件夹的路径

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)   #将目录或路径加入搜索路径

print(__name__)
'''
from . import tMain


