FROM ubuntu

RUN apt-get update \
    && apt-get install -y python3-six 

RUN apt-get update \
    && apt-get install -y build-essential python3-dev vim python3-pip libsndfile1

RUN pip3 install scipy matplotlib librosa soundfile

COPY . ./abbey_road_19/

ENV PYTHONPATH /usr/local/lib/python3/dist-packages

WORKDIR ./abbey_road_19/

