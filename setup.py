from setuptools import setup, find_packages


requirements = [
    'Flask==0.10.1',
]

setup(
    name='Flask-Pundit',
    version='1.0.0',
    license='MIT',
    url='https://github.com/anurag90x/flask-pundit',
    author='Anurag Chaudhury',
    author_email='anuragchaudhury@gmail.com',
    description='Simple library to manage resource authorization and scopoing',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    install_requires=requirements,
    tests_require=['mock==1.3.0'],
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
    ]
)
