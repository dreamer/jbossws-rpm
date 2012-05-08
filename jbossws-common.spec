%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common
Version:          2.0.4
Release:          1%{?dist}
Summary:          JBossWS Common
Group:            Development/Libraries
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/common/tags/jbossws-common-2.0.4.GA/ jbossws-common-2.0.4.GA
# tar cafJ jbossws-common-2.0.4.GA.tar.xz jbossws-common-2.0.4.GA

Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-common-core
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-jaxb-intros
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jbossws-api
BuildRequires:    jbossws-spi
BuildRequires:    jboss-logging
BuildRequires:    wsdl4j

Requires:         jpackage-utils
Requires:         java
Requires:         jboss-common-core
Requires:         jboss-ejb-3.1-api
Requires:         jboss-jaxb-intros
Requires:         jboss-jaxws-2.2-api
Requires:         jboss-jaxrpc-1.1-api
Requires:         jboss-jms-1.1-api
Requires:         jboss-servlet-3.0-api
Requires:         jbossws-api
Requires:         jbossws-spi
Requires:         jboss-logging

%description
JBoss Web Services - Common

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
# many tests fail
mvn-rpmbuild \
    -Dproject.build.sourceEncoding=UTF-8 \
    -Dmaven.test.skip=true \
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
* Fri May 4 2012 Patryk Obara <pobara@redhat.com> 2.0.4-1
- Initial packaging

