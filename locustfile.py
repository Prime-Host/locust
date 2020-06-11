from locust import HttpLocust, TaskSet, between

def custom(l):
    l.client.get("/livestream")

def home(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {custom: 2, home: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
