"""Day4 补充：JSON 知识点速查 demo"""
import json

# ========== 1. JSON 和 Python 的类型对照 ==========
py_obj = {
    "name": "张三",
    "age": 25,
    "is_student": False,
    "scores": [85, 92, 78],
    "address": None,
}

# ========== 2. dumps：Python 对象 -> JSON 字符串 ==========
json_str = json.dumps(py_obj, ensure_ascii=False, indent=2)
print("=== dumps 输出（字符串）===")
print(json_str)
print("类型:", type(json_str))

# ========== 3. loads：JSON 字符串 -> Python 对象 ==========
back = json.loads(json_str)
print("\n=== loads 输出（Python 对象）===")
print("name:", back["name"])
print("scores:", back["scores"])
print("类型:", type(back))
print("注意: false -> False, null -> None:", back["is_student"], back["address"])

# ========== 4. dump / load：和文件配合 ==========
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(py_obj, f, ensure_ascii=False, indent=2)   # 写文件

with open("demo.json", "r", encoding="utf-8") as f:
    data = json.load(f)                                   # 读文件
print("\n=== 文件读写 ===")
print("从文件读回 name:", data["name"])
