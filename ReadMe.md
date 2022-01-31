 This script simple checks a vendor website for a newer BIOS Firmware version.
 
 You will need to update the CURRENT_BIOS and url variables for your own system.
 
 You can place this file in /usr/local/bin 
 
 Run chmod +x get_bios.py
 
 Run crontab -e and add the following entry
 @reboot sleep 300 && ./usr/local/bin/check_bios.py
 
 The above cronjob will run 5 minutes after every reboot
