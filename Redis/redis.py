#usr/bin/python3
import redis

def main():
    client = redis.Redis()
    client.set('k3','v3')
    print(client.get('k2'))  # 注意输出前面有个b，是指byte
    print(client.get('k3').decode()) #利用decode可以去掉
    client.set('k4',500)
    client.incr('k4', 100)
    print(int(client.get('k4').decode()))

    client.hset('stu', 'id','1001')
    print(client.hgetall('stu'))
    print(client.hkeys('stu'))
    print(client.hvals('stu'))
    print(client.hget('stu','id').decode())

    client.rpush('list1',10,20,30,40)
    print(client.lrange('list1',0,-1))

if __name__=='__main__':
    main()
