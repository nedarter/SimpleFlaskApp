# Import the dependencies

from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import os

dbpath = "grades.sqlite"

# Create a base class for declarating class definitions to produce Table objects
Base = declarative_base()

class Grade(Base): 
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True)
    Sex = Column(String)
    Period = Column(Integer)
    Score = Column(Integer)


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
    for i in range(1000):
        period = random.randrange(1,3)


        if random.randrange(1,3) == 1: 
            sex = "Male"

            if period == 2: 
                multiplier = 1
            else: 
                multiplier = .7

        else: 
            sex = "Female"
            multiplier = .9

        score = random.randrange(60, 101) * multiplier

        session.add(Grade(Sex=sex, Period=period, Score=score))

    session.commit()


    results = session.query(Grade).all()

    data = pd.read_sql(session.query(Grade).statement, session.bind)

    print(data.head())
    



        


        

   


