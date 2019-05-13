import csv
import math
import pandas as pd
import numpy as np

global test_data, train_data


def load_test_data():
    global test_data
    test_data = []
    with open('mnist_test.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            test_data.append(row)


def load_train_data():
    global train_data
    train_data = []
    with open('mnist_train.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            train_data.append(row)




def get_distance_matrix_of_test_to_train(test_record,k):
    pass
    distance_vector = []
    train_data.pop(0)
    for train_instance in train_data:
        distance_vector.append((get_euclidean_distance(train_instance, test_record), train_instance[0]))  # sort alert
    distance_vector.sort()
    return distance_vector[0:k]

def get_euclidean_distance(first_record, second_record):
    partial_distance = []
    final_distance = 0
    for col_index in range(len(first_record)):
        if col_index != 0:
            partial_distance.append(int(first_record[col_index]) - int(second_record[col_index]))
    for distance in partial_distance:
        final_distance += distance * distance
    return math.sqrt(final_distance)


if __name__ == '__main__':
    global test_data, train_data
    load_train_data()
    load_test_data()
    candidates=get_distance_matrix_of_test_to_train(test_data[2],5)
    print(candidates)