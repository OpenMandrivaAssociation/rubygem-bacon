%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname bacon
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary:        A ruby-based testing framework
Name:           rubygem-%{gemname}
Version:        1.1.0
Release:	2
Group:          Development/Ruby 
License:        MIT
URL:            http://chneukirchen.org/repos/bacon
Source0:        http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
Requires:       rubygems
Requires:       ruby(abi) = 1.8
BuildRequires:  rubygems
BuildRequires:  rubygem(rake)
BuildArch:      noarch
Provides:       rubygem(%{gemname}) = %{version}

%description
Bacon is a small RSpec clone weighing less than
350 LoC but nevertheless providing all essential features.

%prep


%build


%install
mkdir -p $RPM_BUILD_ROOT%{gemdir}
gem install --local --install-dir $RPM_BUILD_ROOT%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mv $RPM_BUILD_ROOT%{gemdir}/bin/* $RPM_BUILD_ROOT/%{_bindir}
rmdir $RPM_BUILD_ROOT%{gemdir}/bin
find $RPM_BUILD_ROOT%{geminstdir}/bin -type f |xargs chmod a+x

# Derop weird non-utf8 characters in e-mail framework
LANG=C sed 's/\xc2//g' -i $RPM_BUILD_ROOT%{geminstdir}/ChangeLog

%check
cd $RPM_BUILD_ROOT%{geminstdir}
rake test --trace

%files
%{_bindir}/bacon
%dir %{geminstdir}
%dir %{geminstdir}/bin
%attr(0755,root,root) %{geminstdir}/bin/bacon
%{geminstdir}/lib
%{geminstdir}/Rakefile
%doc %{geminstdir}/test
%doc %{geminstdir}/README
%doc %{geminstdir}/RDOX
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/ChangeLog
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
