# 和 Python 一起走过的日子
##目录树：

- [1 HTTP响应码](#1 HTTP响应码)
- [一道 lambda 排序问题](https://github.com/Programscape/From-Python-To-Pythonic/blob/master/Python%E8%AF%AD%E8%A8%80/%E4%B8%80%E9%81%93%20lambda%20%E6%8E%92%E5%BA%8F%E9%97%AE%E9%A2%98.md)
- [杨辉三角问题（生成器）](https://github.com/Programscape/From-Python-To-Pythonic/blob/master/Python%E8%AF%AD%E8%A8%80/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E9%97%AE%E9%A2%98%EF%BC%88%E7%94%9F%E6%88%90%E5%99%A8%EF%BC%89.md)
- [汉诺塔递归玄学](https://github.com/Programscape/From-Python-To-Pythonic/blob/master/Python%E8%AF%AD%E8%A8%80/%E6%B1%89%E8%AF%BA%E5%A1%94%E9%80%92%E5%BD%92%E7%8E%84%E5%AD%A6.md)

# 1 HTTP状态码

状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值：

1xx：指示信息–表示请求已接收，继续处理

2xx：成功–表示请求已被成功接收、理解、接受

3xx：重定向–要完成请求必须进行更进一步的操作

4xx：客户端错误–请求有语法错误或请求无法实现

5xx：服务器端错误–服务器未能实现合法的请求

常见状态代码、状态描述、说明：

200 OK     //客户端请求成功

400 Bad Request  //客户端请求有语法错误，不能被服务器所理解

401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用

403 Forbidden  //服务器收到请求，但是拒绝提供服务

404 Not Found  //请求资源不存在，eg：输入了错误的URL

500 Internal Server Error //服务器发生不可预期的错误

503 Server Unavailable  //服务器当前不能处理客户端的请求，一段时间后可能恢复正常

eg：HTTP/1.1 200 OK （CRLF）