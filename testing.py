from ncclient import manager
import xml.etree.ElementTree as ET

device_ip = '10.10.20.100'
def get_vlans():
    subtree_path = '''      
                <vlans xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan-oper">
                <vlan>
                <id></id>
                <vlan-interfaces>
                    <interface>
                    </interface>
                </vlan-interfaces>
                </vlan>
                </vlans>
                '''
    vlan_list = []
    with manager.connect(host=device_ip, port=830, username=user, password=user_pwd, hostkey_verify=False, device_params={'name':'iosxe'}) as m:
        c = str(m.get(filter=('subtree', subtree_path)))
        data = ET.fromstring(c)
        for child in data[0][0]:
            vlan_list.append(child[0].text)
        print('VLANS CURRENTLY CONFIGURED: ',vlan_list)
        return vlan_list


def main():
    get_vlans()
main()