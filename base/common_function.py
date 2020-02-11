from selenium.webdriver.support.wait import WebDriverWait
from base.base_xpath import Xpath
class Fuction:

    def __init__(self,driver,timeout,clearance):
        self.driver=driver
        self.timeout=timeout
        self.clearance=clearance

    def find_element(self,loc):
        if not isinstance(loc,tuple):
                print("传的数据错误，如：loc=('id','value')")
        else:
                print("正在定位元素----定位方式：%s,value值---%s"%(loc[0],loc[1]))
                ele=WebDriverWait(self.driver,self.timeout,self.clearance).until(lambda x:x.find_element(*loc))
                return ele

    def find_elements(self,loc):
        if not isinstance(loc,tuple):
                print("传的数据错误，如：loc=('id','value')")
        else:
                print("正在定位元素----定位方式：%s,value值---%s"%(loc[0],loc[1]))
                eles=WebDriverWait(self.driver,self.timeout,self.clearance).until(lambda x:x.find_element(*loc))
                return eles

    def element_click(self,loc):
        ele=self.find_element(loc)
        ele.click()

    def send_keys(self,loc,text):
        ele=self.find_element(loc)
        ele.send_keys(text)

    def find_toast(self,message,timeout,clearance,fileName,is_screen_shot=False):
        loc = ("xpath","//*contains[(@text,'"+message+"')]")
        ele = self.find_element(loc,timeout,clearance)
        if is_screen_shot:
            self.screen_shoot(fileName)
        return ele.text

    def is_toast_exit(self,message,timeout,clearance,fileName,is_screen_shot=False):
        try:
            self.find_toast(message,timeout,clearance)
            if is_screen_shot:
                self.screen_shoot(fileName)
            return True
        except Exception:
            return False

    def screen_shoot(self,fileName):
        self.driver.get_screenshot_as_file("./picture"+fileName+".png")
