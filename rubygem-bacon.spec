# Generated from bacon-1.1.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	bacon

Summary:	a small RSpec clone
Name:		rubygem-%{rbname}

Version:	1.1.0
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://chneukirchen.org/repos/bacon
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		bacon-1.1.0-add-missing-licenses-field.patch
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
gunzip metadata.gz
%patch0 -p1 -b .licenses~
gzip metadata

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


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.0-2
+ Revision: 774498
- add missing 'licenses' field to metadata
- regenerate spec with gem2rpm5
- mass rebuild of ruby packages against ruby 1.9.1

  + Alexander Khrukin <akhrukin@mandriva.org>
    - removed clean section

* Wed Sep 07 2011 Alexander Barakin <abarakin@mandriva.org> 1.1.0-1
+ Revision: 698564
- imported package rubygem-bacon

