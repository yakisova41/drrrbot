from setuptools import setup

setup(
    name="drrrbot",
    version="1.0.0",
    install_requires=["requests", "BeautifulSoup4"],
    extras_require={
        "develop": ["requests", "BeautifulSoup4"]
    },
    packages=['drrrbot']
)