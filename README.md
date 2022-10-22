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

1 - Download and run image from dockerhub.com

```bash
docker pull viaramb/twsre:latest
docker run --name sre -p 5000:5000 -d viaramb/twsre
```
2 - Connect to containter and execute code
```bash
docker exec -it sre /bin/bash
python src/client/run.py
```
3 - Report is printed on screen if you would like to see the JSON report
```bash
cat client/data/output.json
```
## Client Output

file destination: src/client/data/output.json
