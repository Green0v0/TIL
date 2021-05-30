import re
import csv
import random
class1 = []
with open('class1.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for idx, line in enumerate(rdr):
        class1.append(line[0])
# 1번만,,
# random.shuffle(class1)
result = []
for s in class1:
    temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
    if 'ESSENTIAL' in temp:
        result.append([temp[0],temp[2]])
        print(temp)
print(result)
# com = re.compile(r'standard|\D+').split()