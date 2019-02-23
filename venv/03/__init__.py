#将 0001 题生成的 200 个激活码（或者优惠券）保存到 redis 关系型数据库中。
import redis
def fun():
    r=redis.Redis(host='localhost',port=6379,password='123456')
    with open("tt") as file:
        for line in file:
            r.lpush('tt',line.strip())
if __name__=="__main__":
    fun()