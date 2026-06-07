from setuptools import setup

setup(
    name='inclusive-language-toolkit',
    version='0.1.0',
    description='Toolkit for inclusive language transformation, highlighting, statistics, and sentiment analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nikhil Preet Saini',
    license='MIT',
    py_modules=['inclusive_toolkit'],
    install_requires=[
        'textblob==0.17.1'
    ],
    entry_points={
        'console_scripts': [
            'inclusive-toolkit=inclusive_toolkit:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
