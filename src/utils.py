import os
import sys
import dill
import pandas as pd
import numpy as np
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)
'''
dill is a Python library, similar to pickle, that serializes Python objects.
Serialization = saving a Python object to a file so you can load it later exactly as it was.


Why use dill or pickle here?

You have a fitted preprocessor (ColumnTransformer).
Fitting involves learning from training data (scaling numbers, encoding categories).
You want to reuse the same preprocessor on test data or new data without refitting.
Saving it with dill.dump ensures consistency and avoids refitting.
'''