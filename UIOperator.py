from appium import webdriver
import time
import subprocess
class UIOperator:
    driver : webdriver = None
    cur_handle = None

    def __init__(self,driver) -> None:
        self.driver = driver

    def click(self,element):
        """
        点击
        :param element: 点击元素
        :return: 
        """
        element.click()

    def sleep(self,t):
        """
        睡眠
        :param t:睡眠时间
        """
        time.sleep(t)

    def longclick(self,coordinate,t):
        """
        长按
        :param coordinate: 坐标
        :param t: 时间
        :return: 
        """
        self.driver.tap(coordinate,t)

    def findElementByXpath(self,xpath):
        """
        通过xpath来查找元素
        :param xpath 
        :return: WebElement
        """
        return self.driver.find_element_by_xpath(xpath)

    def findElementByCss(self,css):
        """
        通过css来查找元素
        :param css
        :return: WebElement
        """
        return self.driver.find_element_by_css_selector(css)

    def findElementByUiautomator(self,uiautomator):
        """
        通过uiautomator语句来查找元素
        :param uiautomator
        :return: WebElement
        """
        return self.driver.find_element_by_android_uiautomator(uiautomator)

    def input(self,content):
        """
        输入文本（需要先focus输入框再调用该方法）
        :param content: 输入文本
        :return: None
        """
        print("输入文本："+content)
        subprocess.call("adb shell am broadcast -a ADB_INPUT_TEXT --es msg "+content, shell=True)

    def tap(self,x,y):
        """
        根据坐标点击
        :param x: x坐标
        :param y: y坐标
        :return: None
        """
        self.driver.tap([(x,y)])

    def swipe(self,x1,y1,x2,y2):
        """
        从某一点滑动到令一点
        :param x1: 起点x坐标 
        :param y1: 起点y坐标  
        :param x2: 终点x坐标
        :param y2: 终点y坐标
        :return: None
        """
        self.driver.swipe(x1,y1,x2,y2)

    def getContexts(self):
        """
        返回当前的contexts
        :return: contexts
        """
        return self.driver.contexts

    def keyevent(self,key):
        """
        发送keycode给手机
        :param key
        :return: None
        """
        return self.driver.keyevent(key)

    def getWindowWidth(self):
        """
        获得屏幕宽度
        :return: 
        """
        return self.driver.get_window_size()['width']

    def getWindowHeight(self):
        """
        获得屏幕高度
        :return: 
        """
        return self.driver.get_window_size()['height']

    def switchToWebView(self,context):
        """
        根据context切换到webview
        :param context
        :return: None
        """
        self.driver.switch_to.context(context)

    def switchToNative(self):
        """
        切换到Native模式
        :return: None
        """
        self.driver.switch_to.context('NATIVE_APP')

    def getHandles(self):
        """
        获取当前所有句柄
        :return: 句柄集合
        """
        return self.driver.window_handles

    def switchToWindow(self,window):
        """
        根据句柄切换窗口
        :param window:句柄 
        :return: None
        """
        self.driver.switch_to.window(window)

    def getPageSource(self):
        """
        获取页面源代码
        :return: 源码
        """
        return self.driver.page_source


    def switchToWindowByContent(self,content):
        """
        根据页面内唯一标识来切换窗口
        :param content: 唯一标识，字符串类型
        :return: None
        """
        handles = self.getHandles()
        for i in handles:
            print(i)
            self.switchToWindow(i)
            source = self.getPageSource()
            if (source.__contains__(content)):
                print("已跳转至目的页面！")
                self.cur_handle = i
                break



