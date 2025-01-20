FROM python:3.13.1-bullseye

COPY . /app

# RUN chmod +x /app/alive.sh

WORKDIR /app

RUN pip install -r ./requirements.txt

CMD ["python", "main.py"]