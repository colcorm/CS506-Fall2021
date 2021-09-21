
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



    
            
            
    
