from setuptools import setup
setup(
  name = 'distancetoroad',
  packages = ['distancetoroad'],
  version = '1.0',
  description = 'compute distance to road for aritrary point using OSM data (automatically downloads). Caches..',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/lionfish0/distancetoroad.git',
  download_url = 'https://github.com/lionfish0/distancetoroad.git',
  keywords = ['OSM','distance','map','roads'],
  classifiers = [],
  install_requires=['numpy'],
)
