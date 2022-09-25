import string
from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import MinMaxScaler
from model import Prediction
import json

app = FastAPI()

# class used for accepting input data into API
class student_data(BaseModel):
    """
    Definition of inputs to pass into API for prediction
    
    Inputs:
        list of student details in the following order:
        school: GP or MS,
        sex: Male or Female,
        age: age of student,
        famsize: number of persons living with student choose GT3 or LE3, 
        Pstatus: A - apart or T - together, 
        Medu: Mother's Education on a scale of 1 - 4, 
        Fedu: Father's Education on a scale of 1 - 4, 
        guardian: Mother, father, other,
        studytime: number of hours study per week,
        failures: number of failures,
        internet: yes or no, 
        freetime: number of hours in free time, 
        goout: number of hours spent going out, 
        health: value from 1 to 5, 
        absences:number of times abscent from school 
    """
    student_details: list



# test server health
@app.get("/health")
def apitest():
    """_summary_
    Health Check 
    Returns:
        (str) : status of server's health
    """
    return {"Healthy: API working"}



# make predictions
@app.post("/prediction")
async def predict(student: student_data):
    """_summary_
    Used to pass data to generate predictions
    Args:
        student (student_data): list of student records

    Returns:
        _type_: student performance prediction
    """
    prediction_model = Prediction()
    performance = prediction_model.predict(student.student_details)
    result = json.dumps(performance.tolist())
    return result


@app.get("/")
async def root():
    return {"Welcome to my first api. This API predicts a students performance based on certain\
    criteria"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# school;sex;age;address;famsize;Pstatus;Medu;Fedu;Mjob;Fjob;reason;guardian;traveltime;studytime;failures;schoolsup;famsup;paid;activities;nursery;higher;internet;romantic;famrel;freetime;goout;Dalc;Walc;health;absences;G1;G2;G3

# "GP","F",18, "GT3","A",4,4,"mother",2,2,"yes",4,3,4,5

# school  sex  age  famsize  Pstatus  Medu  Fedu  guardian  studytime  failures  schoolsup  famsup  paid  activities  higher  internet  famrel  freetime  goout  Dalc  health  absences  G1  G2  G3
#   0      0   18     1        0     4     4         1          2         0          0       1     0           0       1         1       4         2      4     1       4        14  12  10  11  