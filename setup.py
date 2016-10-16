from setuptools import setup, find_packages

setup(
    name="figures",
    version="1",
    description="figures module to create your own figures",
    author="enrique",
    packages=['figures'],
    author_email="dummy@dummy.net",
    url="wwww.dummy.net/dummy/",
    package_dir = {'': 'figures'},
    entry_points={
        'console_scripts': [
            "figures = figures.example_figures:main",
        ],
    },
)
