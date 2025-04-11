from dataclasses import dataclass

@dataclass()
class Cat:
    name :str
    id :int
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def hi(self):
        print(f"{self.name}:hi")
    @staticmethod
    def compare(obj1,obj2):
        if (obj1.name == obj2.name) and (obj1.id == obj2.id):
            return True
        else:
            return False
    def compare(self,obj)-> bool:
        if (self.name == obj.name) and (self.id == obj.id):
            return True
        else:
            return False
cat = Cat(1,2)
cat1 = Cat(1,2)
flag = cat==cat1
print(flag)
