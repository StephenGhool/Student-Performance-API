from fastapi import FastAPI
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

# used to test the api
@app.get("/testapi")
def apitest():
    return {"Healthy: API working"}

@app.get("/prediction")
async def predict():
    # we need to normalize the data
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    return 

@app.get("/")
async def root():
    return {"Welcome to my first api. This API predicts a students performance based on certain\
    criteria"}
