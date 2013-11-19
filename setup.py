from setuptools import setup

long_description = """
Python bindings for Capsule CRM API.

See the repo home for usage instructions at
 https://github.com/leetrout/python-capsule-crm/
"""

setup(
    name='capsule_crm',
    version='0.1.2',
    description='Capsule CRM Python API wrapper',
    long_description=long_description,
    author='Lee Trout',
    author_email='leetrout@gmail.com',
    url='https://github.com/leetrout/python-capsule-crm/',
    py_modules=['capsule_crm'],
    install_requires=['requests>=2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
