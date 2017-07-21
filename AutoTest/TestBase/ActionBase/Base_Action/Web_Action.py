# ！D:\AutoTest\ik_auto_test\py_auto_test\ik_utils
# Filename: ik_web_utils.py
# coding=utf-8
import inspect
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

import TestBase.ActionBase.Base_Action.Result_Action as TR

VALID_BROWSER_LIST = "Firefox"
LOGIN_USER = "user_input1"
LOGIN_PASSWORD = "psod_input1"
LOGIN_SUBMIT = "submit_land"

class Web_Action:
    def get_current_function_name(self):
        return inspect.stack()[1][3]

    def __init__(self, url, browser="Firefox", user="admin", pwd="admin"):
        self.driver = None
        self.url = url
        self.browser = browser
        self.user = user
        self.pwd = pwd
        self.ClassName = self.__class__.__name__

    def __del__(self):
        if self.driver:
            self.driver.quit()
            pass

    def refresh_page(self):
        self.driver.refresh()

    def open_webpage(self, url_arg):
        if "http" not in url_arg:
            url = "http://" + url_arg + "/"
        else:
            url = url_arg
        self.driver.set_page_load_timeout(5)
        self.driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL + 't')
        time.sleep(3)
        handles = self.driver.window_handles
        # print(handles)
        self.driver.switch_to_window(handles[1])
        try:
            self.driver.get(url)
        except:
            pass
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(handles[0])

    def test_ik_speed(self,url_arg):
        self.open_webpage(url_arg)
        time.sleep(30)
        self.driver.find_element_by_id("myButton").click()
        time.sleep(50)
        speed = []
        speed_down = self.driver.find_element_by_id('V').text
        speed_up = self.driver.find_element_by_id('j').text
        speed.append(speed_up)
        speed.append(speed_down)
        return speed

    def find_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath))

    def find_element_by_class_name(self, class_name):
        num = 1
        while num < 8:
            num += 1
            time.sleep(0.4)
            try:
                return self.driver.find_element_by_class_name(class_name)
            except:
                pass

        # return WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_class_name(class_name))
        # return self.driver.find_element_by_class_name(class_name)

    # def find_element_by_xpath(self, xpath):
    #     return self.driver.find_element_by_xpath(xpath)

    def find_element_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_element_by_css_selector(self, css_selector):
        # return WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_css_selector(css_selector))
        return self.driver.find_element_by_css_selector(css_selector)

    def find_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def wait_element_visible_by_xpath(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            return False
        return True

    def wait_element_invisible_by_xpath(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            return False
        return True

    def is_confirm_msg(self):
        alert = self.driver.switch_to.alert
        return alert

    def accept_confirm_msg(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def get_url(self):
        web_url = str(self.driver.current_url)
        return web_url

    def connect(self):
        FunctionName = self.get_current_function_name()
        test = TR.Result_Action(self.ClassName,FunctionName)
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.dir", "C:\\Users\\sujing\\Downloads\\")
        profile.set_preference("browser.download.folderList", "2")
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        if self.browser not in VALID_BROWSER_LIST:
            raise ValueError("Invalid browser: ", self.browser, " valid browser: ", VALID_BROWSER_LIST)

        if self.browser == "Firefox":
            self.driver = webdriver.Firefox(firefox_profile = profile)

        if "http" not in self.url:
            raise ValueError("Invalid url(%s), e.g http://16.16.1.1/" % self.url)

        self.driver.maximize_window() #窗口最大化
        self.driver.get(self.url)
        link = self.driver.find_element_by_id(LOGIN_USER)
        link.clear()
        link.send_keys(self.user)
        time.sleep(1)
        link = self.driver.find_element_by_id(LOGIN_PASSWORD)
        link.clear()
        link.send_keys(self.pwd)
        time.sleep(1)
        self.driver.find_element_by_class_name(LOGIN_SUBMIT).click()
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("首页"))
            return test.show_ok_result()
        except Exception as e:
            test.set_error("登录失败")
            return test.show_error_result()
            # print(e)

    def switch_to_frame(self, frame):
        self.driver.switch_to_frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to_default_content()


def switch_to_default_content(self):
    self.driver.switch_to_default_content()


if __name__ == "__main__":
    url = "http://172.16.175.1/"
    browser = "Firefox"
    user_name = "admin"
    password = "admin"
    web_handler = Web_Action(url, browser, user_name, password)
    web_handler.connect()
    web_handler.open_webpage("www.jd.com")
    time.sleep(2)


