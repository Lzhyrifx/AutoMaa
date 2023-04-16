# AutoMaa
- 基于[MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)的附属<br>
- 包括更多功能的定时执行任务和远程控制
## 定时执行任务
包括Ordinary和Special模式(中途可通过远程控制开关AutoMaa)
- Ordinary(默认一日三次上号,默认为01,09,17整点启动)
- Special(8点开始,50分钟的日常以及Rougelike,10分钟剩下领取每日奖励)
## 远程控制
通过[AutoHotkey](https://github.com/AutoHotkey/AutoHotkey)来搭建内网<br>
并且通过内网穿透以达到远程控制(默认使用的是[星空内网穿透](https://frp.starryfrp.com/))<br>
## 功能
### Ordinary模式
- Start可以随时打开MAA(除非已经有MAA正在运行)
- Kill可以终止MAA和模拟器的运行
- LogNow适用于查看MAA最新的log日志
- Log查看MAA近期日志(1000行以内,超过1000行移至LogLast)
- LogLast查看更早的MAA日志
- Default将关卡选择切换为当前/上次
- Rougelike运行集成战略
- TaskShelved搁置下一次计划任务

### Special模式
- Start可以中途打开MAA(8点前打开,则为添加任务计划)
- Kill可以终止MAA以及模拟器的运行)(7点半后运行会终止AutoMaa定时计划程序)
- LogNow适用于查看MAA最新的log日志
- Log包含了近期的MAA运行日志(1000行以内,超过1000行移至LogLast)
- LogLast是MAA旧的运行日志
- TaskShelved搁置下一次计划任务

### 杂项
- Todesk是打开Todesk程序(远控软件)
- Shutdown2分钟后电脑关机
- CancelShutdown中途阻止电脑关机

# 安装说明
## 快速部署
- 下载最新的[AutoMaa](https://github.com/Lzhyrifx/AutoMaa/releases)
- 解压至D盘(如果解压到其他盘需要更改程序中的变量路径)
- 下载并安装[python3.9](https://www.python.org/downloads/)(默认使用python3.9.6)
- WIN+R,输入cmd,确定,输入pip install -r D:\AutoMaa\Python\requirements.txt
- 等待外部库导入成功后运行D:\AutoMaa\Python\Initialization\Initialization.py
- 如果python解释器使用conda虚拟环境的话(默认使用Python,不需要更改)
  - 打开D:\AutoMaa\Python\Initialization\interpreter.json
  - 更改vbs对象中的environment值为Conda并更改environment_name值为此项目的虚拟环境名(默认为AutoMaa)

## 模拟器([查看模拟器支持情况和ADB设置](https://maa.plus/docs/1.3-%E6%A8%A1%E6%8B%9F%E5%99%A8%E6%94%AF%E6%8C%81.html))
- 建议使用[蓝叠模拟器5国际版](https://wp-s.bluestacks.com/)
- 如果双模式同时使用,推荐[蓝叠模拟器5国际版](https://wp-s.bluestacks.com/)和[夜神模拟器](https://www.yeshen.com/)
- 请在MAA设置中设置模拟器路径(D:\AutoMaa\Python\Module\Module.py)
  - 蓝叠5默认位置C:\Program Files\BlueStacks_nxt\HD-Player.exe
  - 夜神默认位置D:\Program Files\Nox\bin\Nox.exe

## 定时任务
- 在文件资源管理器右键此电脑,选择任务计划程序,导入任务(Ordinary&Special)
  - [Ordinary](https://github.com/Lzhyrifx/AutoMaa/blob/master/Python/Ordinary/ScheduledTask/OrdinaryAutoMaa.xml)的路径在D:\AutoMaa\Python\Ordinary\ScheduledTask\OrdinaryAutoMaa.xml
  - [Special](https://github.com/Lzhyrifx/AutoMaa/blob/master/Python/Special/ScheduledTask/SpecialAutoMaa.xml)的路径在D:\AutoMaa\Python\Special\ScheduledTask\SpecialAutoMaa.xml
- 注意:每次更改任务计划都需要重新选择用户和组,否则会报参数错误<br>
![Image text](https://github.com/Lzhyrifx/AutoMaa/blob/master/Demonstrate/TaskScheduler.png)
- 如果希望AutoMaa在后台使用,可以勾选"不管用户是否登录都要运行"(此功能不推荐,模拟器还是会最小化前台,并且关闭Maa只能通过任务管理器终止进程或使用AutoMaa的Kill.py)
- 自定义任务计划,建议启动程序设置起始于(文件夹),然后再启动程序<br>
![Image text](https://github.com/Lzhyrifx/AutoMaa/blob/master/Demonstrate/Start.png)

# 使用须知
- AutoMaa强烈建议解压至D盘使用(后续将会支持其他路径)
- 由于MAA目前不支持多开,故AutoMaa程序运行前提是不存在其他运行的MAA(比如OrdinaryRougelike运行前提是Ordinary&Special定时运行的MAA不存在)
- 集成战略(默认皆为水月主题,如要更换,MAA设置中更换)
  - 如果要打水月主题,请结束傀影主题的进程(反之亦然)
  - 请将要打的集成战略主题添加至终端(PIN UP)
  - ![Image text](https://github.com/Lzhyrifx/AutoMaa/blob/master/Demonstrate/Rougelike.png)

  
# 远程控制
## AutoHotkey
- 下载[AutoHotkey](https://www.autohotkey.com/)v1.1
- example.ahk第27行为自定义端口号(默认为1024)
## 内网穿透(默认使用[星空内网穿透](https://frp.starryfrp.com/))
- 创建隧道,除了自定义端口外其他默认(自定义端口号默认为1024)
## 启用内网穿透
- 运行D:\AutoMaa\Web\AHKhttp-master\AHKhttp-master\example.ahk(无报错则启动成功)
- 运行D:\AutoMaa\Web\frpc_windows_amd64\Start.bat
- 默认使用星空内网穿透
  - [获取启动命令](https://frp.starryfrp.com/console/Proxies)
  - 复制启动命令输入Start.bat(保持远程状态,此窗口不能关闭)
# 远控须知
- 访问网站即可远程控制,如:http://xxx(隧道名).starryfrp.com:XXXXX(端口名)/XY(X为模式名,Y为远控函数名)
### 远程访问
### Ordinary模式
- http://xxx.starryfrp.com:XXXXX/OrdinaryStart启动MAA
- http://xxx.starryfrp.com:XXXXX/OrdinaryKill终止MAA进程和模拟器进程
- http://xxx.starryfrp.com:XXXXX/OrdinaryLogNow查看正在启动的MAA的日志
- http://xxx.starryfrp.com:XXXXX/OrdinaryLog查看MAA近期日志
- http://xxx.starryfrp.com:XXXXX/OrdinaryLogLast查看更早的MAA日志
- http://xxx.starryfrp.com:XXXXX/OrdinaryDefault将关卡选择切换为当前/上次
- http://xxx.starryfrp.com:XXXXX/OrdinaryRougelike只运行集成战略(目前会被定时任务阻断,待更新)
- http://xxx.starryfrp.com:XXXXX/OrdinaryTaskShelved搁置下一次任务
### Special模式
- http://xxx.starryfrp.com:XXXXX/SpecialStart启动MAA
- http://xxx.starryfrp.com:XXXXX/SpecialKill终止MAA进程和模拟器进程
- http://xxx.starryfrp.com:XXXXX/SpecialLogNow查看正在启动的MAA的日志
- http://xxx.starryfrp.com:XXXXX/SpecialLog查看MAA近期日志
- http://xxx.starryfrp.com:XXXXX/SpecialLogLast查看更早的MAA日志
- http://xxx.starryfrp.com:XXXXX/SpecialTaskShelved搁置下一次任务

### 杂项
- http://xxx.starryfrp.com:XXXXX/Todesk运行Todesk远控软件(默认路径为D:\Program Files (x86)\ToDesk.exe)
- http://xxx.starryfrp.com:XXXXX/Shutdown2分钟后电脑关机
- http://xxx.starryfrp.com:XXXXX/CancelShutdown中途阻止电脑关机