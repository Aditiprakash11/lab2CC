from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(0.5, 1.5)   # Faster ramp-up for load testing
    host = "http://localhost:8000" # Change to your API host

    def on_start(self):
        """Runs once per user when spawned"""
        self.params = {"user": "locust_user"}

    @task(3)
    def view_events(self):
        """Weighted task (runs more frequently)"""
        with self.client.get(
            "/events",
            params=self.params,
            name="View Events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed with status {response.status_code}")


