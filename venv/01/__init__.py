#做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random, string
def rand_str(num,length):
    with open("tt","w") as file:
        for i in range(num):
            chars=string.ascii_letters+string.digits
            s=[random.choice(chars) for i in range(length)]
            file.write(''.join(s)+'\n')

if __name__=="__main__":
    rand_str(200,20)