import folium
import pandas

## base map with opening location , zoom type and type of map
map7=folium.Map(location=[38.58, -99.89],zoom_start=6,tiles="Stamen Terrain")

# reading the volcanoes.txt and converts dataframe array to list
data =pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
long=list(data["LON"])
elevation= list(data["ELEV"])

# this creates a feature group to which child objects can be added
fgv=folium.FeatureGroup(name="Volcanoes")

for la, long, el in zip(lat,long,elevation):
    if(el<=1000):
        colour1='green'
    elif( 1000<el<3000 ):
        colour1='orange'
    else:
        colour1='red'
    fgv.add_child(folium.CircleMarker(location=[la,long], popup=el,radius=10,fill_color=colour1, color='grey', fill_opacity=0.7 ))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
 style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if  10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map7.add_child(fgv)
map7.add_child(fgp)


map7.add_child(folium.LayerControl())

map7.save("NewCircleMarkerMap.html")