from setuptools import setup

setup(name='kant',
      version='0.1',
      description='Critique of pure reason',
      url='http://github.com/suciutwo/kant',
      author='Andrew Suciu',
      author_email='suciu@cs.stanford.edu',
      license='MIT',
      packages=['kant'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)