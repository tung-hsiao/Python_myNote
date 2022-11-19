# Python_myNote

## 變數名稱
```
變數名稱前有單底線, _test : 在測試中，或不希望被直接調用的變數,函數,方法
變數名稱後有單底線, max_ : 為了避免與python的關鍵字(built-in keywords)或內建函數(built-in functions)有相同的名稱，ex:max為python內建求最大值的函數，若想建立自己的max函數/變數，可以使用max_
變數名稱前後有雙底線, __test__: 這是保留給python內建的變數或方法使用
```
## Documentation string
```
def myFunction():
    '''this help you understand this function'''
    print('hello')

help(myFunction)
print(myFunction.__doc__)
```





## Basic functions
### eval()
###### 計算數學運算式的字串
```
eval('5*9+4')    # 49
```

### find()
###### 字串搜尋, 回傳字串的index position, 如果沒有則回傳-1
```
msg = 'AA BB CC DD AA'
msg.find('AA')    # 0
msg.find('EE')    # -1
```

### index()
###### 字串搜尋, 回傳字串的index position, 如果沒有則回傳-1, 可以用在串列(list)
```
msg = 'AA BB CC DD AA'
msg.index('AA')    # 0
msg.index('EE')    # ValueError: substring not found

List = [123, 'xyz', 'runoob', 'abc']
List.index( 'xyz' )    # 1
```

### set

### zip
### enumerate

### dict.update
### del

### any
### lambda

### encode
### decode

## String
### join
### split

## sort
### sort sorted
```
myList = [5,1,3,2,4]

# Approach 1
list_sorted = sorted(myList)
print(list_sorted)          # [1, 2, 3, 4, 5] 

# Approach 2 
print(myList)     # [5, 1, 3, 2, 4]
myList.sort()
print(myList)     # [1, 2, 3, 4, 5]
```
### insertion sort
```
def insertion_sort(Lst):
    if len(Lst) == 1:
        return Lst
    for i in range(len(Lst)):
        for j in range(i,0,-1):
            if Lst[j] < Lst[j-1]:
                Lst[j], Lst[j-1] = Lst[j-1], Lst[j]
            else:
                break
    return Lst
myList = [5,1,3,2,4]
insertion_sort(myList)

# 5, 1,3,2,4
# 1,5, 3,2,4
# 1,3,5, 2,4
# 1,2,3,5, 4
# 1,2,3,4,5  
```

## python3 division
```
print(5/2)       # 2.5
print(5.0/2)     # 2.5

print(5//2)      # 2
print(5.0//2.0)  # 2.0
```

## variables assignment
```
a = 10         # immutable variables
b = a
print(a is b)  # True

b = 20
print(a is b)  # False
```
```
a = []         # mutable variables
b = a
print(a is b)  # True

b.append(20)
print(a is b)  # True

b = [10]
print(a is b)  # False

print(a)       # [20]
```
###### 在執行b = myFunction(a)時其實相當於在函式內部執行了input = a
```
def myFunction(input):
    print(input is a)  # True

    r = a+1        # id(r) = 1994472647280
    print(id(r))
    return r

a = 10
b = myFunction(a)  # id(b) = 1994472647280
```
```
def myFunction(input):
    print(a is input)  # True
    
    input = 100
    print(a is input)  # False

a = 10
myFunction(a)
print(a)      # 10
```

## copy
### shallow copy
```
a = [1,2,[3]]
b = a.copy()

print(a is b) # False

b.append(5)
print(a)     # [1, 2, [3]]
print(b)     # [1, 2, [3], 5]

b[2].append(4)
print(b)     # [1, 2, [3, 4], 5]
print(a)     # [1, 2, [3, 4]]
             # Element 是指向同一位址, 因此若該element為mutable則會連動
```
### deep copy
```
import copy
a = [1,2,[3]]
b = copy.deepcopy(a)

print(a[2] is b[2])  # False
b[2].append(4)
print(a)       # [1, 2, [3]]
print(b)       # [1, 2, [3, 4]]
```





## re
### re.search() re.match()
###### re.search() searches the whole string
###### re.match() searches the beginning of the string
```
sub_string = 'good'
string_1 = 'Black tea is good to drink'
string_2 = 'good? Black tea is good to drink'

print(re.search(sub_string, string_1))
# <re.Match object; span=(13, 17), match='good'>
print(re.match(sub_string, string_1))
# None

print(re.search(sub_string, string_2))
# <re.Match object; span=(0, 4), match='good'>
print(re.match(sub_string, string_2))
# <re.Match object; span=(0, 4), match='good'>

print(re.search('GOOD', string_2, re.IGNORECASE))
# <re.Match object; span=(0, 4), match='good'>
```







## random
### random.shuffle()
```
myList = ['A','B', 'C']
random.shuffle(myList)  # 將list打散
```

###  random.sample()
```
myList = ['A','B', 'C']
n = 2
random.sample(myList, n)   # 從list中隨機挑n個，回傳
```

### random.choice()
```
random.choice(range(0,100)) # 產生一筆0-100間的隨機整數
```

### random.randint()
```
min, max = 0, 100
for i in range(5):
    print(random.randint(min, max))    # 產生 min - max 間的隨機整數
```

### random.seed()
```
min, max = 0, 100
x=1
random.seed(x)    # x是種子值, 設定此種子值後，未來使用隨機函數都會產生相同的隨機數
for i in range(5):
    print(random.randint(min, max))    # 產生 min - max 間的隨機整數
```

### random.random()
```
for i in range(5):
    print(random.random())    # 產生 0(含) - 1.0(不含) 間的隨機浮點數
```

### random.uniform()
```
min, max = 0.0, 100.0
for i in range(5):
    print(random.uniform(min, max))    # 產生 min - max 間的隨機浮點數
```





## 中文處理
### 在Python3因為字串已經全部統一成unicode ，所以不必加上u
### 由於UTF-8可以編解碼任何字集，因此通常我們皆使用UTF-8編碼
```
# -*- coding: utf-8 -*-
import sys
print(sys.getdefaultencoding())     # print 目前系統字符編碼

string = '大樹'                     # 等同於u'大樹', unicode編碼
print(string[0])
print(string[1])
print(len(string))

encoded_string = string.encode('utf-8') # 與外界溝通時, 需先進行utf-8 encode
print(encoded_string)

b_str = b'\xe5\xa4\xa7\xe6\xa8\xb9' 
print(b_str.decode('utf-8'))        # 外界的文字, 透過utf-8 decode成unicode
```