from sqlalchemy.orm import sessionmaker

from dbClient import DBClient
from model.job import Job


class JobHandler:
    def connectToDb(self):
        return DBClient().connectToDb()

    def addJob(self, id, name):
        engine = self.connectToDb()
        new_rec = Job(id=id, name=name)
        factory = sessionmaker(bind=engine)
        session = factory()
        session.add(new_rec)
        session.commit()

    def getJobById(self, id):
        engine = self.connectToDb()
        factory = sessionmaker(bind=engine)
        session = factory()
        session.query(Job).get(id)
        return session.query(Job).get(id)

    def findJob(self, text):
        engine = self.connectToDb()
        factory = sessionmaker(bind=engine)
        session = factory()
        session.query(Job).get(id)
        ##print(session.query(Job).filter(Job.name.ilike(f'%engineer%')).all()[0].id)
        return session.query(Job).filter(Job.name.ilike(f'%engineer%')).all()


