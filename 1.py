numbers= []
defaults=[1000, 9.8, 0.54, 9800, 4488 ]
text=['KiloNw', 'Kilopondio', 'Tonelada', 'Libras en kp', 'Libras en N' ]
print('Ingresa los Newtons');
initial_value= int(input())
i=0
for i in range(5):
    numbers.append(initial_value*defaults[i])
    print(numbers[i], text[i])