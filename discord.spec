%global         debug_package %{nil}
%global         __strip /bin/true
%global         __requires_exclude libffmpeg.so
%global         _build_id_links none
###############################Exclude Private bundled libs###########################
%global __provides_exclude_from %{_libdir}/discord/.*\\.s

Name:           discord
Version:        0.0.49
Release:        1%{?dist}
Summary:        All-in-one voice and text chat

# License Information: https://bugzilla.rpmfusion.org/show_bug.cgi?id=4441#c14
License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
# Adapted from https://raw.githubusercontent.com/flathub/com.discordapp.Discord/master/com.discordapp.Discord.appdata.xml
Source1:        discord.metainfo.xml
ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       glibc%{_isa}
Requires:       alsa-lib%{_isa}
Requires:       GConf2%{_isa}
Requires:       libnotify%{_isa}
Requires:       nspr%{_isa} >= 4.13
Requires:       nss%{_isa} >= 3.27
Requires:       libX11%{_isa} >= 1.6
Requires:       libXtst%{_isa} >= 1.2
Requires:       libappindicator%{_isa}
Requires:       libcxx%{_isa}
Requires:       libatomic%{_isa}
Requires:       hicolor-icon-theme

%if !0%{?el7}
Recommends:     (libappindicator-gtk3%{_isa} if gtk3%{_isa})
Recommends:     google-noto-emoji-color-fonts
Recommends:     libXScrnSaver
%endif

%description
Linux Release for Discord, a free proprietary VoIP application

%prep
%autosetup -n Discord

%build

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_libdir}/discord
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}%{_metainfodir}/

desktop-file-install                            \
--set-icon=%{name}                              \
--set-key=Exec --set-value=%{_bindir}/Discord   \
--delete-original                               \
--dir=%{buildroot}/%{_datadir}/applications     \
discord.desktop

cp -r * %{buildroot}/%{_libdir}/discord/
ln -sf ../%{_lib}/discord/Discord %{buildroot}/%{_bindir}/
install -p -D -m 644 %{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -p -m 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%{_libdir}/discord/
%{_bindir}/Discord
%{_datadir}/applications/discord.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml

%post
%{_libdir}/discord/postinst.sh

%changelog
* Tue Apr 09 2024 Nicolas Chauvet <nchauvet@linagora.com> - 0.0.49-1
- Update to 0.0.49

* Mon Apr 08 2024 Sérgio Basto <sergio@serjux.com> - 0.0.48-1
- Update discord to 0.0.48

* Tue Mar 26 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.0.47-1
- Update to 0.0.47

* Tue Mar 19 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.0.46-1
- Update to 0.0.46

* Mon Mar 18 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.0.45-1
- Update to 0.0.45

* Fri Mar 08 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.0.44-1
- Update to 0.0.44

* Sat Feb 17 2024 Sérgio Basto <sergio@serjux.com> - 0.0.43-1
- Update discord to 0.0.43

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 30 2024 Sérgio Basto <sergio@serjux.com> - 0.0.42-1
- Update discord to 0.0.42

* Wed Jan 10 2024 Sérgio Basto <sergio@serjux.com> - 0.0.40-1
- Update discord to 0.0.40

* Wed Dec 20 2023 Leigh Scott <leigh123linux@gmail.com> - 0.0.39-1
- Update discord to 0.0.39

* Thu Dec 14 2023 Leigh Scott <leigh123linux@gmail.com> - 0.0.38-1
- Update discord to 0.0.38

* Tue Dec 05 2023 Sérgio Basto <sergio@serjux.com> - 0.0.37-1
- Update discord to 0.0.37

* Thu Nov 16 2023 Leigh Scott <leigh123linux@gmail.com> - 0.0.35-1
- Update discord to 0.0.35

* Tue Nov 07 2023 Sérgio Basto <sergio@serjux.com> - 0.0.34-1
- Update discord to 0.0.34

* Thu Nov 02 2023 Leigh Scott <leigh123linux@gmail.com> - 0.0.33-1
- Update discord to 0.0.33

* Wed Oct 11 2023 Sérgio Basto <sergio@serjux.com> - 0.0.31-1
- Update discord to 0.0.31

* Fri Sep 22 2023 Sérgio Basto <sergio@serjux.com> - 0.0.30-1
- Update discord to 0.0.30

* Fri Sep 01 2023 Sérgio Basto <sergio@serjux.com> - 0.0.29-1
- Update discord to 0.0.29

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Sérgio Basto <sergio@serjux.com> - 0.0.28-1
- Update discord to 0.0.28

* Sat Jun 10 2023 Leigh Scott <leigh123linux@gmail.com> - 0.0.27-2
- Add appdata

* Thu Apr 27 2023 Sérgio Basto <sergio@serjux.com> - 0.0.27-1
- Update discord to 0.0.27

* Fri Mar 31 2023 Sérgio Basto <sergio@serjux.com> - 0.0.26-1
- Update discord to 0.0.26

* Wed Feb 15 2023 Sérgio Basto <sergio@serjux.com> - 0.0.25-1
- Update discord to 0.0.25

* Sat Jan 14 2023 Sérgio Basto <sergio@serjux.com> - 0.0.24-1
- Update discord to 0.0.24

* Thu Jan 12 2023 Sérgio Basto <sergio@serjux.com> - 0.0.23-1
- Update discord to 0.0.23

* Sat Dec 10 2022 Sérgio Basto <sergio@serjux.com> - 0.0.22-1
- Update discord to 0.0.22

* Fri Nov 18 2022 Leigh Scott <leigh123linux@gmail.com> - 0.0.21-2
- Fix rfbz6498

* Fri Oct 21 2022 Sérgio Basto <sergio@serjux.com> - 0.0.21-1
- Update discord to 0.0.21

* Thu Sep 15 2022 Sérgio Basto <sergio@serjux.com> - 0.0.20-1
- Update discord to 0.0.20

* Thu Aug 11 2022 Justin Zobel <justin@1707.io> - 0.0.19-1
- Update to 0.0.19

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Jun 08 2022 Sérgio Basto <sergio@serjux.com> - 0.0.18-1
- Update discord to 0.0.18

* Sun Feb 20 2022 David Auer <dreua@posteo.de> - 0.0.17-4
- (#6108) Install icon to icons/hicolor and don't hardcode path in desktop file
- Remove unnecessary build requirement: sed
- Fix original desktop file being shipped

* Sat Feb 19 2022 Sérgio Basto <sergio@serjux.com> - 0.0.17-3
- (#6166) fixes conflicts with files with other packages
- Minor fixes (warning: File listed twice: /usr/lib64/discord/Discord)
- (#5921) Adding libappindicator-gtk3 as a dependency if gtk3 is installed
- Fix "warning: absolute symlink"

* Thu Feb 17 2022 Eric Duvic <eric@ericduvic.com> - 0.0.17-1
- Update 0.0.17

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Sérgio Basto <sergio@serjux.com> - 0.0.16-1
- Update 0.0.16

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Sérgio Basto <sergio@serjux.com> - 0.0.15-1
- Update 0.0.15

* Wed Mar 24 2021 Sérgio Basto <sergio@serjux.com> - 0.0.14-1
- Update 0.0.14

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Sérgio Basto <sergio@serjux.com> - 0.0.13-1
- Update 0.0.13

* Fri Sep 11 2020 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.12-1
* Updated to 0.0.12

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Aug 07 2020 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.11-1
- Updated to 0.0.11

* Tue May 12 2020 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.10-3
- Made emoji fonts a weak dependency

* Sun Mar 01 2020 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.10-2
- Fixed dependency issue

* Wed Feb 26 2020 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.10-1
- Update to 0.0.10
- Add dependency for emoji fonts

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.9-1
- Update to 0.0.9

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.8-2
- Fix permissions issue on binary in source.

* Wed Jan 16 2019 Sean Callaway <seancallaway@fedoraproject.org> - 0.0.8-1
- Updated to 0.0.8

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.5-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Sean Callaway <seancallaway@fedoraproject.org> 0.0.5-1
- Update to 0.0.5

* Fri Apr 27 2018 Sean Callaway <seancallaway@fedoraproject.org> 0.0.4-3
- Added libatomic requirement.

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Sean Callaway <seancallaway@fedoraproject.org> 0.0.4-1
- Update to 0.0.4

* Tue Dec 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.3-1
- Update to 0.0.3
- Now using desktop-file-install.
- Removed unneeded requirements.

* Wed Aug 16 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.2-1
- Update to 0.0.2
- Spec file cleanup.

* Thu Jan 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.1-1
- Initial build using version 0.0.1

