from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(0.5, 1.5)
    host = "http://localhost:8000"   # Change to your API host

    def on_start(self):
        """Initialize user parameters once"""
        self.params = {"user": "locust_user"}

    @task(3)
    def view_my_events(self):
        """Fetch user's events"""
        with self.client.get(
            "/my-events",
            params=self.params,
            name="View My Events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")



