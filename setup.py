from setuptools import setup
REQUIRES = [
    'sqlalchemy',
    'structlog'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/July-vilh/orm_client.git',
    license='MIT',
    author='Yuliya Vilchynskaya',
    install_requires=REQUIRES,
    author_email='-',
    description='orm_client info'
)
