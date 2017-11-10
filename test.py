# -*- coding: utf-8 -*-
import datetime
now = datetime.datetime.now().strftime("%Y%m%d")
print ('111'+now)

from datetime import datetime
time_utc = datetime.utcnow()
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


l = []


searchlog = 'krinight'


def get_search_list(file, searchlog):
    searchloglist = []
    f = open(file)
    lines = f.read().splitlines()
    for i in range(0, len(lines)):
        if lines[i].find(searchlog) != -1:
            searchloglist.append(lines[i]) 
    return searchloglist


filename = 'c:\Users\IBM_ADMIN\PycharmProjects\zfzhou\esearch.csv'
filteredlist=get_search_list(filename, searchlog)
print(filteredlist)
print(type(filteredlist))
# with open(filename) as f:
#     lines = f.read().splitlines()


