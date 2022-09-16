"""Setup file."""
from setuptools import setup  # type: ignore


requirements = []

# Version Info
version = "0.0.4"


with open("README.rst", encoding="utf-8") as fh:
    long_description = fh.read()


packages = [
    "time_str",
]

extras_require = {
    # "docs": get_requirements("docs/requirements.txt"),
    # "dev": get_requirements("requirements-dev.txt"),
}

# extras_require["all"] = list(set(sum(extras_require.values(), [])))

setup(
    name="time_str",
    version=version,
    author="BobDotCom",
    author_email="bobdotcomgt@gmail.com",
    description="A package to convert user input into datetime.timedelta objects",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/BobDotCom/time_str",
    packages=packages,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        # "Typing :: Typed",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require=extras_require,
    license="MIT",
    project_urls={
        "Changelog": "https://github.com/BobDotCom/time_str/blob/main/CHANGELOG.md",
        "Documentation": "https://time-str.rtfd.io/",
        "Source": "https://github.com/BobDotCom/time_str",
        "Tracker": "https://github.com/BobDotCom/time_str/issues",
    },
    include_package_data=True,
)