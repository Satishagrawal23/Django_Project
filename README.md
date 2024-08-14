# Django Data Analysis Project

## Overview

This Django-based web application allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on the web interface.

## Features

1. **File Upload**: Users can upload CSV files.
2. **Data Processing**: Uses pandas to read and analyze the uploaded CSV file.
   - Displays the first few rows of the data.
   - Calculates summary statistics (mean, median, standard deviation) for numerical columns.
   - Identifies and handles missing values.
3. **Data Visualization**: Generates basic plots using matplotlib or seaborn.
   - Histograms for numerical columns.
4. **User Interface**: Simple and user-friendly interface using Django templates.
   - Displays the data analysis results and visualizations in a clear and organized manner.

## Project Structure
```bash
data_analysis_project/
│
├── analysis/
│   ├── migrations/
│   ├── templates/
│   │   ├── analysis/
│   │   │   ├── upload.html
│   │   │   └── results.html
│   │   ├── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── data_analysis_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│
├── manage.py
└── requirements.txt

```


## Setup Instructions

### Prerequisites

- Python 3.x
- Django 5.x
- pandas
- matplotlib
- seaborn

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/data_analysis_project.git
   cd data_analysis_project
   
2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install dependencies**:
   
   ```sh
   pip install -r requirements.txt
   
4. **Run migrations**:

   ```sh
   python manage.py migrate
   
5. **Create the media directory**:

   ```sh
   mkdir media
   
6. **Start the development server**:

   ```sh
   python manage.py runserver

7. **Access the application**:

   Open your browser and go to `http://127.0.0.1:8000/analysis/`

## Usage
1. **Upload a CSV File**:
   - Navigate to the upload page.
   - Select a CSV file and click the upload button.

3. **View Analysis Results**:
   - The application will display the first few rows of the data, summary statistics, and missing values.
   - Histograms for numerical columns will be generated and displayed.
  
## Sample CSV File

### A sample CSV file candy-data.csv is provided in the root directory for testing purposes.

## Example

### Here’s an example of how to upload a CSV file and view the results:

1. **Navigate to the upload page**.
2. **Select the sample_data.csv file**.
3. **Click the upload button**.
4. **View the analysis results and visualizations.**

## Troubleshooting

### If you encounter any issues, ensure that:

- The media directory exists and is writable.
- The file paths in settings.py are configured correctly:
     ```sh
     MEDIA_URL = '/media/'
     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
     
## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)


### Notes

1. Replace the `git clone` URL with the actual URL of your repository.
2. Customize any sections as needed based on your project specifics.
3. Ensure you have a sample CSV file named `sample_data.csv` in your project root directory if referenced in the `README.md`.

This `README.md` file provides a comprehensive guide for setting up and using your Django-based data analysis application.

