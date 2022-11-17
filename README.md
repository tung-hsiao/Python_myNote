# Python_myNote

## 變數名稱
```
變數名稱前有單底線, _test : 在測試中，或不希望被直接調用的變數,函數,方法
變數名稱後有單底線, max_ : 為了避免與python的關鍵字(built-in keywords)或內建函數(built-in functions)有相同的名稱，ex:max為python內建求最大值的函數，若想建立自己的max函數/變數，可以使用max_
變數名稱前後有雙底線, __test__: 這是保留給python內建的變數或方法使用
```

## Basic functions
### eval()
可以計算數學運算式的字串
```
eval('5*9+4')    # 49
```

### find() rfind()
```
```



## python venv
```
cd 到 project folder
python3 -m venv myenv
cd 到 myenv/bin下 source activate
```

## conda
```
conda create --name myenv python=3.9  # create env
conda env list                        # list exist env
activate myenv                        # activate env
conda list                            # list packages in env

conda env remove -n myenv             # remove env
```

## pip
```
pip install -r requirements.txt
```