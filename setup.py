import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyranker",
    version="0.1.2",
    author="AvishrantSh (Avishrant Sharma)",
    author_email="<avishrants@gmail.com>",
    description="A Python based package consisiting of BM25 and\
         Vector Space Rankers for Information Retrieval",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AvishrantsSh/PyRanker",
    project_urls={
        "Bug Tracker": "https://github.com/AvishrantsSh/PyRanker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=["numpy>=1.24.2", "nltk>=3.8.1"],
    python_requires=">=3.8",
)