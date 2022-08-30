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
                 -ooO--(_)--Ooo-ooO--(_)--Ooo-
    _______   ____   ____  _______  __ ___________ ___.__.
    \_  __ \_/ __ \_/ ___\/  _ \  \/ // __ \_  __ <   |  |
     |  | \/\  ___/\  \__(  <_> )   /\  ___/|  | \/\___  |
     |__|    \___  >\___  >____/ \_/  \___  >__|   / ____|
                 \/     \/                \/       \/     
''')

import os, datetime, subprocess, wmi, sys, winreg, sqlite3, win32evtlog
from datetime import datetime
from Registry import Registry
from time import sleep
from printy import printy
from printy import inputy
from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER
)

### ACTIONS ###

# Initializing the wmi constructor
w = wmi.WMI()

def progress():
    #animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    #animation = ['|', '/', '-', '\\']
    animation = ["■         ","■■        ", "■■■       ", "■■■■      ", "■■■■■     ", "■■■■■■    ", "■■■■■■■   ", "■■■■■■■■  ", "■■■■■■■■■ ", "■■■■■■■■■■"]
    try:         
        for a in range(1, len(animation)):
            printy("  Working... [n]"+animation[a]+"@", end='\r')
            sleep(0.01)
            print('                                   ', end='\r')
    except:
        kill_nicelly()
        sys.exit(1)

def check_type(device):
    devices = {
        0: "Unknown",
        1: "No Root Directory",
        2: "Removable Disk",
        3: "Local Disk",
        4: "Network Drive",
        5: "CD",
        6: "RAM Disk"
    }

    for key in devices:
        if (key == device):
            dev_type = devices[key]
    return dev_type
        
# Fechas de cambio de ramas de registro (CurrentVersionRun)
def branch():
    printy("\n  | [rB]CURRENT VERSION RUN@ | \n")
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hive:
        with OpenKey(hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0, KEY_ALL_ACCESS) as hosts_key:
            num_of_values = QueryInfoKey(hosts_key)[1]
            for i in range(num_of_values):
                values = EnumValue(hosts_key, i)
                if (values[0] == "InstallDate"):
                    dt_install = format(datetime.fromtimestamp(values[1]).strftime("%d-%m-%Y - %H:%M:%S"))
                    print('  Installed date: ', dt_install)                
                    #print("\n\n ", values)
    inputy("\n  [gI]Press Enter to continue...@")
    recent_files()
    
    #Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\* | select-object DisplayName
    
# Archivos recientes
def recent_files():
    printy("\n  | [rB]RECENT ACCESSED FILES@ | \n")
    # get list of recent files
    path = r'C:\Users\vagrant\AppData\Roaming\Microsoft\Windows\Recent'
    # list all the files in the recent folder
    dir_list = os.listdir(path)

    for files in dir_list:
        progress()
        access_time = os.path.getatime(path+'//'+files)
        last_access = format(datetime.fromtimestamp(access_time).strftime("%d-%m-%Y - %H:%M:%S"))
        print (" ",last_access," >>> ", files)

    inputy("\n  [gI]Press Enter to continue...@")
    installed_software()

# Programas instalados
def installed_software():
    app_list = set()
    app_list_all = set()
    year = []
    month = []
    day = []

    printy("\n  | [rB]INSTALLED SOFTWARE@ | \n")
    
    #$Apps += Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" # 32 Bit
    #$Apps += Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*"             # 64 Bit

    for p in w.Win32_Product():
        progress()
        app_list.add(p.Name)
        es_date_time = p.InstallDate[0:]
        for i in range(0, len(es_date_time)):
            if i < 4:
                year.append(es_date_time[i])
            elif (i < 6 and i > 3):
                month.append(es_date_time[i])
            else:
                day.append(es_date_time[i])
        str_year = "".join(str(y) for y in year)
        str_month = "".join(str(m) for m in month)
        str_day = "".join(str(d) for d in day)
        es_date_time = str_day+'/'+str_month+'/'+str_year
        printy('  [rB]'+es_date_time+'@ >>> [gB]'+ str(p.Caption)+'@')
        
        year = []
        month = []
        day = []
    
    for inst in w.Win32_InstalledWin32Program ():
        progress()
        print('ALL: ', app_list_all.add(inst.Name))
    
    inputy("\n  [gI]Press Enter to continue...@")
    open_apps()

# Programas abiertos - OK
def open_apps():
    printy("\n  | [rB]OPEN APPS@ | \n")
    app_set = set()
    # Iterating through all the running processes
    for process in w.Win32_Process():
        progress()
        if not process.Name in app_set:
            print(" " , process.Name)
        app_set.add(process.Name)
    
    inputy("\n  [gI]Press Enter to continue...@")
    browser_history()

# Historial de navegación
def browser_history():
    printy("\n  | [rB]BROWSER HISTORY@ |")
    browswers_list = []
    browswers_list.append(os.path.expanduser('~')+r'\AppData\Local\Microsoft\Edge\User Data\Default')
    browswers_list.append(os.path.expanduser('~')+r'\AppData\Local\Google\Chrome\User Data\Default')
    #firefox = os.path.expanduser('~')+r'\AppData\Local\Google\Chrome\User Data\Default'
    for browser in browswers_list:
        try:
            if (os.path.isdir(browser)):
                browser_name = browser.split('\\')[6]
                printy('\n  | [rB]'+browser_name.upper()+'@ |\n')        
                files = os.listdir(browser)
                history_db = os.path.join(browser, 'history')
                db = sqlite3.connect(history_db)
                cursor = db.cursor()
                cursor.execute("SELECT url, title, datetime(urls.last_visit_time/1000000-11644473600, 'unixepoch') last_visit_time from urls")
                browsing_data = (cursor.fetchall())
            
            for record in browsing_data:
                progress()
                es_date_time = datetime.strftime((datetime.strptime(record[2], '%Y-%m-%d %H:%M:%S')),'%d-%m-%Y - %H:%M:%S')
                printy('  [rB]'+es_date_time+'@ >>> [gB]'+record[0]+'@')
        except:
            pass
    inputy("\n  [gI]Press Enter to continue...@")
    connected_devices()

# Dispositivos conectados
def connected_devices():
    printy("\n  | [rB]CONNECTED DEVICES@ |\n")
    today = datetime.today()
    today = today.strftime("%d-%m-%Y - %H:%M:%S")
    print("  NOW:", today)
    if w.Win32_PhysicalMedia():
        for item in w.Win32_PhysicalMedia():
            if item.Name:
                print("  ITEM: ", item.Name)
    else:
        print("No Physical Media devices")

    for drive in w.Win32_DiskDrive():
        print("  DRIVE:", drive.Name)

    for disk in w.Win32_LogicalDisk():
        print("  DISK: ", disk.Name)
        print("  DISK TYPE: ", check_type(disk.DriveType))

    for usb in w.Win32_USBController():
        print("  USB: ", usb.Name)
        
    inputy("\n  [gI]Press Enter to continue...@")
    log_events()
    
# Eventos de log 
def log_events():
    printy("\n  | [rB]LOG EVENTS@ |\n")
    server = 'localhost'
    logtype = 'Application'
    h = win32evtlog.OpenEventLog(None,'EventLogRegister')
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(h)
    num = 0
    while 1:
        events = win32evtlog.ReadEventLog(h,flags,0)
        if not events:
            break
        for event in events:
            es_date_time = event.TimeGenerated.strftime("%d-%m-%Y - %H:%M:%S")
            printy('  [rB]'+es_date_time+'@ >>> [gB]'+str(event.EventID)+' - '+event.SourceName+'@')
        num = num + len(events)
        print ("  Log record read",len(events))
    if total == num:
        print ("\n  Total number of Event records ",total)
        print ("  Log record read",len(events))
    else:
        print ("  Couldn't get all records - reported %d, but found %d" % (total, num))
        print ("  (Note that some other app may have written records while we were running!)")
    win32evtlog.CloseEventLog(h)

### HAPPY ENDING ###    
      
# pretty script end after ctrl + c

def exit_nicelly():
    print('\n -------------------------- *** Succesfully ends!!! *** ------------------------- \n')

def kill_nicelly():
    print('\n -------------------------- *** Keyboard Interrupted!!! *** -------------------------', end="\r")
    sleep(0.5)
    print("                                                                                                          ", end="\r")

### MAIN ### 

def main():
    #try:
    installed_software()
        #branch()
        #open_apps()
        #browser_history()
        #connected_devices()
        #log_events()
    #except:
        #print('\n  WTF!')

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        kill_nicelly()
    finally:
        exit_nicelly()