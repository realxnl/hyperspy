"""

This module is deprecated and will be removed in HyperSpy 0.10,
please use :mod:`~hyperspy.api` instead.

"""
# -*- coding: utf-8 -*-

from hyperspy.Release import version as __version__
from hyperspy import components
from hyperspy import signals
from hyperspy.io import load
from hyperspy.defaults_parser import preferences
from hyperspy import utils
from hyperspy.datasets import example_signals
import warnings
from hyperspy.misc.hspy_warnings import VisibleDeprecationWarning


def get_configuration_directory_path():
    import hyperspy.misc.config_dir
    return hyperspy.misc.config_dir.config_path

warnings.warn(
    "This module is deprecated and will be removed in HyperSpy 0.10,"
    "please use `hyperspy.api` instead.", VisibleDeprecationWarning)
