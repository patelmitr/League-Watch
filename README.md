# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## Start the Docker Containers
1. To start the docker containers, we must activate our environment which should be created using Anaconda-Navigator.
1. To activate the environment we use the command "conda activate <environment-name>".
1. This will then start the docker containers. 
1. To run the application we must use the command "docker compose up" in the terminal.
1. This will then start our application to be accessed locally.
1. To then access the application, go to a browser and go to "localhost:8080" and it should open up the appsmith page.
