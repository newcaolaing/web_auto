#/usr/bin/python
#encoding:utf-8
import csv
import os
import time


class App(object):
    def __init__(self,appname,means):
        self.means = means
        self.appname = appname
        self.content = ""
        self.startTime = 0

    #启动App
    def LaunchApp(self):
        print("正在打开"+self.appname)
        cmd = 'adb shell am start -W -n '+self.appname
        self.content=os.popen(cmd)

    #停止App
    def StopApp(self):
        print("正在关闭"+self.appname)
        cmd = 'adb shell am force-stop '+self.appname.split("/")[0]  if self.means == '1' else 'adb shell input keyevent 3'
        os.popen(cmd)

    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        print("本次启动时间为" + self.startTime.strip() + "毫秒")
        return self.startTime

#控制类
class Controller(object):
    def __init__(self, count,appname,types):
        self.app = App(appname,types)
        self.counter = count
        self.alldata = [("timestamp", "elapsedtime")]

    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elpasedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        time.sleep(3)
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, elpasedtime))

    #多次执行测试过程
    def run(self):
        while self.counter >0:
            self.testprocess()
            self.counter = self.counter - 1

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToCSV(self):
        with open('startTime2.csv', 'w') as f :
            writer = csv.writer(f)
            writer.writerows(self.alldata)


if __name__ == "__main__":
    # pyinstaller - F launchTime.py
    print("请输入包名")
    app = input()
    print("请选择启动方式：\n1---冷启动\n2---热启动")
    while True:
        a = input()
        if a == '1' or a == '2' :
            break
        else:
            print("输入有误,请重新输入")
    print("请选择启动次数")
    while True:
        c = input()
        if c.isdigit():
            break
        else:
            print("输入有误,请重新输入")
    print("正在执行，请稍等")
    apprun =Controller(int(c),app,a)
    apprun.run()
    apprun.SaveDataToCSV()
    input("执行完毕，请关闭")