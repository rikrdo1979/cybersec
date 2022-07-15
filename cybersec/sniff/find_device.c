/* Compile with: gcc find_device.c -lpcap */
#include <pcap.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	char *device;                        /* Name of device (e.g. eth0, wlan0) */
	char error_buffer[PCAP_ERRBUF_SIZE]; /* Size defined in pcap.h */
	/* Find a device */
	device = pcap_findalldevs(error_buffer);
	if (device == NULL)
	{
		printf("Error finding device: %s\n", error_buffer);
		return (1);
	}
	printf("Network device found: %s\n", device);
	return (0);
}
