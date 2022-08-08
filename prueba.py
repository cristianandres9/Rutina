import subprocess

uptime = subprocess.check_output("uptime | awk '{print $3}'", shell=True,universal_newlines=True)
uptime = uptime.replace("\n","")

dic = dict({
    'UPTIME': uptime
})
h = str(dic)

with open("/opt/home/cristian.gil/Prueba/tex.json", "w") as x:
    x.write(h)