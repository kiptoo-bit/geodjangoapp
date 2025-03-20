 Kenya Geospatial Data Visualization

This project is a web-based geospatial visualization tool that displays key geographical features of Kenya using Leaflet.js, Django, and Bootstrap. The map includes features such as counties, wetlands, towns, highland roads, and forest ranges. The tool allows users to interact with the map and download geospatial data in various formats (Shapefile and CSV).

 Features

- Interactive map displaying geographical features of Kenya.
- Geolocation button that centers the map on the user's current location.
- Download buttons for shapefiles and CSV files for various datasets (Counties, Wetlands, Towns, Roads, Forests).
- Responsive layout using Bootstrap for a mobile-friendly experience.

 Tech Stack

Frontend: HTML, CSS, JavaScript (Leaflet.js for map visualization, Bootstrap for styling)
Backend: Django (Python-based web framework)
Geospatial Data: GeoDjango with PostGIS database (for geospatial data storage and management)

 Setup Instructions

 Prerequisites

- Python 3.x
- Django
- GeoDjango
- Leaflet.js
- Bootstrap

 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/kenya-geospatial-data-visualization.git
   cd kenya-geospatial-data-visualization
   ```

2. Set up a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your database (PostgreSQL with PostGIS enabled).

5. Run the migrations to set up the database schema:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

 Using the Map

Once the server is running, navigate to `http://127.0.0.1:8000` to view the interactive map. You can click the **Geolocation** button to center the map on your current location. The **Download** buttons allow you to download data in Shapefile or CSV format.

Downloadable Data

The following datasets are available for download:

Counties.shp / Counties.CSV
Wetlands.shp / Wetlands.CSV
Towns.shp / Towns.CSV
Roads.shp / Roads.CSV
Forest.shp / Forest.CSV

 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 Acknowledgements

- Leaflet.js: A leading open-source JavaScript library for interactive maps.
- Bootstrap: A front-end framework for responsive web design.
- Django & GeoDjango: A powerful Python-based web framework for building web applications with geospatial capabilities.
```

This README provides a concise overview of the project, installation steps, and features. You can customize it further based on any additional details or modifications specific to your project.
