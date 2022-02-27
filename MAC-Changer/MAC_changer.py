import subprocess
import os
import json
import optparse

try:
    env_typ = os.environ['SHELL']
    print(env_typ)
    if str(env_typ).capitalize() == 'ZSH' or 'BASH':
        try:
            parser_handler = optparse.OptionParser()
            parser_handler.add_option("-i", '--interface', dest="interface", help="Target interface for the MAC Address change")
            parser_handler.parse_args()


            subprocess.call(["ifconfig"], shell=True)
            user_defined_interface = str(input("Interface > "))
            user_defined_MAC = str(input("New MAC Address > "))
            print_string = "[+] Changing MAC Address for "+user_defined_interface+" to "+user_defined_MAC+"..."
            print(print_string)
            third_call = ["ifconfig ", user_defined_interface," hw ether ", str(user_defined_MAC)]
            subprocess.call("ifconfig eth0 down", shell=True)
            subprocess.call(third_call, shell=True)
            subprocess.call("ifconfig eth0 up", shell=True)
            subprocess.call("ifconfig", shell=True)

        except:
            print("Not Bash")        

    else:
        try:
            subprocess.call("ipconfig", shell=True)
        except:
            print("Not Unix Shell")

except:
    try:
        subprocess.call("ipconfig", shell=False)
    except:
        print("not Powershell")

