from setuptools import setup, find_packages

setup(
    name="figures",
    version="1",
    description="figures module to create your own figures",
    author="enrique",
    packages=find_packages('figures'),
    author_email="dummy@dummy.net",
    url="wwww.dummy.net/dummy/",
    entry_points={
        'console_scripts': [
            "figure_creator = figures.example_figures:main",
        ],
    },
)
