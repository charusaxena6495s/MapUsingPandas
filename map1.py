
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

map=folium.Map(location=[38.58, -99.89], zoom_start=6, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="My Map")


for lt,ln, el in zip(lats , longs, elev):
   # iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    if(el<=1000):
        colour1='green'
    elif( 1000<el<3000 ):
        colour1='orange'
    else:
        colour1='red'

    print(lt,ln, el,colour1)

    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el) + "m",icon=folium.Icon(colour=colour1)))


map.add_child(fg)
map.save("map3.html")


