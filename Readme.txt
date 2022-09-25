This project is aimed at taking an existing ml model and deploying it
locally first then on AWS. 

We aim to use fastapi

Firstly, start by ensuring your model is saved in either the pickle of hdf5 format.
In our case, we utilized the pickle format. 

import joblib
joblib_file = "best_model_15_inputs.pkl"   
joblib.dump(model, joblib_file)

We next need to create a file that does preprocessing on the input data (based on your system).
The model.py file contains the functions that are utilized with our model. A preprocessing function 
was written in this module.

Next, we need to pass the user data input the model. For this, we would create a class that defines 
the structure of the input. In our case, we utilized the student_data class in the main.py

Once these things are completed, run the following command:

uvicorn main:app --reload

Test the api by passing data into the /predict method.