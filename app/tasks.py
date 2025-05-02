from celery import Celery
from app.mock_scraper.core import run_scraper

app = Celery(
    "tasks",
    broker="pyamqp://guest@localhost//",  # RabbitMQ
)


@app.task
def process_job(job_id, data):
    print(f"[{job_id}] Job received with data: {data}")
    run_scraper(data)
    print(f"[{job_id}] Job completed.")
