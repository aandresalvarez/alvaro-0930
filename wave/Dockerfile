FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install wget
RUN wget https://github.com/h2oai/wave/releases/download/v0.16.0/wave-0.16.0-linux-amd64.tar.gz

RUN tar -xvf wave-0.16.0-linux-amd64.tar.gz && mv wave-0.16.0-linux-amd64 /wave && chmod +x /wave/waved

WORKDIR /wave
EXPOSE 10101/tcp
ENTRYPOINT ["./waved"]