from setuptools import setup

setup (
    name="wshpackages",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "weather app models and sqlalchemy objects",
    packages=['wsh_config','wsh_models'],
    python_requires=">=3.6",
    )