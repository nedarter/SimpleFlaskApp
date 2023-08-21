# Import the dependencies

from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import os
import pandas as pd

dbpath = "grades.sqlite"

# Create a base class for declarating class definitions to produce Table objects
Base = declarative_base()

class Grade(Base): 
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True)
    Sex = Column(String)
    Period = Column(Integer)
    Score = Column(Integer)


def LoadScoresPerPeriod(period):
    #Load your SQLITE database
    engine = create_engine(f'sqlite:///{dbpath}')
    session = Session(engine)

    

    #Pull the data into pandas. We are filtering by the period    

    try:
    #SQL Alchemy 1.X version 
        query = session.query(Grade).filter(Grade.Period == period).statement
        data = pd.read_sql(query, session.bind)    
    except:
        #SQL Alchemy 2.0 version 
        query  = text(str(session.query(Grade).filter(Grade.Period == period).statement))
        data = pd.read_sql(query, engine.connect(), params={"Period_1":period})

    return data


if __name__ == "__main__":
    import pandas as pd
    import random
    from sqlalchemy.orm import Session
    random.seed(42)


    if os.path.exists(dbpath):
        os.remove(dbpath)

    engine = create_engine(f'sqlite:///{dbpath}')
    Base.metadata.create_all(engine)

    session = Session(engine)
    for i in range(75):
        period = random.randrange(1,4)


        if random.randrange(1,3) == 1: 
            sex = "Male"
        else: 
            sex = "Female"
 

        score = random.randrange(60, 101)

        session.add(Grade(Sex=sex, Period=period, Score=score))

    session.commit()


    results = session.query(Grade).all()

    #data = pd.read_sql(session.query(Grade).statement, session.bind)
    data = LoadScoresPerPeriod(1)

    print(data.head())
    



        


        

   


