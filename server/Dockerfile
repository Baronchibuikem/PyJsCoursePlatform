
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.3-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

#PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B)
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /pyjs

# Set the working directory to /pyjs
WORKDIR /pyjs

# Copy the current directory contents into the container at /pyjs
ADD . /pyjs/

# install psycopg2 dependencies
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# RUN pip install -r /requirements.txt
# RUN apk del .tmp

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# FOR RUNNING ON PRODUCTION
# # The first instruction is what image we want to base our container on
# # We Use an official Python runtime as a parent image
# FROM python:3.8-alpine

# COPY ./requirements.txt /requirements.txt
# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# RUN pip install -r /requirements.txt
# RUN apk del .tmp

# RUN mkdir /pyjs
# COPY . /pyjs
# WORKDIR /app
# COPY ./scripts /scripts

# RUN chmode +x /scripts/

# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# # creates a user that will be used for running our processes
# RUN adduser -D user
# RUN chown -R user:user /vol
# RUN chmod -R 755 /vol/web
# USER user

# CMD ["entrypoint.sh"]

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONUNBUFFERED 1

# ENV PATH="/scripts:${PATH}"

# #PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B)
# ENV PYTHONDONTWRITEBYTECODE 1



# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers


# # create root directory for our project in the container
# RUN mkdir /docker_pyjs_app

# # Set the working directory to /pyjs
# WORKDIR /docker_pyjs_app

# # Copy the current directory contents into the container at /pyjs
# COPY . /docker_pyjs_app/
# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
# RUN apk del .tmp

# RUN chmode +x /scripts/*

# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# # creates a user that will be used for running our processes
# RUN adduser -D user
# RUN chown -R user:user /vol
# RUN chmod -R 755 /vol/web
# USER user

# CMD ["entrypoint.sh"]