# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "ENGO645/537-Lab-2025"
author = "Reza Safarzadeh"

# The short X.Y version
version = "2025"
# The full version, including alpha/beta/rc tags
release = "ENGO645/537-Labs-2025"

# Set documentation language
language="en"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx_thebe",
    # "sphinxcontrib.googleanalytics",
    "sphinxcontrib.youtube",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "myst_nb",
    "jupyter_sphinx",
]

# Google Analytics ID to enable tracking of site traffic
# googleanalytics_id = "UA-105019106-1"
# googleanalytics_enabled = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# ======================
# TODO: Remove OLD SETUP
# ======================
# import sphinx_rtd_theme
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# def setup(app):
#    app.add_stylesheet('theme_overrides.css')
# html_logo = 'img/HY-logo-2017.png'

# =======================
# NEW SPHINX THEME SETUP
# =======================

html_theme = "sphinx_book_theme"
html_logo = "img/banner/logo_02.png"
html_title = ""

html_theme_options = {
    # "external_links": [],
    "repository_url": "https://github.com/safarzadeh-reza/Spatial_Data_Mining_Winter2025/",
    "repository_branch": "master",
    "path_to_docs": "source/",
    # "twitter_url": "https://twitter.com/pythongis",
    # "google_analytics_id": "UA-159257488-1",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "thebe": True,
        "notebook_interface": "jupyterlab",
        "collapse_navigation": False,
    },
}

# Add last modified to all pages
html_last_updated_fmt = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    'css/custom.css',
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    "display_github": True,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    "github_user": "safarzadeh-reza",
    "github_repo": "Spatial_Data_Mining_Winter2025",
    "github_version": "master/",
    "conf_py_path": "/source/",
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "engo645-Pythondoc"


# -- Options for LaTeX output ------------------------------------------------
# latex_docclass = {
#    'howto': 'krantz.cls',
#    'manual': 'krantz.cls',
# }
#
# latex_additional_files = ["hyperref.sty"]

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "engo645.tex",
        "engo645 Documentation",
        "R. Safarzadeh",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "engo645/537", "Engo645 Documentation", [author], 1)]

# Allow errors
execution_allow_errors = True

# Execute cells only if any of the cells is missing output
jupyter_execute_notebooks = "auto"

# Exclude execution of some notebooks
execution_excludepatterns = ['advanced-data-processing-with-pandas.ipynb', 'errors.ipynb', 'matplotlib.ipynb', 'advanced_plotting.ipynb']

# Add math config options for new version of MyST
myst_enable_extensions = ["dollarmath"]