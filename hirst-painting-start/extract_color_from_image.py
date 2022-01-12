import colorgram

# set the size as big as possible 2**32
color_list = colorgram.extract('image.jpg', 2**32)

color_palette = []
#
# for count in range(len(color_list)):
#     rgb = color_list[count]
#     color = rgb.rgb
#     color_palette.append(color)

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)

print(color_palette)