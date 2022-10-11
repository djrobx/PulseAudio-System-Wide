#!/bin/sh
if echo -e '\r?P\r' | nc -w 1 192.168.0.6 8102 | grep 'PWR2'; then 
  RESET="true"
  if sudo PULSE_RUNTIME_PATH=/var/run/pulse -u pulse pacmd list-sinks | grep '\<duplicate\>'; then
    RESET="false"
  fi
  [ "$RESET" = "true" ] && sudo systemctl --system stop pulseaudio.service
  echo -e '\rPO\r' | nc -w 1 192.168.0.6 8102
  sleep 10
  [ "$RESET" = "true" ] && sudo systemctl --system start pulseaudio.service && sleep 1
fi

