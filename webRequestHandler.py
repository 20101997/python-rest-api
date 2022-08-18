
from fastapi import FastAPI

# Press the green button in the gutter to run the script.
from handler.jobHandler import JobHandler
from starlette.responses import Response

class WebRequestHandler:

    def __init__(self,app):
        self.app = app
    def addJob(self):
      @self.app.post("/job")
      async def addJob():
        try:
            JobHandler().addJob(10, "engineer")
        except:
            return Response("Internal error", status_code=500)
        return Response("Job added successfully", status_code=200)

    def getJob(self,id: int):
      @self.app.get("/job")
      async def getJob(id: int):
         return JobHandler().getJobById(id)

    def findJob(self, id: int):
      @self.app.post("/job")
      async def findJob(self):
         JobHandler().findJob("dev")