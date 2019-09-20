from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/khufu/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()

setup(
    name='khufu',
    version=__version__,
    description='Twitter Bootstrap elements via Python',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords=['web'],
    url='https://github.com/thespacedoctor/khufu',
    download_url='https://github.com/thespacedoctor/khufu/archive/v%(__version__)s.zip' % locals(
    ),
    author='David Young',
    author_email='davidrobertyoung@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'khufu': [
        'resources/*/*', 'resources/*.*']},
    include_package_data=True,
    # install_requires=[
    #     'pyyaml'
    # ],
    test_suite='nose2.collector.collector',
    tests_require=['nose2', 'cov-core'],
    # entry_points={
    #     'console_scripts': ['funniest-joke=funniest.cmd:main'],
    # },
    zip_safe=False
)
