# MT16121
# Ankit Sharma
# Python V2.7

gap_penalty = -2
match_score = 2
mismatch_score = 1

# Class created with value and direction as the attributes
class MatrixElement:

    def __init__(self, value, direction):
        self.value = value
        self.direction = direction


# Method written to find the maximum of the 3 arguments
def get_max(a, b, c):
    if a > b:
        temp = a
        idx = 0
    else:
        temp = b
        idx = 1
    if temp > c:
        return temp, idx
    else:
        return c, 2

# Method to return the score for match/mismatch
def match_mismatch(char1, char2):
    if char1 == char2:
        return match_score
    else:
        return mismatch_score

# Method to get the alignment score
def get_score(list1, list2):
    score = 0
    for i in range(0, len(list1)):
        if list1[i] == '-' or list2[i] == '-':
            score += gap_penalty
        elif list1[i] == list2[i]:
            score += match_score
        else:
            score += mismatch_score
    return score


string1 = raw_input("Enter the first string: ")
string2 = raw_input("Enter the second string: ")
list1 = ['-']
list2 = ['-']

for char_elt in string1:
    list1.append(char_elt)
for char_elt in string2:
    list2.append(char_elt)

# if len(list(string1)) >= len(list(string2)):
#     for char_elt in string1:
#         list1.append(char_elt)
#     for char_elt in string2:
#         list2.append(char_elt)
# else:
#     for char_elt in string2:
#         list1.append(char_elt)
#     for char_elt in string1:
#         list2.append(char_elt)

# Matrix initialization
my_matrix = []
for i in range(0, len(list2)):
    inner_list = []
    my_matrix.append(inner_list)
for i in range(0, gap_penalty*len(list1), gap_penalty):
    elt = MatrixElement(i, -1)
    my_matrix[0].append(elt)
gp = gap_penalty
for i in range(1, len(list2)):
    elt = MatrixElement(gp, -1)
    my_matrix[i].append(elt)
    gp += gap_penalty

# Code to populate the matrix
i = 1
j = 1
while i <= len(list2) - 1:
    above = my_matrix[i - 1][j].value
    diagonal = my_matrix[i - 1][j - 1].value
    left = my_matrix[i][j - 1].value
    maximum, idx = get_max(above + gap_penalty, diagonal + match_mismatch(list1[j], list2[i]), left + gap_penalty)
    element = MatrixElement(maximum, idx)
    my_matrix[i].append(element)
    if j == len(list1) - 1:
        j = 1
        i += 1
    else:
        j += 1

# for inner_list in my_matrix:
#     for e in inner_list:
#         print e.value
#     print '*****'


# Code to backtrack and get the alignment as well as the score
final_alignment_list_1 = []
final_alignment_list_2 = []
i = len(list2) - 1
j = len(list1) - 1
elt = my_matrix[i][j]
while i != 0 and j != 0:
    if elt.direction == 0:
        final_alignment_list_1.append('-')
        final_alignment_list_2.append(list2[i])
        i -= 1
        elt = my_matrix[i][j]
    elif elt.direction == 1:
        final_alignment_list_1.append(list1[j])
        final_alignment_list_2.append(list2[i])
        i -= 1
        j -= 1
        elt = my_matrix[i][j]
    elif elt.direction == 2:
        final_alignment_list_1.append(list1[j])
        final_alignment_list_2.append('-')
        j -= 1
        elt = my_matrix[i][j]

while j != 0:
    final_alignment_list_1.append(list1[j])
    final_alignment_list_2.append('-')
    j -= 1

while i != 0:
    final_alignment_list_2.append(list2[i])
    final_alignment_list_1.append('-')
    i -= 1
print 'The score of the alignment is: ' + str(get_score(final_alignment_list_1, final_alignment_list_2))
print 'The alignment is as follows: '
print list(reversed(final_alignment_list_1))
print list(reversed(final_alignment_list_2))

