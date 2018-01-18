from distutils.core import setup

setup(
    name='lumpy',
    version='0.11.16',
    packages=['lumpy'],
    install_requires=['numpy', 'pygame', 'imagehash', 'PIL', 'ephem'],
    url='',
    license='',
    author='astrostaszic',
    author_email='',
    description='',
    entry_points={
        'console_scripts': ['mnist=test.cam:main']
    }
)
