Wymagana jest 

##Instrukcja instalacji wtyczki

Wszystkie pliki znajdujące się w folderze "Wymagane pliki" należy umieścić w folderze plugins, znajdującym się w lokalizacji:
Qgis Białowieża
```sh
  C:/Users/<nazwa użytkownika>/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/<nazwa wtyczki>
```
lub dla Qgis Firenze
```sh
C:/Users/<nazwa użytkownika>/AppData/Roaming/Qgis/apps/qgis-ltr/python/plugins/<nazwa wtyczki>
```
Następnie należy w menu "wtyczki" wybrać opcję "zarządzanie wtyczkami" i znaleźć pozycję <nazwa wtyczki> i upewnić się że zaznaczony jest checkbox obok nazwy naszej wtyczki

Wtyczka wykonuje następujące czynności:

OBLICZANIE RÓŻNICY WYSOKOŚCI

Po zaznaczeniu dwóch punktów na tej samej warstwie i naciśnięciu przycisku 'policz' w interface wtyczki oblicza różnicę wysokości między nimi.
W wiadomości wynikowej (wyświetlanej w komunikatach) wyświetlane są numery punktów wykorzystanych do obliczeń na podstawie wartości atrybutu 'nr_punktu'. Program przyjmuje wartości do obliczeń zawsze w tej samej kolejności, takiej samej w jakiej wymienione są numery punktów. aby uzyskać odwrotne przewyższenie należy przyjąć obliczoną wartość z odwrotnym znakiem.
Obsługiwane są wysokości podane w systemach:
- PL-EVRF2007
- PL-KRON86
Których atrybuty są opisane w tabeli atrybutów jako kolejno: "h_plevrf2007nh" i "h_plkron86nh".
W przypadku gdy nazwa atrybutu wysokości jest inna zostanie wyświetlony komunikat "Nieobsługiwany system wysokości."

OBLICZANIE POLA POWIERZCHNI

Pole powierzchni obliczane jest dla dowolnej liczby punktów większej niż 3, metodą Gaussa.
Po zaznaczeniu min. trzech  punktów na tej samej warstwie i naciśnięciu przycisku 'policz' w interface wtyczki obliczone zostanie pole powierzchni między punktami o wybranych wierzchołkach. Ich numery pobierane są na podstawie wartości atrybutu 'nr_punktu'.
Pole powierzchni obliczane jest TYLKO dla punktów w układzie PL-2000, których współrzędne 'x' i 'y' są opisane w tabeli atrybutów jako kolejno: 'x2000' 'y2000'.

