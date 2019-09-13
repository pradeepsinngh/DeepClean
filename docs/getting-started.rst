:tocdepth: 3

Getting Started
===============

Installing DeepClean
-----------------

To install TinyDB from PyPI, run::

    $ pip install deepclean

You can also grab the latest development version from GitHub_. After downloading
and unpacking it, you can install it using::

    $ python setup.py install


Basic Usage
-----------

Let's cover the basics before going more into detail. We'll start by setting up
a  database:

>>> from deepclean import Normalizer, Tokenization
>>> nm = Normalizer(text)

You now have a TinyDB database that stores its data in ``db.json``.
What about inserting some data? TinyDB expects the data to be Python ``dict``\s:

>>> db.insert({'type': 'apple', 'count': 7})
>>> db.insert({'type': 'peach', 'count': 3})

.. note:: The ``insert`` method returns the inserted document's ID. Read more
          about it here: :ref:`document_ids`.


Now you can get all documents stored in the database by running:

>>> db.all()
[{'count': 7, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]

You can also iter over stored documents:

>>> for item in db:
>>>     print(item)
{'count': 7, 'type': 'apple'}
{'count': 3, 'type': 'peach'}

Of course you'll also want to search for specific documents. Let's try:

>>> Fruit = Query()
>>> db.search(Fruit.type == 'peach')
[{'count': 3, 'type': 'peach'}]
>>> db.search(Fruit.count > 5)
[{'count': 7, 'type': 'apple'}]


Next we'll update the ``count`` field of the apples:

>>> db.update({'count': 10}, Fruit.type == 'apple')
>>> db.all()
[{'count': 10, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]


In the same manner you can also remove documents:

>>> db.remove(Fruit.count < 5)
>>> db.all()
[{'count': 10, 'type': 'apple'}]

And of course you can throw away all data to start with an empty database:

>>> db.purge()
>>> db.all()
[]


Recap
*****

.. References
.. _GitHub: http://github.com/msiemens/tinydb/
