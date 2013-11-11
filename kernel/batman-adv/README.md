Herein is a BATMAN-adv kernel module for kernel for kernel 3.6.11-7 from the 
Pidora Raspberry Pi repositories.

This module was specifically built against the following kernel RPM:
	raspberrypi-kernel-3.6.11-7.20130415git197d15b.rpfr18.armv6hl

You should be able to find the appropriate kernel on Pidora's Koji.


( TODO : cleanup this horrible abuse of markdown )

Additionally here are some build instructions:

0) yum groupinstall “Development Tools”
1) Download raspberrypi-kernel.src.rpm (i used this one: http://koji.pidora.ca/koji/buildinfo?buildID=59932 –raspberrypi-kernel-3.6.11-12.20130920git966efc7.rpfr18.src.rpm).. should match your “rpm -q raspberrypi-kernel”
2) rpm ivh raspberrypi-kernel-3.6.11-12.20130920git966efc7.rpfr18.src.rpm
- installs to ~/rpmbuild
3) sudo yum-builddep raspberrypi-kernel-3.6.11-12.20130920git966efc7.rpfr18.src.rpm
- installs dependencies to build kernel sources
4)cd ~/rpmbuild/SPECS; rpmbuild -bp
- untars the kernel sources to ~/rpmbuild/BUILD
5)cd ~/rpmbuild/BUILD/raspberrypi-linux-197d15b
6) make oldconfig
- prepare the old configuration
7)  vi .config and add the following lines:
CONFIG_BATMAN_ADV=m
CONFIG_BATMAN_ADV_BLA=y
8) make prepare && make net/batman-adv&& make net/batman-adv/batman-adv.ko
- prepare the kernel sources and build the new kernel modules
9) sudo mkdir /lib/modules/3.6.11/kernel/net/batman-adv
- create a new directory for the new module
10) sudo cp net/batman-adv/batman-adv.ko /lib/modules/3.6.11/kernel/net/batman-adv
- copy compiled module into the kernel’s modules dir
11) sudo su -
12) depmod -a
- configures the new modules
13) modprobe batman-adv
