**和 Python 一起走过的日子**

- [Python语言相关](#python语言相关)
 - [一道lambda排序问题](#1-一道lambda排序问题)
 - [ff]（）
 - [汉诺塔递归玄学](https://github.com/Programscape/From-Python-To-Pythonic/blob/master/Python%E8%AF%AD%E8%A8%80/%E6%B1%89%E8%AF%BA%E5%A1%94%E9%80%92%E5%BD%92%E7%8E%84%E5%AD%A6.md)
- [Flask漫游指南](#flask漫游指南)
  -[HTTP响应码]()
- [其他说明](其他说明)
- []()


# python语言相关
## 1 一道lambda排序问题
对一个列表进行排序，`lists = [7, -8, 5, 4, 0, -2, -5]`

要求：

- 正数在前，负数在后
- 整数从小到大
- 负数从大到小

- 来源：[V2EX](https://www.v2ex.com/t/286691)

## 代码

 `lists = [ 7, -8, 5, 4, 0, -2, -5 ]`

`sort_lists = sorted  ( lists , key = lambda x : ( x<0 , abs (x)  )`

## 解释

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

综合可得出：

```
[0, 4, 5, 7, -2, -5, -8]
# flask漫游指南


