
def check(func):
    def inner(a,b):
        if b>a:
            return b/a
        func(a,b)
    return inner

@check
def div(a,b):
    return a/b

print(div(2,10))