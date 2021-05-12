import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'bcrypt',
    'cryptography',
    "mod_wsgi",
    'pymysql',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_tm',
    'sqlalchemy',
    'zope.sqlalchemy',
]

develop_require = [
    'pyramid_debugtoolbar',
    'waitress',
    'mypy',
    'autopep8',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(name='thinkStream',
      version='0.1',
      description='thinkStream is web app',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
          'develop': develop_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = thinkStream:main
      [console_scripts]
      initialize_thinkStream_db = thinkStream.scripts.initializedb:main
      """,
      )
