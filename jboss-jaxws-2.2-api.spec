%global namedreltag .20120507gitd6937f
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxws-2.2-api
Version:          2.0.2
Release:          0.1%{namedreltag}%{?dist}
Summary:          Java API for XML-Based Web Services 2.2
Group:            Development/Libraries
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org/

# git clone git://github.com/jboss/jboss-jaxws-api_spec.git jboss-jaxws-api
# cd jboss-jaxws-api && git archive --format=tar --prefix=jboss-jaxws-2.2-api/ d6937fd2ebf76bfa8ea4706d6b50a172dbda9f9e | xz > jboss-jaxws-2.2-api-2.0.2.20120507gitd6937f.tar.xz

Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    jboss-specs-parent

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
%setup -q -n %{name}

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jaxws-api_2.2_spec-%{version}.Final-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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

%doc src/main/resources/LICENSE.txt
%doc src/main/resources/NOTE.txt

%files javadoc
%{_javadocdir}/%{name}

%doc src/main/resources/LICENSE.txt
%doc src/main/resources/NOTE.txt

%changelog
* Mon May 7 2012 Patryk Obara <pobara@redhat.com> 2.0.2-0.1.20120507gitd6937f
- Initial packaging

