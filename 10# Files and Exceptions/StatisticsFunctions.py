import statistics

with open('E:\SSUET Course AI\Python-Practice\\10# Files and Exceptions\\Statistics Functions File\\numbers.txt') as f:
    lines = f.readlines()
    list = []
    for line in lines:
        list.append(int(line))
    print("The List is:\n"+str(list))
    mean = statistics.mean(list)
    print("The 'Mean' of these numbers are: "+str(mean))
    median = statistics.median(list)
    print("The 'Median' of these numbers are: "+str(median))
    mode = statistics.mode(list)
    print("The 'Mode' of these numbers are: "+str(mode))
    variance = statistics.pvariance(list)
    print("The 'Variance' of these numbers are: "+str(variance))
    standardDeviation = statistics.pstdev(list)
    print("The 'Standard Deviation' of these numbers are: " + str(standardDeviation))

