FROM python:3.9-slim

COPY timer.py /timer.py
COPY run.sh /run.sh

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
