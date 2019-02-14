 #!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    cleaned_data = []
    
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    score1 = []
    import math
    for i in range(len(predictions)):
        score1.extend(abs(predictions[i] - net_worths[i]))
    score1.sort()
    score1 = score1[:81]
    for i in range(len(predictions)):
        score = abs(predictions[i] - net_worths[i])
        if score in score1:
           cleaned_data.append([ages[i], net_worths[i], score])
    return cleaned_data

"""
    import math

    sortedError = []
    for index in range(len(predictions)):
        sortedError.extend(abs(predictions[index] - net_worths[index]))

    sortedError.sort()

    keeperCount = int(math.floor(len(sortedError) * 0.9))

    topErrors = sortedError[keeperCount:]

    for index in range(len(predictions)):
        error = abs(predictions[index] - net_worths[index])
        if error in topErrors:
            pass
        else:
            cleaned_data.append([ages[index], net_worths[index], error])
    
    return cleaned_data
    """