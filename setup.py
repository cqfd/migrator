from setuptools import setup

setup(
    name="migrator",
    version="0.0",
    packages=["migrator", "migrator.commands"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        migrator=migrator.migrator:cli
    """,
)
