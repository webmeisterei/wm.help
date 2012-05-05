Introduction
============

wm.help provides infrastructure to add a help/documentation system to your plonesite
that is based on restructured text files.

It registers a browser page ``plone/@@help`` that lists all packages
that provide help/documentation and displays the resturctured text
rendered as html.

`wm.help` is a great way to provide `up to date` documentation on how to
complete certain tasks (eg manage images of the carousel on the front page)
to users of the portal.


Usage
=====

In your package create a directory that contains the documentation.

One document is the index document that either contains all documentation or links to other documentation files.

See wm.help.example for documentation on how to write your own help plugin.


TODOS
=====

XXX

fix regex for images to handle directives that uses options too

use a separate permision to access help