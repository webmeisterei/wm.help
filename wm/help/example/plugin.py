from wm.help.interfaces import IHelpPlugin
from zope.interface import implements

class ExampleHelpPlugin(object):
    implements(IHelpPlugin)

    title = u"Example Help"

    description = u"This plugin demonstrates the usage of wm.help"

    indexFile = 'start.rst'

    resourceDir = '++resource++wm.help.example.images'

    docPackage = 'wm.help.example'
