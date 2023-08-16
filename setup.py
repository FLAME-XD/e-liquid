from setuptools import setup



from Cython.Build import cythonize
setup(
    ext_modules = cythonize("liquid.pyx",compiler_directives={'language_level' : "3"})
)
