from distutils.core import setup
setup(
  name = 'GETWEATHER',         # How you named your package folder (MyLib)
  packages = ['GETWEATHER'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Takes city name as input and gives youy weather for 5 days.',   # Give a short description about your library
  author = 'Sai Venkata Ramana P',                   # Type in your name
  author_email = 'saivenkat288@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/saivenkat288/Weather',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/saivenkat288/Weather/archive/0.3.tar.gz',    # I explain this later on
  keywords = ['CITY', 'WEATHER', 'OPENWEATHER'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'fastapi',
          'uvicorn',
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)