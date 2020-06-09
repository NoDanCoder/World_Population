#!/usr/bin/env python
import read_write.rw_model as rw
import matplotlib.pyplot as plt
from datetime import datetime

dataset_path = "dataset.json"
dataset = rw.read_json(dataset_path)


def linear_regresion(list_x, list_y, label):

    size_data = len(list_x)
    mean_x = sum(list_x) / size_data
    mean_y = sum(list_y) / size_data

    slope = sum( (x - mean_x) * (y - mean_y) for x, y in zip(list_x, list_y) ) / sum( (x - mean_x) ** 2 for x in list_x )

    y_intercept = (sum(list_y) - slope * sum(list_x)) / size_data

    linear_eqn(list_x, list_y, slope, y_intercept, label)


def linear_eqn(list_x, list_y, slope, y_intercept, label):

    ordinate = lambda abscissa : (abscissa * slope) + y_intercept

    range_abscissa = [list_x[0], list_x[-1]]
    min_ordinate = ordinate(range_abscissa[0])
    max_ordinate = ordinate(range_abscissa[1])
    range_ordinate = [min_ordinate, max_ordinate]

    plt.plot(range_abscissa, range_ordinate, 'b-', list_x, list_y, 'ro')
    plt.suptitle(label[0])
    plt.xlabel(label[1])
    plt.ylabel(label[2])
    plt.show()


def date_to_minutes(datetime_str, start_date=datetime(2020, 6, 3)):
    
    format_date = '%m/%d/%Y, %H:%M:%S'
    date_time = datetime.strptime(datetime_str, format_date)
    relative_date = date_time - start_date
    to_minutes = relative_date.total_seconds() / 60
    
    return to_minutes
