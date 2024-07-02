from setuptools import setup

setup(
    name = 'roc_det_plotter',
    version = '0.1.0',
    author = 'Doruk Ozar',
    author_email = 'dorukozar@gmail.com',
    packages = ['roc_det_plotter'],
    url = 'https://github.com/Dorukozar/New-Package',
    license = 'MIT',
    description = 'Create ROC and DET plots',
    long_description = open('README.md').read(),
    install_requires = ["matplotlib", "pandas", "numpy"],
)