# CHAPTER 2. Data Structures Used in Algorithms
# 1 Exploring data structures in Python

# 1.1 Lists
list_a = ["John", 33, "Toronto", True]

list_a # list_a is a list of four elements
type(list_a) # list_a is a list

bin_color = ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Orange']
bin_color[0]  # Red
bin_color[1]  # Green
bin_color[2]  # Blue
bin_color[3]  # Yellow
bin_color[4]  # Black
bin_color[5]  # White
bin_color[6]  # Orange

# 1.1.2 Slicing

bin_color[0:2]  # ['Red', 'Green']
bin_color[1] # Green

bin_color[2:] # ['Blue', 'Yellow', 'Black', 'White', 'Orange']
bin_color[:2] # ['Red', 'Green']


# `1.1.3 Negative Indices` is a subheading that suggests the topic being discussed is negative indices
# in Python lists.
# 1.1.3 Negative Indices

print(bin_color[-1]) # Orange
print(bin_color[-2]) # White
print(bin_color[-2: -1]) # ['White']

