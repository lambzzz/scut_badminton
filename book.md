#### 抓包

[Windows抓包指南①：Proxifier+Fiddler对第三方程序强制抓包-CSDN博客](https://encoderlee.blog.csdn.net/article/details/90383486?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-2-90383486-blog-130902310.235^v43^pc_blog_bottom_relevance_base4&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-2-90383486-blog-130902310.235^v43^pc_blog_bottom_relevance_base4&utm_relevant_index=5)

[Fiddler在抓取https数据包时如何解决Tunnel to 443的问题，微信小程序打不开无法抓包的问题和无法抓取https包的问题，数据包上锁的问题等_fiddler抓包都是带锁的443-CSDN博客](https://blog.csdn.net/HAIDIDECHUAN/article/details/133804538?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-133804538-blog-90486208.235^v43^pc_blog_bottom_relevance_base4&spm=1001.2101.3001.4242.2&utm_relevant_index=4)

#### 信息

> 一号场venueId：511508061201884，二号场venueId：511589859434885，五号场venueId：511839951512888，六号场venueId：511942956511889，七号场venueId：512037093039890，八号场venueId：512160523250891

> 1715875200000：2024年5月17日，1715961600000：2024年5月18日，1716048000000：2024年5月19日，1716134400000：2024年5月20日

#### post包

```http
POST https://venue.spe.scut.edu.cn/api/mini/order/rental/orders/apply HTTP/1.1
Host: venue.spe.scut.edu.cn
Connection: keep-alive
Content-Length: 164
xweb_xhr: 1
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiI5OWZhZTFiZC02NGRiLTRlYjctODNkMS05ZDU3YzU3NTUyMzMiLCJpYXQiOjE3MTU4NTg5ODIsImV4cCI6MTcxNTk0NTM4MiwidXNlckluZm8iOnsidXNlclJvbGVJZCI6MSwiYWNjb3VudCI6IjIwMjIyMTAxNzc5OCIsInNubyI6IjIwMjIyMTAxNzc5OCJ9LCJzZXgiOjEsInVzZXJJZCI6MjU5MjM0NTA1NzgzMzcsInNlcmlhbFZlcnNpb25VSUQiOi03NzAwODI1OTA0ODMwNzA0NjE5LCJpc0luaXRQYXNzd29yZCI6ZmFsc2UsInBob25lIjoiJHNpZ246cTl4djNBME4zMmtESkQyVVhueHlYZz09Iiwibmlja25hbWUiOiLljY7mhYjmtpsiLCJ0YWciOiJtaW5pIiwiaXNSZWFsTmFtZSI6dHJ1ZSwiYWNjb3VudCI6IiRzaWduOk1BN1krcFhGR0JDeEZaSlFKalNmQUE9PSJ9.B5rYUMxhzrQK1SZecyaGRlrQSt9KtTHJAVj0SWsgnHI1cOHnp-VaTk9ShvHvfQRhaZIrUZ0LYEeH82357vWSstaaz-aFwKIbAR5SXaQ1PYofUyXiX0-j7Oo1qhCEOhNOlnmeoa1JRH9MSW1YAv5Ms-_DZiqq4_MTwf7caVZYuy164gHwYM0Yv61Dvlavl2UetUaJRgOyuo_WJZdSV7H4IjYT9_gN50gmQrvqMA87lm5too-jnes-0-p5nJYCRQindneAjnB7P83_ks7873Cui1iJFCUGyqIQ9oMqaIk97o9GK3trM3Sjm-Ip0paoGhP2aaaXwlPKxptosgGGTWMXNQ
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129
Content-Type: application/json;charset=UTF-8
Accept: */*
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://servicewechat.com/wxe4bbc47ea32ad29f/6/page-frame.html
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

{"receipts":0,"mode":"week","buyerSource":1,"stadiumId":1,"rentals":[{"venueId":511942956511889,"belongDate":1715875200000,"week":5,"start":"07:00","end":"08:00"}]}
```

