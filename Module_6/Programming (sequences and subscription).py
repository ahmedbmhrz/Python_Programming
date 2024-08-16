colors = ('white', 'red', 'blue', 'yellow')
mixed_colors = ['white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow']
first_color = input('Enter one of: ' + str(colors))
second_color = input('Enter one of: ' + str(colors))
first_index = colors.index(first_color)
second_index = colors.index(second_color)
if first_index == 0:
  mix_index = second_index*second_index
elif second_index == 0:
  mix_index = first_index*first_index
else:
  mix_index = first_index*second_index
mix_color = mixed_colors[mix_index]
print(first_color, '+', second_color, '=', mix_color)
