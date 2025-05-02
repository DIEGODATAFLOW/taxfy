from fastapi import FastAPI, Request
from app.tasks import process_job
import uuid

app = FastAPI()


@app.post("/submit-job")
async def submit_job(request: Request):
    data = await request.json()
    job_id = str(uuid.uuid4())
    process_job.delay(job_id, data)
    return {"message": "Job submitted", "job_id": job_id}
