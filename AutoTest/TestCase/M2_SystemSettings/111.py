# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time


class Web_Test:
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.accept_next_alert = True

    def open_webpage(self):
        driver = self.driver
        driver.get(self.base_url[0]+ '/')
        for url in self.base_url:
            driver.get(url + '/')
            time.sleep(10)

    def close_webpage(self):
        self.driver.quit()


if __name__ == "__main__":
    url = ["http://www.jd.com/","http://www.qq.com/","http://www.hao123.com/","http://www.tmall.com/"]
    IKSP = Web_Test(url)
    IKSP.open_webpage()
    IKSP.close_webpage()