# AutoMaa
基于[MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)的附属<br>
包括更多功能的定时执行任务和远程控制
## 定时执行任务
包括Ordinary和Special模式
- Ordinary:无防沉迷(默认一日三次上号,默认为01,09,17整点启动)
- Special:防沉迷(50分钟的日常剿灭及Rougelike,10分钟剩下领取每日奖励)<br>
中途可通过远程控制开关AutoMaa
## 远程控制
 通过[AutoHotkey](https://github.com/AutoHotkey/AutoHotkey)来搭建内网<br>
 并且通过内网穿透以达到远程控制(默认使用的是[星空内网穿透](https://frp.starryfrp.com/))
### 主要功能
- 远程打开Maa(Start.py)
- 远程关闭Maa(Kill.py)
- 远程查看Maa日志
# 使用说明
## 模拟器([关于模拟器支持情况和ADB设置](https://maa.plus/docs/1.3-%E6%A8%A1%E6%8B%9F%E5%99%A8%E6%94%AF%E6%8C%81.html))
- 建议使用[蓝叠模拟器5国际版](https://wp-s.bluestacks.com/)
- 如果双模式同时使用,推荐[蓝叠模拟器5国际版](https://wp-s.bluestacks.com/)和[夜神模拟器](https://www.yeshen.com/)<br>
## 定时任务
- 在文件资源管理器右键此电脑,选择任务计划程序,导入任务([Ordinary](https://github.com/Lzhyrifx/AutoMaa/blob/master/Python/Ordinary/ScheduledTask/OrdinaryAutoMaa.xml)&[Special](https://github.com/Lzhyrifx/AutoMaa/blob/master/Python/Special/ScheduledTask/SpecialAutoMaa.xml))
- 注意:每次更改任务计划都需要重新选择用户和组,否则会报参数错误<br>
![Image text](https://github.com/Lzhyrifx/AutoMaa/blob/master/Demonstrate/TaskScheduler.png)
- 如果希望AutoMaa在后台使用,可以勾选"不管用户是否登录都要运行"(此功能不推荐,模拟器还是会最小化前台,并且关闭Maa只能通过任务管理器终止进程或使用AutoMaa的Kill.py)
- 自定义任务计划,建议启动程序设置起始于(文件夹),然后再启动程序<br>
![Image text](https://github.com/Lzhyrifx/AutoMaa/blob/master/Demonstrate/Start.png)
# 远程控制
## AutoHotkey
- 下载[AutoHotkey](https://www.autohotkey.com/)V1.1
- [AHK文件设置](https://github.com/Lzhyrifx/AutoMaa/blob/master/Web/AHKhttp-master/AHKhttp-master/example.ahk)
  - 21行是自定义端口,可更改(不和默认端口冲突即可)
  - 86行是AHKsock.ahk位置,需要根据文件位置更改
## 内网穿透(默认使用[星空内网穿透](https://frp.starryfrp.com/))
- 创建隧道,除了自定义端口外其他默认
## 启用内网穿透
- 打开AutoMaa/Web/AHKhttp-master/AHKhttp-master/example.ahk(无报错则启动成功)
- 打开AutoMaa/Web/frpc_windows_amd64/Start.bat
- [获取启动命令](https://frp.starryfrp.com/console/Proxies)并输入命令行
- 访问网站即可远程控制,如:"http://xxx.starryfrp.com:XXXXX/SpecialTest"
# 注意事项
- 目前暂时无配置文件来设置模拟器&python等路径(大部分使用的是相对路径,有些只能使用绝对路径)

