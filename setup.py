from distutils.core import setup

setup(name='StarWars',
      version='1.0',
      description='A few demo scripts run against the Star Wars API (https://swapi.co/)',
      author='Brian Hammill',
      author_email='hammillbc@gmail.com',
      url='https://github.com/deaconblues86/starwars',
      install_requires=[
        'protobuf>=3.0.0',
        'mysqlclient==1.4.1',
        'sqlalchemy==1.2.17',
        'requests==2.21.0',
      ]
)