#02_functions
def greet(name,greeting='你好'):
    return f"{greeting},{name}"

print(greet("张三"))                    #你好，张三
print(greet("张三",greeting="早上好"))  #早上好，张三

#不定长参数:*args 收集位置参数,**kwargs 收集关键字参数
def log(level,*args,**kwargs):
    print(f"[{level}]",args,kwargs)

log("INFO","请求开始",user="张三",path="/api")

#lambda:一个表达式的小函数
double = lambda x:x *2
print(double(21))       #42

#配合sorted排序
users = [{"name":"张三","age":25},{"name":"李四","age":20}]
users.sort(key=lambda u:u["age"])   #按年龄升序

#自己写：一个 calc(a, b, op) 函数，支持 + - * /，用 lambda 实现运算
def calc(a,b,op):
    operations = {
        "+": lambda x,y:x+y,
        "-": lambda x,y:x-y,
        "*": lambda x,y:x*y,
        "/": lambda x,y:x/y,
    }
    if op not in operations:
        raise ValueError(f"不支持的运算符:{op}")
    return operations[op](a,b)

print(calc(1,1,"+"))
print(calc(4,3,"*"))