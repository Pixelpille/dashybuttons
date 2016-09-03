#!/usr/bin/python2 

from scapy.all import *
import os

def arp_display(pkt):
  if pkt.haslayer(ARP):        
        # Hallway
        if pkt[ARP].hwsrc == '38:f2:3e:e4:aa:9c':
          print "Hallway"
	  os.system("mpc toggle")
      
        # Kitchen
        elif pkt[ARP].hwsrc == '5c:35:3b:de:ad:07':
          print "Kitchen"
	  os.system("mpc toggle")

	# Couch
        elif pkt[ARP].hwsrc == 'dc:53:7c:ae:5c:78':
	   print "Couch"
	   os.system("mpc toggle")
	    
	# Bed
        elif pkt[ARP].hwsrc == 'dc:53:7c:b5:37:93':
	  print "Bed"
	  os.system("mpc toggle")
	  
print sniff(prn=arp_display, filter="arp", count=1,  store=0)
