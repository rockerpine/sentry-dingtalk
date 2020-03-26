#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry-dingtalk",
    version='1.0.0',
    author='ansheng',
    author_email='ianshengme@gmail.com',
    url='https://github.com/anshengme/sentry-dingtalk',
    description='A Sentry extension which send errors stats to dingtalk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry dingtalk',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'sentry.plugins': [
            'Sentry_DingTalk = Sentry_DingTalk.plugin:DingTalkPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
