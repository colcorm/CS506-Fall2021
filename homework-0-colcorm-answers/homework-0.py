
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
    return at_arry, cl_arry

# Purpose: Replaces "NaN" values in at_arry with the median of the attributes
def impute_missing(at_arry):
    # Takes as input an array
    # Returns an updated version of the input array
    medians = find_medians(at_arry)
    for line in at_arry:
        attr_cat = 0
        for attr in at_arry:
            attr_cat += 1
            if attr == float("nan"):
                attr = medians[attr_cat]
    return at_arry

# Purpose: Finds the median values of each category of attributes
def find_medians(at_arry):
    # Takes as input an array
    # Returns an array of the median values of each attribute
    medians, temp = [], []
    for line in at_arry:
        for attr in at_arry:
            if attr == float("nan"):
                attr = 0
    
    medians = [[row[i] for row in at_arry] for i in range(len(at_arry[0]))]

    for line in medians:
        count = 0
        sum = 0
        for val in line:
            count += 1
            sum += val
        line = sum/count 

    return medians

    
    
            
            
    
