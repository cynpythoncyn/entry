
import base64
from appium import webdriver


def driver_name(device_Name):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": device_Name, # device_name android中可以随便写，iOS中不可以
        # app信息 包名和启动名
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        # "unicodeKeyboard":True,
        # "resetKeyboard":True,
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    return driver


if __name__ == "__main__":
    driver = driver_name("emulator-5554")
    # 1.获取当前应用的包名和启动名
    # print(driver.current_package)
    # print(driver.current_activity)
    # 2.打开指定的app，根据包名和启动名，获取方式（adb shell dumpsys window windows | findstr mFocusedApp ）
    # driver.start_activity("com.google.android.apps.messaging",".ui.ConversationListActivity")

    # 3.判断app是否已经安装，安装True 未安装 False
    print(driver.is_app_installed("com.android.settings"))
    # 4.发送文件到手机
    # data = str(base64.b64encode('test 123'.encode('utf-8')), 'utf-8')
    # driver.push_file('/sdcard/chen/test.txt', data)

    # 5.获取手机中的文件
    # data = driver.pull_file("/sdcard/chen/test.txt")
    # print(str(base64.b64decode(data), "utf-8"))

    # 6.定位app中一个元素
    # driver.find_element_by_class_name("android.widget.ImageButton").click()

    # 7.定位app中的多个元素
    elems = driver.find_elements_by_id("android:id/title")
    print(elems)
    print(type(elems))
    print(len(elems))
    # driver.close_app()


