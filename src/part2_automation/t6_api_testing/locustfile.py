from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def welcome_message(self):
        self.client.get('http://localhost:5000')
# http://localhost:8089
# https://betterprogramming.pub/introduction-to-locust-an-open-source-load-testing-tool-in-python-2b2e89ea1ff
