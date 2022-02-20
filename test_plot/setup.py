from setuptools import setup

setup(
    name = "test_plot",
    version = "0.1.0",
    description = "testing a plot package",
    url = "https://github.com/shuds13/pyexample",
    author = "Henry of Skalitz",
    author_email = "popcorndevils@gmail.com",
    license = "BSD 2-clause",
    packages = ["test_plot"],
    install_requires = ["ipywidgets", "plotly", "ipython"],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
