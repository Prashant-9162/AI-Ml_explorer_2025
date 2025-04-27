import joblib
print("Welcome to AI..")
hrs = input(" Enter ur hrs : ")
model = joblib.load("mrksmodel")
model.predict ([[ hrs ]])
print ( model.predict([[ int( hrs ) ]]) )