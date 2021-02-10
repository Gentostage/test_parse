FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv install --system --deploy --ignore-pipfile
ADD . /web_django/ 