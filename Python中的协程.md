```
def consumer():
    r = ""
    while True:
        b = yield r
        if not b:
            return
        print("[消费者] Consuming %s..." % b)
	#等下一次执行yield 时候 r值已经变为 200 ok
        r = "200 ok"


def produce(c):
    c.send(None)
    n = 0
    while n<5:
        n = n + 1
        print("[生产者] Producing %s..." % n )
        r = c.send(n)
        print("[生产者] Consumer return: %s"% r)
    #关闭消费者
    c.close()

c = consumer()
produce(c)
```

b = Yield r
通过 send(n) 为 b赋值，当下一次执行到yield 处时返回 r
