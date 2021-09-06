# Exercise 6 - Level 1

# Python has the module called statistics and we can use this module to do all the statistical calculations.
# However, to learn how to make function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# len(ages)

class stats:

    def __init__(self, x):
        self.data = x
        
    def stat_count(self):
        return len(self.data)

    def stat_sum(self):
        data_sum = 0
        for e in self.data:
            data_sum += e
        return data_sum

    def stat_mean(self):
        return self.stat_sum() / self.stat_count()

    def stat_min(self):
        return min(self.data)

    def last(self):
        return (self.data[-1])


obj = stats([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])

print(obj.stat_count())

print(obj.stat_sum())

print(obj.stat_mean())

print(obj.stat_min())

print(obj.last())



