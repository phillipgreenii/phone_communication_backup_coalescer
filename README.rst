===========================================================================
phone_communication_backup_coalescer: Coalesces communication backup files.
===========================================================================

.. image:: https://travis-ci.org/phillipgreenii/phone_communication_backup_coalescer.svg
    :target: https://travis-ci.org/phillipgreenii/phone_communication_backup_coalescer
    :alt: Build Status

This project takes multiple backup files and coalesces them into a single backup file.  It currently supports
 - `SMSBackupRestore <https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore>`_ for SMS
 - `CallLogBackupRestore <https://play.google.com/store/apps/details?id=com.riteshsahu.CallLogBackupRestore>`_ for Calls

Installation
------------

The easiest way to install most Python packages is via ``easy_install`` or ``pip``:

.. code-block:: bash

  $ easy_install phone_communication_backup_coalescer

Usage
-----

.. code-block:: bash

  $ phone_communication_backup_coalescer [--no-sms] [--no-calls] rootDirectoryToSearch


Development
-----------

For consistency, development is done with a docker container that mounts the source code:

.. code-block:: bash

  $ docker run -it -v $(pwd):/src python:2.7.12 /bin/bash

Run Tests
^^^^^^^^^

.. code-block:: bash

  $ python setup.py test

Install
^^^^^^^

.. code-block:: bash

  $ python setup.py develop

Copyright & License
-------------------

  - Copyright 2016, Phillip Green II
  - License: MIT
