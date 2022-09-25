import string
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

# class used for accepting input data into API
class student_data(BaseModel):
    student_details: list

# used to test the api
@app.get("/testapi")
def apitest():
    return {"Healthy: API working"}

@app.post("/prediction")
async def predict(student: student_data):
    # we need to normalize the data
    scaler = MinMaxScaler()
    # X_train = scaler.fit_transform(X_train)
    return student.student_details

@app.get("/")
async def root():
    return {"Welcome to my first api. This API predicts a students performance based on certain\
    criteria"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
