import warnings
from importlib.metadata import PackageNotFoundError, version

__all__ = ("__version__",)

try:
    __version__ = version("time_str")
except PackageNotFoundError:
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
