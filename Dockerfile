FROM python:3.9.10-bullseye

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY api/ /code/
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
