from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="spar-model",
    version="0.1.0",
    author="Sofien Kaabar, CFA",
    author_email="sofien-kaabar@hotmail.com",
    description="Sequential Pattern Averaging Regressor - A non-parametric time series forecasting model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sofienkaabar/spar-model",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
    ],
    extras_require={
        "fast": ["numba>=0.50.0"],
        "examples": ["yfinance", "matplotlib"],
        "dev": ["pytest", "yfinance", "matplotlib"],
    },
    keywords="time-series forecasting pattern-recognition finance trading machine-learning",
)
