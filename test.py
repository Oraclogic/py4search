# -*- coding: utf-8 -*-
import datetime
import sys
import time

now = datetime.datetime.now().strftime("%Y%m%d")
print ('111' + now)

time_utc = datetime.datetime.utcnow()
print(time_utc)

x = 3
y = 4

if x < 4:
    print("x=" + str(x))


def plus_one(x):
    x = x + 1
    print(x)


print(x, plus_one(x))

plus_one(x)


class Car:
    def set_brand(self, brand):
        self.brand = brand


x = Car()
type(x)
x.set_brand('Toyota')
print (x.brand)


class Car:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)


my_car = Car("Tyota")
my_car.get_brand()


x = [1, 2, 3]
print (x)
x.extend([4, 5])
print (x)
for c in x:
    print(c)


attachment = "c:\Users\IBM_ADMIN\PycharmProjects\zfzhou\run_ora.sql"
print len(attachment)


ll = []


searchlog = 'krinight'


def get_search_list(file, searchlog):
    searchloglist = []
    f = open(file)
    lines = f.read().splitlines()
    for i in range(0, len(lines)):
        if lines[i].find(searchlog) != -1:
            searchloglist.append(lines[i])
    return searchloglist


filename = '/Users/zhoufeng/Documents/OneDrive/GitHub-Oraclogic/py4search/esearch.csv'
filteredlist = get_search_list(filename, searchlog)
print(filteredlist)
print(type(filteredlist))
# with open(filename) as f:
#     lines = f.read().splitlines()


print (u'\u8def\u5f84\u4e0d\u5b58\u5728\u3002\u8bf7\u9a8c\u8bc1\u6b64\u8def\u5f84\u662f\u5426\u6b63\u786e\u3002').encode('utf8')
# print u"Exception(u'\xb1\xbb\xba\xf4\xbd\xd0\xb7\xbd\xbe\xdc\xbe\xf8\xbd\xd3\xca\xd5\xba\xf4\xbd\xd0\xa1\xa3',)"
# bytes = '\xb1\xbb\xba\xf4\xbd\xd0\xb7\xbd\xbe\xdc\xbe\xf8\xbd\xd3\xca\xd5\xba\xf4\xbd\xd0\xa1\xa3'
bytes = '\u8def\u5f84\u4e0d\u5b58\u5728\u3002\u8bf7\u9a8c\u8bc1\u6b64\u8def\u5f84\u662f\u5426\u6b63\u786e\u3002'
print bytes.decode('gbk')

my_list = ['p', 'r', 'o', 'b', 'e']
print len(my_list)

s1 = '10:33:26'
s2 = '11:15:49'  # for example
FMT = '%H:%M:%S'
tdelta = datetime.datetime.strptime(now, "%Y%m%d") - datetime.datetime.strptime(now, "%Y%m%d")

for my_single_list in my_list:
    print(my_single_list)


for my_single_list in my_list:
    print(my_single_list),

for num in (range(5)):
    print(num)


print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)

print(sys.version)


for i in (range(5)):
    print (datetime.datetime.now().strftime("%Y%m%d %H%M%S") + "\tHello World!")
    time.sleep(1)


for i in (range(5)):
    print (datetime.datetime.now().strftime("%Y%m%d %H%M%S") + "\tHello World!")
    time.sleep(1)

for x in xrange(1, 10):
    print x
