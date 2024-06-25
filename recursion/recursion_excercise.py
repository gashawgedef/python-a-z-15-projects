# def recursion():
#     print("Hello")
#     recursion()

# recursion()
# def fun():
#     val = 10
#     return val
# def example():
#     print("UL")
#     x = fun()
#     y =20
#     result = x+y
#     return result

# print(example())
def run(n):
    if n == 0:
        return
    print("UL")
    run(n-1)
    print("Ul")

n = 3
run(n)
print("Completed")