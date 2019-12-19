from distutils.core import setup

entry_points = {
    'console_scripts': [
        'querypy=querypy.main:main'
    ]
}

setup(
    name="querypy",
    packages=["querypy"],
    version="0.0.0",
    entry_points=entry_points,
    dependencies=[]
)