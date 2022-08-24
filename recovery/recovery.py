#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "rikrdo"
__copyright__ = "Copyright 2022, Bootcamp Cybersec "
__credits__ = ["rikrdo"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "rikrdo"
__email__ = "rikrdo@rikrdo.es"
__status__ = "Production"

print('''                         
         ...           ...      
        (- -)         (- o)
    ooO--(_)--Ooo-ooO--(_)--Ooo-
    ''')

# import OS module
import os, datetime, subprocess, wmi, sys, winreg
from Registry import Registry
from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER
)
 
# get list of recent files
path = r'C:\Users\vagrant\AppData\Roaming\Microsoft\Windows\Recent'
# list all the files in the recent folder
dir_list = os.listdir(path)

print("\n  | RECENT ACCESSED FILES | \n")

for files in dir_list:
    access_time = os.path.getatime(path+'//'+files)
    last_access = format(datetime.datetime.fromtimestamp(access_time).strftime("%d-%m-%Y - %H:%M:%S"))
    print (" ",last_access," >>> ", files)

print('')

# # traverse the software list
# Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
# a = str(Data)

# # try block
# try:
    
    # # arrange the string
    # for i in range(len(a)):
        # print(a.split("\\r\\r\\n")[6:][i])
  
# except IndexError as e:
    # print("All Done")

w = wmi.WMI()
for p in w.Win32_Product():
    print (str(p.Caption))
    

# with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hive:
    # with OpenKey(hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0, KEY_ALL_ACCESS) as hosts_key:
        # num_of_values = QueryInfoKey(hosts_key)[1]
        # for i in range(num_of_values):
            # values = EnumValue(hosts_key, i)
            # print(values)

print("****************") 

#connecting to key in registry
access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)

access_key = winreg.OpenKey(access_registry,r"SOFTWARE\SMicrosoft\Currentversion\Search\RecentApps")
#accessing the key to open the registry directories under
for n in range(20):
   try:
      x =winreg.EnumKey(access_key,n)
      print(x)
   except:
      break

#Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\* | select-object DisplayName
