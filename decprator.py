from datetime import datetime

def timeit(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):#принимаем и транзитируем аргументы и именнованные аргументы
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now()- start)
            return result
        return wrapper
    return outer

@timeit('fio')#c декоратором функция может содержать теперь только целевой код, без доп обвеса
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit("fio")
def two(n):
    l = [x for x in range(n) if x % 2 == 0]#генератор списка
    return l 

# l1 = one(100)
# l2 = two(100)
l1 = timeit('fio')(one)(10)