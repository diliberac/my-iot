FROM python:3.9-slim-buster
LABEL description="DASHBOARD"
LABEL maintainer="cfreire@cfreire.com.pt"
ARG FRONTEND_VERSION='DEV'
ENV FRONTEND_VERSION=${FRONTEND_VERSION}
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV TZ=Europe/Lisbon
EXPOSE 8050
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python3", "app.py"]

# docker run -it --rm  -p 80:8050 --link rest_server dashboard

