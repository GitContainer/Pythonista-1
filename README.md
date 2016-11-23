**和Python一起走过的日子**

---
- [Python语言相关](#python语言相关)
 - [用Python编写简历]()
 - [一道lambda排序问题](#1-一道lambda排序问题)
 - [汉诺塔递归玄学](#2-汉诺塔递归玄学)
 - [杨辉三角(生成器)](#3-杨辉三角生成器)
 - [正则笔记](#4-正则笔记)
 - [匹配标准格式时间](#5-匹配标准格式时间)
 - [正则验证邮箱](#6-正则验证邮箱)
- [Flask漫游指南](#flask漫游指南)
 - [HTTP响应码](#1-http响应码)
- [注疏](#注疏)

# python语言相关
## 1 一道lambda排序问题
对一个列表进行排序，`lists = [7, -8, 5, 4, 0, -2, -5]`

要求：

- 正数在前，负数在后
- 整数从小到大
- 负数从大到小

- 来源：[V2EX](https://www.v2ex.com/t/286691)

### 代码

 `lists = [ 7, -8, 5, 4, 0, -2, -5 ]`

`sort_lists = sorted  ( lists , key = lambda x : ( x<0 , abs (x)  )`

### 解释

逐个分析，sorted 中 key 可接受函数作为排序的条件，此处将 lambda 匿名函数传入

在 lambda 中 **x<0** 起到的作用是将列表中数映射为 True 和 False ，对布尔型进行比较

```
>>>False < True 
True
```

不考虑 abs( x ) ，此处列表由：

`[ 7, -8, 5, 4, 0, -2, -5]`

变为：

False 在前  `7 , 5 , 4 , 0`     True 在后  `-8 , -2 ,-5`

abs( x )，作用为对列表中元素进行取绝对值，再进行排序

 `0 , 4 , 5, 7`   与  `-2 , -5 ,-8` 

综合可得出： [0, 4, 5, 7, -2, -5, -8]

## 2 汉诺塔递归玄学
### 要解决汉诺塔问题，首先得解决(汉诺塔-1)的问题

在汉诺塔问题中，a 是出发地，c 是目的地，b作用是缓冲区，而整个递归的过程，就是随着 a 上盘子数目的减少导致缓冲区位置的不断变化

```
def han (n, a, b, c)
  if n == 1:
    print(a ,'-->'c )  # 只有一个，轻松从 a 到 c
  return #函数出口
  han (n-1 ,a , c, b) #如果不止一个，以 c 为缓冲区，把上面的 n-1 个搬到 b
  han (1, a, b,c) #前面搬到了b，把a 剩下的最后一个搬到 c ，接下来搬 b 到 c 
  han (n-1, b, a,c) #风水轮流转，a 当缓冲区，把 (n-1) 的b 搬到 c
```
  
  

## 3 杨辉三角(生成器)

1

1 		1

1		2		1

1		3		3		1

1		4		6		4		1

1		5		10		10		5		1

```python
def trangels():
    L=[1]
    while True:
        yield L #返回生成器
        L.append(0) #为下一行末尾加0
        L=[L[x-1]+L[x] for x in range(L)] #让每个数对应前一行的相应数和再前一位相加，第一个数比较特殊，是上一行第一个数与末尾数相加（这也是加0的用意所在）
```

##4 正则笔记



##5 匹配标准格式时间
```
re.mathc('^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0[0-9]|1[1-9]|2[1-9]|3[1-9]|4[1-9]|[1-9])\:([0[0-9]|1[1-9]|2[1-9]|3[1-9]|4[1-9]|[1-9])$'
```
##6 正则验证邮箱
```
import re

t=input('Input Your mail')
a=re.match(r'^([\w\d\.]+)\@([\w\d]+)\.([\w]+)$',t)
#匹配带名字的邮箱
#a=re.match(r'^(\<[\w\s]+\>)\s[\w\d\.]+\@[\w\d]+\.[\w]+$',t)
if a:
    print('ok')
else:
    print('no')
```

---

# flask漫游指南
## 1 http响应码
### 状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值：
- 1xx：指示信息–表示请求已接收，继续处理
- 2xx：成功–表示请求已被成功接收、理解、接受
- 3xx：重定向–要完成请求必须进行更进一步的操作
- 4xx：客户端错误–请求有语法错误或请求无法实现
- 5xx：服务器端错误–服务器未能实现合法的请求
### 常见状态代码、状态描述、说明：
- 200 OK     //客户端请求成功
- 400 Bad Request  //客户端请求有语法错误，不能被服务器所理解
- 401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
- 403 Forbidden  //服务器收到请求，但是拒绝提供服务
- 404 Not Found  //请求资源不存在，eg：输入了错误的URL
- 500 Internal Server Error //服务器发生不可预期的错误
- 503 Server Unavailable  //服务器当前不能处理客户端的请求，一段时间后可能恢复正常

# 注疏
作为一个自嗨型 Github，本文之所以目录不加空格、大小写飘忽不定（例如 HTTP 与 http ），非不为也，实不能也，而是因为 Github 的 Markdown 编辑器在目录树中只能识别--toc-- 中小写字母，否则便不能跳转，详细跳转规则请右上角点击源代码查看。




