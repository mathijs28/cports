pkgname = "kontact"
pkgver = "24.12.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "grantleetheme-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kontactinterface-devel",
    "libkdepim-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
]
pkgdesc = "KDE PIM unified UI"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only AND GPL-2.0-or-later"
url = "https://kontact.kde.org"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kontact-{pkgver}.tar.xz"
sha256 = "92a8e7b6cc2d6a7b4c729f3813d4fe316c123028c63ff0086a9ac491162c3abd"
