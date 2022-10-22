# Storage SRE Coding Challenge

## Description

This project emulates 1000 servers that returns the Cache, Webapp or Database status
through the server.py API. Client.py connects to server API a 1000 times 
to emulate 1000 servers, collects data and generates 2 reports one human 
readable and another in JSON format.

## Versions
Server Version: 1.0

Client Version: 1.0

Python: 3.8 

## Installation

## Option 1: Directly on a Linux host
1 - Extract files in a directory under the destination server.
```bash
git clone https://github.com/viaramb/twsre.git
or 
unzip twsre.zip
```

2 - Install python requirements (is recommended to use a python virtual environment)
```bash
cd twsre/
pip install -r requirements.txt
```

3 - Turn on API server

```bash
cd twsre/src/
python server/server_run.py &
```

4 - Execute client
```bash
python client/run.py
```
## Option 2: Docker Desktop

1 - Generate docker image.

```bash
docker build  -t twsre .
docker run -i -p 5000:5000 -d twsre
```

2 - Get client name or container id
```bash
docker container ls
```

3 - Run client
```bash
docker exec -it <container-id/name> sh -c "python client/run.py"
```

## Option 3: Docker Hub

1 - Download and run image from dockerhub.com

```bash
docker pull viaramb/twsre:latest
docker run -i -p 5000:5000 -d viaramb/twsre:latest
```
2 - Run client
```bash
docker exec -it <container-id/name> sh -c "python client/run.py"
```
3 - To get JSON report login to Container
```bash
docker exec -it <container-id/name> bash
cat client/data/output.json
```
## Client Output

file destination: src/client/data/output.json
