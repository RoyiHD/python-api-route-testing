from setuptools import find_packages, setup


setup(
    name = "Testing Tutorial",
    description = "Tutorial on writing python tests",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    install_requires = [
        "Flask==3.0.0",
        "pydantic==2.4.2",
        "pytest==7.4.2"
    ]    
)
