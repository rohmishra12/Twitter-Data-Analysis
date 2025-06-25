# Twitter Data Analysis App

This project provides a graphical interface to interact with the Twitter API, download tweets, store them in a MySQL database, and analyze the data. The application allows users to:
- Fetch tweets using the Twitter API.
- Store the tweets in a MySQL database.
- Sort and manipulate the data.
- Visualize the data via a plot of tweet counts over time.

## Technologies Used

- **Python**: Programming language for the application.
- **Tkinter**: Python GUI library used to create the application interface.
- **Tweepy**: Python library for accessing the Twitter API.
- **MySQL**: Relational database used to store and manipulate tweet data.
- **Matplotlib**: Python library for creating visualizations of the data.
- **CSV**: Format used to store and transfer data between the application and MySQL database.

## Prerequisites

Before running the application, you need to have the following installed:

1. **Python 3.x**: You can check the version using `python --version`.
2. **MySQL Server**: Make sure MySQL is running and accessible locally.
3. **Required Python Libraries**:
   - `tweepy`
   - `mysql-connector-python`
   - `matplotlib`
   - `tkinter` (usually comes pre-installed with Python)

You can install the necessary libraries using the following command:

```bash
pip install tweepy mysql-connector-python matplotlib
