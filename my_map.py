import folium
import pandas

data = pandas.read_csv("VolcanoesOfUSA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def foo(elevation):
    if elevation < 1000:
        return "red"
    elif 1000 <= elevation < 3000:
        return "blue"
    else:
        return "orange"

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
folium_static(map)
feat_GV = folium.FeatureGroup(name="Volcanoes in the USA")

for lt, ln, el in zip(lat, lon, elev):
    feat_GV.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + "m", fill_color=foo(el), color="grey", fill_opacity=0.7))

feat_GP = folium.FeatureGroup(name="World Population in 2005/ Less than 10mln - orange, less than 20mln and more than or equal 10mln - blue, more than 20mln - red")
feat_GP.add_child(folium.GeoJson(data=open("PopulationOfWorld.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(feat_GV)
map.add_child(feat_GP)
map.add_child(folium.LayerControl())
map.save("WorldMap.html")
