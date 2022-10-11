# PulseAudio-System-Wide
 Git to help you setup pulse audio as a system wide service. this has been tested and found to work on Raspberry Pi

## Run the following commands one after another. ```sudo``` should be used only where indicated.            
```
sudo apt-get update     
sudo apt-get install git    
cd /home/${USER}/       
git clone https://github.com/shivasiddharth/PulseAudio-System-Wide       
cd ./PulseAudio-System-Wide/      
sudo cp ./pulseaudio.service /etc/systemd/system/pulseaudio.service    
systemctl --system enable pulseaudio.service       
systemctl --system start pulseaudio.service       
sudo cp ./client.conf /etc/pulse/client.conf        
sudo sed -i '/^pulse-access:/ s/$/root,pi/' /etc/group    
```     
All done. Now you should have PulseAudio as a system service.     

# Shairport-Sync config with System Wide Pulse Aduio

Additional files in this with Shairport-Sync config in conjunction with a system-wide PulseAduio to support Airplay2

Goal:

Shairport-Sync with Airplay2 to an HDMI output of a Raspberry Pi 4 to an a/v receiver.   
A/v receiver powered on/off on demand (see scripts in opt)

Problems:

1) Plain ALSA config is flaky, and sometimes drops to very choppy audio
2) Shairport-sync documentation says to use dmix to solve this, but dmix does not work with HDMI / IEC958.
3) PulseAudio seems stable, but needs to be installed as a service to work on boot.
4) PulseAudio does not enable the HDMI port if the AV receiver is off at boot.
5) Some things suggest making it "Sticky" but that doesn't seem to be supported in PulseAudio 14.0 that Raspberry OS uses.
6) Need the power on script to restart PulseAudio if HDMI port is not present 
7) Shairport-sync will crash if PulseAudio was restarted. -> Set Shairport-sync service to auto-restart (see shairport-sync.service)

Because it took me 3 solid days of experimentation to get this to mostly work the way I wanted, I'm committing here for others to see and as a personal backup!




