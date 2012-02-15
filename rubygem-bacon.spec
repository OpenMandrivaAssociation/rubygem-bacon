# Generated from bacon-1.1.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	bacon

Summary:	a small RSpec clone
Name:		rubygem-%{rbname}

Version:	1.1.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://chneukirchen.org/repos/bacon
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Bacon is a small RSpec clone weighing less than 350 LoC but nevertheless
providing all essential features.  http://github.com/chneukirchen/bacon

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%files
%{_bindir}/bacon
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/bacon
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/autotest
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/autotest/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/RDOX
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
