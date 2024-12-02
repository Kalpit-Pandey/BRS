from setuptools import setup

with open ("README.md","r",encoding="utf-8")as f:
    long_description = f.read()

##edit below variable as per your requirements
REPO_NAME ="Books-Recommender"
AUTHOR_NAME = "kalpit-pandey"
SRC_REPO ="src"
LIST_OF_REQUIREMENTS = ['streamlit','numpy']

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email="kalpeetpandey@gmail.com",
    description="A small package for Books Recommender",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    packages=[SRC_REPO],
    python_requires=">=3.11.4",
    install_requires=LIST_OF_REQUIREMENTS,
)