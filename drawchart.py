
# importing package
import matplotlib.pyplot as plt
import numpy as np
import json
dictionary = json.load(open("result.json","r"))
 
def drawChart():
    x = []
    y1 = []
    y2 = []

    for key,value in dictionary.items():
        x.append(key)
        y1.append(value['num_true'])
        y2.append(value['num_false'])
    
    # plot bars in stack manner
    width = 20
    height = 7
    plt.subplots(figsize=(width, height))
    plt.xticks(rotation=45)
    plt.bar(x, y1, color='b')
    plt.bar(x, y2, bottom=y1, color='r')
    plt.xlabel("Hero")
    plt.ylabel("Numbers")
    plt.legend(["True", "False"])
    plt.title("Predict result")
    plt.show()

drawChart()