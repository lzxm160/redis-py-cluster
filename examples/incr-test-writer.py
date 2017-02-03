from redis._compat import xrange
from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
r = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
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
