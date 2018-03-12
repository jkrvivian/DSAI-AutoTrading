import csv
from collections import OrderedDict
from sklearn.svm import SVC 
import matplotlib.pyplot as plt 
import numpy as np

class Trader():
    def __init__(self, kernel):
        self.clf = SVC(kernel=kernel)
        self.unit = 0
        self.money = 0
        self.pre_act = 0

    def train(self, training_data):
        y = []
        for i in range(0, len(training_data)-1):
            open_p = training_data[i][0]
            close_p = training_data[i + 1][0]
            if (close_p - open_p) > 0: 
                y.append(-1)
            elif close_p - open_p < 0:
                y.append(1)
            else:
                y.append(0)
        self.clf.fit(training_data[0:-1], y)
        return
    
    def predict_action(self, test_datum):
        act = self.clf.predict([test_datum])[0]

        # Check if the unit is valid after action
        if (self.unit + act) > 1:
            act = 0
        elif (self.unit + act) < -1:
            act = 0

        # Update money
        if self.pre_act == 1:
            self.money -= test_datum[0]
        elif self.pre_act == -1:
            self.money += test_datum[0]

        self.unit = self.unit + act
        self.pre_act = act

        return str(act)

    def get_profit(self, testing_last_data):
        if self.pre_act == 1:
            self.money -= testing_last_data[0]
        elif self.pre_act == -1:
            self.money += testing_last_data[0]

        if self.pre_act + self.unit == 1:
            self.money += testing_last_data[1]
        elif self.unit + self.pre_act == -1:
            self.money -= testing_last_data[1]

        return self.money

def load_data(filename):
    ret_list = []
    with open(filename, 'rt') as csvfile:
        cin = csv.reader(csvfile)
        for row in cin:
            a = [float(row[0]), float(row[1]), float(row[2]), float(row[3])]
            ret_list.append(list(a))
    return ret_list

# You can write code above the if-main block.

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.

    # Load data
    training_data = load_data(args.training)
    testing_data = load_data(args.testing)
    testing_last_data = testing_data.pop()
    
    # Start to predict
    with open(args.output, 'w') as output_file:
        for row in testing_data:
            action = trader_rbf.predict_action(row)
            action = trader_lin.predict_action(row)
            output_file.write(action)
            output_file.write("\n")


    print('rbf: ', trader_rbf.get_profit(testing_last_data))
    print('linear: ', trader_lin.get_profit(testing_last_data))
