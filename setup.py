from setuptools import setup


template_patterns = ['templates/*.html',
                     'templates/*/*.html',
                     'templates/*/*/*.html',
                     ]

package_name = 'django-bitcoin'
packages = ['django_bitcoin',
            'django_bitcoin.management',
            'django_bitcoin.management.commands',
            'django_bitcoin.templatetags',
            'django_bitcoin.templates',
            'django_bitcoin.migrations',
            'django_bitcoin.jsonrpc']

long_description = open("README.rst").read() + "\n" + open("CHANGES.rst").read()

requirements = [
    'celery',
    'distributedlock',
    'pytz',
    #'qrcode>2.3.1',
]

setup(name='django-bitcoin',
      version='0.2.1',
      description='Bitcoin application integration for Django web framework',
      long_description=long_description,
      author='42 Coffee Cups',
      url='https://github.com/42cc/django-bitcoin',
      #requires=["qrcode (>2.3.1)", "South (>0.7.4)"],
      license="MIT",
      packages=packages,
      package_data=dict((package_name, template_patterns) for package_name in packages),
      install_requires=requirements,
      )
