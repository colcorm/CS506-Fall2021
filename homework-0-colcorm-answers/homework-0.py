import random

# Purpose: read data from a file that contains information about patients.
#          seperate patient attributes from their class and returns both arrays 
def import_data(filename):
    # Takes as input a filename
    # Returns two arrays
    at_arry, cl_arry = [], [] # creates two empty arrays
    file = open(filename, 'r') # opens the file "filename" in read mode
    # loop through the file
    for line in file:
        lst = line.split(',') # split up entries with comma
        cl_arry.append(lst[-1]) # get the class value off the end
        # get attributes
        for x in lst[0:len(lst) - 1]:
            # if attribute is "?" store as "NaN"
            if x == "?":
                at_arry.append(float("nan"))
            else:
                at_arry.append(x)
    # return arrays
    file.close()
    return at_arry, cl_arry

# Purpose: Replaces "NaN" values in at_arry with the median of the attributes
def impute_missing(at_arry):
    # Takes as input an array
    # Returns an updated version of the input array
    medians = find_medians(at_arry)
    for line in at_arry:
        attr_cat = 0
        for attr in line:
            if attr != attr:
                line[attr_cat] = medians[attr_cat]
            attr_cat += 1
    return at_arry

# Purpose: Finds the median values of each category of attributes
def find_medians(at_arry):
    # Takes as input an array
    # Returns an array of the median values of each attribute
    medians = []
    medians = [[row[i] for row in at_arry] for i in range(len(at_arry[0]))]

    count = 0
    for line in medians:
        line = [attr for attr in line if attr == attr]
        line = sorted(line)
        len_line = len(line)
        index = (len_line - 1) // 2

        if (len_line % 2):
            medians[count] = line[index]
        else:
            medians[count] = (line[index] + line[index + 1])/2.0
        count += 1
    return medians

# Purpose: Discards samples tht do not have an entry for every attribute
def discard_missing(at_arry, cl_arry):
    # Takes as input two arrays
    # Returns both arrays with missing entries discarded from both
    delete = []
    x_count = 0
    del_count = 0
    for x in at_arry:
        for y in x:
            if y != y:
                at_arry[x_count] = -1
                cl_arry[x_count] = -1
                del_count += 1
        x_count += 1
    
    for x in range(0, del_count):
        at_arry.remove(-1)
        cl_arry.remove(-1)
        
    
    return at_arry

# Purpose: Shuffles the data points while keeping the corresponding at and cl
#          values at the same index
def shuffle_data(at_arry, cl_arry):
    # Takes as input two arrays
    # Returns both arrays shuffled 
    temp = list(zip(at_arry, cl_arry))
    random.shuffle(temp)
    at_arry_sh, cl_arry_sh = zip(*temp)
    return at_arry_sh, cl_arry_sh

# Purpose: Calculates the standard deviation of of each attribute in the sample set
def compute_sd(at_arry):
    # Takes as input an array
    # Returns an array in which each value is the stdev of the corresponding attribute.
    sd_list = []
    for line in at_arry:
        mean = sum(line) / len(line)
        variance = sum([((attr - mean) ** 2) for attr in line]) / len(line)
        sd = variance ** 0.5
        sd_list.append(sd)
    return sd_list

# Purpose: Removes entries that contain outlier attributes, outlier is definded as
#          being 2 stdev away from the mean value
def remove_outlier(at_arry, cl_arry):
    # Takes as input two arrays
    # Returns both arrays with the outlier entries excluded
    stdev = compute_sd(at_arry)
    delete = []
    line_count = 0
    del_count = 0
    for line in at_arry:
        mean = sum(line) / len(line)
        for attr in line:
            if attr > (mean + (2 * stdev[line_count])):
                at_arry[line_count] = -1
                cl_arry[line_count] = -1
                del_count += 1
        line_count += 1
    
    for x in range(0, del_count):
        at_arry.remove(-1)
        cl_arry.remove(-1)
    
    return at_arry

# Purpose: Read data from the train.csv file. Splits the data into two arrays.
# at_arry handles the attributes, sur_arry handles if they survived or not
def import_train(filename):
    # Takes as input a filename
    # Returns two arrays
    at_arry, sur_arry, lst = [], [], [] # creates two empty arrays
    file = open(filename, 'r') # opens the file "filename" in read mode
    # loop through the file
    lines = file.readlines()
    line_count = 0
    for line in lines:
        lst = line.split(',') # split up entries with comma
        for x in [11, 9, 4, 3]:
            del lst[x]
        if line_count > 0:
            sur_arry.append(lst[1])
            del lst[1]
            att_num = 0
            for x in lst:
                if att_num == 2:
                    if x == "female":
                        lst[2] = 0
                    else:
                        lst[2] = 1
                elif att_num == 7:
                    if x == "C":
                        lst[7] = 0
                    elif x == "Q":
                        lst[7] = 1
                    else:
                        lst[7] = 2
                else:
                    lst[att_num] = x
                att_num += 1
            at_arry.append(lst)
        line_count += 1      
    return at_arry, sur_arry

# Purpose: Splits a data set between a train and a test set based on a
# value t_f which represents the porportion of data to be used in the test set
def train_test_split(X, y, t_f):
    # Takes two lists and a value t_f that is a number 0 < t_f < 1
    # Returns four lists that represent the split data set
    X_train, y_train = [], []
    X_test = X
    y_test = y

    len_entry = len(X)
    len_t_entry = round(len_entry * t_f)
    
    # picks a random list of non-repeated integers representing indicies in a list
    t_picks = random.sample(range(len_entry - 1), len_t_entry)
    num_list = list(range(0,len_entry - 1))

    for num in t_picks:
        X_train.append(X[num])
        y_train.append(y[num])
    
    count = (len(num_list) - 1)
    for num in num_list[::-1]:
        if num in t_picks:
            del X_test[count]
            del y_test[count]
        count += -1
    
    return X_train, y_train, X_test, y_test

# Purpose: Splits a data set between a train, cv, and test set based on a
# value t_f, and cv_f which represents the porportion of data to be used in 
# the test set and cv test respectively
def train_test_CV_split(X, y, t_f, cv_f):
    # Takes two lists and two values t_f, c_f that are numbers 0 < t_f,c_f < 1
    # Returns six lists that represent the split data set

    X_train, y_train= [], []
    X_test = X
    y_test = y

    len_entry = len(X)
    len_t_entry = round(len_entry * t_f)
    len_cv_entry = round(len_entry * cv_f)
    
    # picks a random list of non-repeated integers representing indicies in a list
    t_picks = random.sample(range(len_entry - 1), len_t_entry)
    num_list = list(range(0,len_entry - 1))

    for num in t_picks:
        X_train.append(X[num])
        y_train.append(y[num])
    
    count = (len(num_list) - 1)
    for num in num_list[::-1]:
        if num in t_picks:
            del X_test[count]
            del y_test[count]
        count += -1
    

    # this nexts section repeats the above process but uses X_test to pull the cv values from
    X_cv = X_test
    y_cv = y_test

    len_test = len(X_test)

    # picks a random list of non-repeated integers representing indicies in a list
    cv_picks = random.sample(range(len_test - 1), len_cv_entry)
    cv_list = list(range(0, len_test - 1))

    for num in cv_picks:
        X_cv.append(X_test[num])
        y_cv.append(y_test[num])
    
    count = (len(cv_list) - 1)
    for num in cv_list[::-1]:
        if num in cv_picks:
            del X_test[count]
            del y_test[count]
        count += -1


    return X_train, y_train, X_test, y_test, X_cv, y_cv

    
            
            
    
