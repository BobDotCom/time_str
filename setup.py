import re

from setuptools import setup
# Requirements

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()


# Version Info
version = ""
with open("time_str/__init__.py") as f:

    search = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)

    if search is not None:
        version = search.group(1)

    else:
        raise RuntimeError("Could not grab version string")

if not version:
    raise RuntimeError("version is not set")

if version.endswith(("a", "b", "rc")):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()
        p = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = p.communicate()
        if out:
            version += f"+g{out.decode('utf-8').strip()}"
    except Exception:
        pass

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


packages = [
    "time_str",
]

extras_require = {
    "docs": [
        "sphinx_rtd_theme==1.0.0",
    ],
}

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
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    extras_require=extras_require,
    license='MIT',
    project_urls={
        'Documentation': 'https://time-str.readthedocs.io/en/latest/index.html',
        'Source': 'https://github.com/BobDotCom/time_str',
        'Tracker': 'https://github.com/BobDotCom/time_str/issues',
    },
)
