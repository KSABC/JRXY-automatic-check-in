# 今日校园自动签到
通过python+appium控制手机。


需要手动输入你的手机密码和所用的系统
里面有注释，请自行查看


使用方法:

1.新建bat文件，写python [此脚本的绝对路径]

2.在任务计划程序里，设置执行此bat文件的时间(只需执行一次)

3.在使用之前要在电脑上打开appium,当然也可以在任务计划程序里设置打开

4.使用时要使手机连接电脑


注意事项:

1.此脚本本人用于安卓11，如果您的版本不同，则需手动编辑，将platformVersion: 11的'11'改成您对应的版本

2.如果您是IOS用户，要将platformName:Android的'Android'改为IOS

3.每次执行的成功率并非100%，但此脚本会运行到签到成功为止，如果您一觉醒来仍未签到成功，那么就要您手动签到了

4.若今日校园更新，此脚本可能会失效，请等待新版本，或者由您自己更新

5.如果您使用的是笔记本，则可能需要在“编辑电源计划”上设置一下，让电脑休眠时也可以执行脚本


最后:

欢迎各位朋友对其进行优化
