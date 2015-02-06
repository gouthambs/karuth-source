Using SQLAlchemy in Luigi Workflow Pipeline
###########################################

:date: 2015-02-05
:tags: Programming, Python, Luigi, SQLAlchemy
:slug: sqlalchemy-luigi-workflow-pipeline
:author: Gouthaman Balaraman
:description: This is a very basic example on using Luigi sqla contrib module in a task pipeline while using luigi
:keywords: Python, Programming, Luigi, Task Pipeline, SQLAlchemy, sqla 

The ``luigi.contrib.sqla`` provides support for SQLAlchmey through the ``SQLAlchemyTarget`` 
for storing in databases supported by SQLAlchemy. The user would be responsible for 
installing the required database driver to connect using ``SQLAlchemy``.

Minimal example of a job to copy data to database using ``SQLAlchemy`` is as shown
below:

.. code-block:: python

    from sqlalchemy import String
    import luigi
    from luigi.contrib import sqla

    class SQLATask(sqla.CopyToTable):
        # columns defines the table schema, with each element corresponding
        # to a column in the format (args, kwargs) which will be sent to
        # the sqlalchemy.Column(*args, **kwargs)
        columns = [
            (["item", String(64)], {"primary_key": True}),
            (["property", String(64)], {})
        ]
        connection_string = "sqlite://"  # in memory SQLite database
        table = "item_property"  # name of the table to store data

        def rows(self):
            for row in [("item1" "property1"), ("item2", "property2")]:
                yield row

    if __name__ == '__main__':
        task = SQLATask()
        luigi.build([task], local_scheduler=True)


If the target table where the data needs to be copied already exists, then
the column schema definition can be skipped and instead the reflect flag
can be set as True. Here is a modified version of the above example:

.. code-block:: python

    from sqlalchemy import String
    import luigi
    from luigi.contrib import sqla

    class SQLATask(sqla.CopyToTable):
        # If database table is already created, then the schema can be loaded
        # by setting the reflect flag to True
        reflect = True
        connection_string = "sqlite://"  # in memory SQLite database
        table = "item_property"  # name of the table to store data

        def rows(self):
            for row in [("item1" "property1"), ("item2", "property2")]:
                yield row

    if __name__ == '__main__':
        task = SQLATask()
        luigi.build([task], local_scheduler=True)


In the above examples, the data that needs to be copied was directly provided by
overriding the rows method. Alternately, if the data comes from another task, the
modified example would look as shown below:

.. code-block:: python

    from sqlalchemy import String
    import luigi
    from luigi.contrib import sqla
    from luigi.mock import MockFile

    class BaseTask(luigi.Task):
        def output(self):
            return MockFile("BaseTask")

        def run(self):
            out = self.output().open("w")
            TASK_LIST = ["item%d\tproperty%d\n" % (i, i) for i in range(10)]
            for task in TASK_LIST:
                out.write(task)
            out.close()

    class SQLATask(sqla.CopyToTable):
        # columns defines the table schema, with each element corresponding
        # to a column in the format (args, kwargs) which will be sent to
        # the sqlalchemy.Column(*args, **kwargs)
        columns = [
            (["item", String(64)], {"primary_key": True}),
            (["property", String(64)], {})
        ]
        connection_string = "sqlite://"  # in memory SQLite database
        table = "item_property"  # name of the table to store data

        def requires(self):
            return BaseTask()

    if __name__ == '__main__':
        task1, task2 = SQLATask(), BaseTask()
        luigi.build([task1, task2], local_scheduler=True)


In the above example, the output from `BaseTask` is copied into the
database. Here we did not have to implement the `rows` method because
by default `rows` implementation assumes every line is a row with
column values separated by a tab. One can define `column_separator`
option for the task if the values are say comma separated instead of
tab separated.

The other option to `sqla.CopyToTable` that can be of help with performance aspect is the
`chunk_size`. The default is 5000. This is the number of rows that will be inserted in
a transaction at a time. Depending on the size of the inserts, this value can be tuned
for performance.

