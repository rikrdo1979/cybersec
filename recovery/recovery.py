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
    ''')

import os, datetime, subprocess, wmi, sys, winreg, sqlite3
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
             
    for a in range(1, len(animation)):
        printy("  Working... [n]"+animation[a]+"@", end='\r')
        sleep(0.01)
        print('                                   ', end='\r')

# Fechas de cambio de ramas de registro (CurrentVersionRun)
def branch():
    printy("\n  | [rB]CURRENT VERSION RUN@ | \n")
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hive:
        with OpenKey(hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0, KEY_ALL_ACCESS) as hosts_key:
            num_of_values = QueryInfoKey(hosts_key)[1]
            for i in range(num_of_values):
                values = EnumValue(hosts_key, i)
                if (values[0] == "InstallDate"):
                    dt_install = format(datetime.datetime.fromtimestamp(values[1]).strftime("%d-%m-%Y - %H:%M:%S"))
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
        last_access = format(datetime.datetime.fromtimestamp(access_time).strftime("%d-%m-%Y - %H:%M:%S"))
        print (" ",last_access," >>> ", files)

    inputy("\n  [gI]Press Enter to continue...@")
    installed_software()

# Programas instalados
def installed_software():
    printy("\n  | [rB]INSTALLED SOFTWARE@ | \n")

    for p in w.Win32_Product():
        progress()
        print (" ", str(p.Caption))
    
    inputy("\n  [gI]Press Enter to continue...@")
    open_apps()

# Programas abiertos
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
    reg_access()

# Historial de navegación
def browser_history():
    database_file = r'C:\Users\Vagrant\AppData\Local\Microsoft\Edge\User Data\Default\History'
    print(database_file)
    print ("Accessing Google Chrome browsing history.")
    db = sqlite3.connect(database_file)
    print(db)
    cursor = db.cursor()
    cursor.execute("SELECT * from urls")
    browsing_data = (cursor.fetchall())
    for record in browsing_data:
        visit_time = str(datetime.datetime(1601,1,1) + datetime.timedelta(microseconds=record[5]))
        if visit_time[:4] == "1601":
            pass
        else:
            visit_time = str(datetime.datetime.strptime(visit_time, "%d-%m-%Y %H:%M:%S"))
            visit_time = visit_time[:-7]
    printable = set(string.printable)
    visit_title = filter (lambda x: x in printable, record[2])
    visit_title = visit_title.replace(",","")
    visit_url = record[1]
    visit_line = visit_time + "," + "Website visited (Chrome)" + "," + "\"" + visit_title + "\"" + "," + "\"" + visit_url + "\"" + "," + username + "," + "," + "," + visit_time + "," + "," + "Google Chrome history" + "," + "History" + "\n"

    print(visit_line)

# Dispositivos conectados
def connected_devices():
    pass
    
# Eventos de log 
def log_events():
    pass

### HAPPY ENDING ###    
      
# pretty script end after ctrl + c

def exit_nice():
    print('\n -------------------------- *** Succesfully ends!!! *** ------------------------- \n')

def kill_key():
    print('\n -------------------------- *** Keyboard Interrupted!!! *** -------------------------', end="\r")
    sleep(0.5)
    print("                                                                                                          ", end="\r")

### MAIN ### 

def main():
    try:
        #branch()
        #open_apps()
        browser_history()
    except:
        print('\n  WTF!')

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        kill_key()
    finally:
        exit_nice()