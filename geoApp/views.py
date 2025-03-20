from django.shortcuts import render, redirect
import os
import folium
import geopandas as gpd
from folium import GeoJson
import zipfile
from django.http import HttpResponse, FileResponse

# Create your views here.
def home(request):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')

    m = folium.Map(location=[-0.2223, 36.7622], zoom_start=6)

# Initialize Folium Map with Min and Max Zoom Levels
    m = folium.Map(
        location=[-0.2223, 36.7622], 
        zoom_start=6,  # Set initial zoom level
        min_zoom=5,  # Set minimum zoom level
        max_zoom=18  # Set maximum zoom level
    )
    
    #styling
    style_Kenya_county_dd = {'fillColor': '#0d81eb', 'color': '#0d81eb'}
    style_kenya_wetlands = {'color': 'green'}
    style_kenya_all_towns = {'color': 'red'}
    style_kenya_highland_roads = {'color': '#e9b107'}
    style_kenya_forestranges = {'color': '#3d9112'}

    Kenya_county_dd = gpd.read_file(os.path.join(shp_dir, 'Kenya_county_dd.shp'))
    Kenya_county_dd_geojson = Kenya_county_dd.to_crs("EPSG:4326").to_json()

    kenya_wetlands = gpd.read_file(os.path.join(shp_dir, 'kenya_wetlands.shp'))
    kenya_wetlands_geojson = kenya_wetlands.to_crs("EPSG:4326").to_json()

    kenya_towns = gpd.read_file(os.path.join(shp_dir, 'kenya_all_towns.shp'))
    kenya_towns_geojson = kenya_towns.to_crs("EPSG:4326").to_json()

    kenya_roads = gpd.read_file(os.path.join(shp_dir, 'kenya_highland_roads.shp'))
    kenya_roads_geojson = kenya_roads.to_crs("EPSG:4326").to_json()

    kenya_forestranges = gpd.read_file(os.path.join(shp_dir, 'kenya_forestranges.shp'))
    kenya_forestranges_geojson = kenya_forestranges.to_crs("EPSG:4326").to_json()

    GeoJson(Kenya_county_dd_geojson, name='Kenya_counties', style_function=lambda x: style_Kenya_county_dd).add_to(m)
    GeoJson(kenya_wetlands_geojson, name='kenya_wetlands', style_function=lambda x: style_kenya_wetlands).add_to(m)

    # Create a feature group for kenya_all_towns layer
    kenya_all_towns_fg = folium.FeatureGroup(name='kenya_all_towns')
    # Iterate over the points and add colored circles to the feature group
    for _, row in kenya_towns.iterrows():
        folium.CircleMarker(location=[row['geometry'].y, row['geometry'].x], radius=2, fill=True, color='red', fill_opacity=1).add_to(kenya_all_towns_fg)
    kenya_all_towns_fg.add_to(m)

    GeoJson(kenya_roads_geojson, name='kenya_highland_roads', style_function=lambda x: style_kenya_highland_roads).add_to(m)
    GeoJson(kenya_forestranges_geojson, name='kenya_forestranges', style_function=lambda x: style_kenya_forestranges).add_to(m)

    folium.LayerControl().add_to(m)

    m = m._repr_html_()
    context = {'my_map': m}
    return render(request, 'geoApp/home.html', context)

# Function to Download Shapefile as ZIP
def download_shapefile(request, filename):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    file_path = os.path.join(shp_dir, filename)

    # Create ZIP archive
    zip_filename = f"{filename}.zip"
    zip_path = os.path.join(shp_dir, zip_filename)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for ext in ['.shp', '.shx', '.dbf', '.prj']:
            file = file_path.replace('.shp', ext)
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))

    response = FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=zip_filename)
    return response

# Function to Download CSV
def download_csv(request, filename):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    file_path = os.path.join(shp_dir, filename)

    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)

    gdf = gpd.read_file(file_path)
    csv_path = file_path.replace('.shp', '.csv')
    gdf.to_csv(csv_path, index=False)

    response = FileResponse(open(csv_path, 'rb'), as_attachment=True, filename=f"{filename}.csv")
    return response