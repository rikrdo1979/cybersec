import wmi
from printy import printy
from printy import inputy

w = wmi.WMI()
 
def get_all_installed_win10_store():
    try:
        for p in w.Win32_InstalledStoreProgram():
            if '-' in p.Name: continue
            app_name = str(p.Name).encode('utf8','ignore').decode()
            app_name = app_name.replace('.', ' ')
            print(str(p.InstallDate).encode('utf8','ignore').decode())
            print(app_name)
    except:
        pass # Handle errors here
  
def get_installed_product_software():
    year = []
    month = []
    day = []
    try:
        for p in w.Win32_Product():
            app_name = str(p.Name).encode('utf8','ignore').decode()
            es_date_time = p.InstallDate[0:]
            str_size = len(es_date_time)
            if str_size:
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
            else:
                continue
            print(es_date_time+ ' >>> ' +app_name)
    except:
        pass
  
def get_all_installed_win10_software():
    for p in w.Win32_InstalledWin32Program():
        print(str(p.Name).encode('utf8','ignore').decode())
	
#print(get_all_installed_win10_store())
print(get_installed_product_software())
#print(get_all_installed_win10_software())
