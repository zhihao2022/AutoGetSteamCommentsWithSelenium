# AutoGetSteamCommentsWithSelenium
慢速自动获取steam某个游戏的评论

## 介绍:
1. 通过selenium以及Firefox驱动打开某个提前获取的steam游戏的评论界面
2. 用selenium自动翻页到底部,大概每小时加载12000条评论
3. 用selenium获取界面的源代码
4. 用beautifulsoup以及lxml提取需要的内容并写入一个txt文件

## 注意:
1. 由于使用selenium翻页的方法,所以速度极慢,但是写起来简单(bushi)
2. 在国内需要先翻墙才能访问steam游戏评论界面
3. 如果只是需要大概的数据,可以直接访问[steamspy](https://steamspy.com/)(也需要翻墙)

