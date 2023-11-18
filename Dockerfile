FROM python:3.10-alpine

WORKDIR /app

COPY . /app/

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

# # to build and run the game
# docker build -t flask_docker .
# docker run -it -p 5000:5000 -d --name calc flask_docker

# # to start existing container and run the game
# docker start calc
# docker exec -it calc python3 main.py