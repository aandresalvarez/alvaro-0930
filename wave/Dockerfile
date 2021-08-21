# FROM ubuntu:18.04
# RUN apt-get update
# RUN apt-get -y install wget
# RUN wget https://github.com/h2oai/wave/releases/download/v0.16.0/wave-0.16.0-linux-amd64.tar.gz

# RUN tar -xvf wave-0.16.0-linux-amd64.tar.gz && mv wave-0.16.0-linux-amd64 /wave && chmod +x /wave/waved

# WORKDIR /wave
# EXPOSE 10101/tcp
# ENTRYPOINT ["./waved"]
FROM ubuntu:18.04

ARG WAVE_VERSION

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y \
    curl

RUN curl -L https://github.com/h2oai/wave/releases/download/v${WAVE_VERSION}/wave-${WAVE_VERSION}-linux-amd64.tar.gz -o wave-${WAVE_VERSION}-linux-amd64.tar.gz \
    && tar -xzf wave-${WAVE_VERSION}-linux-amd64.tar.gz \
    && mv wave-${WAVE_VERSION}-linux-amd64 /usr/wave