import matplotlib.pyplot as plt

def get_sample_data():
  """Returns predefined sample data for creating a bar chart.

  This function provides a fixed set of labels (categories) and corresponding
  values suitable for demonstrating the bar chart functionality.

  Returns:
      tuple[list[str], list[int]]: A tuple containing two lists:
          - The first list contains string labels for the chart's bars.
          - The second list contains integer values for the height of each bar.
  """
  labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple']
  values = [12, 19, 3, 5, 2]
  return labels, values

def create_bar_chart(labels, values, title="Sample Chart", xlabel="X-axis", ylabel="Y-axis", bar_color="skyblue"):
  """Creates and configures a bar chart using matplotlib.

  Generates a bar chart based on the provided labels and values. Allows
  customization of the title, axis labels, and bar color through parameters.

  Args:
      labels (list[str]): A list of strings representing the category labels for the x-axis.
      values (list[int | float]): A list of numerical values representing the height of
          each bar corresponding to the labels. Must be the same length as `labels`.
      title (str, optional): The title to display above the chart.
          Defaults to "Sample Chart".
      xlabel (str, optional): The label for the x-axis. Defaults to "X-axis".
      ylabel (str, optional): The label for the y-axis. Defaults to "Y-axis".
      bar_color (str, optional): The color of the bars in the chart. Accepts
          matplotlib color formats. Defaults to "skyblue".

  Raises:
      ValueError: If the length of the `labels` list and the `values` list
          are not equal.
  """
  # Error handling: Check if labels and values have the same length
  if len(labels) != len(values):
    raise ValueError("Labels and values must have the same length.")

  plt.figure(figsize=(8, 5))
  plt.bar(labels, values, color=bar_color, edgecolor='black')

  # Add labels and title
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)

def display_chart():
  """Finalizes the layout and displays the current matplotlib chart.

  Adjusts the plot layout to prevent labels from overlapping and then
  renders the chart in a window or saves it, depending on the matplotlib backend.
  Should be called after creating a chart using functions like `create_bar_chart`.
  """
  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
  chart_labels, chart_values = get_sample_data()
  # Example usage with custom parameters
  create_bar_chart(
      chart_labels,
      chart_values,
      title='Vote Count by Color',
      xlabel='Colors',
      ylabel='Votes',
      bar_color='lightcoral'
  )
  display_chart()
