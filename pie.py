import matplotlib.pyplot as plt
#de kleuren die worden gebruikt in de tabel
my_colors = ["red", "blue", "orange"]
#de data dat i omzet in procenten
my_data = [900, 505, 1900]
# de labels die aangeven wat bij wat hoort
my_labels = 'Tasks Pending', 'Tasks Ongoing', 'Tasks Completed'
# styling 
plt.pie(my_data, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow=True, colors=my_colors)
# de titel
plt.title('My Tasks')
plt.axis('equal')
plt.show()