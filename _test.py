from model import Prediction as prediction

def test_model_input():
    model_input = ["GP","F",18, "GT3","A",4,4,"mother",2,2,"yes",4,3,4,5]
    return model_input

def test_load_model():
    model = prediction()
    return

def test_preprocessing():
    model_inputs = ["GP","F",18, "GT3","A",4,4,"mother",2,2,"yes",4,3,4,5]
    model = prediction()
    return model.preprocess(model_inputs)

def test_prediction():
    model_inputs = ["GP","F",18, "GT3","A",4,4,"mother",2,2,"yes",4,3,4,5]
    model = prediction()
    performance = model.predict(model_inputs)
    print(performance)
    return performance
   