int	main(void)
{
	char	errbuf[PCAP_ERRBUF_SIZE + 1];
	FILE	*fp;
		goto prompt;

	pcap_if_t *iface, *devs;
	int j, i;
	printf("Copyright (C) Ahmed Samy 2014 <f.fallen45@gmail.com>\n\n");
	printf("\t\t\tNetwork Traffic Analyzer\n");
	if (pcap_findalldevs(&devs, errbuf) == -1 || !devs)
	{
		fprintf(stderr, "No network devices are currently connected\n");
		return (1);
	}
	printf("Enabled Network Devices:\n");
	for (i = 1, iface = devs; iface; iface = iface->next)
		printf("%d - %s\n", i++, iface->description);
prompt:
	printf("Device Index> ");
	scanf("%d", &j);
	/* Find the interface pointer.  */
	for (i = 1, iface = devs; iface && i != j; iface = iface->next, ++i)
		;
	if (!iface)
	{
		fprintf(stderr, "Invalid device index %d, please try again.", j);
	}
	c = capture_new();
	c->capture_fn = print_data;
	if (!capture_set_iface(c, iface))
	{
		fprintf(stderr,
				"Internal error: could not set the interface to capture!\n");
		pcap_freealldevs(devs);
		return (1);
	}
	pcap_freealldevs(devs);
	fp = fopen("last_bandwidth.txt", "r");
	if (fp)
	{
		fscanf(fp, "%lf", &c->cur_bw);
		fclose(fp);
	}
	signal(SIGINT, handle_sig);
	signal(SIGABRT, handle_sig);
	signal(SIGTERM, handle_sig);
	capture_start(c);
	return (0);
}
