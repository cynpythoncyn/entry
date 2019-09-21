from appium import webdriver

def init_driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "12",  # device_name android中可以随便写，iOS中不可以
        # app信息 包名和启动名
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

    return driver