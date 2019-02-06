FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN pip3 install django==2.1.5 mysqlclient==1.4.1 django-crispy-forms==1.7.2
