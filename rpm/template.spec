Name:           ros-lunar-pid
Version:        0.0.24
Release:        0%{?dist}
Summary:        ROS pid package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pid
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-std-msgs

%description
Launch a PID control node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat May 05 2018 Andy Zelenak <andyz@utexas.edu> - 0.0.24-0
- Autogenerated by Bloom

* Wed Nov 29 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.23-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.22-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.21-5
- Autogenerated by Bloom

* Fri Apr 28 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.21-4
- Autogenerated by Bloom

* Fri Apr 28 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.21-3
- Autogenerated by Bloom

* Thu Apr 27 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.21-2
- Autogenerated by Bloom

* Thu Apr 27 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.21-1
- Autogenerated by Bloom

* Thu Apr 27 2017 Andy Zelenak <andyz@utexas.edu> - 0.0.21-0
- Autogenerated by Bloom

