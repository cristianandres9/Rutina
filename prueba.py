import subprocess
uptime = subprocess.check_output("uptime | awk '{print $3}'", shell=True,universal_newlines=True)
pwd = subprocess.check_output("pwd", shell=True)
print(uptime, pwd)
uptime2 = subprocess.check_output("uptime | awk '{print $3}'", shell=True)
print(uptime2)

file1 = open("/home/cristian/Codigos/Prueba/1RUTINA.txt", "w")
str1 = repr(uptime)
str2 = repr(pwd)
file1.write('uptime = '+ str1 + "\n")
file1.write('pwd = ' + str2 + "\n")
file1.close()