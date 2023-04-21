# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Adi's Website"
copyright = '2023, Adithya Yerramsetty'
author = 'Adithya Yerramsetty'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", 'sphinx_sitemap']
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath"
]
myst_heading_anchors = 3

templates_path = ['_templates']
exclude_patterns = []

html_baseurl = "https://adithyay.com/"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# -- Options for Furo Config -------------------------------------------------
html_title = "Adi's Website"

# -- Options for the sitemap -------------------------------------------------
sitemap_url_scheme = "{link}"