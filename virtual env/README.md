# Python venv

## python venv
```
cd 到 project folder
python3 -m venv myenv
cd 到 myenv/bin下 source activate
```

## conda cmd
```
conda create --name myenv python=3.9  # create env
conda env list                        # list exist env
activate myenv                        # activate env
conda list                            # list packages in env

conda env remove -n myenv             # remove env
```

## conda install (window10)
```
到官網下載安裝檔後，安裝

將以下路徑加入到系統環境變數
D:\Anaconda
D:\Anaconda\Scripts
D:\Anaconda\Library\bin

conda -V               # 確認conda版本，確認conda可以正常執行
conda update conda     # 更新 conda 版本指令
即可開始使用
```

## pip
```
pip install -r requirements.txt
```