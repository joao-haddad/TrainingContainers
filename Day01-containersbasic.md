# Day 1 - Containers Basic

Present the slides

open http://hub.docker.com

start the container:
`docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=P@ssw0rd!' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-CU8-ubuntu`

open the SQL client and create a database

`docker exec -it <container_id|container_name> /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P <your_password>`
`CREATE DATABASE ITS;`
`GO`
`exit`

connect to the container:

`docker exec -it <containter_id> bash`
`cd /var/opt/mssql`

show the data

Now delete the container and recreate:

`docker kill container`

`docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=P@ssw0rd!' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-CU8-ubuntu`

No database anymore
`docker kill container`

create the container with a folder direction

`docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=P@ssw0rd!' -p 1433:1433 -v /home/ubuntu/sqldata:/var/opt/mssql/data -d mcr.microsoft.com/mssql/server:2017-CU8-ubuntu`

Create the DB, delete the container and recreate the container. The DB should still be there

## PART B - creating a DockerFile

Show the app
Show the DockerFile

`docker build --tag hello-world .`

`docker run -p 8080:8080 hello-world`
