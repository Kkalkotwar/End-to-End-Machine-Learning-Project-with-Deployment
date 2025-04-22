# To import the necessary files from the particular folder we need to install that folders as the local package.
# # The setup.py file is used to install the package.
# To install setup.py file -e . is mentioned in requirements.txt file.
# The -e flag is used to install the package in editable mode, which means that...
# ...any changes made to the package will be reflected immediately without needing to reinstall it.

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Project-with-Deployment"       # GitHub repo name
AUTHOR_USER_NAME = "Kkalkotwar"                                         # GitHub username
SRC_REPO = "mlProject"                                                  # Name of the main source folder in the repo
                                                                        # The name of the main source folder in the repo should be same as the name of the package
AUTHOR_EMAIL = "kunalkalkotwar21@gmail.com"                             # Author email address


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package for ML App",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)