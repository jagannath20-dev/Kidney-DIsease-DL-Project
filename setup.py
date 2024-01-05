import setuptools

with open("README.md" , "r", encoding = "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "Kidney-Disease-Classification-DeepLearning-Project"
AuthorUserName = "Jagannath20"
SRC_REPO  = "cnnClassifier"
AUTHOR_EMAIL = "devarakondajagannath6378@gmail.com"




setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AuthorUserName,
    author_email=AUTHOR_EMAIL,
    description = "A Small Python Package for CNN APP",
    long_description = long_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AuthorUserName}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AuthorUserName}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)