# Storage SRE Coding Challenge

## Description

This project emulates 1000 servers that returns the Cache, Webapp or Database status
through the server.py API. Client.py connects to server API a 1000 times 
to emulate 1000 servers, collects data and generates 2 reports one human 
readable and another in JSON format.

## Versions
Server Version: 1.0

Client Version: 1.0

Python: 3.9

## Installation

IMPORTANT: You will need to install docker in to your workstation. Follow instructions
under https://docs.docker.com/engine/install/ once docker is installed continue with below steps.

1 - Download and run image from dockerhub.com

```bash
docker pull viaramb/twsre:latest
docker run --name sre -p 5000:5000 -d viaramb/twsre
```
2 - Connect to containter
```bash
docker exec -it sre /bin/bash
```
3 - Execute code to print report on screen
```bash
python src/client/run.py
```
4 - If you would like to see report in JSON format
```bash
cat client/data/output.json
```

