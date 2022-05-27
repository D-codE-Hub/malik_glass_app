from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in malik_glass_app/__init__.py
from malik_glass_app import __version__ as version

setup(
	name="malik_glass_app",
	version=version,
	description="App for Malik Glass and Interiors",
	author="D-codE",
	author_email="mailtodecode@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
