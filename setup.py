from distutils.core import setup

entry_points = {
    'console_scripts': [
        'querypy=querypy.main:main'
    ]
}

setup(
    name="querypy",
    packages=["querypy", "querypy.utils"],
    version="0.0.0",
    entry_points=entry_points,
    dependencies=[]
)