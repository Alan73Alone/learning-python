class User:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value < 0:
            raise ValueError("age 不能为负")
        self._age = value

    def __str__(self):
        return f"User({self.name},{self.age})"
    
class Admin(User):          #继承
    def __init__(self,name,age,level):
        super().__init__(name,age)      #调用父类结构
        self.level = level
    
    def __str__(self):
        return f"Admin({self.name},level={self.level})"
    
u = Admin("张三",25,3)
print(u)                #Admin(张三，level=3)
u.age = 30              #走setter
print(u.age)            #30