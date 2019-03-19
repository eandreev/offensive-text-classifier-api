FROM ubuntu:18.04
RUN apt-get clean && apt-get update
RUN apt-get install locales
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

EXPOSE 80

RUN apt-get update
RUN apt-get install \
    python3 \
    python3-pip \
    python3-dev \
    supervisor \
    nginx \
    vim curl \
    psmisc htop \
    -y

RUN pip3 install \
    sklearn nltk \
    uwsgi Django djangorestframework

ADD . /src-code
ADD model/model.pickle /opt/

RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY nginx.global.conf /etc/nginx/nginx.conf

ADD supervisord.conf /etc/supervisor/conf.d/

CMD ["/usr/bin/supervisord"]
