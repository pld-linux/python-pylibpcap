%include	/usr/lib/rpm/macros.python

Summary:	An Python interface to libpcap
Summary(pl):	Interfejs Pythona do libpcap
Name:		python-pylibpcap
Version:	0.3
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pylibpcap/pylibpcap-%{version}.tar.gz
URL:		http://pylibpcap.sourceforge.net/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	libpcap-devel
BuildRequires:	swig
BuildRequires:	swig-python
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the libpcap packet capture library, based on the
original python libpcap module by Aaron Rhodes.

%description -l pl
Modu³ Pythona do przechwytywania pakietów za pomoc± biblioteki
libpcap.

%prep
%setup -q -n pylibpcap-%{version}

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
