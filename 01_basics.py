name = "张三"       #string
age = 25            #int
height = 1.75       #float
is_student = True   #boolean

nums = [1,2,3]      #list,可变
nums.append(4)
print(nums[0],len(nums),nums[-1])   #1 4 4

user = {"name": "张三","age" : 25}  #dict
print(user["name"])                 #张三
print(user.get("email","unknown"))  #unknown(get 不会报错)

point = (1,2)       #tuple,不可变
tags = {"a","b","a"}#set,自动去重->{"a","b"}

#流程控制
for i in range(3):
    if i % 2 == 0:
        print(i,"偶数")
    else:
        print(i,"奇数")

#列表推导式
squares = [x * x for x in range(5)]  #[0,1,4,9,16]
even = [x for x in range(10) if x % 2 == 0]

#用dict存 3 个同学的姓名和分数，打印出平均分
# user1 = {"name":"zhang","score":80}
# user2 = {"name":"li","score":78}
# user3 = {"name":"wang","score":91}
# avg_score = [(user1["score"]+user2["score"]+user3["score"]) / 3]
# print("三人的平均分为",avg_score)

students = [
    {"name":"zhang","score":80},
    {"name":"li","score":78},
    {"name":"wang","score":90},
]
avg_score = sum(s["score"] for  s in students) / len(students)
print("三人的平均分为",avg_score)