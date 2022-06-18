import setuptools

setuptools.setup(
    name="pyfin",
    version="0.0.1",
    description="financial calculation experiments",
    author="Glen Cooper",
    install_requires=["numpy_financial"],
    url="https://github.com/coopergf/pyfin",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: MIT License",
        "Intended Audience :: Research and Development",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
