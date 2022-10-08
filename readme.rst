==============
X-Wing Copilot
==============

A companion application for X-wing TMG by Atomic Mass Games. This application is built using Python's Kivy library.

About
-----
Made for scenarios in xwing 2.5

App Usage
~~~~~~~~~

Building
~~~~~~~~
Building requires buildozer:::

$ pip install buildozer buildozer
$ buildozer init
.. code-block::shell

Building to APK file for android:
``buildozer -v android debug``

The apk file gets thrown into a created a bin folder.

Development
~~~~~~~~~~~
Project uses tox to check development. Tox will run pytest, flake8 and mypy. 

`Note: for future development, can run buildozer in tox`




