from netmiko import Netmiko
import time

device ={'host':'192.168.0.201','username':'cisco','password':'cisco','device_type':'cisco_ios','secret':'cisco'}
netCon = Netmiko(**device)

t = time.time()
out = netCon.send_command('show ip inte bri',delay_factor=2)
print(out)
t2= time.time()
print(t2-t)
t = time.time()
out = netCon.send_command_timing('show ip inte bri',last_read=1,read_timeout=20)
print(out)
t2= time.time()
print(t2-t)
t = time.time()


if not netCon.check_enable_mode():
    netCon.enable()

config_commands = [ 'logging buffered 20000',
                    'logging buffered 20010',
                    'no logging console' ]
output = netCon.send_config_set(config_commands)
print(output)
