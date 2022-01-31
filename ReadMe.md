 This script simple checks a vendor website for a newer BIOS Firmware version.
 
 You will need to update the CURRENT_BIOS and url variables for your own system.
 ![Alt text](images/BIOS_Version_Vendor_Site.png?raw=true "Title")
 
 Additionally you will need to update the class name it is looking for and the string in the if block.
 
 In my case the BIOS version div tags are div-table-cell download-version and all the BIOS 
 versions start with an "F". 
 
  ![Alt text](images/BIOSClassScript.png?raw=true "Title")
 
 You can place this file in /usr/local/bin 
 
 Run chmod +x get_bios.py
 
 Run crontab -e and add the following entry
 @reboot sleep 300 && ./usr/local/bin/check_bios.py
 
 The above cronjob will run 5 minutes after every reboot

If the script cannot connect to the vendor website you will get a system message informing you.

If a newer version of BIOS is available a system message will pop up informing you.
