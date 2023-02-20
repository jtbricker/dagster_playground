from setuptools import find_packages, setup

setup(
    name="guides",
    packages=find_packages(exclude=["guides_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
