from distutils.core import setup

setup(name='django-bitcoin',
      version='1.0',
      description='bitcoin payment management for django',
      author='Jeremias Kangas',
      url='https://github.com/kangasbros/django-bitcoin',
      packages=['django_bitcoin', 
                'django_bitcoin.management',
                'django_bitcoin.management.commands',
                'django_bitcoin.jsonrpc'],
     )