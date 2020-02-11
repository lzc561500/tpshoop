import allure

from base.connect_mobile import TestConnetMobile
from page.loginPage import LoginPage
from base.base_yml import base_yml
import pytest
import time
class TestLgon:
    connet_mobil=TestConnetMobile()
    data = base_yml("login.yml","test_login")

    def setup_class(self):
       self.driver= self.connet_mobil.connectMobile()
       self.login_page =LoginPage(self.driver,10,1)

    allure.step("登录测试用例")
    @pytest.mark.parametrize("arg",data)
    #将解析过来的数据局传给一个参数，然后要用的时候进行拆分
    def test_login(self,arg):
        username = arg["userName"]
        password = arg["password"]
        fileName = arg["screenName"]
        #进入首页
        allure.attach("首页","进入淘宝首页")
        self.login_page.get_into_taobao()
        #输入用户名
        allure.attach("用户名"+username,"输入用户名")
        self.login_page.login_account(username)
        #输入密码
        allure.attach("用户密码","输入用户密码")
        self.login_page.login_psw(password)
        #点击登录
        allure.attach("点击登录按钮","点击登录按钮")
        self.login_page.element_click()
        #上传图片
        allure.attach("登录是否成功截图",open("./picture"+fileName+".png").read(),allure.attach_type.PNG)
        result=self.login_page.is_toast_exit("成功",10,0.5,fileName,True)
        assert result == True


    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()
