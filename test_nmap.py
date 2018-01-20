from libnmap.process import NmapProcess

nm = NmapProcess("192.168.1.53", options="-sV")
rc = nm.run()

if nm.rc == 0:
    print (nm.stdout)
else:
    print (nm.stderr)