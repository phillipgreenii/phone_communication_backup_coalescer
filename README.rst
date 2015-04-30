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

The easiest way to install most Python packages is via ``easy_install`` or ``pip``::

  $ easy_install phone_communication_backup_coalescer

  Usage
  -----

    >> phone_communication_backup_coalescer [--no-sms] [--no-calls] rootDirectoryToSearch+


Copyright & License
-------------------

  - Copyright 2015, Phillip Green II
  - License: MIT
