from setuptools import setup
import re

with open('rqmailer/__init__.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

setup(
    name='MailShake-RQMailer',
    version=version,
    author='Robbie Clarken',
    author_email='robbie.clarken@gmail.com',
    license='MIT',
    url='https://github.com/RobbieClarken/MailShake-RQMailer',
    packages=['rqmailer'],
    install_requires=[
        'MailShake',
        'rq',
    ],
)
