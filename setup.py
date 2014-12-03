from distutils.core import setup
MAJOR = 0
MINOR = 1
MICRO = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

with open('README.md') as readme:
    readme_lines = readme.readlines()

description = readme_lines[3].strip()
long_description = ''.join(readme_lines[4:])

setup(
    name = "crfmg_utils",
    packages = ["crmfg_utils"],
    description = description,
    long_description = long_description,
    version = VERSION,
    license = 'Apache 2.0',
    author = 'Fahrzin Hemmati',
    author_email = 'fahhem@gmail.com',
    url = 'https://github.com/crmfg/crmfg-utils',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)