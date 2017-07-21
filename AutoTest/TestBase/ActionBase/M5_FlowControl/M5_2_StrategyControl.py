import sys

sys.path.append("..")
import TestBase.ElementBase as CSS
import TestBase.TopoBase as Topo
import time


class StrategyControl:

    def __init__(self, web_handler, ssh_handler, TestData):
        self.web_handler = web_handler
        self.ssh_handler = ssh_handler
        self.MenuCss = CSS.ElementBase.Menu
        self.ElementCss = CSS.ElementBase.StrategyControl
        self.TestData = TestData
        self.bool = True

    def find_element(self, pera):
        return self.web_handler.find_element_by_css_selector(pera)

    def find_element_value(self, pera, get):
        return self.web_handler.find_element_by_css_selector(pera).get_attribute(get)

    def check_on(self):
        return True

    def add_strategy(self):
        return True



