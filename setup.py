import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ca_query",
    version="0.0.1",
    author="Tom Seimandi",
    description="Disponibilité des comptes sociaux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/InseeFrLab/ca-document-querier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "s3fs",
        "requests"
    ],
    packages=[
        "ca_query",
    ],
    python_requires=">=3.7",
    package_data={"extraction_core_comptes": ["data/*"]},
)
