from redis._compat import xrange
from rediscluster import RedisCluster
import shutil

startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
rc = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
# rc.set("foo", "bar")
# rc.set("foo", "bar")
# print(rc.get("{{*}_test_flow_number}:id"))
# rc.delete("{{*}_test_flow_number}:id")
# 1月1日23:59分
# 59 23 1 1 * command line
# bak data
shutil.copy2('/usr/local/redis/data/appendonly-6380.aof', '/usr/local/redis/data/appendonly-6380-2016.12.31bak.aof')
shutil.copy2('/usr/local/redis/data/appendonly-6381.aof', '/usr/local/redis/data/appendonly-6381-2016.12.31bak.aof')
shutil.copy2('/usr/local/redis/data/appendonly-6382.aof', '/usr/local/redis/data/appendonly-6382-2016.12.31bak.aof')
shutil.copy2('/usr/local/redis/data/appendonly-7380.aof', '/usr/local/redis/data/appendonly-7380-2016.12.31bak.aof')
shutil.copy2('/usr/local/redis/data/appendonly-7381.aof', '/usr/local/redis/data/appendonly-7381-2016.12.31bak.aof')
shutil.copy2('/usr/local/redis/data/appendonly-7382.aof', '/usr/local/redis/data/appendonly-7382-2016.12.31bak.aof')
shutil.copy2('/usr/local/redis/data/dump-6380.rdb', '/usr/local/redis/data/dump-6380-2016.12.31bak.rdb')
shutil.copy2('/usr/local/redis/data/dump-6381.rdb', '/usr/local/redis/data/dump-6381-2016.12.31bak.rdb')
shutil.copy2('/usr/local/redis/data/dump-6382.rdb', '/usr/local/redis/data/dump-6382-2016.12.31bak.rdb')
shutil.copy2('/usr/local/redis/data/dump-7380.rdb', '/usr/local/redis/data/dump-7380-2016.12.31bak.rdb')
shutil.copy2('/usr/local/redis/data/dump-7381.rdb', '/usr/local/redis/data/dump-7381-2016.12.31bak.rdb')
shutil.copy2('/usr/local/redis/data/dump-7382.rdb', '/usr/local/redis/data/dump-7382-2016.12.31bak.rdb')
keys=set(rc.keys(pattern='{*_test_flow_number}:id'))
for i in keys:
	print(rc.get(i))
	rc.delete(i)
# print(rc.get("{test2_test_flow_number}:id"))
# rc.delete("{test2_test_flow_number}:id")
# print(rc.get("{test1_test_flow_number}:id"))
# rc.delete("{test1_test_flow_number}:id")
# print(rc.get("{test_test_flow_number}:id"))
# rc.delete("{test_test_flow_number}:id")