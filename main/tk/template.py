pkgname = "tk"
pkgver = "8.6.16"
pkgrel = 0
build_wrksrc = "unix"
build_style = "gnu_configure"
configure_args = [
    "--enable-threads",
    "--enable-man-symlinks",
    "--disable-rpath",
    "--without-tzdata",
    "tk_cv_strtod_unbroken=ok",
    "LIBS=-ltcl8.6",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "zlib-ng-compat-devel",
    "tcl-devel",
    "libxext-devel",
    "libxscrnsaver-devel",
    "libxft-devel",
]
provides = ["so:libtk8.6.so=0"]
pkgdesc = "TK graphical user interface toolkit for TCL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TCL"
url = "http://www.tcl.tk"
source = f"$(SOURCEFORGE_SITE)/tcl/tk{pkgver}-src.tar.gz"
sha256 = "be9f94d3575d4b3099d84bc3c10de8994df2d7aa405208173c709cc404a7e5fe"
# no check target
options = ["!check", "!cross", "!lto"]


def init_configure(self):
    self.make_install_args += [
        "install-private-headers",
        "DESTDIR=" + str(self.chroot_destdir),
    ]


def post_install(self):
    self.install_link("usr/bin/wish", "wish8.6")
    self.install_license("../license.terms")


@subpackage("tk-devel")
def _(self):
    self.options = ["!splitstatic"]
    return self.default_devel(
        extra=[
            "usr/lib/tkConfig.sh",
            "usr/share/man/mann",
        ]
    )
