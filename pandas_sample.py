import math
import pandas as pd
import time

def getLatitude(st):
    st2=st.replace("(","").replace(")","").split(",")
    return float(st2[0])

def getLongitude(st):
    st2=st.replace("(","").replace(")","").split(",")
    return float(st2[1])

def run():
    csv_input = pd.read_csv(filepath_or_buffer="./result_4.csv", encoding="utf8", sep=",")

    csv_input.assign(
        latitude=csv_input.apply(lambda x: getLatitude(x['location']), axis=1)
    ).assign(
        longitude=csv_input.apply(lambda x: getLongitude(x['location']), axis=1)
    ).to_csv("employee.csv")


start = time.time()
run()
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
