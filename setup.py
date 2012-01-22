#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'TracExposeAttachmentPerms',
    version = '1.0',
    packages = ['exposeattachmentperms'],

    author = 'Colin Snover',
    author_email = 'tracplugins@zetafleet.com',
    description = 'Expose attachment plugins for Trac',
    long_description = 'A Trac plugin that exposes attachment permissions so they can be controlled separately.',
    license = 'MIT',
    keywords = 'trac plugin attachment permissions',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = ['Trac'],
    
    entry_points = {
        'trac.plugins': [
            'exposeattachmentperms = exposeattachmentperms',
        ],
    }
)

