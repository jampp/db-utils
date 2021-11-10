.. _installation:

============
Installation
============

Install the system dependencies. For Debian based distributions,
they are:


.. code-block:: bash

    apt-get install -y gcc python3-dev libpq-dev


.. note::

    Use python2-dev if you are running migratron when using Python 2.7
    instead of Python 3.X


You can install ``migratron`` as another Python package:

.. code-block:: bash

    pip install migratron


Or you can install it from the repo:

.. code-block:: bash

    cd $WORKSPACE
    git clone https://github.com/jampp/migratron.git
    cd migratron
    python setup.py install


You will require different setups based on the database against which
you need to run the migrations.

PostgreSQL
==========

When using PostgreSQL, you only need to need to install a system package
to be able to use ``psql``. On Debian based distributions:

.. code-block:: bash

    apt-get install -y postgresql-contrib


Hive
====

You need to setup ``beeline``. This shouldn't be done on a production environment
or locally, but a **very** basic guide is:

.. code-block:: bash

    apt-get install -y openjdk-11-jre curl

    export HIVE_VERSION=1.2.1
    export HADOOP_VERSION=2.5.1

    cd /opt && \
        curl https://archive.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz -o apache-hive-bin.tar.gz && \
        tar -xzf apache-hive-bin.tar.gz && \
        rm -rf apache-hive-bin.tar.gz

    # Download apache-hadoop
    cd /opt && \
        curl https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -o hadoop-$HADOOP_VERSION.tar.gz && \
        tar -xzf hadoop-$HIVE_VERSION.tar.gz && \
        rm -rf apache-hive-bin.tar.gz

    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
    export HIVE_HOME=/opt/apache-hive-$HIVE_VERSION-bin
    export HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
    export PATH=$PATH:$HIVE_HOME/bin

PrestoDB or PrestoSQL
=====================

You need to setup ``presto-cli``. This shouldn't be done on a production environment
or locally, but a **very** basic guide is:

.. code-block:: bash

    apt-get install -y openjdk-11-jre curl

    # Download PrestoCli
    mkdir /opt/presto-cli && \
        cd /opt/presto-cli && \
        curl https://repo1.maven.org/maven2/io/prestosql/presto-cli/$PRESTO_CLI_VERSION/presto-cli-$PRESTO_CLI_VERSION-executable.jar -o presto-cli && \
        chmod +x presto-cli

    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
    export PATH=$PATH:$HIVE_HOME/bin

SQLAlchemy
==========

For the SQLAlchemy option you only need to install the drivers needed for you particular URI.
