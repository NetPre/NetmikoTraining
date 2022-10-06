from netmiko import Netmiko
import time

device ={'host':'192.168.0.201','username':'cisco','password':'cisco','device_type':'cisco_ios','secret':'cisco'}
netCon = Netmiko(**device)

# print(netCon.find_prompt())

def getoutputFile(netCon,file):
    time.sleep(0.1)
    out = netCon.read_channel()
    file.write(out)
    while out:
        time.sleep(0.1)
        print('-----while---')
        out = netCon.read_channel()
        file.write(out)        
    else:
        print('-----else---')
        time.sleep(2)
        out = netCon.read_channel()
        file.write(out)
        if out:
            getoutputFile(netCon, file)


def getoutput(netCon):
    finalOut = ''
    time.sleep(0.1)
    out = netCon.read_channel()
    finalOut +=out
    while out:
        time.sleep(0.1)
        print('-----while---')
        out = netCon.read_channel()        
        finalOut +=out
    else:
        print('-----else---')
        time.sleep(2)
        out = netCon.read_channel()
        finalOut +=out
        if out:
            finalOut = getoutput(netCon)
    return finalOut



def sendCommand(netCon, cmd):
    netCon.write_channel(cmd+'\n')
    getoutput(netCon)
            

def sendCommandFile(netCon, cmd,file):
    netCon.write_channel(cmd+'\n')
    getoutputFile(netCon,file)
            




netCon.enable()

t = time.time()
# with open('fileout.txt','w') as f:
#    sendCommandFile(netCon, 'show tech ',f)

sendCommand(netCon, 'show tech ')
t2=time.time()
print(t2-t)
t = time.time()

netCon.send_command_timing('show tech')

t2=time.time()
print(t2-t)
t = time.time()









