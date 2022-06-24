#!/usr/bin/python
import os
import re
import subprocess
import time

report_path="/home/$USER/bandwidth_monitor/report/speedtest.csv"

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

response = response.decode('ascii')

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping[0] = ping[0].replace(',', '.')
download[0] = download[0].replace(',', '.')
upload[0] = upload[0].replace(',', '.')

try:
    if os.stat(report_path).st_size == 0:
        print ('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)')
except:
    pass

print ('{},{},{},{},{}'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping[0], download[0], upload[0]))
