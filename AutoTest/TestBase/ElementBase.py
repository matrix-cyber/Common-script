import sys
import TestBase.ActionBase.Base_Action.Public_Action as PF
sys.path.append("..")
import time
import redis

class ElementBase_from_xls:
    # 网络设置
    # PATH_WanSettings= "E:\\Git_AutoTest\\ElementBase\\ElementBase_NetworkSettings.xlsx"
    # Menu = PF.ReadElement(PATH_WanSettings, "模块目录")
    # WAN_Public = PF.ReadElement(PATH_WanSettings, "外网公共")
    # LanSettings = PF.ReadElement(PATH_WanSettings, "内网设置")
#     StaticIP = PF.ReadElement(PATH_WanSettings, "静态IP")
#     DHCP = PF.ReadElement(PATH_WanSettings, "DHCP")
#     ADSL = PF.ReadElement(PATH_WanSettings, "ADSL")
#     Adsl_by_Vlan = PF.ReadElement(PATH_WanSettings, "基于VLAN的多拨")
#     StaticIP_by_Vlan = PF.ReadElement(PATH_WanSettings, "基于VLAN的静态IP")
#     Adsl_by_Lan = PF.ReadElement(PATH_WanSettings, "基于物理网卡的多拨")
#     PortFlow = PF.ReadElement(PATH_WanSettings, "端口分流")
#     ProFlow = PF.ReadElement(PATH_WanSettings, "协议分流")
#     UpDownFlow = PF.ReadElement(PATH_WanSettings, "上下行分离")
#     DnsSettings = PF.ReadElement(PATH_WanSettings, "DNS设置")
#     MultiDns = PF.ReadElement(PATH_WanSettings, "多线路DNS")
#     DhcpSettings = PF.ReadElement(PATH_WanSettings, "DHCP设置")
#     MultiRoute = PF.ReadElement(PATH_WanSettings, "多线负载")
#
#     # 系统设置
#     PATH_SafeSettings = "E:\\Git_AutoTest\\ElementBase\\ElementBase_SafeSettings.xlsx"
#     WebAccountMange = PF.ReadElement(PATH_SafeSettings, "WEB账号管理")
#
    #流控设置
    PATH_FlowControl = "E:\\Git_AutoTest\\ElementBase\\ElementBase_FlowControl.xlsx"
    SmartControl = PF.ReadElement(PATH_FlowControl, "一键流控")
    StrategyControl = PF.ReadElement(PATH_FlowControl, "手工流控")
    IPSpeedLimit = PF.ReadElement(PATH_FlowControl, "IP限速")
#
#     def abc(self):
#         print('abc')

class ElementBase:
    #网络设置
    test = redis.Redis()
    Menu = PF.read_keys(test, 'ElementBase.Menu')
    WAN_Public = PF.read_keys(test,  'ElementBase.WAN_Public')
    LanSettings = PF.read_keys(test,  'ElementBase.LanSettings')
    StaticIP = PF.read_keys(test,  'ElementBase.StaticIP')
    DHCP = PF.read_keys(test,  'ElementBase.DHCP')
    ADSL = PF.read_keys(test,  'ElementBase.ADSL')
    Adsl_by_Vlan = PF.read_keys(test,  'ElementBase.Adsl_by_Vlan')
    StaticIP_by_Vlan = PF.read_keys(test,  'ElementBase.StaticIP_by_Vlan')
    Adsl_by_Lan = PF.read_keys(test,  'ElementBase.Adsl_by_Lan')
    PortFlow = PF.read_keys(test,  'ElementBase.PortFlow')
    ProFlow = PF.read_keys(test,  'ElementBase.ProFlow')
    UpDownFlow = PF.read_keys(test, 'ElementBase.UpDownFlow')
    DnsSettings = PF.read_keys(test, 'ElementBase.DnsSettings')
    MultiDns = PF.read_keys(test, 'ElementBase.MultiDns')
    DhcpSettings = PF.read_keys(test, 'ElementBase.DhcpSettings')
    MultiRoute = PF.read_keys(test, 'ElementBase.MultiRoute')

    # 系统设置
    WebAccountMange = PF.read_keys(test, 'ElementBase.WebAccountMange')

    # 流控设置
    SmartControl = PF.read_keys(test, 'ElementBase.SmartControl')
    StrategyControl = PF.read_keys(test, 'ElementBase.StrategyControl')
    IPSpeedLimit = PF.read_keys(test,'ElementBase.IPSpeedLimit')
    MACSpeedLimit = PF.read_keys(test, 'ElementBase.MACSpeedLimit')

if __name__ == "__main__":
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # Element = ElementBase.PortFlow
    # print(Element)
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    #从EXCEL导入到REDIS数据库
    sheetname = ['IPSpeedLimit']
    for name in sheetname:
        e = ElementBase_from_xls()
        print(getattr(e, name))
        Element = getattr(e, name)
        test = redis.Redis(host="192.168.30.3",port="16379")
        test.set('ElementBase.'+name, Element)


