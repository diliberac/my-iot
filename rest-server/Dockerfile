FROM python:3.9-slim-buster
LABEL description="REST_SERVER"
LABEL maintainer="cfreire@cfreire.com.pt"
ARG REST_VERSION='DEV'
ENV REST_VERSION=${REST_VERSION}
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV TZ=Europe/Lisbon
EXPOSE 8000
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python3", "webservice.py"]

# docker run -it --rm  -p 8000:8000 --link redis --link mongo rest_server
