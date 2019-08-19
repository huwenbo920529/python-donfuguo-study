import wmi

bios = wmi.WMI()
for s in bios.Win32_Service():
    if s.State == 'Stopped':
        print s.Caption, s.State
