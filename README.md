Python Projects' Best Practices
===============================

Small repo and slides for the talk delivered at Python Barcelona Meetup in October'16

**Slides:** https://github.com/esaezgil/pythonBestPractices/blob/master/Python%20Projects%20Best%20Practices.pdf

The **figures** package is a simple project that aims to highlight some of the best practices for Python projects.

It contains the required configuration to:

- Make a wheel

    ```python setup.py bdist_wheel```

- Use tox

    ```tox ```

- Run nose

    ```nosetests tests/```

- Run pytest

    ``` py.test tests/```

- Install the package using setup.py

    ```python setup.py install```

The **best_practices_slides** folder contains the source code required to generate the slides of the presentation.
Simply:

Install the requirements:

```
cd best_practices_slides/
```
  
```
pip install -r requirements-slides.txt
```
Generate the slides:
```
make slides
```

Slides are generated from an .rst file using hieroglyph: https://github.com/nyergler/hieroglyph
