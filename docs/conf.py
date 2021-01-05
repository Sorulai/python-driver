# -*- coding: utf-8 -*-

import os
import sys
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))
import cassandra
import recommonmark
from recommonmark.transform import AutoStructify
from sphinx_scylladb_theme.utils import multiversion_regex_builder


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.githubpages', 'sphinx.ext.viewcode', 'sphinx_scylladb_theme', 'sphinx_multiversion', 'recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
autosectionlabel_prefix_document = True

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Cassandra Driver'
copyright = u'2013-2017 DataStax'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = cassandra.__version__
# The full version, including alpha/beta/rc tags.
release = cassandra.__version__

autodoc_member_order = 'bysource'
autoclass_content = 'both'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'cloud.rst', 'core_graph.rst', 'geo_types.rst', 'graph.rst', 'graph_fluent.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Setup Sphinx
def setup(sphinx):
    sphinx.add_config_value('recommonmark_config', {
        'enable_eval_rst': True,
        'enable_auto_toc_tree': False,
    }, True)
    sphinx.add_transform(AutoStructify)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_scylladb_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'header_links': [
    ('Scylla Python Driver', 'https://scylladb.github.io/python-driver/'),
    ('Scylla Cloud', 'https://docs.scylladb.com/scylla-cloud/'),
    ('Scylla University', 'https://university.scylladb.com/'),
    ('ScyllaDB Home', 'https://www.scylladb.com/')],
    'github_issues_repository': 'scylladb/python-driver',
    'show_sidebar_index': True,
}

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['side-nav.html']}

# If false, no index is generated.
html_use_index = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'CassandraDriverdoc'

# URL which points to the root of the HTML documentation. 
html_baseurl = 'https://python-driver.docs.scylladb.com'

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {'html_baseurl': html_baseurl}

# -- Options for not found extension -------------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template =  '404.html'

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ''

# -- Options for redirect extension --------------------------------------------

# Read a YAML dictionary of redirections and generate an HTML file for each
redirects_file = "_utils/redirections.yaml"

# -- Options for multiversion --------------------------------------------------
# Whitelist pattern for tags (set to None to ignore all tags)
TAGS = ['stable','3.21.0-scylla', '3.22.0-scylla', '3.22.3-scylla', '3.24.0-scylla', '3.24.1-scylla']
smv_tag_whitelist = multiversion_regex_builder(TAGS)
# Whitelist pattern for branches (set to None to ignore all branches)
BRANCHES = []
smv_branch_whitelist = multiversion_regex_builder(BRANCHES)
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r'^tags/.*$'
# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'scylla-driver.tex', u'Cassandra Driver Documentation', u'DataStax', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'scylla-driver', u'Cassandra Driver Documentation',
     [u'DataStax'], 1)
]
