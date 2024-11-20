from setuptools import find_packages, setup

setup(
    name="my_package",
    version="0.0.10",
    description="An awesome package that does nothing",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    author="me",
    author_email="me@me.com",
    license="MIT",
    install_requires=["colorama >= 0.4.4"],
    python_requires=">=3.10",
)