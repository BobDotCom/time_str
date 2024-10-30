"""
MIT License.

Copyright (c) 2020 BobDotCom

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import warnings
from importlib.metadata import PackageNotFoundError, version

__all__ = ("__version__",)

try:  # pragma: no cover
    __version__ = version("time_str")
except PackageNotFoundError:  # pragma: no cover
    # Package is not installed
    try:
        from setuptools_scm import get_version  # type: ignore[import]

        __version__ = get_version()
    except ImportError:
        # setuptools_scm is not installed
        __version__ = "0.0.0"
        warnings.warn(
            (
                "Package is not installed, and setuptools_scm is not installed. "
                f"As a fallback, {__name__}.__version__ will be set to {__version__}"
            ),
            RuntimeWarning,
            stacklevel=2,
        )
