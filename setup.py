from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='wm.help',
      version=version,
      description="Infrastructure to add a ReStructuredText based help system to plone sites",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone collective help documentation docutils rest restructuredtext',
      author='Harald Friessnegger',
      author_email='harald (at) webmeisterei dot com',
      url='http://webmeisterei.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
