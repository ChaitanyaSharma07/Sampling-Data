import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

data = df["reading_time"].tolist()

#finding mean
population_mean = statistics.mean(data)
print("Population mean is " + str(population_mean))

#plotting graph of population data
fig = ff.create_distplot([data], ["reading time"], show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

#Population mean is 6.134910878918254
#mean of sampling distribution is 6.1155