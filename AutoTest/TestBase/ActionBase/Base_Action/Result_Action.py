# ! D:\AutoTest\ik_auto_test\py_auto_test\ik_web_autotest
# Filename: ik_web_test_stats.py
class Result_Action:
    def __init__(self,ClassName="",FunctionName=""):
        self.ret = True
        self.error = "Unknown Error"
        self.result = "OK"
        self.ClassName = ClassName
        self.FunctionName = FunctionName

    def set_error(self, error):
        if self.ret:
            self.ret = False
            self.result = error

    def show_ok_result(self):
        print("\t", self.ClassName, "—>", self.FunctionName, ":", "\033[1;32;m%s\033[0m" % "%s" % (self.result))

    def show_error_result(self):
        print("\t", self.ClassName, "—>", self.FunctionName,":", "\033[1;31;m错误：%s\033[0m" % "%s" % (self.result))


class Result_Count:
    def __init__(self):
        self.ErrorNum = 0
        self.RightNum = 0

    def add_RightNum(self):
        self.RightNum = self.RightNum + 1

    def add_ErrorNum(self):
        self.ErrorNum = self.ErrorNum + 1

    def show_all_result(self):
        print("*** 结果汇总 ***")
        print("总计：", self.ErrorNum + self.RightNum, "\n正确：", self.RightNum, "\n错误：", self.ErrorNum)


