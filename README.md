### 前言

茅台不好抢，但是抢mate60还是很容易的。代码同样适用于JD的其他抢购商品，配置文件中添加 task 即可。
之前手册用的vnet抓包，很多人失败在这一步。重新找了一个好用的抓包软件，[手册参考](https://blog.auto100.org/posts/fd7cb838/)

### 推荐
另一个项目，葫芦娃自动预约和查询茅台的。脚本，手册，群都已具备，感兴趣的可关注。
https://github.com/yuweiping/huluwa

### 更新说明：
2024/3/28  **此版本不再更新了**，后续的更新只在捐赠的小圈子里发布了。此版本**还能用**，不能用的时候会说明。

增加了显示登录用户名，推送消息时也加了用户名
增加了对api_jd_url的校验处理

---
1. 通过收到html来判断抢完了还是觉得有点虚。所以还是改回去了，按照配置文件中的时间来结束运行。不用配置太长时间（都是秒没，配长时间没用还可能降分）。
2. 增加了抢购失败也发送通知
3. 增加了一些配置参数的判断，更友好一些吧


### 提高成功率的方法：
参与抢购至少要发起 6 次请求，而抢购时间两秒内就结束。所以理论上单次请求时间超过 400ms 的希望都不大。

下文介绍一种方案能够有效降低单次请求的时间（[付费文章](https://mp.weixin.qq.com/s?__biz=Mzg4NzYzMDQxMg==&mid=2247483727&idx=1&sn=efc36be1ba86da0c0af611b0ba570e8c&chksm=cf863e6cf8f1b77a4e2a93cb43b2912f3f72baa65f5dc277bce8b95a43bbecbd7eb6be8b5e9f#rd)），非通过代码手段来实现的，所有的代码都是开源的。

只是提高成功率，不代表一定能抢到。请大家理性选择。

<img src=".\doc\img1.png"  />
新方案效果
<img src=".\doc\img2.png"  />

### 操作步骤：
1. 将config-test.ini改名为config.ini
2. 按照手册抓包补全信息，注意config中的配置信息是不用加引号的，**末尾不要有分号**。
3. `pip install -r requirements.txt` 安装依赖
4. `main.py`

如果sign失败大概率是api_jd_url有问题，大家可参考如下格式
api_jd_url = https://api.m.jd.com/client.action?functionId=genToken&clientVersion=12.2.2……

### 参数说明

| 参数            | 是否必填 | 说明                                  |
|---------------|------|-------------------------------------|
| local_cookies | 是    | 抓包                                  |
| local_jec     | 是    | 抓包                                  |
| local_jdgs    | 是    | 抓包                                  |
| api_jd_url    | 是    | 抓包                                  |
| continue_time | 是    | 持续时间，实际jd返回html就认为结束了               |
| work_count    | 是    | 多进程，可参考CPU核数                        |
| fp            | 是    | [点击获取](https://blog.auto100.org/jd) |
| task          | 是    | 配置任务,商品，预约时间，抢购时间                   |
| address_id    | 否    | 如果不使用默认收货地址，可指定地址列表中的其他地址           |
| push_token    | 否    | 抢购成功后的推送                            |

### address_id设置方法
1. 打开jd_seckill.py 找到get_address_by_pin方法
2. 取消 # logger.info(resp_json['addressList'])这行的注释
3. 运行 main.py 可用获取到所有的address。根据自己的标识或者手机号等信息判断要选择的id即可

### 注意事项
1. **注意本库只能作为学习用途, 造成的任何问题与本库开发者无关, 如侵犯到你的权益，请联系删除**
2. 为限制大范围传播，不提供打包好的exe和docker image，当然赞助者可跟我索要，但不得传播。
3. 抢茅台需要plus分>=103 ,本程序是否会造成封号，降分未完全测试，**后果自负**。
4. 亲测，plus分低于103获取到真实的抢购url要在3s之后，这时候早就抢完了。所以分不够不用参与，不会有任何意外。
5. 有人用本仓库抢到过茅台，参考下图，我没抢到过。

<img src=".\doc\微信图片_20240224112038.jpg"  />

### 参考
sign部分使用的是如下大佬的库，有兴趣的可以关注下
[n1ptune/jdSign(github.com)](https://github.com/n1ptune/jdSign)


### 支持
1. 右上角star支持一下
2. 如果各位老板需要联系我支持，请**打赏后再加微信**（小号s84iis）并注明已捐赠。

<img src="https://www.freeimg.cn/i/2024/02/19/65d34bf6d9958.png" alt="wx"  />

