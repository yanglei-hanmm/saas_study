import redis
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,db='9')
conn = redis.Redis(connection_pool=pool)

verification_code_redis = conn.get('123')
type(verification_code_redis)
print(verification_code_redis)