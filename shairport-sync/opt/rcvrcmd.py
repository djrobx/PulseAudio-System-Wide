#!/bin/python

import telnetlib
import time
import sys
import os

host = "192.168.10.2"
port = 8102
telnet = telnetlib.Telnet(host, port)

def send_cmd(cmd):
  telnet.read_very_lazy()
  telnet.write(("{}\r\n").format(cmd).encode('ascii'))
  response = telnet.read_until(b"\n").rstrip().decode("utf-8")
  return response

def power_on():
  if (send_cmd('?P') == "PWR2"):
    print("Powering on")
    send_cmd('PO')
    time.sleep(9)
    os.system("sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd unload-module module-udev-detect")
    os.system("sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd unload-module module-remap-sink")
    os.system("sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd unload-module module-alsa-card")
    os.system("sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd load-module module-udev-detect")
    os.system("sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd load-module module-remap-sink sink_name=duplicate sink_properties=device.description=duplicate master=alsa_output.platform-fef00700.hdmi.hdmi-surround71 channels=8 master_channel_map=front-left,front-right,rear-left,rear-right,front-center,lfe,side-left,side-right channel_map=front-left,front-right,front-left,front-right,front-left,front-right,front-left,front-right remix=no")
    os.system("sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd set-default-sink duplicate")

def power_off():
  if (send_cmd('?P') == "PWR0"):
   print("Powering off")
   send_cmd('PF')

if (sys.argv[1] == "on"):
  power_on()
elif (sys.argv[1] == "off"):
  power_off()
else:
  print("Unknown request")

telnet.close()
