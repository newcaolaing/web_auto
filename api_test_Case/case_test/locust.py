from locust import HttpLocust,TaskSet,task

class Userbe(TaskSet):

    @task(2)
    def test_users(self):
        self.client.get("/users/",auth=('test','test12345'))

    @task(1)
    def test_groups(self):
        self.client.get("/groups/",auth=('test','test12345'))

class Website(HttpLocust):
    task_set = Userbe
    min_wait = 3000
    max_wait = 6000