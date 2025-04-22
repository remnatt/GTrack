# setup.py
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="logger_wrapper",
        sources=["logger_wrapper.pyx", "logger.c"],
        include_dirs=["src"]
    )
]

setup(
    name="GTrackLogger",
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': "3"}
    )
)
