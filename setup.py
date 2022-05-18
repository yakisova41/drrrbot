from setuptools import setup

setup(
    name="drrrbot",
    version="0.0.1",
    install_requires=["requests", "BeautifulSoup4"],
    extras_require={
        "develop": ["requests", "BeautifulSoup4"]
    },
    packages=['drrrbot']
)
