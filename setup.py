from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import nltk
import spacy
import subprocess
import sys

def readme():
    with open('README.md', encoding="utf8") as f:
        README = f.read()
    return README

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        nltk.download('vader_lexicon')
        try:
            spacy.load('en_core_web_sm')
        except IOError:
            subprocess.call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        nltk.download('vader_lexicon')
        try:
            spacy.load('en_core_web_sm')
        except IOError:
            subprocess.call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        install.run(self)

setup(
    name='finemotion',
    version='0.1',
    description='Our emotional annotation algorithm is built upon the foundation laid by the Text2Emotion project, with a series of key enhancements aimed at optimizing its functionality for financial news analysis',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author="AliceNN-ucdenver",
    author_email="shawn.mccarthy@ucdenver.edu",
    url="https://github.com/AliceNN-ucdenver/Fin-Emotion",
    license="MIT",
    install_requires=[
        'spacy',
        'nltk',
        'contractions',
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    package_data={
        '': ['data/*'],
    },
    include_package_data=True,
)