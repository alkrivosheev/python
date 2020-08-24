def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Dividing by zero')
    except:
        print('Some error')

print(divide(1,0))