from setuptools import setup, find_packages
setup(
    name='gembox',
    version='0.1.14.0',
    packages=find_packages(),
    install_requires=[
    ],
    url='https://github.com/stevieflyer/gembox',
    author='Steve Flyer',
    author_email='steveflyer7@gmail.com',
    description='This is the gembox toolbox for steve flyer. You can also find your hammers here.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'ls-py=gembox.scripts.ls_py:main'
        ]
    },
)
# To build
# python setup.py sdist bdist_wheel
# To upload
# twine upload dist/*
