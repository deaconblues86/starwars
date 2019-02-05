from distutils.core import setup

setup(name='StarWars',
      version='1.0',
      description='A few demo scripts run against the Star Wars API (https://swapi.co/)',
      author='Brian Hammill',
      author_email='hammillbc@gmail.com',
      url='https://github.com/deaconblues86/starwars',
      install_requires=[
        'sqlalchemy==1.2.17',
        'requests==2.21.0',
        'protobuf>=3.0.0',
      ]
)