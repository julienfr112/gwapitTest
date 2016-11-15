# gwapitTest

This is an employement test for http://gwapit.com/

## Prerequisite

- docker
- docker-compose

It does work with
- docker version 1.12.3, build 6b644ec
- docker-compose version 1.8.1, build 878cff1

It should work with other versions

## Install and run on Linux (ubuntu 16.04)

    git clone https://github.com/julienfr112/gwapitTest.git
    cd gwapitTest
    docker-compose up

Use your browser and go to the url : http://localhost:8081

## Problem it solve :

Using
* Ptyhon
* Django REST framework
* Angular

Do an application allowing to
* Start project with django docker
    https://docs.docker.com/compose/django/
* Use DjangoREST framework (improve django docker setup)
* Allow to subscribe as a django/user using the authorization of google allowing to access emails
    https://github.com/omab/python-social-auth
    http://django-social-auth.readthedocs.io/en/latest/backends/google.html
* Calls the last 100 emails
    https://developers.google.com/gmail/api/quickstart/python
* don't forget to init credential on google
    https://console.developers.google.com/apis/dashboard
* Display the 100 emails
* Allow to logout
* Allow to logback in
