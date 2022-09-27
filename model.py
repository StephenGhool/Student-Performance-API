# This script is used to do the following:
#   1. preprocess the daata
#   2. load the model
#   3. make predictions
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Prediction():
    """_summary_
    This class contains methods that would be used to make predictions about the \
    students performance
    """

    def __init__(self) -> None:
        self.model = self.load_model()
        return


    def load_model(self):
        """_summary_
        This function is used to load the prediction model
        """ 
        loaded_model = joblib.load('best_model_15_inputs.pkl')
        return loaded_model


    def preprocess(self, model_input):
        """_summary_
        This function modifies the user input to be compatiable with the 
        model
        Args:
            model_input (list): _description_

        Returns:
            list: encodes str values values
        """
     
        # create dataframe from list
        
        modified_model_input = pd.DataFrame([model_input],columns=['school','sex','age','famsize','Pstatus','Medu','Fedu','guardian','studytime','failures','internet','freetime','goout','health','absences'])

        #creating list of features than needs to be encoded
        encoded_features = ['school','sex','famsize','Pstatus','internet','guardian']
        
        # encode the list of features with numeric values
        modified_model_input[encoded_features] = modified_model_input[encoded_features].apply(LabelEncoder().fit_transform)

        # test = [1,"3"]
        # modified_model_input = pd.DataFrame([test],columns=['a','b'])
        return modified_model_input

    def predict(self, model_input:list):
        """_summary_

        Args:
            model_input (list): contains the student details

        Returns:
            performance (int): the predicted performance 
        """
        processed_model_input = self.preprocess(model_input) 
        performance = self.model.predict(processed_model_input)
        return performance
