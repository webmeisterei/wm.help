import Globals
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import os
import re

from Products.CMFCore.utils import getToolByName
from zope.cachedescriptors.property import Lazy
from zope.dottedname.resolve import resolve
from operator import itemgetter
from zope.component import getUtilitiesFor, getUtility, getMultiAdapter
from wm.help.interfaces import IHelpPlugin
from zope.component.interfaces import ComponentLookupError
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFPlone.utils import safe_unicode
from plone.memoize.ram import cache, DontCache



def _cache_key(method, self):
    if Globals.DevelopmentMode:
        #don't cache help in debug mode
        raise DontCache()
    return (method, self.request.get('plugin',None), self.request.get('file', None))

class DocumentationView(BrowserView):

    @Lazy
    def availablePlugins(self):
        """list all available help plugins sorted by their name
        """
        plugins = []
        for name, util in getUtilitiesFor(IHelpPlugin):
            plugins.append(dict(name=name,
                                title = util.title,
                                description=util.description))

        return sorted(plugins, key=itemgetter('name'))



    @property
    def plugin(self):
        pluginName = self.currentPlugin
        if pluginName is not None:
            try:
                return getUtility(IHelpPlugin,name=pluginName)
            except ComponentLookupError, e:
                IStatusMessage(self.request).addStatusMessage(u"could not find plugin %s" % pluginName , 'error')
                self.request.response.redirect(self._baseUrl)
                return
        else:
            return None


    @Lazy
    def currentPlugin(self):
        """returns the name of the currently selected help plugin.
        in case there is only one plugin available, it automatically gets selected.
        in case no plugin is available, it's set to None
        """
        plugin = self.request.get('plugin', None)
        if plugin is None and len(self.availablePlugins)==1:
            plugin = self.availablePlugins[0]['name']
        return plugin


    def _rstData(self):
        """return the documentation text as rst.
        """

        if self.plugin is None:
            return u""

        filename = self.request.get('file', self.plugin.indexFile)

        docPkg = resolve(self.plugin.docPackage)
        pkgDir = os.path.dirname(docPkg.__file__)

        try:
            f = file(os.path.join(pkgDir, filename), 'r')
            try:
                data = f.read()
            finally:
                    f.close()
        except IOError:
            return "could not read documentation file"

        return data

    @cache(_cache_key)
    def htmldata(self):
        convert = getToolByName(self.context, 'portal_transforms').convertTo
        text = safe_unicode(convert('text/html', self._rstData(), mimetype='text/x-rst').getData())
        text = self._imageLinks(text)
        text = self._convertLinks(text)
        return text


    def _imageLinks(self, text):
        """
        convert
          <img alt="img/user-sharing.png" src="img/user-sharing.png" />

        to
          <img alt="img/user-sharing.png" src="++resource++my.documentation.images/user-sharing.png" />

        """

        return re.sub(r'<img alt="[\w/.-]*" src="img/(?P<img_id>[\S]+)" />',
                      '<img src="%s/\g<img_id>"/>' % self.plugin.resourceDir,
                      text)


    def _convertLinks(self, text):
        """
        convert
          <a class="reference external" href="fotoalbum.txt">
        to
          <a class="reference external" href="@@help?plugin=x.y&file=fotoalbum.txt">

        convert
          <a class="reference" href="#quicklinks">
        to
          <a class="reference" href="@@help?plugin=x.y#quicklinks">
        (happens automatically)
        """

        # do not touch href="# or href="http:// links
        text = re.sub(r'<a class="reference external" href="(?P<target_file>[\w.-]+?)">',
                      '<a class="reference external" href="%s&file=\g<target_file>">' % '%s?plugin=%s' % (self._baseUrl, self.currentPlugin),
                      text)

        text = text.replace('href="#', 'href="%s#' % self.viewStr)

        return text


    @Lazy
    def _baseUrl(self):
        context_state = getMultiAdapter((self.context, self.request), name='plone_context_state')
        return context_state.current_base_url()

    @Lazy
    def viewStr(self):
        url = self._baseUrl
        if self.currentPlugin:
            f = self.request.form.get('file', None)
            if f:
                return '%s?plugin=%s&file=%s' % (url, self.currentPlugin, f)
            else:
                return '%s?plugin=%s' % (url, self.currentPlugin)
        return url
