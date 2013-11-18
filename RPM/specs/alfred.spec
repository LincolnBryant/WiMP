Name:		alfred
Version:	20131117git67e0d7e
Release:	1%{?dist}
Summary:	A.L.F.R.E.D - Almighty Lightweight Fact Remote Exchange Daemon

Group:		System Environment/Daemons
License:	GPL 2.0
URL:		http://www.open-mesh.org/projects/open-mesh/wiki/Alfred
Source0:	%{name}-%{version}-source.tar.gz		

BuildRequires:	gpsd-devel
Requires:	gpsd-libs

%description
alfred is a user space daemon for distributing arbitrary local information over
the mesh/network in a decentralized fashion. This data can be anything which
appears to be useful - originally designed to replace the batman-adv
visualization (vis), you may distribute hostnames, phone books, administration
information, DNS information, the local weather forecast ...

alfred runs as daemon in the background of the system. A user may insert
information by using the alfred binary on the command line, or use special
programs to communicate with alfred (done via unix sockets). alfred then takes
care of distributing the local information to other alfred servers on other
nodes. This is done via IPv6 link-local multicast, and does not require any
configuration. A user can request data from alfred, and will receive the
information available from all alfred servers in the network.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# need to move from local/sbin to sbin
mv %{buildroot}/usr/local/sbin %{buildroot}/usr/sbin
# likewise with man
mv %{buildroot}/usr/local/share %{buildroot}/usr/share

%files
%{_sbindir}/alfred
%{_sbindir}/alfred-gpsd
%{_sbindir}/batadv-vis
%{_mandir}/man8/alfred-gpsd.8.gz
%{_mandir}/man8/alfred.8.gz
%{_mandir}/man8/batadv-vis.8.gz

%doc



%changelog
* Sun Nov 17 2013 Lincoln Bryant lincolnb@uchicago.edu [67e0d7egit20131016-1]
- Initial build
