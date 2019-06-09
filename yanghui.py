#! 
#coding:utf-8

def yanghui(level):
        if level <= 1:
            a = [1]
            yield a
        a = [1] + [i for i in range(level+1)] + [1]
        yield a


if __name__ == "__main__":
    for i in yanghui(4):
        print(i)