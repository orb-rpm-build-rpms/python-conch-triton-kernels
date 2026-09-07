Name:           python-conch-triton-kernels
Version:        1.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Triton kernel repository

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/stackav-oss/conch
Source:         %{pypi_source conch_triton_kernels}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'conch-triton-kernels' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-conch-triton-kernels
Summary:        %{summary}

%description -n python3-conch-triton-kernels %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-conch-triton-kernels cpu,cuda,dev,rocm,xpu


%prep
%autosetup -p1 -n conch_triton_kernels-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cpu,cuda,dev,rocm,xpu


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l conch


%check
%pyproject_check_import


%files -n python3-conch-triton-kernels -f %{pyproject_files}


%changelog
%autochangelog
