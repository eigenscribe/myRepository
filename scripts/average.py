# function to compute average of a list
def average(input_list):
    # sum calculation
    sum_list = 0
    for i in input_list:
        sum_list = sum_list + i 

    # average calculation
    avg = sum_list /len(input_list)
    return avg


sample_list = [2,4,5,1]
avg_list = average(sample_list)
print(avg_list)
