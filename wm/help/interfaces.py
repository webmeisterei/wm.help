from zope.interface import Interface
from zope.interface.interface import Attribute

class IHelpPlugin(Interface):
    """
    """

    title = Attribute(u"Plugin Title")

    description = Attribute(u"Describes what is being generated (optional)")

    indexFile = Attribute(u"this file will be displayed first")

    resourceDir = Attribute(u"directory images are located in XXX document better")

    docPackage = Attribute(u"XXX document")
