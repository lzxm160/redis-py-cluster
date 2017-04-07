from redis._compat import xrange
from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": 6380}]
r = RedisCluster(startup_nodes=startup_nodes, max_connections=32, decode_responses=True)
# r.hincrby('a', '1', amount=-2) == 1
for i in xrange(1280,1294):
    num="%06d" % i
    attr='FR_PO_'+num+'_GDN' #FR_PO_001235_GDN
    value=r.hget('{flow_no_sub_2}',attr)
    print attr,value
    if int(value)==-1:#have to convert,or ret is wrong
        ret=r.hincrby('{flow_no_sub_2}', attr, amount=1)
        print "incr:",ret