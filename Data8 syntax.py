# Common Python operators
1 + 2  # 3		Addition
1 - 2  # -1		Subtraction
1 * 2  # 2		Multiplication
1 / 2  # 0.5	Division
1 % 2  # 1		Modulo
1 ** 2 # 1		Exponentiate
# Division is not integer division
# follow PEMDAS precedence

# Assignments
a = 10
b = 2 * a
a + b # 30

# Import math for fun things
# https://docs.python.org/3/library/math.html
import math
math.log(2, 16) 				# 0.25
math.sqrt(operator.add(4, 5)) 	# 3.0

# Types
# int, float, string, boolean
# Common Python comparisons
2 < 3	# True		less than
3 > 2	# True		greater than
2 <= 2	# True		less than or equal
3 >= 3	# True		greater than or equal
3 == 3	# True		equal
3 != 2	# True		not equal

# Arrays (numpy), sequences, lists
import numpy as np
english_parts_of_speech = make_array("noun", "pronoun", "verb", "adverb", "adjective", "conjunction", "preposition", "interjection")
# https://www.inferentialthinking.com/chapters/05/1/Arrays
# entrywise operations: can just 'add' or 'multiply' normally
# diff, sum, sort most useful
# np.arange([start, end), skip)
np.arange(1.5, -2, -0.5)
# instantiate numpy array. Can convert table rows to arrays
np.array(row)

# Tables
from datascience import *
Table() 			# blank table
.with_columns("Column title", make_array("array", "of", "stuff"),
			  "Next column", make_array(420, 23547648, 343))
# read from existing csv
.read_table(path_data + 'table_title.csv')
.show(n) 		# shows first n rows, PURELY cosmetic
.num_columns
.num_rows
.labels 		# list of column labels
.column('Column title')	# retrieves column of this name
.column(3)				# or index, starting at 0
.column(0).item(4)		# retrieves entry in index 4 of column 0
# format can be DateFormatter, CurrencyFormatter, PercentFormatter
.set_format('New Name', PercentFormatter)

# makes new table with selected columns
# DIFFERENT FROM .column
.select('col1 name', 'col2 name', etc)
.select(start, end index)
# makes new table with some columns dropped
.drop('col1 name', 'col2 name', etc)
# sorts table
.sort('column name', descending=False, distinct=False)
# makes new table with specified range of row(s)
.take(n) # takes row of index n
.take(np.arange(4, 19))
# applies a function to each element of a column
.apply(func_name, "column name"[, "column2 name", etc])

# CONDITIONAL SELECTION: *WHERE*
.where('column name', are.equal_to(x))
						 .above(x)
						 .above_or_equal_to(x)
						 .below(x)
						 .below_or_equal_to(x)
						 .between(x, y)
						 .strictly_between(x, y)
						 .between_or_equal_to(x, y)
						 .containing(S)
# Can negate any of these, e.g.
						 .not_above(x)

# Visualizations
sample = Table().read_table(path_data + 'sample.csv')
# scatter plot, table can be modified before plotting
sample.scatter('x axis label', 'y axis label')
# line graph
sample.plot('x axis label', 'y axis label')
# bar chart (horizontal)
sample.barh('category axis label', 'quantity label')
# histogram (vertical)
sample.hist('column'[, bins=np.arange(start, end, size), unit='axes unit'])
# histogram: makes table with count in each bin
bins = sample.bin('column', bins=np.arange(start, end, size))
# histogram: construct from bin table
sample.hist('x axis label', bin_column='bins', unit='Million Dollars')

# vertical axis uses DENSITY SCALE: bar height = %entries relative to bin size
# https://www.inferentialthinking.com/chapters/07/2/Visualizing_Numerical_Distributions#the-histogram-general-principles-and-calculation
# area of bar = % entries in bin
# 			  = bar height * bin width
# bar height = bar area/bin width = % entries in bin/bin width

# can use unequal bins to construct histogram
uneven_bins = make_array(50, 100, 200, 420, 500, 1337)

# overlay multiple graphs of the same type (for scatter, plot, barh)
# edit table first! plots all other columns against 'col label'
sample.barh('col label')



# Functions
def func_name(arg1, arg2):
	"""Adds arg1 and arg2"""
	return arg1+arg2

# Aggregations
# groups/aggregates information in col1, col2 according to groupBy_function
# 	-default function is count
# 	-returns 2-column table: | 'col1 name' | groupedByFunction |
.group('col1 name'[, groupBy_function])
# creates new table where sample is augmented by table2 column data
.join('col1 for joining', table2, 'table2col for joining')
# group but for multiple columns
.pivot('col labels', 'row labels'[, values='count column', collect=groupBy_function])

# Random variables and probabilities
# returns random entry in an nparray
np.random.choice(nparray[, number_of_trials])
# (non-mutative) appends value to array, returns new array
np.append(array, value)
# returns # of nonzero (True) elements in an array
np.count_nonzero(array)
# returns item at index i in an array
array.item(i)
# returns corresponding percentile value of an array
percentile(percentile, array)

# Sampling methods
# simple random sample from a table, default is the entire table
.sample(sample_size[, with_replacement=True])
# returns array of proportions given buckets summing to 1
sample_proportions(sample_size, distribution_array)

# Miscellaneous
# returns array of all 1's (floats)
np.ones((size_tuple)[, dtype=float])
# returns array of all 0's (floats)
np.zeros((size_tuple)[, dtype=float])
# returns mean of array
np.mean(array)
# returns standard deviation of array
np.std(array)
# area under normal curve with mean=0 and std=1
from scipy import stats
stats.norm.cdf(z_score)

