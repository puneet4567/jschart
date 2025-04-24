import unittest
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt

# Assuming main.py is in the same directory or accessible in the Python path
from main import create_bar_chart, display_chart, get_sample_data

class TestMain(unittest.TestCase):

    def test_create_bar_chart_valid_input(self):
        """Test create_bar_chart runs without error for valid inputs."""
        labels, values = get_sample_data() # Use sample data for valid input
        # Mock plt.show to prevent actual plot display during test
        with patch('matplotlib.pyplot.show') as mock_show:
            try:
                create_bar_chart(labels, values)
                # Optionally add more checks here if needed, e.g., mock figure/axes calls
            except Exception as e:
                self.fail(f"create_bar_chart raised an exception unexpectedly: {e}")
            # Check that plt.show() wasn't called by create_bar_chart itself
            mock_show.assert_not_called()

    def test_create_bar_chart_mismatched_lengths(self):
        """Test create_bar_chart raises ValueError for mismatched input lengths."""
        labels = ['A', 'B', 'C']
        values = [1, 2] # Mismatched length
        with self.assertRaisesRegex(ValueError, "Labels and values must have the same length."):
            create_bar_chart(labels, values)

    @patch('matplotlib.pyplot.show')
    def test_display_chart_calls_show(self, mock_show):
        """Test display_chart calls plt.show()."""
        # We might need to ensure a figure exists for display_chart to run fully
        # although display_chart itself doesn't depend on it directly in current form.
        # Let's create a dummy figure context just in case future changes require it.
        plt.figure() # Create a figure context
        display_chart()
        mock_show.assert_called_once()
        plt.close() # Close the dummy figure

    # It might be useful to also mock plt.figure, plt.bar, etc. in the valid input test
    # to ensure they are called as expected, but for now, we focus on error handling and display.

if __name__ == '__main__':
    # Suppress matplotlib figure creation during tests if possible
    # This might require more setup depending on the environment
    unittest.main()
