### This App uses the folium library to create an interactive map that displays
### the entire world's countries, highlights them based on population, and 
### displayes color coded markers with elevation info for all north american
### volcanoes. Also, the layers have an ON/OFF button.

# Import necessary libraries
import folium
import pandas

# Read in volcano data using pandas and store needed data
data=pandas.read_csv("volcanoes.txt")
latitude=data["LAT"]
longitude=data["LON"]
elevation=data["ELEV"]

# Function for chnaging popup color for volcanoes based on elevation
def colorPopups(elevation):         # Takes in an elevation as an argument
    if elevation < 1000:            # Short = Green
        return 'green'
    elif 1000 <= elevation < 3000:  # Medium = Orange
        return 'orange'
    else:
        return 'red'                # Tall = Red

# Define starting point on the map, how zoomed in you will be, and map style (help(folium.Map))
map=folium.Map(location=[33.819855, -118.36758], zoom_start=10, tiles = "CartoDB positron")

# Save the volcano objects as a layer named "Volcanoes" for layer control (can turn ON/OFF)
fgv = folium.FeatureGroup(name="Volcanoes")

# Loop through the latitude, longitude, and elevation and assign them as 'tooltips' (hover mouse info) to individual volcanoes.
# Also, create the markers as Circles and assign them colors, radii, and opacities.
for lat, lon, elev in zip(latitude,longitude,elevation):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius=6, tooltip=str(elev)+" m", fill=True, fill_color=colorPopups(elev), 
    color='black', fill_opacity=0.7))

# Save the country polygon objects as a layer names "Population" for layer control (can turn ON/OFF)
fgp = folium.FeatureGroup(name="Population")

# Use the json file to draw a line following the given coordinates around each country and highlight the country with a different color based on population
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Add the volcano and population layers to the map
map.add_child(fgv)
map.add_child(fgp)

# Looks for objects (children) added to the map and adds an ON/OFF box to the map
map.add_child(folium.LayerControl()) 

# Save map to html file
map.save("Map1.html")