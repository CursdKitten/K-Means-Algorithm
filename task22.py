import numpy as np
import csv
import matplotlib.pyplot as plt
import random
from sklearn.metrics import pairwise_distances_argmin
from collections import Counter, defaultdict

def readCSV(file):
    
    with open(file, 'r') as csvfile:

        x = []                # initialising a list to hold birthrate values (x axis values)
        y = []                # initialising a list to hold life ecountpectancy values (y axis values)
        countries = []        # initialising a list to hold country values 
        lines = 0             # initialising a row counter

        for line in csvfile:
            if lines >= 1: # excluding the line at position 0 which contains the count and y labels
                no_space = line.strip()   # getting rid of spaces
                split_line = no_space.split(",") # splitting up the data by comma so that each word is a position in the line
                countries.append(split_line[0])
                x.append(float(split_line[1])) # adding the data in the second position to count 
                y.append(float(split_line[2])) # adding the data in the third position to y
                lines += 1
            else:
                lines +=1
    
    return x, y, countries
    

def euclidean_distance_calc(point1, point2):

    ed = pairwise_distances_argmin(point1, point2) # using the pairwise_distances function from sklearn to get the euclidean distance
    
    return ed
   
   
def init_clusters(str_list, num_clusters, num_iterations, random = 2):
    
    randomize = np.random.RandomState(random)                   # randomizing our clusters

    i = randomize.permutation(str_list.shape[0])[:num_clusters] # permutation function to get our random i position
    centroids = str_list[i] # assigning the center to the ith position in list of coordinates as determined above

    for j in range (0, num_iterations):         # this loop will continue for the number of iterations the user specifies
        points = euclidean_distance_calc(str_list, centroids) # assigning each point based on the centroid the smallest distance (closest)
        new_centroids = np.array([str_list[points == i].mean(0) for i in range(num_clusters)]) 
        centroids = new_centroids
        
    return centroids, points
    

def k_means_alg(x, y):

    coordinates = np.vstack((x, y)).T   # merging our x and y lists into one list of tuples or coordinates
    centroid, points = init_clusters(coordinates, cluster_amount, iteration_number) # initilalising our clusters

    print("\nNumber of countries per cluster:")
    print(Counter(points))

    clusters_indices = defaultdict(list) # initialising a dictionary to hold cluster indices

    for index, i in enumerate(points): # creating an index for each country in each cluster
        clusters_indices[i].append(index)

    count = 0                       # initialising a counter
    means_birthrate = []
    means_life = []

    while count < cluster_amount:   # while in range of the no. of clusters provided by the user

        print("\nCluster no. " + str(count + 1) + ":\n") # displaying cluster number 1, 2, 3 etc. for however many clusters there are
        for i in clusters_indices[count]: # for each index in each cluster
            print(countries[i])           # display the countries in said cluster
    
        print("\nAverage birth rate:")
        mean_birthrate = centroid[count][0]
        means_birthrate.append(mean_birthrate)
        print(mean_birthrate) # displaying the average birth rate of each cluster
        
        print("\nAverage life expectancy:")
        mean_life_expectancy = centroid[count][1]
        means_life.append(mean_life_expectancy)
        print(mean_life_expectancy) # displaying the average life expectancy of each cluster

        count += 1

    plt.scatter(coordinates[:,0], coordinates[:,1], c = points, cmap = 'plasma' ) # plotting our scatter plot
    plt.scatter(means_birthrate, means_life, c = "r") # adding our centroids
    plt.gcf().set_size_inches((7, 7)) # resizing plot to fit title
    plt.title('K-Means Plot displaying Relationship between Birth Rate and Life Expectancy')
    plt.xlabel("Birth Rate")
    plt.ylabel("Life Expectancy")
    plt.show()                 
    

x, y, countries = readCSV(input('''Plese enter the file name you want to use: 
                    data1953.csv
                    data2008.csv
                    dataBoth.csv \n''' ))

cluster_amount = int(input("Input cluster amount: "))
iteration_number = int(input("Please enter the number of iterations: "))        

k_means_alg(x,y)


                                                              



