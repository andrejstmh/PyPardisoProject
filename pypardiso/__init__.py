# coding: utf-8

from .pardiso_wrapper import PyPardisoSolver, Matrix_type
from .scipy_aliases import spsolve, factorized
from .scipy_aliases import pypardiso_solver as ps

__version__ = '0.4.1'
__all__ = ['PyPardisoSolver', 'spsolve', 'factorized', 'ps']
