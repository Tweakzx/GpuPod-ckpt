USE_TEST_SUITE="yes"
USE_M32=0
USE_MULTILIB=0
DEBUG="no"
HBICT_DELTACOMP="no"
ARM_HOST="no"

# We may be running a user's python, but we should only test with canonical one
HAS_PS="yes"
HAS_PYTHON="yes"
HAS_READLINE="no"
HAS_DASH="yes"
HAS_TCSH="no"
HAS_ZSH="no"
HAS_VIM="yes"
VIM="/usr/bin/vim"
HAS_EMACS="no"
HAS_EMACS_NOX="no"
HAS_SCRIPT="yes"
HAS_SCREEN="no"
SCREEN="no"
HAS_STRACE="yes"
HAS_GDB="no"
HAS_JAVA="no"
HAS_JAVAC="no"
HAS_SSH_LOCALHOST="no"
HAS_CMA="yes"
HAS_EPOLL_CREATE1="yes"
HAS_CILK="no"
HAS_GCL="no"
GCL="no"
HAS_MATLAB="no"
MATLAB="no"
TEST_POSIX_MQ="yes"
HAS_MUTEX_WRAPPERS="no"

OPENMP_CFLAGS="-fopenmp"
if OPENMP_CFLAGS != "":
  HAS_OPENMP="yes"
else:
  HAS_OPENMP="no"

HAS_MPICH="no"
MPICH_PATH=""

# USES_OPENMPI_ORTED="@USES_OPENMPI_ORTED@"
HAS_OPENMPI="no"
OPENMPI_MPICC="no"
OPENMPI_MPIRUN="no"

if USE_M32:
  HAS_READLINE="no"
  HAS_MPICH="no"
  HAS_OPENMPI="no"
  HAS_CILK="no"

