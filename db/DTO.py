class Test:
    def __init__(self,a , b):
        self.a = a
        self.b = b


test1 = ("1" , "2")
obj = Test(*test1)
print(obj.fullname)
print(test1[1])

