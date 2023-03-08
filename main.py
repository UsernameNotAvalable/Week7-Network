# Router>enable
# Router#configure terminal
# Router(config)#enable secret Testing123
#
# Router(config)#ip domain-name testing123.com
# Router(config)#crypto key generate rsa
# 1024
# Router(config)#username Admin password Testing123
# Router(config)#line vty 0 4
# Router(config-line)#transport input ssh
# Router(config-line)#login local
#
# Router(config)#service password-encryption
#
# Router(config)#interface FastEthernet 0/0
# Router(config-if)#ip address 172.16.0.2 255.255.255.224
# Router(config-if)#no shutdown
#
# Exit
# Exit
# Show running-config
# Copy run
# Copy running-config st
# Copy running-config startup-config
# Write
# reload



#launch 2 vm - enable SMBv2/3 - can enable through powershell - document on the week 7 content


# SMB v2/v3
#  Detect:
# Get-SmbServerConfiguration | Select
# EnableSMB2Protocol
#  Disable:
# Set-SmbServerConfiguration -
# EnableSMB2Protocol $false
#  Enable:
# Set-SmbServerConfiguration -
# EnableSMB2Protocol $true
#  New-SmbShare –Name Syed_Shared –Path C:\Public\Shared
#  Get-SmbShareAccess Syed_Shared
#  Grant permission:
# Grant-SmbShareAccess –Name Syed_Shared –AccountName
# Everyone –AccessRight Full -force

#Getdown - password

the netcad backend - longest answer

1 - 2
2 - 1
3 - 3
4 - 1
5 - 2
6 - 1