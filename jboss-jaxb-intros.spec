%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxb-intros
Version:          1.0.2
Release:          1%{?dist}
Summary:          JBoss JAXB Intros
Group:            Development/Libraries
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/projects/jaxbintros/tags/1.0.2.GA/ jboss-jaxb-intros-1.0.2.GA
# tar cafJ jboss-jaxb-intros-1.0.2.GA.tar.xz jboss-jaxb-intros-1.0.2.GA
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-logging
BuildRequires:    glassfish-jaxb-api
BuildRequires:    glassfish-jaxb
BuildRequires:    jvnet-parent

Requires:         jpackage-utils
Requires:         java
Requires:         apache-commons-beanutils
Requires:         apache-commons-logging
Requires:         glassfish-jaxb

%description
JBoss JAXB Introductions.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
mvn-rpmbuild \
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
* Fri May 4 2012 Patryk Obara <pobara@redhat.com> 1.0.2-1
- Initial packaging

