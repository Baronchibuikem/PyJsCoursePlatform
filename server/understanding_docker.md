## For Dockerfile in the root directory

The first directive in the Dockerfile, FROM python:3.6 tells Docker which image to base our container on. We use the official Python image from Dockerhub that comes with Python and Linux setup for you, ready for use in a python project.

The next directive ENV PYTHONUNBUFFERED 1 is an environment variable, which instructs Docker not to buffer the output from Python in the standard output buffer, but simply send it straight to the terminal.

The directive that starts with RUN instructs Docker to execute what ever command that comes after as if you were executing it in a terminal on a server.

In the Dockerfile above, RUN mkdir /pyjs instructs Docker to create a folder in the container called pyjs which we shall use to store our application files.

The directive that starts with WORKDIR sets the working directory and all the directives that follow in the Dockerfile will be executed in that directory.
In the Dockerfile above, I set the working directory to pyjs . I then ADD all files in my project root directory where the Dockerfile is to the pyjs directory in the container. The ADD directive copies files and directories from the source to the destination specified in the directive.

The last directive instructs Docker to RUN the pip command to install the requirements listed in the requirements.txt .

With that, we have our Dockerfile for the container image.

## For the docker compose

The first line in the docker-compose.yml file specifies which syntax version of Docker compose you want to use.

Next, we define a service called web . The build directive tells Docker compose to build an image from the files in the project root directory. The command directive is the default command that will be executed when Docker runs the container image.

The container_name directive assigns a name for the container. If no name is specified, Docker will assign the container a random name. The volume directive mounts the project root directory to the container music_service folder. In essence what this does is; It makes sure that when I edit any file in the project folder, the container folder is updated immediately.

Lastly we expose the port we want to access the container on using the ports directive.

With that done, you can now build and run the container with the command; docker-compose up . If your build is successful, open your browser and access your API or application. In my case I access all my songs using my API on 127.0.0.1:8000/api/v1/songs . You can also try to access the Django admin at 127.0.0.1:8000/admin . If you can see the login page, then your container is up and running.





Restart : This container should always be up, and it will restart if it crashes
Build : We have to build this image using a Dockerfile before running it, this specifies the directory where is located the Dockerfile
Expose : We expose the port 8000 to linked machines (that will be used by the NGINX container)
Links : We need to have access to the postgres instance using the postgres name (This create a postgres entry in the /etc/hosts files that point to the postgres instance IP), idem for the redis.
Env_file : This container will load all the environment variables from the env file.
Volumes : we specify the different mountpoints we want on this instance
Command : What command run when starting the container ? Here we start the wsgi process.

Here instead of the build option, we have the image option that targets an existing image on the Docker registry
we also use volumes_from to load all the volumes of another container. We use it on the Nginx container to load the static directory from the application and serve it, and on the PostgreSQL container to load the persistent tablespace that is in the data container.