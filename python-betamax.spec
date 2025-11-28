#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (6 failing as of 0.8.1)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-betamax.spec)

Summary:	VCR imitation for python-requests
Summary(pl.UTF-8):	Imitacja VCR dla python-requests
Name:		python-betamax
# keep 0.8.x here for python2 support
Version:	0.8.1
Release:	7
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/betamax/
Source0:	https://files.pythonhosted.org/packages/source/b/betamax/betamax-%{version}.tar.gz
# Source0-md5:	b8182d43a200fc126a3bf7555626f964
URL:		https://pypi.org/project/betamax/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Betamax is a VCR imitation for requests. This will make mocking out
requests much easier.

%description -l pl.UTF-8
Betamax to imitacja magnetowidu dla żądań HTTP (pakietu requests).
Znacząco ułatwia to podstawianie atrap dla requests.

%package -n python3-betamax
Summary:	VCR imitation for python-requests
Summary(pl.UTF-8):	Imitacja VCR dla python-requests
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-betamax
Betamax is a VCR imitation for requests. This will make mocking out
requests much easier.

%description -n python3-betamax -l pl.UTF-8
Betamax to imitacja magnetowidu dla żądań HTTP (pakietu requests).
Znacząco ułatwia to podstawianie atrap dla requests.

%package apidocs
Summary:	API documentation for Python betamax module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona betamax
Group:		Documentation

%description apidocs
API documentation for Python betamax module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona betamax.

%prep
%setup -q -n betamax-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="betamax.fixtures.pytest" \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="betamax.fixtures.pytest" \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/betamax
%{py_sitescriptdir}/betamax-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-betamax
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/betamax
%{py3_sitescriptdir}/betamax-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
