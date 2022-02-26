import subprocess
import optparse


parser = optparse.OptionParser()
interface =  input("Interface >")
new_mac = input("New MAC Address >")

print("[+] Changing MAC Address for "+interface+" to "+new_mac)

try:
    try:
        subprocess.call("ifconfig")
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw",'ether',new_mac])
        subprocess.call(["ifconfig",interface,"up"])
    except:
        print("Not GNU shell")
except:
    subprocess.call(["ipconfig",interface,""])
    #subprocess.call(["",,""])
    #subprocess.call(["",,""])
    