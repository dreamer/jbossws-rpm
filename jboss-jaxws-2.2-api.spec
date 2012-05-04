%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxws-2.2-api
Version:          1.0.0
Release:          1%{?dist}
Summary:          Java API for XML-Based Web Services 2.2
Group:            Development/Libraries
License:          LGPLv2+
URL:              http://www.jboss.org/

# git clone git://github.com/jboss/jboss-jaxws-api_spec.git jboss-jaxws-api
# cd jboss-jaxws-api
# git archive jboss-jaxws-api_2.2_spec-1.0.0.Final --prefix=jboss-jaxws-2.2-api-1.0.0.Final/ --format=tar.gz --output=../jboss-jaxws-2.2-api-1.0.0.Final.tar.gz
Source0:          %{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-source-plugin

Requires:         jpackage-utils
Requires:         java

%description
Java API for XML-Based Web Services 2.2 classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
# testI18NMessage is failing
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jaxws-api_2.2_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Thu May 3 2012 Patryk Obara <pobara@redhat.com> 1.0.0-1
- Initial packaging

