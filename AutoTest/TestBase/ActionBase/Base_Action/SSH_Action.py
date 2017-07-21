# ！D:\AutoTest\ik_auto_test\py_auto_test\ik_utils
# Filename: ik_ssh_utils.py
import paramiko
import time
import datetime
import TestBase.TopoBase as Topo

class IkSSHUtils:

    @classmethod
    def get_one_block_data(cls, input_str):
        out_lines = input_str.split('\n')
        block_data = []
        for line in out_lines:
            if line is "":
                break
            block_data.append(line)
        return block_data

    @classmethod
    def parse_data_to_dict(cls, input_str, sep=':'):
        ret_dict = {}
        for line in input_str:
            sep_values = line.split(sep)
            if len(sep_values) >= 2:
                name = sep_values[0]
                value = sep_values[1]
                name = name.strip(' ')
                value = value.strip(' ')
                ret_dict[name] = value
        return ret_dict

    @classmethod
    def DeleteNull(cls,input_str):
        ret_str=[]
        len1 = len(input_str)
        for i in range(0, len1):
            if input_str[i] != "":
                ret_str.append(input_str[i].strip(" "))
            else:
                continue
        return ret_str

    @classmethod
    def GetRoute(cls,input_str):
        new_str = input_str.split("\n")
        RouteName = new_str[1].split(" ")
        RouteData = new_str[2].split(" ")
        str1 = IkSSHUtils.DeleteNull(RouteName)
        str2 = IkSSHUtils.DeleteNull(RouteData)
        len1 = len(str1)
        RouteDict = {}
        for i in range(0, len1):
            RouteDict[str1[i]] = str2[i]
        return RouteDict

    @classmethod
    def GetNF_Conntrack(cls,input_str):
        new_str = input_str.split("skb_mark=0")
        len1 = len(new_str)
        DNSdata = []
        for i in range(0, len1):
            new = new_str[i].split(" ")
            if new == " ":
                continue
            dictstr = {}
            for str in new:
                if "=" not in str:
                    continue
                else:
                    newstr = str.split("=")
                    name = newstr[0].strip(" ")
                    value = newstr[1].strip(" ")
                    dictstr[name] = value
            if len(dictstr) > 0:
                DNSdata.append(dictstr)
        return DNSdata

class IkSSHHandler:
    def __init__(self, host, port=22, user="sshd", pwd="www.ikuai8.com"):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.ssh = None

    def __del__(self):
        if self.ssh:
            self.ssh.close()

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.pwd,timeout=10)

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        orig_result = stdout.read()
        str_result = orig_result.decode("utf-8")
        return str_result

if __name__ == "__main__":
    handler = IkSSHHandler("192.168.123.1")
    handler.connect()
    address = handler.exec_cmd('nslookup www.qq.com | grep -A 5 Name | awk \'{print $3}\' | grep [0-9] | sed ":a ;N;s/\\n/|/;t a;"')
    print('%r test' % address)
    address = address.replace("\n","")
    print('%r test' % address)
    test = handler.exec_cmd('cat /proc/net/nf_conntrack | grep -E ' + address + ' | grep '+ Topo.TEST_PC + '|grep wan2  | wc -l')
    print(test)











