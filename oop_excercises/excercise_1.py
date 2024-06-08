
class Example:
    def __init__(self):
        self.x=10
        self.__y=20
        self.__z=30
    def get_y(self):
        return self.__y
    def set_y(self,value):
        self.__y=value


    def public_method(self):
        print(self.x)
        print(self.__y)
        print(self.__z)
        self.__private_method()
    def __private_method(self):
        print("Inside Private Method")

s=Example()
s.set_y(100)
s.public_method()
print(s.get_y())
