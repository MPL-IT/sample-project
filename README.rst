==============
Sample Project
==============

|Build Status| |Coverage Status|

This is a sample Python project that you can use as a template at MPL.

Section
^^^^^^^

This is a section.

Subsection
----------

This is a subsection with code examples. Indentation matters!

.. code-block:: ipython

    import numpy as np
    from sample.hello import greetings

    greetings()

How to Build the Documentation
------------------------------

In the `docs` folder, Mac or Linux users type

.. code-block::

    make html


and Windows users execute

.. code-block::

    make.bat html


To trigger the build of the documentation. 

After that open `docs/build/index.html`
in your browser.


.. |Build Status| image:: https://img.shields.io/github/workflow/status/MPL-IT/sample-project/Checks
   :target: https://github.com/MPL-IT/sample-project/actions?query=workflow%3AChecks
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/MPL-IT/sample-project/main.svg
   :target: https://codecov.io/gh/MPL-IT/sample-project
