from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name="Kanishkan-Test",
        version="0.1.1",
        packages=find_packages(),
        description="Test Package to try functionality",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/kkanishkan/testpypi-package",
        author="Kanishkan Kukarajah",
        author_email="kanishkan77@gmail.com",
        license="MIT",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
        ],
        install_requires=[],
        entry_points="""
        [console_scripts]
        testPackage=testPackage.__main__:main
        """,
        )
