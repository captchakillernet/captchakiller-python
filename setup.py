import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
    
def getversion():
    with open("captchakiller/__init__.py", "r", encoding = "utf-8") as fh:
        return fh.read().split("__version__ = \"", 1)[1].split("\"", 1)[0]

setuptools.setup(
    name = "captchakiller-python",
    version = getversion(),
    author = "captchakiller",
    author_email = "support@captchakiller.net",
    description = "CaptchaKiller Python API Client Library, for solving captchas. Fast Recaptcha Captcha Solver",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/captchakillernet/captchakiller-python",
    project_urls = {
        "Homepage": "https://captchakiller.net",
        "Documentation": "https://captchakiller.gitbook.io",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["requests"],
    packages = setuptools.find_packages(),
    include_package_data=True,
    py_modules=["captchakiller"],
    python_requires = ">=3.6"
)