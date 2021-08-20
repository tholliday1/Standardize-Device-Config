from ncclient import manager
import getpass
import pprint
import xml.dom.minidom
import xmltodict


device_ip = '10.10.20.100'
# user = input("Enter Username: ",)
# user_pwd = getpass.getpass("Enter Password: ",)

user = 'developer'
user_pwd = 'C1sco12345'

def get_running():
    with manager.connect(host=device_ip, port=830, username=user, password=user_pwd, hostkey_verify=False, device_params={'name':'iosxe'}) as m:
        c = m.get_config(source='running').data_xml
        with open("running_config.xml", 'w') as f:
            f.write(c)

def get_hostname():
    with manager.connect(host=device_ip, port=830, username=user, password=user_pwd, hostkey_verify=False, device_params={'name':'iosxe'}) as m:
        hostname =  m.get_config(source='running', filter=('xpath', '/native/hostname')).data_xml
        
        xmldict = xmltodict.parse(hostname)
        print ('Connecting to Switch:',xmldict['data']['native']['hostname'])
        return (xmldict['data']['native']['hostname'])



def main():
    # get_running()
    get_hostname()
main()