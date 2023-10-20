import pickle
import json
import numpy as np

_address = None
_furnishing = None
_available_for = None 
_facing = None

__data_columns = None
__model = None


import numpy as np

def get_estimated_rent(address, bedroom, area, parking, furnishing, available_for, facing, propertyage_encoded):
    # Initialize the input array with zeros
    x = np.zeros(len(__data_columns))
    
    # Set the values for the known features
    x[0] = bedroom
    x[1] = area
    x[2] = parking
    
    # Set the value for 'propertyage_encoded'
    x[-1] = propertyage_encoded
    
    # Find the index corresponding to the 'address' category in the columns
    address_index = np.where(__data_columns == address)[0]
    
    # Find the index corresponding to the 'furnishing' category in the columns
    furnishing_index = np.where(__data_columns == furnishing)[0]
    
    # Find the index corresponding to the 'available_for' category in the columns
    available_for_index = np.where(__data_columns == available_for)[0]
    
    # Find the index corresponding to the 'facing' category in the columns
    facing_index = np.where(__data_columns == facing)[0]
    
    # If the categories exist in the columns, set their values to 1
    if len(address_index) > 0:
        x[address_index] = 1
    
    if len(furnishing_index) > 0:
        x[furnishing_index] = 1
    
    if len(available_for_index) > 0:
        x[available_for_index] = 1
    
    if len(facing_index) > 0:
        x[facing_index] = 1
    
    return round(__model.predict([x])[0],2)







def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global _address
    global _furnishing
    global _available_for
    global _facing 

    with open("./artifacts/columns1.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        _address = __data_columns[12:106]
        _furnishing = __data_columns[3:6]  
        _available_for = __data_columns[6:12]
        _facing = __data_columns[106:114]

    global __model
    if __model is None:
        with open('./artifacts/pune_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_all_names():
    return _address

def get_furnishing_names():
    return _furnishing

def get_available_for_names():
   return _available_for

def get_facing_names(): 
     return _facing 

def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_all_names())
    print(get_estimated_rent('Baner', 2, 1050.00, 0, 'Semifurnished', 'Bachelors (Men Only)','North', 2.00))