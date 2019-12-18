from setuptools import setup, find_packages
import os

repo_base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(repo_base_dir, "README.md"), "r") as read_me:
    long_description = read_me.read()

setup(
    name="dev-tools",
    version="0.1.0",
    description="Development tools used in MatterMiners ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatterMiners/dev-tools.git",
    author="Max Fischer, Manuel Giffels",
    author_email="maxfischer2781@gmail.com, giffels@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": ["contributors = pre_commit_hooks.contributors:main"]
    },
    keywords="development tools, contributors",
    packages=find_packages(exclude=["tests"]),
    extras_require={"contrib": ["flake8", "flake8-bugbear", "black"]},
    project_urls={
        "Bug Reports": "https://github.com/matterminers/dev-tools/issues",
        "Source": "https://github.com/matterminers/dev-tools",
    },
)
