"""Sphinx configuration."""

project = "wFirma"
author = "Dominik Kozaczko"
copyright = "2023, Dominik Kozaczko"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
