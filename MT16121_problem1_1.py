# MT16121
# Ankit Sharma
# Python V2.7

length_str = raw_input('Enter the length array as a space separated string: ')
cost_str = raw_input('Enter the cost array as a space separated string: ')
length_str_arr = length_str.split()
cost_str_arr = cost_str.split()
cost_arr = []
for s in cost_str_arr:
    cost_arr.append(int(s))

total_length = 0
for l in length_str_arr:
    if int(l) > total_length:
        total_length = int(l)


# Class created with value and direction as the attributes
class MatrixElement:

    def __init__(self, value, direction):
        self.value = value
        self.direction = direction


# Method for returning the max along with the argument number that is maximum
def get_max(a, b):
    if a > b:
        return a, 0
    else:
        return b, 1


# Method to compute the prices given the list of cuts
def get_price(my_list):
    price = 0
    for e in my_list:
        index = length_str_arr.index(str(e))
        price += cost_arr[index]
    return price

# Initialization of the matrix
matrix_list_1 = [0]
matrix_list_2 = []
for l in length_str_arr:
    matrix_list_1.append(int(l))
    matrix_list_2.append(int(l))

my_matrix = []
for i in range(0, len(length_str_arr)):
    zero_obj = MatrixElement(0, -1)
    inner_list = [zero_obj]
    my_matrix.append(inner_list)
for i in range(1, len(length_str_arr) + 1):
    obj = MatrixElement(matrix_list_1[i]*cost_arr[0], -1)
    my_matrix[0].append(obj)
i = 1
j = 1

# Code to populate the matrix
while i < len(length_str_arr) and j <= len(length_str_arr):
    if matrix_list_1[j] < matrix_list_2[i]:
        obj = MatrixElement(my_matrix[i-1][j].value, 0)
        my_matrix[i].append(obj)
    else:
        val, idx = get_max(my_matrix[i - 1][j].value, my_matrix[i][j - matrix_list_2[i]].value + cost_arr[i])
        obj = MatrixElement(val, idx)
        my_matrix[i].append(obj)
    if j == len(length_str_arr):
        j = 1
        i += 1
    else:
        j += 1

# Code to find the cuts using back tracking
cut_list = []
i = len(length_str_arr) - 1
j = len(length_str_arr)
elt = my_matrix[i][j]
while elt.value != 0:
    if elt.direction == 0:
        i -= 1
        elt = my_matrix[i][j]
    else:
        cut_list.append(matrix_list_2[i])
        j -= matrix_list_2[i]
        elt = my_matrix[i][j]

if j != 0:
    cut_list.append(matrix_list_2[i])

print 'The final selling price is ' + str(get_price(cut_list))
print 'The cuts are as follows: '
for cut in cut_list:
    print cut


