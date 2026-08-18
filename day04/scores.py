"""Day4 打卡任务：把张三的分数列表写进 scores.json,再读出来求平均分"""
import json

# 1. 写入 scores.json
scores = {"张三": [85, 92, 78]}
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False, indent=2)
print("scores.json 写入完成")

# 2. 读出来并求平均分
with open("scores.json", "r", encoding="utf-8") as f:
    data = json.load(f)

score_list = data["张三"]                       # [85, 92, 78]
avg = sum(score_list) / len(score_list)          # sum 求和，len 求个数
print(f"张三的分数: {score_list}")
print(f"张三的平均分: {avg:.1f}")
