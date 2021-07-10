#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    perc_errors=10
    cleaned_data = []
    errors = []
    
    ### your code goes here

    for pred, age, net_worth in zip(predictions,ages, net_worths):
        error = (pred-net_worth)*(pred-net_worth)
        cleaned_data.append((age, net_worth, error))
        errors.append(error)

    errors.sort(reverse=True)
    errors_removed=errors[0:int(len(errors)/perc_errors)]

    cleaned_data=[data for data in cleaned_data if data[2] < min(errors_removed)]
    print("Remaining data points after cleaning are {}".format(len(cleaned_data)))
    return cleaned_data

