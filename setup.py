import setuptools
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="atlantic",
    version="1.0.21",
    description="Atlantic is an automated preprocessing framework for supervised machine learning",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    url="https://github.com/TsLu1s/Atlantic",
    author="Luís Santos",
    author_email="luisf_ssantos@hotmail.com",
    license="MIT",
    python_requires='>=3.7.1',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["atlantic"],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},  
    keywords=[
        "data science",
        "machine learning",
        "data processing",
        "predictive modeling",
        "data preprocessing",
        "automated data preprocessing",
        "automated machine learning",
        "automl",
    ],           
    install_requires=open("requirements.txt").readlines(),
)
  
