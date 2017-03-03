/**
 * Created by rockdong on 2017/2/8.
 */
{% load staticfiles %}

function regist() {
    self.location = "{% url 'regist' %}";
}

function forget() {
    self.location = "forget";
}

function login() {
    self.location = "login";
}