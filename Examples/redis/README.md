# redis

### xadd
```
# id: Location to insert this record. By default it is appended.
# maxlen: truncate old stream members beyond this size
# approximate: actual stream length may be slightly more than maxlen

redis.xadd(stream_name, {key: value}, id='*', maxlen=None, approximate=True)
```
### xread
```
# $ means the most new message.
# count=NONE if you want to receive the newest, not just any number of messages
# block with a timeout of 0 milliseconds -> never timeout

redis.xread({stream_name: '$'}, count=None, block=0)  
```