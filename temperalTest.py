# urllib 是 Python 的标准库，包含了从网页请求数据，处理 cookie，甚至改变像请求头和用户代理这些元数据的函数。
# from curses import meta
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
# BeautifulSoup通过定位 HTML 标签来格式化和组织复杂的网页信息，用简单易用的Python对象为我们展现XML结构信息。
from bs4 import BeautifulSoup

url = 'https://imf.wd5.myworkdayjobs.com/zh-CN/IMF'

def getTitle(url):
    # urlopen 用来打开并读取一个从网络获取的远程对象，可以轻松读取 HTML 文件、图像文件或其他任何文件流。
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        # 一个 BeautifulSoup 对象时，需要传入两个参数：第一个参数是该对象所基于的 HTML 文本，第二个参数指定了你希望 BeautifulSoup 用来创建该对象的解析器。
        # html.parser 是 Python 3 中的一个解析器，不需要单独安装。
        # 另一个常用的解析器是 lxml ，和 html.parser 相比， lxml 的优点在于解析“杂乱”或者包含错误语法的 HTML 代码的性能更优一些。
        # 另外一个常用的 HTML 解析器是 html5lib，和 lxml 一样， html5lib 也是一个具有容错性的解析器，它甚至可以容忍语法更糟糕的 HTML。
        bs = BeautifulSoup(html.read(), 'html.parser')
        
        # 调用bs.find_all(tagName, tagAttributes) 可以获取页面中所有指定的标签。
        nameList = bs.findAll('meta',{'name':'title'})
    except AttributeError as e:
        return None
    return nameList

nameList = getTitle(url)
if nameList == None:
    print('Title could not be found')
else:
    for name in nameList:
        print(name)

