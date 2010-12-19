# Generated from abstract-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname abstract
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: a library which enable you to define abstract method in Ruby
Name: rubygem-%{gemname}
Version: 1.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/abstract
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
'abstract.rb' is a library which enable you to define abstract method in Ruby.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.0.0-1
- Initial package
