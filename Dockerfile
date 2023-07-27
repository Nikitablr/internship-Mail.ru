FROM python:3.8-alpine

WORKDIR ./usr/lessons

COPY . .

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev


RUN pip install -r requirements.txt

CMD pytest -s -v tests/test_letter.py tests_api/test_api.py --alluredir=allure

