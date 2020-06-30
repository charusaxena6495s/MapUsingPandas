import folium
import pandas

## base map with opening location , zoom type and type of map
map6=folium.Map(location=[38.58, -99.89],zoom_start=6,tiles="Stamen Terrain")

# reading the volcanoes.txt
data =pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
long=list(data["LON"])
elevation= list(data["ELEV"])

# this creates a feature group to which child objects can be added
fg=folium.FeatureGroup(name="My Map")

for la, long, el in zip(lat,long,elevation):
    if(el<=1000):
        colour1='green'
    elif( 1000<el<3000 ):
        colour1='orange'
    else:
        colour1='red'
    fg.add_child(folium.Marker(location=[la,long], popup=el, icon= folium.Icon(color=colour1)))

map6.add_child(fg)


map6.save("NewMap.html")