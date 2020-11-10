FROM python:3.7-buster

LABEL version="2.0.1"
LABEL maintainer="Jampp Tech Team <tech@jampp.com>"

# << Container build arguments

ARG MIGRATRON_VERSION=2.0.1
ARG HIVE_VERSION=2.3.2
ARG HADOOP_VERSION=2.5.1
ARG PRESTO_CLI_VERSION=345


ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=linux
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
ENV HIVE_HOME=/opt/apache-hive-$HIVE_VERSION-bin
ENV HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
ENV PATH=$PATH:$HIVE_HOME/bin:/opt/presto-cli

USER root

# Install OS dependencies
RUN apt-get update && \
    apt-get install -y curl gcc python3 python3-dev libpq-dev openjdk-11-jre postgresql-contrib

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py

# Download all the Jars required to run Beeline
RUN cd /opt && \
    curl https://archive.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz -o apache-hive-bin.tar.gz && \
    tar -xzf apache-hive-bin.tar.gz && \
    rm -rf apache-hive-bin.tar.gz

# Download apache-hadoop
RUN cd /opt && \
    curl https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -o hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzf hadoop-$HADOOP_VERSION.tar.gz && \
    rm -rf apache-hive-bin.tar.gz

# Download PrestoCli
RUN mkdir /opt/presto-cli && \
    cd /opt/presto-cli && \
    curl https://repo1.maven.org/maven2/io/prestosql/presto-cli/$PRESTO_CLI_VERSION/presto-cli-$PRESTO_CLI_VERSION-executable.jar -o presto-cli && \
    chmod +x presto-cli
    

# Install migratron
RUN pip install migratron==$MIGRATRON_VERSION
