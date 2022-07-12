# test-mly
def dec(f):
    print("Enter dec now。。。")
    def wrapper(args):
        if int(args) < 0:
            raise TypeError("Negative wrong!")
        else:
            print("got args: ", args)
            f(args)
    return wrapper


@dec   # 这里的装饰器等同于 myprint = dec(myprint)，但更准确的说法是myprint = dec(myprint).wrapper。所以，下次遇到myprint(*args)，就要想到dec(myprint).wrapper(*args)
def myprint(a):
    print("myprint: ", a)


while True:
    f = input("enter a number:")
    myprint(f)
