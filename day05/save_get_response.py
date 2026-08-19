"""Day5 打卡任务：请求 https://httpbin.org/get，把返回的 JSON 保存到文件"""
import json
import requests

resp = requests.get("https://httpbin.org/get", timeout=10)
print(f"状态码: {resp.status_code}")

data = resp.json()                       # 响应体解析成字典
with open("get_response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已保存到 get_response.json")
