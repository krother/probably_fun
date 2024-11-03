# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Probably Fun'
copyright = '2024, Kristian Rother'
author = 'Kristian Rother'
release = '1.0'
html_title = project

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxcontrib.cairosvgconverter',
    ]

templates_path = ['_templates']
exclude_patterns = ['README.md', '_build', 'Thumbs.db', '.DS_Store', 'articles/de/*']

language = 'en'

# ---- Options for HTML output ----
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_path = ['themes']
html_static_path = ['_static']
html_logo = "_static/academis_logo.png"
html_favicon = "_static/favicon.ico"

html_css_files = [
    "academis.css",
]
html_theme_options = {
    "source_repository": "https://github.com/krother/probably_fun",
    "source_branch": "main",
    "source_directory": "",
}
# ---- Options for PDF output ----

latex_elements = {
    'preamble': "\linespread{1.25}",
}