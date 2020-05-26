import folium
map=folium.Map(location=[33.819855, -118.36758], zoom_start=10, tiles = "Stamen Terrain")

fg = folium.featureGroup(name="My Map")
fg.add_child(folium.Marker(location=[33.819855, -118.36758], popup="Home", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")