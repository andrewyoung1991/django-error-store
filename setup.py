from setuptools import setup, find_packages

version = '0.1'

setup(
    name='django-error-store',
    packages=find_packages(),
    version=version,
    description='store django request objects for debugging server errors.',
    author='Andrew Young',
    author_email='ayoung@thewulf.org',
    download_url='https://github.com/andrewyoung1991/django-error-store.git',
    keywords=['django', 'debug', 'request', 'server-error'],
    package_data={},
)
