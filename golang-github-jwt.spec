# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/golang-jwt/jwt
%global goipath         github.com/golang-jwt/jwt
%global goaltipaths     github.com/golang-jwt/jwt/v5
Version:                5.2.0

%gometa -f


%global common_description %{expand:
Community maintained clone of https://github.com/dgrijalva/jwt-go.}

%global golicenses      LICENSE
%global godocs          MIGRATION_GUIDE.md README.md SECURITY.md\\\
                        VERSION_HISTORY.md cmd/jwt/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Community maintained clone of https://github.com/dgrijalva/jwt-go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc MIGRATION_GUIDE.md README.md SECURITY.md VERSION_HISTORY.md
%doc cmd/jwt/README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
