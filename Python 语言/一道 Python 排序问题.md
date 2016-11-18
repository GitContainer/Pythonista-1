# 一道Python排序问题的解答
##题目
对一个列表进行排序，lists = [7, -8, 5, 4, 0, -2, -5]

要求：

- 正数在前，负数在后，
- 整数从小到大
- 负数从大到小
来源：[V2EX](https://www.v2ex.com/t/286691)

## 解答

 lists = [ 7, -8, 5, 4, 0, -2, -5 ]

sort_lists = sorted  ( lists , lambda x : ( x<0 , abs))