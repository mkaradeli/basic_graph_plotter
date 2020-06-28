import matplotlib.pyplot as plt

title='Voltage versus Current'
x_label = 'Voltage (V)'
y_label = 'Current (I)'
array_x = ([
1.12, 2.23, 3.35, 4.46, 5.58, 6.70, 7.81, 8.93, 10.04, 11.16])
array_y = ([
0.04, 0.09, 0.13, 0.18, 0.22, 0.27, 0.31, 0.36, 0.40, 0.45])

plt.plot(array_x,array_y, '--bo')
plt.grid(True)
plt.title(title)
plt.xlabel(x_label); plt.ylabel(y_label)



plt.show()

