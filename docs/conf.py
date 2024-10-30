# pylint: skip-file
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from importlib.metadata import version as get_version

old_changelog = os.path.join(os.path.dirname(__file__), "..", "CHANGELOG.md")
new_changelog = os.path.join(os.path.dirname(__file__), "changelog.md")


with open(old_changelog) as f:
    changelog_lines = f.readlines()


CHANGELOG_TEXT = "".join(changelog_lines)


# Only write if it's changed to avoid recompiling the docs
def write_new() -> None:
    with open(new_changelog, "w") as fw:
        fw.write(CHANGELOG_TEXT)


try:
    c_file = open(new_changelog)
except FileNotFoundError:
    write_new()
else:
    if c_file.read() != CHANGELOG_TEXT:
        write_new()
    c_file.close()


sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = [
#     "sphinx.ext.autodoc",
#     "sphinx.ext.coverage",
#     "sphinx.ext.napoleon",
#     "sphinx_rtd_theme",
# ]
extensions = [
    # "builder",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.duration",
    "sphinxcontrib_trio",
    # "details",
    # "exception_hierarchy",
    # "attributetable",
    "resourcelinks",
    # "nitpick_file_ignorer",
    "myst_parser",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_autodoc_typehints",
    "sphinxarg.ext",
]

always_document_param_types = True
toc_object_entries_show_parents = "hide"

# ogp_site_url = ""
# ogp_image = ""

autodoc_member_order = "bysource"
autodoc_typehints = "none"
# autoclass_content = "init"
# maybe consider this?
# napoleon_attr_annotations = False

extlinks = {
    "issue": ("https://github.com/BobDotCom/time_str/issues/%s", "GH-"),
}
# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
}

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",  # Used For The Other Docs
    ".md": "markdown",  # Used ONLY In the Guide For Faster Making Time
}

master_doc = "index"


project = "time_str"
copyright = "2020, BobDotCom"

release = get_version("time_str")


# The short X.Y version.
version = ".".join(release.split(".")[:2])

# This assumes a tag is available for final releases
branch = (
    "main"
    if "a" in version or "b" in version or "rc" in version or "dev" in release
    else f"v{release}"
)

html_title = f"{project} v{version} Documentation"

language = "en"

gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = "friendly"

html_experimental_html5_writer = True

# autodoc_default_options = {
#     'imported-members': True
#     }
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
#     "updater-action": ("https://github.com/marketplace/actions/oprf-asset-updater", "asdf")
html_context = {
    "discord_invite": "https://discord.gg/gGc2WAJKMA",
}

resource_links = {
    "discord": "https://discord.gg/gGc2WAJKMA",
    "issues": "https://github.com/BobDotCom/time_str/issues",
    "discussions": "https://github.com/BobDotCom/time_str/discussions",
    "examples": f"https://github.com/BobDotCom/time_str/tree/{branch}/examples",
}


# -- Extension configuration -------------------------------------------------

html_theme_options = {
    "source_repository": "https://github.com/BobDotCom/time_str",
    "source_branch": "main",
    "source_directory": "docs/",
}

# html_logo = "./images/oprf-logo.png"
# html_favicon = "./images/oprf.ico"


html_static_path = ["_static"]
# html_css_files = ["css/custom.css"]
# html_js_files = ["js/custom.js"]


# html_search_scorer = "_static/js/scorer.js"

htmlhelp_basename = "time_strdoc"
