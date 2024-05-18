
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create engine and connect to the PostgreSQL database
engine = create_engine('postgresql://postgres:2024@localhost/', echo=True)  # Replace username and password with your PostgreSQL credentials

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the AccidentReport model
class AccidentReport(Base):
    __tablename__ = 'accident_report'

    id = Column(Integer, primary_key=True)
    location = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    severity = Column(String(20), nullable=False)
    description = Column(Text, nullable=True)
    weather_condition = Column(String(50), nullable=True)
    road_condition = Column(String(50), nullable=True)
    cause = Column(Text, nullable=True)
    num_vehicles_involved = Column(Integer, nullable=False, default=1)
    casualties = relationship("Casualty", backref="accident_report")

# Define the Casualty model
class Casualty(Base):
    __tablename__ = 'casualty'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(10), nullable=True)
    accident_id = Column(Integer, ForeignKey('accident_report.id'))

# Create all tables in the database
Base.metadata.create_all(engine)

# Establish a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a new AccidentReport to the database
new_accident = AccidentReport(location='Sample Location',
                              date=datetime.now().date(),
                              time=datetime.now().time(),
                              severity='High',
                              description='Sample accident description',
                              weather_condition='Sunny',
                              road_condition='Dry',
                              cause='Driver error',
                              num_vehicles_involved=2)
session.add(new_accident)
session.commit()

# Example: Add a new Casualty related to the AccidentReport

new_casualty = Casualty(name='John Doe', age=30, gender='Male', accident_id=new_accident.id)
session.add(new_casualty)
session.commit()

# Close the session
session.close()