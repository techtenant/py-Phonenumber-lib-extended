import folium
from numberLocation import actualLocation
import cordinates

lat = cordinates.lat
lng = cordinates.lng
mapInfo = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=actualLocation).add_to(mapInfo)

mapInfo.save("index.html")