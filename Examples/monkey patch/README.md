# Monkey patch
## A MonkeyPatch is a piece of Python code which extends or modifies other code at runtime (typically at startup).

### old.py
```
class myClass:
    def function(self, num):
        print('[old] ' + str(num))
```
### main.py
```
import old

def function_new(self, num):
    print('[new] ' + str(num))

old.myClass.function = function_new

instance = old.myClass()
instance.function(2)      # [new] 2
```