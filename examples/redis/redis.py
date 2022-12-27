

redis.xadd(stream_name, {key: value})

redis.xread({stream_name: '$'}, count=None, block=0)  
# $ means the most new message.
# count=NONE if you want to receive the newest, not just any number of messages
# block with a timeout of 0 milliseconds -> never timeout
