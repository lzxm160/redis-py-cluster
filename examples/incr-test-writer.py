from redis._compat import xrange
from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
rc = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
#rc.set("foo", "bar")

#print(rc.get("{test3_test_flow_number}:id"))
# for i in xrange(1000000):
#     d = str(i)
#     r.set(d, d)
#     r.incrby(d, 1)
rc.sadd("set1","1")
rc.sadd("set1","2")
rc.sadd("set1","3")
rc.sadd("set2","2")
rc.sadd("set2","3")
rc.sadd("set2","4")
print(rc.sdiff("set1","set2"))
print(rc.sinter("set1","set2"))
print(rc.sunion("set1","set2"))
print("----------------------------")
rc.zadd("test","1","4")
rc.zadd("test","2","7")
rc.zadd("test","3","2")
rc.zadd("test","4","1")
rc.zadd("test","5","9")
rc.zadd("test","6","41")
print(rc.zscore("test","6"))
print(rc.zrange("test","0","-1"))
print("----------------------------")
print(rc.zrange("test","0","-1","withscores"))
print(rc.zrevrange("test","0","-1","withscores"))
print(rc.zrangebyscore("test","9","41"))