from setuptools import setup, find_packages

setup(
    name="adult-creator-deplatforming-insurance",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
)

# commit-006: add setup.py for backward compatibility
