.PHONY: stop
docker_name = django_container
docker_img = django_app
pwd = `pwd`

help: #prints list of commands
	@cat ./makefile | grep : | grep -v "grep"

show_containers: #start docker container #
	@sudo sudo docker ps

build: #build docker container #
	@sudo docker build -t $(docker_img) .

run: #start docker container #
	@sudo docker run --name $(docker_name) -v $(pwd):/home/docker/code/ -d -p 80:80 $(docker_img)

start:
	@sudo docker start $(docker_name)

stop: #stop docker container
	@sudo docker stop $(docker_name)

remove: stop #remove docker image
	@sudo docker rmi -f $(docker_name)

connect: #connect docker container #
	@sudo docker exec -it $(docker_name) bash

test:
	@echo $(pwd):/home/docker/code/