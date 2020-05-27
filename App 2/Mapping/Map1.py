import folium
import pandas

data=pandas.read_csv("volcanoes.txt")
latitude=data["LAT"]
longitude=data["LON"]
elevation=data["ELEV"]

def colorPopups(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[33.819855, -118.36758], zoom_start=10, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lat, lon, elev in zip(latitude,longitude,elevation):
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=6, tooltip=str(elev)+" m"), fill=True, fill_color=colorPopups(elev), color='grey', fill_opacity=0.7)

map.add_child(fg)
    

map.save("Map1.html")