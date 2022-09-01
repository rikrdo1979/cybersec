import winreg
from printy import printy
from printy import inputy
import os
import glob
import time
import datetime
 
def search_datetime(path):
    path = path+'\\*'
    path = min(glob.glob(path, recursive=True), key=os.path.getmtime)
    print(path)
    dtime = os.stat(path).st_ctime
    format(datetime.fromtimestamp(dtime).strftime("%d/%m/%Y - %H:%M:%S"))
    filer = os.path.basename(path)
    print(filer)

    
    

def intalled_software():
    year = []
    month = []
    day = []

    locations = {'winreg.KEY_WOW64_32KEY' : 'winreg.HKEY_LOCAL_MACHINE'  , 'winreg.KEY_WOW64_64KEY' : 'winreg.HKEY_LOCAL_MACHINE' , '0' : 'winreg.HKEY_CURRENT_USER'}

    for loc in locations:
        aReg = winreg.ConnectRegistry(None, eval(locations[loc]))
        aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                              0, winreg.KEY_READ | eval(loc))
     
        count_subkey = winreg.QueryInfoKey(aKey)[0]

        for i in range(count_subkey):

            try:
                asubkey_name = winreg.EnumKey(aKey, i)
                asubkey = winreg.OpenKey(aKey, asubkey_name)
                name = winreg.QueryValueEx(asubkey, "DisplayName")[0]
                if winreg.QueryValueEx(asubkey, "InstallLocation")[0]:
                    path = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
                    search_datetime(path)
                else:
                    path = 'undefined'
                try:
                    es_date_time = winreg.QueryValueEx(asubkey, "InstallDate")[0]
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
                    year = []
                    month = []
                    day = []
                except EnvironmentError:
                    es_date_time = 'undefined'
            except EnvironmentError:
                continue
            printy('  [rB]'+es_date_time+'@ >>> [gB]'+ name+'@')
               
intalled_software()