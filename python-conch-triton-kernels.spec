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
# conch imports torch and triton unconditionally across most of its modules, so
# they are needed for the %check imports (and are de facto hard runtime deps).
# Upstream only declares them inside the hardware-variant extras we dropped (see
# DROPPED-EXTRAS.md), so they must be requested explicitly here. torch 2.12 is in
# the localrepo; triton comes from the base.
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(triton)

# Not declared as core deps upstream (only via the dropped variant extras), but
# imported unconditionally, so require them for a self-consistent package.
Requires:       python3dist(torch)
Requires:       python3dist(triton)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'conch-triton-kernels' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-conch-triton-kernels
Summary:        %{summary}

%description -n python3-conch-triton-kernels %_description

%prep
%autosetup -p1 -n conch_triton_kernels-%{version}


%generate_buildrequires
# The upstream extras (cpu, cuda, rocm, xpu, dev) are not built. The hardware
# variants each hard-pin torch==2.7.0 (rocm: torch==2.7.0+rocm6.2.4) to select a
# prebuilt torch wheel from PyTorch's index -- meaningless against our single
# system torch 2.12, and the rocm local-version tag isn't valid RPM version
# syntax (it aborts the buildrequires generator). dev is lint/test tooling. The
# real runtime dep is numpy (in the base); triton is provided by the base and
# pulled in by the vLLM stack. See DROPPED-EXTRAS.md in the package dir.
%pyproject_buildrequires


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
