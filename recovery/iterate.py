locations = {'winreg.KEY_WOW64_32KEY' : 'winreg.HKEY_LOCAL_MACHINE'  , 'winreg.KEY_WOW64_64KEY' : 'winreg.HKEY_LOCAL_MACHINE' , '0' : 'winreg.HKEY_CURRENT_USER'}

for loc in locations:
	print (loc, ' : ', locations[loc])