FROM python:3.6-jessie

ENV noninteractive=true

RUN apt-get update && \
	apt-get install -y apt-utils \
	apt-transport-https \
	locales \
	python3-dev \
	supervisor \
	nginx

WORKDIR /challenge_app

COPY ./requirements.txt /challenge_app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /challenge_app/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \
    cp -r /challenge_app/conf/challenge_nginx.conf /etc/nginx/sites-available/default && \
    cp -r /challenge_app/conf/challenge_supervisor.conf /etc/supervisor/conf.d/ && \
    cp -r /challenge_app/conf/uwsgi.ini /challenge_app/

EXPOSE 6606
CMD ["supervisord"]