from redis._compat import xrange
from rediscluster import RedisCluster
import shutil
import datetime
import os
startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
rc = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
# rc.set("foo", "bar")
# rc.set("foo", "bar")
# print(rc.get("{{*}_test_flow_number}:id"))
# rc.delete("{{*}_test_flow_number}:id")
# 1.1 23:59
# 59 23 1 1 * command line
# bak data
file=os.path.split(os.path.realpath(__file__))[0]+'/flow_no.txt'
f=open(file,"a")
f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
f.write('---------------------\r\n')
keys=set(rc.keys(pattern='{*_flow_number}:id'))
for i in keys:
	str=i+':'+ rc.get(i)+'\r\n'
	print(str)
	f.write(str)
	rc.delete(i)
f.close()
# print(rc.get("{test2_test_flow_number}:id"))
# rc.delete("{test2_test_flow_number}:id")
# print(rc.get("{test1_test_flow_number}:id"))
# rc.delete("{test1_test_flow_number}:id")
# print(rc.get("{test_test_flow_number}:id"))
# rc.delete("{test_test_flow_number}:id")