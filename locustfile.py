from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def view_post(self):
        self.client.get("/post/1")

    @task(3)
    def signup(self):
        self.client.get("/signup")

    @task(4)
    def policy(self):
        self.client.get("/privacyPolicy")

    @task(5)
    def login(self):
        self.client.get("/login/redirect=&")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
