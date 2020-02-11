from base.common_function import Fuction

class LoginPage(Fuction):
    loc=("id","com.tmall.wireless:id/ll_main_tab_container")
    loc_click = ("xpath","//*[contains(@text,'账户密码登录')]")
    loc_userName = ("id","com.taobao.taobao:id/aliuser_login_account_et")
    loc_password = ("id","com.taobao.taobao:id/aliuser_login_password_et")
    loc_btn = ("id","com.taobao.taobao:id/aliuser_login_login_btn")


    def get_into_tianmao(self):
        self.element_click(self.loc)
        self.element_click(self.loc_click)

    def login_account(self,text):
        self.send_keys(self.loc_userName,text)

    def login_psw(self,text):
        self.send_keys(self.loc_password,text)

    def click_login_btn(self):
        self.element_click(self.loc_btn)

