# Rest Server

WEB REST API from redis and mongo server


## Build

    docker build -t rest_server rest-server/
    
## Run

    docker run -it --rm  -p 8000:8000 --link redis --link mongo rest_server