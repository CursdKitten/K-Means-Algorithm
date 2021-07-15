# K-Means-Algorithm
## Description

A Python program that implements the k-means algorithm in order to read from one of three CSV files that contain a list of countries, their average life expectancy and their 
 average birth rate and plots this information on a scatter plot in a user determined number of clusters. This program also runs for a user-specified number of iterations
and plots the centroid (mean) of each cluster.

### Dependencies

The libraries imported are:  
* numpy
* csv
* matplotlib.pyplot
* random
* pairwise_distances_argmin from sklearn.metrics 
* Counter, defaultdict from collections

The program works with one of the 3 following CSV files:
 * data1953.csv
 * data2008.csv
 * dataBoth.csv

### Executing program

The user will be prompted to enter the following information:
* The name of the csv file they wish to plot
* The number of clusters they want the information divided into
* The number of iterations they want the program to run for
  
The program then prints out the number of countries in each cluster, the name of the countries in each cluster, the mean life expectancy of each cluster and the mean birth rate
of each cluster. It also displays a scatter plot with the user-specified number of clusters and their centroids plotted.
 
## Authors

* Kirsten Forrester

## Contributors names and contact info

Tel: 071 872 0132

Email: forrestermkirsten@gmail.com
