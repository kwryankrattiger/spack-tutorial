# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class TutorialMpileaks(AutotoolsPackage):
    """Tool to detect and report MPI objects like MPI_Requests and
    MPI_Datatypes."""

    homepage = "https://github.com/LLNL/mpileaks"
    url = "https://github.com/LLNL/mpileaks/releases/download/v1.0/mpileaks-1.0.tar.gz"

    maintainers("adamjstewart")
    license("BSD-3-Clause", checked_by="adamjstewart")

    version("1.0", sha256="2e34cc4505556d1c1f085758e26f2f8eea0972db9382f051b2dcfb1d7d9e1825")

    variant("stackstart", values=int, default=0,
            description="Specify the number of stack frames to truncate")

    depends_on("mpi")
    depends_on("adept-utils")
    depends_on("callpath")

    def configure_args(self):
        args = [
            f"--with-adept-utils={self.spec['adept-utils'].prefix}",
            f"--with-callpath={self.spec['callpath'].prefix}",
        ]

        stackstart = int(self.spec.variants["stackstart"].value)
        if stackstart:
            args.extend([
                f"--with-stack-start-c={stackstart}",
                f"--with-stack-start-fortran={stackstart}",
            ])

        return args
