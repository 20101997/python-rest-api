
from fastapi import FastAPI

# Press the green button in the gutter to run the script.
from starlette.responses import Response

from jobHandler import JobHandler
from model.request.job import Job


class WebRequestHandler:

    def __init__(self,app):
        self.app = app
    def addJob(self):
      @self.app.post("/job")
      async def addJob(job: Job):
        try:
            JobHandler().addJob(job.id, job.name)
        except:
            return Response("Internal error", status_code=500)
        return Response("Job added successfully", status_code=200)

    def getJob(self):
      @self.app.get("/job/")
      async def getJob(id: int = 0):
         return JobHandler().getJobById(id)

    def findJob(self):
      @self.app.get("/job/search")
      async def findJob():
          ## to check : how to parse it into json with fastApi
         return JobHandler().findJob("dev")