from setuptools import setup, find_packages # type: ignore

setup(
    name='pi_lib',
    version='0.1',
    packages=find_packages(),
    description="This is a library created for tasks on the 'Podstawy informatyki'.",
    author='Kamil Cygan',
    author_email='kacygan@student.agh.edu.pl',
    url='https://github.com/ModeryINC/pi_lib.git',
    install_requires=[
        'numpy>=2.1.2',
        'scipy>=1.14.1',
        'matplotlib>=3.9.2'
    ],
)
