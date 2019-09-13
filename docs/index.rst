Welcome to DeepClean!
==================

DeepClean is a multimodal data pre-processing and cleaning package written in python.

Features
-----------
- Single package for multi modal data pre-processing and cleaning.
- Fast Experimentation
- Modularity in the data (processing) pipeline
- Implements techniques like:
    - Normalization
    - Tokenization
    - Augmentation
    - Denoising
    - and much more.

>>> from deepclean.image import Augmentation
>>> aug = Augmentation('path/to/image')

>>> from deepclean.text import Tokenization
>>> tk = Tokenization('path/to/text')

User's Guide
------------

.. toctree::
   :maxdepth: 2

   intro
   getting-started
   usage


API Reference
-------------

.. toctree::
   :maxdepth: 2

   api
