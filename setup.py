import json
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

with open("manifest.json", "r", encoding="utf-8") as fh:
    manifest_data = json.load(fh)
    version = manifest_data.get("version", "1.0.0")  # Default to 1.0.0 if version is not found

setup(
    name='directory-mapper',
    version=version,
    author='Mohamed Gueye (Orbit Turner)',
    author_email='orbitturner@gmail.com',
    license='CC BY-NC-SA 4.0 DEED',
    description='Directory Mapper - A tool for mapping directories and visualizing file structures.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/orbitturner/directory-mapper',
    project_urls={
        "Bug Tracker": "https://github.com/orbitturner/directory-mapper/issues/new",
    },
    packages=find_packages(),
    include_package_data=True, # Include additional files into the package
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        dirmap=dirmap.orbit_directory_mapper:bootstrap
    '''
)
