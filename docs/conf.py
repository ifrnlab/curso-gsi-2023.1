# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Livro de gerência e configuração de serviços para Internet 2023.1'
copyright = '2023, Livro de gerência e configuração de serviços para Internet 2023.1'
author = '<Nome> <Sobrenome>'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.bibtex',
#    'sphinxcontrib.mermaid',
]

bibtex_bibfiles = [
    'bibliografia.bib',
    ]


templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_title = ''
html_static_path = ['_static']
