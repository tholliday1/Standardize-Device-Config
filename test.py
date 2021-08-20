from ncclient import manager
import getpass

device_ip = '10.10.20.100'
user = input("Enter Username: ",)
user_pwd = getpass.getpass("Enter Password: ",)

def get_running():
    with manager.connect(host=device_ip, port=830, username=user, password=user_pwd, hostkey_verify=False, device_params={'name':'iosxe'}) as m:
        c = m.get_config(source='running').data_xml
        with open("running_config.xml", 'w') as f:
            f.write(c)

def main():
    get_running()
main()