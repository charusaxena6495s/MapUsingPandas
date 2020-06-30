
import folium
import pandas

print("test2")
data = pandas.read_csv("Volcanoes.txt")
lats=list( data["LAT"])
longs = list(data["LON"])
elev = list(data["ELEV"])
#html = """<h4>Volcano information:</h4>
#Height: %s m
#"""

map=folium.Map(location=[27.33, 78.39], zoom_start=6, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="My Map")


for lt,ln, el in zip(lats , longs, elev):
   # iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    colour1='orange'
    fg.add_child(folium.Marker(location=[lt,ln],popup=el,icon=folium.Icon(colour=colour1)))


map.add_child(fg)
map.save("map1.html")


