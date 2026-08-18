"""Day4 练习：异常处理 + 文件读写 + JSON"""
import json
from pathlib import Path

# ========== 练习1：写 JSON 文件 ==========
data = {"name": "张三", "age": 25, "tags": ["后端", "学习AI"]}
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("user.json 写入完成")

# ========== 练习2：读 JSON 文件 + 异常处理 ==========
try:
    with open("user.json", "r", encoding="utf-8") as f:
        user = json.load(f)
    print(user["name"])
except FileNotFoundError:
    print("文件不存在")
except json.JSONDecodeError:
    print("JSON 格式错误")
except Exception as e:          # 兜底（尽量少用）
    print(f"未知错误: {e}")
finally:
    print("无论是否出错都会执行")

# ========== 练习3：读取不存在的文件，捕获 FileNotFoundError ==========
try:
    with open("not_exist.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("文件不存在，已捕获 FileNotFoundError")

# ========== 练习4：pathlib 查看文件信息 ==========
p = Path("user.json")
print(p.exists(), p.name, p.suffix, p.stat().st_size)
