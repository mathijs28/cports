pkgname = "kmod"
pkgver = "33"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-zlib",
    "--with-zstd",
    "--disable-test-modules",
]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "gmake",
    "pkgconf",
    "scdoc",
    "slibtool",
]
makedepends = ["zlib-ng-compat-devel", "zstd-devel"]
checkdepends = ["bash"]
pkgdesc = "Linux kenrel module handling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.gz"
sha256 = "d7c59c76bb3dd0eeeecdb1302365cf4bd5cb54e977be43a00efa2c96c519c1dc"
# broken testsuite build system
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "depmod-search.conf",
        "usr/lib/depmod.d",
        name="search.conf",
    )

    # empty dirs
    self.install_dir("etc/depmod.d", empty=True)
    self.install_dir("etc/modprobe.d", empty=True)
    self.install_dir("usr/lib/modprobe.d", empty=True)

    # initramfs-tools
    self.install_initramfs(self.files_path / "kmod.initramfs-tools")


@subpackage("libkmod-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()


@subpackage("libkmod")
def _lib(self):
    self.subdesc = "runtime library"
    return self.default_libs()
