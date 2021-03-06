
.. image:: https://travis-ci.org/laysakura/rainbow_logging_handler.png?branch=master
   :target: https://travis-ci.org/laysakura/rainbow_logging_handler

Ultimate Python colorized logger.

.. contents:: :local:

Usage
-----

Generic usage example
##################################

.. image:: http://github.com/laysakura/rainbow_logging_handler/raw/master/doc/screenshot.png

This script runs like above screenshot.

.. code-block:: python

    import sys
    import logging
    from rainbow_logging_handler import RainbowLoggingHandler

    if __name__ == '__main__':
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        handler = RainbowLoggingHandler(sys.stderr)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
        logger = logging.getLogger('test')

        logger.debug("debug msg")
        logger.info("info msg")
        logger.warn("warn msg")
        logger.error("error msg")
        logger.critical("critical msg")

        try:
            raise RuntimeError("Opa!")
        except Exception as e:
            logger.exception(e)

Usage with Django
##################################

.. image:: http://github.com/miohtama/rainbow_logging_handler/raw/master/doc/screenshot_django.png

`Django <https://www.djangoproject.com/>`_ is a popular Python web framework.

Put the following to your ``settings.py`` to get more pleasant development server console output::

    # Add this to your settings.py
    if DEBUG:
        # Install rainbow logging handler when running Django in develoment mode
        LOGGING["handlers"]["rainbow"] = {"level": "DEBUG", "class": "rainbow_logging_handler.RainbowLoggingHandler"}
        LOGGING["loggers"]['']["handlers"].append("rainbow")

`More about configuring loggers for Django <https://docs.djangoproject.com/en/dev/topics/logging/>`_.

Install
-------

Install from PyPI
#################
.. code-block:: bash

    $ pip install nextversion

Install from Github repo
########################
.. code-block:: bash

    $ git clone https://github.com/laysakura/rainbow_logging_handler.git
    $ cd rainbow_logging_handler
    $ ./setup.py install

Author
======

Mikko Ohtamaa <mikko@opensourcehacker.com>, Sho Nakatani <lay.sakura@gmail.com>

License
-------

This is free and unencumbered public domain software. For more information,
see <http://unlicense.org/> or the accompanying `LICENSE.txt` file.
