==========================================
Example Documentation
==========================================

.. contents:: Custom TOC Title
   :depth: 2
   :backlinks: top

.. sectnum::
   :depth: 2


This document demonstrates how to write a help plugin for `wm.help`_.

.. _`wm.help`: http://pypi.python.org/pypi/wm.help

If you're not familiar with ReStructuredText Syntax don't worry -
it's well documented (http://docutils.sourceforge.net/rst.html#user-documentation) and easy to learn.



Add Images
==========


Put images in the img/ directory, register it as
a zope ``browser:resourceDirectory`` and provide the name
of the resourceDirectory in your plugin::

    ...
    resourceDir = '++resource++wm.help.example.images'




Image w/o alignemnt and alternative text

.. image:: img/logo.png



Image with alignment

.. image:: img/logo.png
   :align:  center



Image with alignement and link to a section

.. image:: img/logo.png
   :alt:    plone logo
   :align:  left
   :target: `Add images`_



Link other Files
================

You can link to `other documentation files <additional-documentation.rst>`_
of the same plugin.

To sections of the currently displayed file such as `Error Handling`_


To the index of wm.help: XXX not yet possible
(in case multiple plugins are available a link `Back to Help Index` is displayed a the top)

To plugins of other packages: XXX not yet possible

And, of course, any other URL: http://webmeisterei.com


Error Handling
==============

`Non existing link targets`_ look like this.

We also can `forget to close quotation marks.


