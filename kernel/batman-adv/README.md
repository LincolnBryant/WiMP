Herein is a BATMAN-adv kernel module for kernel for kernel 3.6.11-7 from the 
Pidora Raspberry Pi repositories.

*This module was specifically built against the following kernel RPM*:
````
raspberrypi-kernel-3.6.11-7.20130415git197d15b.rpfr18.armv6hl
````

*Please run the following to determine your kernel version:*
````
$ rpm -q raspberrypi-kernel
````

You should be able to find the appropriate kernel on Pidora's Koji.



Additionally here are some build instructions:

1. Install the development tools compilation from yum:
````
$ yum groupinstall “Development Tools”
````

2. Download the *appropriate* kernel src tarball from the Pidora Koji:
````
$ wget http://japan.proximity.on.ca/kojifiles/packages/raspberrypi-kernel/3.12.0/5.20131106git839f349.rpfr18/src/raspberrypi-kernel-3.12.0-5.20131106git839f349.rpfr18.src.rpm 
````
3. Install the source RPM locally to ~/rpmbuild:
````
$ rpm -ivh raspberrypi-kernel-3.12.0-5.20131106git839f349.rpfr18.src.rpm
````
4. Install the Kernel's dependency packages:
````
$ sudo yum-builddep raspberrypi-kernel-3.12.0-5.20131106git839f349.rpfr18.src.rpm
````
5. Run a build prepare from rpmbuild to unpack the source tarball to ~/rpmbuild/BUILD: 
````
$ cd ~/rpmbuild/SPECS; rpmbuild -bp
````
6. Move to the unpacked kernel source directory:
````
$ cd ~/rpmbuild/BUILD/raspberrypi-linux-839f349
````
7. Prepare the old configuration
````
$ make oldconfig
````
8.  Edit .config and add the following lines:
````
CONFIG_BATMAN_ADV=m
CONFIG_BATMAN_ADV_BLA=y
````

9. Build the module:
````
$ make prepare && make net/batman-adv&& make net/batman-adv/batman-adv.ko
````
10. Create a directory in the running kernel's module path:
````
$ sudo mkdir /lib/modules/3.6.11/kernel/net/batman-adv
````

11. Copy the compiled newly module over into the appropriate directory:
````
$ sudo cp net/batman-adv/batman-adv.ko /lib/modules/3.6.11/kernel/net/batman-adv
````

12. Assume root and refresh the depmod file:
````
$ sudo su -
# depmod -a
````
13. Finally, load the new module:
````
# modprobe batman-adv
````
