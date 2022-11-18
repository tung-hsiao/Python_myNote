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
### sort sorted

### zip
### enumerate

### dict.update
### del

### any
### lambda

## String
### join
### split





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
