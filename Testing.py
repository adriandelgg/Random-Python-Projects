#Left Brain or Right Brain Dominant Quiz!

lesly_points = {'A': 0, 'B': 0}
adrian_points = {'A': 0, 'B': 0}
karen_points = {'A': 0, 'B': 0}

for i in range(9):
    lesly_answer = input('Lesly: A or B? ').upper()
    adrian_answer = input('Adrian: A or B? ' ).upper()
    karen_answer = input('Karen: A or B? ' ).upper()

    if lesly_answer == 'A':
        lesly_points['A'] += 1 
    elif lesly_answer == 'B':
        lesly_points['B'] += 1
    if adrian_answer == 'A':
        adrian_points['A'] += 1
    elif adrian_answer == 'B':
        adrian_points['B'] += 1
    if karen_answer == 'A':
        karen_points['A'] += 1
    elif karen_answer == 'B':
        karen_points['B'] += 1

print('\n \n')

if lesly_points['A'] < lesly_points['B']:
    print('Lesly, you are right brain dominant! Final Score:',lesly_points)
elif lesly_points['A'] == lesly_points['B']:
    print('Lesly, you are the best of both worlds! Final Score:',lesly_points)
else:
    print('Lesly, you are left brain dominant! Final Score:',lesly_points)

if adrian_points['A'] < adrian_points['B']:
    print('Adrian, you are right brain dominant! Final Score:',adrian_points)
elif adrian_points['A'] == adrian_points['B']:
    print('Adrian, you are the best of both worlds! Final Score:',adrian_points)
else:
    print('Adrian, you are left brain dominant! Final Score:',adrian_points)

if karen_points['A'] < karen_points['B']:
    print('Karen, you are right brain dominant! Final Score:',karen_points)
elif karen_points['A'] == karen_points['B']:
    print('Karen, you are the best of both worlds! Final Score:',karen_points)
else:
    print('Karen, you are left brain dominant! Final Score:',karen_points)