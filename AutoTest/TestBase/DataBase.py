import TestBase.ActionBase.Base_Action.Public_Action as PF

class TestData:
    file_path_network = "..\\TestData\\网络设置\\"
    Login = PF.read_json_data(file_path_network, "登录")
    LanSettings = PF.read_json_data(file_path_network, "内网设置")
    WAN_Public = PF.read_json_data(file_path_network, "外网公共")
    StaticIP = PF.read_json_data(file_path_network, "静态IP")
    DHCP = PF.read_json_data(file_path_network, "DHCP")
    ADSL = PF.read_json_data(file_path_network, "ADSL")
    Adsl_by_Vlan = PF.read_json_data(file_path_network, "基于VLAN的多拨")
    StaticIP_by_Vlan = PF.read_json_data(file_path_network, "基于VLAN的静态IP")
    Adsl_by_Lan = PF.read_json_data(file_path_network, "基于物理网卡的多拨")
    PortFlow = PF.read_json_data(file_path_network, "端口分流")
    ProFlow = PF.read_json_data(file_path_network, "协议分流")
    UpDownFlow = PF.read_json_data(file_path_network, "上下行分离")
    DnsSettings = PF.read_json_data(file_path_network, "DNS设置")
    MultiDns = PF.read_json_data(file_path_network, "多线路DNS")
    DhcpSettings = PF.read_json_data(file_path_network, "DHCP设置")
    MultiRoute = PF.read_json_data(file_path_network, "多线负载")

    file_path_flow_control = "..\\TestData\\流控设置\\"
    IPSpeedLimit = PF.read_json_data(file_path_flow_control, "IP限速")
    MACSpeedLimit = PF.read_json_data(file_path_flow_control, "MAC限速")


if __name__ == "__main__":
    test = TestData.PortFlow
    for data in test:
        print(data)