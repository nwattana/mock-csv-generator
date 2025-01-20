FROM python:3.13.1-bullseye

COPY . /app

ARG UID=1000
ARG GID=1000
ARG SIZE=100

RUN groupadd -g ${GID} appgroup && \
    useradd -m -u ${UID} -g appgroup appuser

    
RUN mkdir -p /app 
RUN chown appuser:appgroup -R /app
    
USER appuser
# RUN chmod +x /app/alive.sh

WORKDIR /app

RUN pip install -r ./requirements.txt

CMD ["python", "main.py"]