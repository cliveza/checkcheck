FROM selenium/standalone-firefox

WORKDIR /home/seluser

ADD . /home/seluser

RUN sudo apt-get update && \
    sudo apt-get -y install python3-pip firefox

# RUN sudo chown -R seluser .local 

RUN pip3 install -r requirements.txt 

CMD bash bin/start.sh