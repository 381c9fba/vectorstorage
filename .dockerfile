FROM python:3.10

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN pip install --no-cache-dir fastapi

# CMD ["fastapi", "run", "app/main.py", "--port", "80"]
