# stringdb-beacon

Knowledge Beacon Wrapper for the StringDb resource (https://string-db.org/)

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Running with Docker

Use [Docker Compose](https://docs.docker.com/compose/) to build and run the application. 
Before using compose in the project, you should first copy the configuration file:

```
cp docker-compose.yaml-template docker-compose.yaml
```

The host machines `NEO4J_AUTH` environment variable is passed into the docker containers.  If it is not set then it will default to neo4j/password.  You can also directly modify the default password (plus Docker port redirections, etc.) 
in this 'docker-compose.yaml' file.  

Once ready to build, type the following into the terminal::

```
export NEO4J_AUTH=neo4j/<password>  # if you wish to change your default password
cd stringdb-beacon
docker-compose build
docker-compose up
```

> **Note:** If you don't wish to set a password, you can simply set NEO4J_AUTH=none. You can control which ports, if any at all, are exposed with the `docker-compose.yaml` file.

The Neo4j container's data, import, logs, and config directories will be mounted on the host machine at `$HOME/neo4j`. All the data in the database, including the username and password, will persist in the `$HOME/neo4j/data` directory over multiple runs of the container.

> **Note:** If the docker-compose commands are is giving you trouble, try running them as the system administrator with the `sudo` command. Remember, though, that if you are running  your commands as 'sudo', then depending on how your Linux instance configures sudo, in some cases, $HOME may actually be '/root' or it may otherwise still be in your normal user home. This may consequences for data importation (see below)

The API should now be running at http://localhost:5000/api, and the Neo4j browser user interface should be running at http://localhost:7474. You can open your browser with these addresses to see these applications in action. You wont see much until you load data into the database, though.

## Loading Data

String-db hosts its database at https://string-db.org/cgi/download.pl. You can get subsets of the database by selecting a species, so far we have only been using *Homo sapiens*. There is a python script `neo4j/download_stringdb_data.py` that can be used to download, unzip, and properly format the data for *Homo sapiens*. This script must be run with version 3 of python, in the terminal run `python --version` to check your version. If you will not be using this script you will need to manually fix TSV headers in some of the data files.

```
cd stringdb-beacon/neo4j
python3 download_stringdb_data.py
```

If you have used docker-compose to run the application, you will have a `neo4j/import` directory mounted in your $HOME directory. If you are running docker-compose as 'sudo', this directory may be '/root' in which case, you should may also run the download script as 'sudo' so thta $HOME defaults to '/root', which is where your Docker neo4j database will expect to see the data. If your $HOME directory is still your normal user home directory, you can likely still run this download script without sudo.

Your Neo4j docker container should be named stringdbbeacon_db_1, run `docker-compose ps` to confirm this. We will execute the load.cql file, which was copied over to the 'import' directory with the downloaded data, sing the Neo4j shell.

Before loading the data, you first turn off the docker container (from within the stringdb-beacon directory):

```
sudo docker-compose stop db

```

This will allow data loading directly using the neo4j-shell script, as follows:

```
sudo docker run --env=NEO4J_dbms.directories.import=/import --env=NEO4J_dbms_memory_heap_maxSize=1G  --volume=$HOME/neo4j/import:/import --volume=$HOME/neo4j/data:/data neo4j:latest /var/lib/neo4j/bin/neo4j-shell -path /data -file /import/load.cql
```

> **Note:** Again, if running other commands as 'sudo', then run this command as 'sudo' as well. If you see `java.lang.OutOfMemoryError: Java heap space`, then you may need to increase the Java heap size with the *NEO4J_dbms_memory_heap_maxSize* environment variable noted above.


## Issues

This beacon is a work in progress. Here are a few points that still need to be addressed
- So far the evidence and exactmatches API are not implemented.
- I have only been using data for *Homo sapiens*. We should also include mouse, rat, yeast, c. elegans, drosphila, and zebrafish species as well, to complement monarch biolink.
- Only a very small subset of the database files are being used.
