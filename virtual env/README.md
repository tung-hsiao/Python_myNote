# Python venv

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