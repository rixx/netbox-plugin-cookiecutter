from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.repo_name}}",
    version="0.0.0",
    description="{{cookiecutter.short_description}}",
    url="{{cookiecutter.repo_url}}",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    license="Apache Software License",
    install_requires=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    zip_safe=False,
)
