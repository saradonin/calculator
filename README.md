## Flask Volume Calculator

This is a simple Flask web application that calculates the current volume of liquid in a bottle based on initial volume, initial weight, current weight, and liquid density to obtain the current volume.


### Getting started
To set up the Scent Swap App locally for development or testing purposes, follow these steps:

1. Build and run:
```
docker build -t flask_docker .
docker run -it -p 5000:5000 -d --name calc flask_docker
```
2. Stop:
```
docker stop calc
```
3. Restart:
```
docker start calc
docker exec -it calc python3 main.py
```
Ensure you have [Docker](https://www.docker.com/get-started/) installed before running these commands.

![flack_calc-removebg-preview](https://github.com/saradonin/flask-calculator/assets/124811561/fd45cd51-0c2a-4675-9815-59166054fd0b)
