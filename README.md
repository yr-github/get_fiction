# get_fiction
小说追更：自动获取小说更新并发送到邮箱

### 使用方法
1. 需要在根目录新建一个config.ini的文件，文件内容如下：
```
[mail]
smtp_host = smtp.163.com
neateasy_user = 你的邮箱地址
neatease_code = 你的
send_email = 你的邮箱地址

[receive]
receive_emails1 = 接收邮箱地址1
receive_emails2 = 接收邮箱地址2

[fiction_chapter]

[query_time]
time = 60
```
其中query_time 下的time字段意义是查询更新周期，单位为秒<br>
以上邮箱参数配置可以参考此[文章](https://www.yrblog.cn/2019/08/27/androidlinux03/ "文章")具体学习 <br>
2. 前往[小说网站](http://www.biquge.info/ "小说网站")获取你想追更的小说id，本文以万族之劫为例<br>
在该网站找到万族之劫的书籍页面url为：https://www.biquge.info/0_273/<br>
那么它的id就为0_273，进入书籍页面获取你的观看进度<br>
获取id与观看进度后在[fiction_chapter]下新建该id字段<br>
```
id=章节名(部分即可)
```
例如
```
0_273=你的眉头有些紧
0_274=第一千一
```
3. 此时你的config.ini应该如下
```
[mail]
smtp_host = smtp.163.com
neateasy_user = 你的邮箱地址
neatease_code = 你的
send_email = 你的邮箱地址

[receive]
receive_emails1 = 接收邮箱地址1
receive_emails2 = 接收邮箱地址2

[fiction_chapter]
0_273=你的眉头有些紧
0_274=第一千一

[query_time]
time = 60
```
此时运行main.py 将会每隔60s查询id为0_273 与 0_274 是否有更新内容，如果更新了将会发送到接受邮箱地址1与接收邮箱地址2中。

## TODO

- [ ] 小说排版<br>
- [ ] 异常处理<br>
- [ ] 日志添加<br>
- [ ] web服务(用户输入邮箱与订阅网文名称即可自动发送至用户邮箱)<br>
