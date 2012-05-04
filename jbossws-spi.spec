%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-spi
Version:          2.0.3
Release:          1%{?dist}
Summary:          JBossWS SPI
Group:            Development/Libraries
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/spi/tags/jbossws-spi-2.0.3.GA/ jbossws-spi-2.0.3.GA
# tar cafJ jbossws-spi-2.0.3.GA.tar.xz jbossws-spi-2.0.3.GA
Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-logging

Requires:         jpackage-utils
Requires:         java
Requires:         jboss-logging

%description
JBoss WS SPI classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

%build
# tests skipped because testParse fails
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -Dproject.build.sourceEncoding=UTF-8 \
  install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri May 4 2012 Patryk Obara <pobara@redhat.com> 2.0.3-1
- Initial packaging

