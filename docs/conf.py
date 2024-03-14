# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

# Specify the path to the Django project directory
django_project_dir = '/Users/c_snippy/Dropbox/CS23080009134/3 - Advanced Software Engineering/L3T10 - Capstone Project - Consolidation/capstone_project/pollProject/'

# Add the Django project directory to the Python path
sys.path.insert(0, os.path.abspath(django_project_dir))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'pollProject.settings'

# Initialize Django
django.setup()

project = 'pollProject'
copyright = '2024, Chadley Snippers'
author = 'Chadley Snippers'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
