pkgname = "ruff"
pkgver = "0.6.3"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = [
    "rust-std",
    "zstd-devel",  # checks only
]
depends = ["python"]
pkgdesc = "Python formatter and linter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://docs.astral.sh/ruff"
source = f"https://github.com/astral-sh/ruff/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e19b90c85f8d0cd1395429eee748bdf8bc95e2165018fe12f0331307e4d1689b"
# generates completions with host bin
options = ["!cross"]


if self.profile().arch == "riscv64":
    broken = "runs for hours, uses 100GB memory, dies"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"ruff.{shell}", "w") as f:
            self.do(
                "./target/release/ruff",
                "generate-shell-completion",
                shell,
                stdout=f,
            )


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check(args=["--workspace", "--exclude", "ruff_benchmark"])


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"ruff.{shell}", shell)
    self.install_license("LICENSE")
