"""Main setup file"""

import setuptools

setuptools.setup(
    name="lfhohmann",
    author="Lucas Hohmann",
    author_email="lfhohmann@gmail.com",
    version="0.0.3",
    description="Hello world from @lfhohmann!",
    keywords="example, pypi, package, helloworld",
    py_modules=["lfhohmann_test"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # entry_points={
    #     "console_scripts": [  # This can provide executable scripts
    #         "lfhohmann_run=lfhohmann:entry_point",
    #     ],
    # },
)
