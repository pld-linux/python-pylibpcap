
Summary:	A Python interface to libpcap
Summary(pl.UTF-8):	Interfejs Pythona do libpcap
Name:		python-pylibpcap
Version:	0.4
Release:	4
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pylibpcap/pylibpcap-%{version}.tar.gz
# Source0-md5:	38c9a47db4113594b57aa0944b1ebdcf
Patch0:		%{name}-swig_sources.patch
URL:		http://pylibpcap.sourceforge.net/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	libpcap-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the libpcap packet capture library, based on the
original Python libpcap module by Aaron Rhodes.

%description -l pl.UTF-8
Moduł Pythona do przechwytywania pakietów za pomocą biblioteki
libpcap.

%prep
%setup -q -n pylibpcap-%{version}
%patch0 -p1

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
