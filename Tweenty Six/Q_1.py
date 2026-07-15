class Demo:
    # class variable
    value = 0
    
    def __init__(self, no1, no2):
        # instance variale
        self.No1 = no1
        self.No2 = no2

    def Fun(self):
        print("Inside Fun One:", self.No1)
        print("Inside Fun Two:", self.No2)
    
    def Gun(self):
        print("Inside Fun One:", self.No1)
        print("Inside Fun Two:", self.No2)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun() # 11 21
Obj2.Fun() # 51 101
Obj1.Gun() # 11 21
Obj2.Gun() # 51 101