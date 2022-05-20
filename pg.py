from pprint import pprint
import re
import json
import time


s = "[qasdasd] avni: hello"
regex= "(?<=\[).+?(?=\])"

pprint(s.split(":")[1].lstrip())
pprint(re.search(regex, s).group())
pprint(s.split(" ")[1].replace(":", ""))

obj = '{"time": "qwe", "user": "avni", "msg": "asdfasf"}' 
dic = json.loads(obj)

print(dic["time"])
print(type(time.time()))
