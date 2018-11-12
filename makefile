docker_name = django_app
docker_img = django_img

help: #prints list of commands
	@cat ./makefile | grep : | grep -v "grep"

show_containers: #start docker container #
	@sudo sudo docker ps

build: #build docker container #
	@sudo docker build -t $(docker_name) .

start: #start docker container #
	@sudo docker run --rm --name django_app -d -p 80:80 django_app 
stop: #stop docker container
	@sudo docker stop $(docker_name)

remove: stop #remove docker image
	@sudo docker rmi -f $(docker_name)