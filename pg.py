from pprint import pprint
import re
import json
import time
from datetime import datetime


s = "[qasdasd] avni: hello"
regex= "(?<=\[).+?(?=\])"

pprint(s.split(":")[1].lstrip())
pprint(re.search(regex, s).group())
pprint(s.split(" ")[1].replace(":", ""))

obj = '{"time": "qwe", "user": "avni", "msg": "asdfasf"}' 
dic = json.loads(obj)

print(dic["time"])
print(type(time.time()))

def convertTimestampToDateTime(ts):
    s = int(str(ts).split(".")[0])
    print(s)
    return datetime.utcfromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')

print(convertTimestampToDateTime(1653072505.4005535))