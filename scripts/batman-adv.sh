#!/bin/bash
# Checks for wlan0 device and starts batman-adv mesh
# -L.B. 11 Nov 2013

# set the mesh network name
MESH_NAME="lbmeshnet"

# load BATMAN module
modprobe batman-adv

# systemd doesn't really respect network.target all that well
# need to write a small script to check if the network devices have settled
WLAN_ACTIVE=0
while [ $WLAN_ACTIVE -eq 0 ]; do
	echo "Checking for wlan0..."
	ifconfig wlan0 | grep ether && WLAN_ACTIVE=1
	sleep 2
done

# Set MTU and initial configuration
ifconfig wlan0 mtu 1528
# turn down txpower for bt3
iwconfig wlan0 txpower 18

iwconfig wlan0 mode ad-hoc essid $MESH_NAME ap 02:12:34:56:78:9A channel 1

#configure the interface in BATMAN-adv
batctl if add wlan0
ifconfig wlan0 up
ifconfig bat0 up
