from setuptools import setup, find_packages

setup(
    name="computer_vision",
    version="0.1",
    author="nusret",
    author_email="-",
    description="A computer vision project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "opencv-python",
        "mediapipe",
        "scipy",
        "matplotlib",
        "scikit-learn",
        "pandas",
        "loguru",
        "pytest",
        "coverage"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
