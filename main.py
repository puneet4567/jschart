import matplotlib.pyplot as plt

# Sample data
labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple']
values = [12, 19, 3, 5, 2]

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Colors')
plt.ylabel('Votes')
plt.title('Vote Count by Color')

# Show chart
plt.tight_layout()
plt.show()
