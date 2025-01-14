# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'USF COMIT Development And Deployment Conventions'
copyright = '2022, USF COMIT'
author = 'Kristopher Krasnosky, Emir Gezer, and USF COMIT Authors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.githubpages',
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'myst_parser'

]

templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = "sphinx_rtd_theme"

# Make sure the target is unique
autosectionlabel_prefix_document = True
