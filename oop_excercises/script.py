class Speed:
    def __init__(self) -> None:
        self.speed=10
        self.__new_speed=60

    def get_new_speed(self):
        return self.__new_speed  
    def set_new_speed(self,value):
        self.__new_speed=value


s= Speed()
s.speed=60
s.set_new_speed(890)
s.__new_speed=100
print(s.get_new_speed())