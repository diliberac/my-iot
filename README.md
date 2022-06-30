# My Iot

IoT temperature Dashboard in Python


## Create a swarm
3 managers and 2 workers

## Set up a Docker registry

`docker service create --name registry --publish published=5000,target=5000 registry:2`

## Manual Build

Clone repo  
`git clone https://gitlab.com/form-cfreire/my_iot.git`

`cd my_iot`

## Build images
`docker build -t 127.0.0.1:5000/mqtt_client mqtt-client/`
`docker build -t 127.0.0.1:5000/rest_server rest-server/`
`docker build -t 127.0.0.1:5000/dashboard dashboard/`

# Push images to local repository
`docker push 127.0.0.1:5000/mqtt_client:latest`
`docker push 127.0.0.1:5000/rest_server:latest`
`docker push 127.0.0.1:5000/dashboard:latest`

## Remove all local images
`docker rmi $(docker images -q)`

## Deploy Stack
`docker stack deploy --compose-file docker-compose.yml iot`

## Verify stack
`docker service ls`


