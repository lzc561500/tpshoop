from appium import webdriver


class TestConnetMobile:

    def connectMobile(self):
        desried_crap={}
        desried_crap["platformName"] = "Android"
        desried_crap["platformVersion"] ="5.1"
        desried_crap["deviceName"] = "192.168.161.101:5555"
        desried_crap["appPackage"] = "com.android.systemui"
        desried_crap["appActivity"] = ".recents.RecentsActivity"
        desried_crap["automationName"] = "uniautomator2"
        desried_crap["unicodeKeyboard"] = True
        desried_crap["resetKeyboard"] = True
        return webdriver.Remote("http://localhost:4723/wd/hub",desried_crap)




