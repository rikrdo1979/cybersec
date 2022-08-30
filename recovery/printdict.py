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
    if (key == 3):
        print (devices[key])