#!/Users/c_snippy/Dropbox/CS23080009134/3 - Advanced Software Engineering/L3T10 - Capstone Project - Consolidation/capstone_project/.venv/bin/python3.12

# Author:
# Contact: grubert@users.sf.net
# Copyright: This module has been placed in the public domain.

"""
man.py
======

This module provides a simple command line interface that uses the
man page writer to output from ReStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.writers import manpage

description = ("Generates plain unix manual documents.  "
               + default_description)

publish_cmdline(writer=manpage.Writer(), description=description)
