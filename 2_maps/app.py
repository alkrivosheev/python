import folium # pip install folium

map = folium.Map(location=[54.514673, 36.248834], zoom_start=6, tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[54.514673, 36.248834], popup="Hi a'm a marker", icon=folium.Icon(color='green')))
# 54.514673, 36.248834
map.save("Map1.html")