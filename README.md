**ISS TRACKER**
Aplikacja w Pythonie, która w czasie rzeczywistym śledzi położenie Międzynarodowej Stacji Kosmicznej (ISS), sprawdza, nad jakim krajem się znajduje i generuje interaktywną mapę w przeglądarce.

**FUNKCJE**
Live Tracking: Pobiera aktualne współrzędne ISS z API Open-Notify.
Geocoding: Wykorzystuje bibliotekę geopy, aby sprawdzić nazwę państwa pod stacją (lub informuje, że ISS jest nad oceanem).
Interaktywna Mapa: Tworzy plik HTML z mapą (Folium/Leaflet), która automatycznie odświeża się co 10 sekund.
Custom Marker: Oznacza pozycję ISS ikoną rakiety.

**STRUKTURA PROJEKTU**
ISSlocation.py – Główna logika programu: pobieranie danych, odwrócone geokodowanie i generowanie mapy.
whereisiss.html – Automatycznie generowana mapa (wykorzystuje Leaflet.js).

**UŻYTE TECHNOLOGIE**
Język: Python
Biblioteki: * requests (komunikacja z API)
folium (generowanie map HTML)
geopy (identyfikacja lokalizacji/krajów)
API: [Open-Notify ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
