from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict()

# Add some key-value pairs
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Iterate through the OrderedDict
for key, value in ordered_dict.items():
    print(f"{key}: {value}")