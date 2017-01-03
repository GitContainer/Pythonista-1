#利用装饰器实现缓存加速递归
def decoration(func):
    cache={}
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

@decoration
def fib(n):
    if n<2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))

print(fib(10))
