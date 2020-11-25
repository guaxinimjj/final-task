FROM python:3.9-alpine

RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev

WORKDIR /department-app

COPY department_app ./department_app
COPY scripts ./scripts
COPY setup.py run.py ./

RUN pip install -e .

CMD ["gunicorn", "run:app"]
