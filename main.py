
from dbClient import DBClient
from fastapi import FastAPI

# Press the green button in the gutter to run the script.
from starlette.responses import Response

# JobHandler().addJob(2, "engineer")
from webRequestHandler import WebRequestHandler
app = FastAPI()

WebRequestHandler(app).findJob()



