# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time

class IkSpeedtest:

    def __init__(self, url="http://www.speedtest.cn/"):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ik_speed(self):
        driver = self.driver
        driver.get(self.base_url+'/')
        time.sleep(30)
        driver.find_element_by_id("myButton").click()
        time.sleep(50)
        speed = []
        speed_down = driver.find_element_by_id('V').text
        speed_up = driver.find_element_by_id('j').text
        speed.append(speed_up)
        speed.append(speed_down)
        return speed

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    IKSP = IkSpeedtest("http://www.speedtest.cn/")
    test_speed = IKSP.test_ik_speed()
    IKSP.tearDown()

