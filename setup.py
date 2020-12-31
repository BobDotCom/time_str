import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_str",
    version="0.0.1.dev1",
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
    license='MIT'
)