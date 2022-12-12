import random

import redis
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,db='9')
conn = redis.Redis(connection_pool=pool)

# verification_code_redis = conn.get('123')
verification_code =''.join(str(i) for i in random.sample(range(0, 9), 6))
verification_code_redis = conn.set('123',verification_code,300)
# type(verification_code_redis)
print(conn.get('123'))