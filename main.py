from appium import webdriver
from UIOperator import UIOperator

# 参数初始化
cur_handle = None
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'HUAWEI NXT-TL00'
desired_caps['browserName'] = "";
desired_caps['fastReset'] = False;
desired_caps['fullReset'] = False;
desired_caps['showChromedriverLog'] = True;
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['noReset'] = True

# 不加的话，识别webview的时候, 会把com.tencent.mm:tools的webview识别成com.tencent.mm的webview. 从而导致context切换失败
desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

# 不指定地址会提示Original error: No Chromedriver found
desired_caps[
    'chromedriverExecutable'] = '/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver'

# driver初始化
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

print("打开App")
operator = UIOperator(driver)

operator.sleep(3)
print("点击发现")
print(operator.getWindowHeight(),"*",operator.getWindowWidth())
operator.findElementByUiautomator("new UiSelector().text(\"发现\")").click()
operator.sleep(3)
operator.findElementByUiautomator("new UiSelector().text(\"搜一搜\")").click()
operator.sleep(5)
search_box = operator.findElementByUiautomator("new UiSelector().text(\"搜索\")")
search_box.click()
search_box.send_keys("meituanwaimai")

operator.tap(160,250)
operator.sleep(2)
operator.tap(160,250)
operator.sleep(3)
operator.tap(460,560)

# 切换webview
operator.sleep(5)
print("当前Contexts:",operator.getContexts())

# 长按
# operator.longclick([(500,500)],5000)
operator.switchToWebView("WEBVIEW_com.tencent.mm:tools")
# 切换handle，通过判断页面是否包含所需元素来判断该handle是否为目标handle
handles = operator.getHandles()
print(handles.__len__())
flag = False
operator.switchToWindowByContent("npm/@wmfe/wxapp-component-navigator/src/components/index")
operator.sleep(3)

print("开始点击！！！！！！！！！！！")
operator.findElementByXpath("/html/body/wx-view/wx-view/wx-view/wx-view/wx-wm-navigator[2]/wx-navigator/wx-view/wx-view").click()
operator.sleep(3)
operator.switchToWindowByContent("index-search-input")
operator.sleep(3)


operator.sleep(1)
operator.input("黄焖鸡")
operator.sleep(1)
operator.findElementByCss(".ui-btn.ui-btn-no-border.btn-search").click()
operator.sleep(6)

# swipe 滑动前需要先切换到native_app才能用
operator.switchToNative()
operator.sleep(3)
operator.swipe(500,1000,500,500)
operator.sleep(3)
operator.swipe(500,1000,500,500)
operator.sleep(3)
operator.tap(500,1100)

# 点击回退、降低音量、菜单键
operator.sleep(3)
operator.keyevent(4)
operator.sleep(3)
operator.keyevent(4)
operator.sleep(3)
operator.keyevent(24)
operator.sleep(3)
operator.keyevent(3)
driver.quit()
print("点击完成")
