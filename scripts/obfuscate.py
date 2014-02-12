# -*- coding: utf-8 -*-
"""
Obfuscate email adresses as well as complete `mailto:` tags

Based on [django-email-obfuscator](https://github.com/morninj/django-email-obfuscator)
by Joseph Mornin.
"""

def obfuscate_string(value):
    return ''.join(['&#%s;' % str(ord(char)) for char in value])

def obfuscate(value):
    return obfuscate_string(value)

def obfuscate_mailto(value):
    mail = obfuscate_string(value)
    return '<a href="%s%s">%s</a>' % (obfuscate_string('mailto:'), mail, mail)
