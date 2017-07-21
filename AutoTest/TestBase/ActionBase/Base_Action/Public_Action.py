# -*- coding:utf-8 -*-
import xlrd
import subprocess,traceback,platform
import json
import codecs
import time
import redis
import TestBase.TopoBase as Topo
import sys,os
sys.path.append("..\\..")

def ReadData(Path,SheetName):
    DATA_LIST = []
    wb = xlrd.open_workbook(Path)
    sh = wb.sheet_by_name(SheetName)
    row = sh.nrows
    col = sh.ncols
    for i in range(1, row):
        data = {}
        for j in range(0, col):
            data[str(sh.cell_value(0, j)).strip()] = str(sh.cell_value(i, j)).strip()
        DATA_LIST.append(data)
    return DATA_LIST

def read_keys(redis, keys=''):
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # test = redis.Redis()
    keys = redis.get(keys)
    keys = str(keys, encoding='utf8')
    keys = eval(keys)
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    return keys

def ReadElement(Path,SheetName):
    i = 0
    data = {}
    wb = xlrd.open_workbook(Path)
    sh = wb.sheet_by_name(SheetName)
    while (1):
        try:
            sh.cell_value(i, 0)
            data[sh.cell_value(i, 0).strip()] = sh.cell_value(i, 1).strip()
            i = i + 1
        except:
            break
    return data


#如果有键,就不进行操作.
def write_excel_to_redis(PATH, SheetName, name):
    Elements = ReadElement(PATH, SheetName)
    write_redis = redis.Redis(host=Topo.Redis_Server,port=Topo.Redis_Server_Port)
    write_redis.set('ElementBase.'+name, Elements, nx=True)


#如果没有键,就不进行操作.
def updata_excel_to_redis(PATH, SheetName, name):
    Elements = ReadElement(PATH, SheetName)
    write_redis = redis.Redis(host=Topo.Redis_Server, port=Topo.Redis_Server_Port)
    write_redis.set('ElementBase.' + name, Elements, xx=True)


def write_data_to_json(path, sheetname):
    file_path = "E:\\Git_AutoTest\\TestData\\test\\"
    DATA_LIST = ReadData(path, sheetname)
    json_str = json.dumps(DATA_LIST, ensure_ascii=False)
    file = file_path + sheetname + ".json"
    fp = codecs.open(file, 'w', "utf-8")
    fp.write(json_str)
    fp.close()


def read_json_data(file_path, filename):
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    file_path = file_path + filename + ".json"
    fp = open(file_path, "r", encoding="utf-8")
    json_str = fp.read()
    array = json.loads(json_str)
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    return array

def ping(host, num=5):
    if platform.system() == "Windows":
        cmd = "ping -n %d %s" % (num, host)
    else:
        cmd = "ping -c %d %s" % (num, host)
    try:
        p = subprocess.Popen(args=cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (stdoutput,erroutput) = p.communicate()
        info=stdoutput.decode("gb2312")
        if info.find("TTL")>1:
            return True
        else:
            return False
    except:
        traceback.print_exc()


def nslookup(host):
    cmd = "nslookup " + host
    try:
        p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutput, erroutput) = p.communicate()
        info = stdoutput.decode("gb2312")
        # print(info)
        if info.find("timed out") > 0 or info.find("Query refused")>0:
            return False
        else:
            return True
    except:
        traceback.print_exc()

def windows_cmd(cmd):
    try:
        p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # (stdoutput, erroutput) = p.communicate()
        # info = stdoutput.decode("gb2312")
        # print(info)
    except:
        traceback.print_exc()

if __name__ == "__main__":
    print("test")

    #下面是从EXCEL导入到JSON
    #     array = ["登录"]
    # path = "E:\\Git_AutoTest\\TestData\\excel_data\\TestData_SystemSettings.xlsx"
    # print(path)
    # for name in array:
    #     sheetname = name
    #     write_data_to_json(path, sheetname)

    # 将新建的元素表，从EXCEL导入到REDIS数据库  更新redis keys --> updata_excel_to_redis()
    # print(os.getcwd())
    path = "..\\..\\..\\ElementBase\\ElementBase_FlowControl.xlsx"
    test = ['MAC限速']
    redis_name = "MACSpeedLimit"
    for name in test:
        sheetname = name
        write_excel_to_redis(path, name, redis_name)

    # 更新已存在的元素表，从EXCEL导入到REDIS数据库  更新redis keys --> updata_excel_to_redis()
    # print(os.getcwd())
    # path = "..\\..\\..\\ElementBase\\ElementBase_NetworkSettings.xlsx"
    # test = ['模块目录']
    # redis_name = "Menu"
    # for name in test:
    #     sheetname = name
    #     updata_excel_to_redis(path, name, redis_name)

    #从REDIS数据库读出元素
    test = redis.Redis()
    elem = read_keys(test,"ElementBase.MACSpeedLimit")
    print(elem)


