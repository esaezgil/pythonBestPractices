Python Projects' Best Practices
===============================

Small repo and slides for the talk delivered at Python Barcelona meetup in October'16

The **figures** package is a simple project that aims to highlight some of the best practices for Python projects.
It also contains the required configuration to make a wheel, use tox, py.test nosetests and install the package using setup.py

The **best_practices_slides** folder contains the source code required to generate the slides of the presentation.
Simply:

Install the requirements:
  
```
pip install -r requirements-slides.txt
```
Generate the slides:
```
make slides
```

Slides are generated from an .rst file using hieroglyph: https://github.com/nyergler/hieroglyph
