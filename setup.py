import os
from setuptools import setup, find_packages


def src(pth):
    return os.path.join(os.path.dirname(__file__), pth)


setup(name='occamypy',
      version='0.1.0',
      url="https://github.com/fpicetti/occamypy",  # used for the documentation. TODO switch to readthedocs?
      description='An Object-Oriented Optimization Framework for Large-Scale Inverse Problems',
      long_description=open(src('README.md'), "r").read(),
      long_description_content_type='text/markdown',
      keywords=['algebra', 'inverse problems', 'large-scale optimization'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          # 'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Operating System :: Unix'
      ],
      license='GNU',
      author='Ettore Biondi, Guillame Barnier, Robert Clapp, Francesco Picetti, Stuart Farris',
      author_email='francesco.picetti@polimi.it',
      install_requires=['numpy >= 1.15.0', 'scipy', 'matplotlib', 'imageio', 'numba', 'h5py',
                        'dask', 'dask-jobqueue', 'dask-kubernetes', 'torch'],
      extras_require={  # one can install two of them with pip install occamypy[cuda]
          'cuda': ['cupy>=8.0', 'gputil', 'cusignal']},
      packages=find_packages(),
      
      zip_safe=True)
