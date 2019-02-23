#任一个英文的纯文本文件，统计其中的单词出现的个数。
from collections import Counter
import re
tct=open("04")
data=[]
for line in tct:
    re.sub("\"|,|\.","",line)
    data.extend(line.strip().split())

def creat(filename):
    tct = open(filename)
    data = []
    for line in tct:
        re.sub("\"|,|\.", "", line)
        data.extend(line.strip().split())
    return data
def wc(filename):
    print(Counter(creat(filename)))
if __name__ == "__main__":
    filename="04"
    wc(filename)