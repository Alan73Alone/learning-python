import json
import re
import requests
from datetime import datetime
from collections import Counter

#requests.GET 请求
resp = requests.get("https://httpbin.org/json",timeout=5)
print(resp.status_code)         #200
data = resp.json()              #自动解析 JSON
print(json.dumps(data,ensure_ascii = False,indent=2))

#datatime:时间格式化
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%A"))       #星期几

#re:正则
text = "今天是2026-08-15,下次还款日是2026-09-15"
dates = re.findall(r"\d{4}-\d{2}-\d{2}",text)
print(dates)                    #['2026-08-15','2026-09-15']

#collections.Counter:统计
words = ["java","python","java","ai","python","python"]
print(Counter(words).most_common(2))    #[('python',3),('java',2)]
