import setuptools, codecs, os.path

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="time_str",
    version=get_version("time_str/__init__.py"),
    author="BobDotCom",
    author_email="bobdotcomgt@gmail.com",
    description="A package to convert user input into datetime.timedelta objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BobDotCom/time_str",
    packages=setuptools.find_packages(exclude=['tests*','build.py']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[

    ],
    license='MIT',
    project_urls={
        'Documentation': 'https://time-str.readthedocs.io/en/latest/index.html',
        'Source': 'https://github.com/BobDotCom/time_str',
        'Tracker': 'https://github.com/BobDotCom/time_str/issues',
    },
)