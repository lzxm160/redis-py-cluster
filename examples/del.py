from redis._compat import xrange
from rediscluster import RedisCluster
import shutil

startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
rc = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
# rc.set("foo", "bar")
# rc.set("foo", "bar")
# print(rc.get("{{*}_test_flow_number}:id"))
# rc.delete("{{*}_test_flow_number}:id")
# 1.1 23:59
# 59 23 1 1 * command line
# bak data
port=['6380','6381','6382','7380','7381','7382']
for i in port:
	from='/usr/local/redis/data/appendonly-'+i+'.aof'
	to='/usr/local/redis/data/appendonly-'+i+'-2016.12.31bak.aof'
	try:
		shutil.copy2(from, to)
	except (IOError, os.error, shutil.Error), why:
            print("Unable to remove \"%s\": %s" % (cur_path, why))
            continue;
for i in port:
	from='/usr/local/redis/data/dump-'+i+'.rdb'
	to='/usr/local/redis/data/dump-'+i+'-2016.12.31bak.rdb'
	try:
		shutil.copy2(from, to)
	except (IOError, os.error, shutil.Error), why:
            print("Unable to remove \"%s\": %s" % (cur_path, why))
            continue;

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