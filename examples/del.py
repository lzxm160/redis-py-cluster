from redis._compat import xrange
from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
rc = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
# rc.set("foo", "bar")
# rc.set("foo", "bar")
print(rc.get("{test3_test_flow_number}:id"))
rc.delete("{test3_test_flow_number}:id")

print(rc.get("{test2_test_flow_number}:id"))
rc.delete("{test2_test_flow_number}:id")
print(rc.get("{test1_test_flow_number}:id"))
rc.delete("{test1_test_flow_number}:id")
print(rc.get("{test_test_flow_number}:id"))
rc.delete("{test_test_flow_number}:id")