FROM python:3.6.5

WORKDIR /usr/src/app

COPY k8test .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/sh","docker-entrypoint.sh"]
