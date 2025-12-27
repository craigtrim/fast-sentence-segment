# -*- coding: utf-8 -*-
"""Base object providing logging functionality."""

import logging

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s() : %(lineno)d : %(message)s',
    level=logging.DEBUG)


class BaseObject:
    """Base class providing logging capabilities."""

    def __init__(self, component_name: str):
        self.logger = logging.getLogger(component_name)
        self.isEnabledForDebug = self.logger.isEnabledFor(logging.DEBUG)
        self.isEnabledForInfo = self.logger.isEnabledFor(logging.INFO)
        self.isEnabledForWarning = self.logger.isEnabledFor(logging.WARNING)
