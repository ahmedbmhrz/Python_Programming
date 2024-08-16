colors = ('red', 'purple', 'blue', 'green', 'yellow', 'orange')
old_color = input('Enter a color to replace >')
new_color = input('Enter a new color >')
if old_color in colors:
  new_index = colors.index(old_color)
  colors[new_index] = new_color
else:
  colors.append(new_color)
print(colors)
