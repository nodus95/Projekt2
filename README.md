# Projekt 2 - wtyczka do programu QGIS
Za pomocą której użytkownik będzie w stanie obliczyć różnicę wysokości oraz pole powierzchni pomiędzy wybranymi punktami na warstwie.

### Wymagania
Aby użytkownik mógł przetestować naszą wtyczke musi posiadać na swoim urządzeniu program QGIS.

Wymagana jest również instalacja wtyczki:

Wszystkie pliki znajdujące się w folderze "Wymagane pliki" należy umieścić w folderze plugins, znajdującym się w lokalizacji:
Przykładowo dla wersji QGIS 3.22.16:

```sh
  C:/Users/<nazwa_użytkownika>/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/<nazwa_wtyczki>
```

Następnie w programie QGIS należy w menu "Wtyczki" wybrać opcję "Zarządzanie wtyczkami", znaleźć pozycję "Naszawtyczka" i upewnić się że zaznaczony jest checkbox obok nazwy naszej wtyczki. Następnie należy kliknąć "Zainstaluj wtyczkę".

### Jak działa nasza wtyczka

Aby uruchomić interfejs graficzny naszej wtyczki należy kliknąć w żółtą ikonkę w prawym górnym rogu QGISa.

Wtyczka wykonuje następujące czynności:

##### OBLICZANIE RÓŻNICY WYSOKOŚCI

Po zaznaczeniu dwóch punktów na tej samej warstwie i naciśnięciu przycisku 'Policz' w interfejsie wtyczki, oblicza różnicę wysokości między nimi.
W wiadomości wynikowej (wyświetlanej w komunikatach) wyświetlane są numery punktów wykorzystanych do obliczeń na podstawie wartości atrybutu 'nr_punktu' wraz z wynikiem przeprowadzonego działania.
Przykładowo:
```sh
Obliczenie różnicy wysokości : Różnica wysokości między punktami 819214.2.5006 i 819214.2.5007 w systemie wysokościowym PL_EVRF2007 wynosi: -8.899 [m]
```
Program przyjmuje wartości do obliczeń zawsze w tej samej kolejności, takiej samej w jakiej wymienione są numery punktów. Aby uzyskać odwrotne przewyższenie należy przyjąć obliczoną wartość z odwrotnym znakiem.
Obsługiwane są wysokości podane w systemach:
- PL-EVRF2007
- PL-KRON86
Których atrybuty są opisane w tabeli atrybutów jako kolejno: "h_plevrf2007nh" i "h_plkron86nh".
W przypadku gdy nazwa atrybutu wysokości jest inna zostanie wyświetlony komunikat "Nieobsługiwany system wysokości."

##### OBLICZANIE POLA POWIERZCHNI

Pole powierzchni obliczane jest dla dowolnej liczby punktów większej niż 3, metodą Gaussa.
Po zaznaczeniu min. trzech  punktów na tej samej warstwie i naciśnięciu przycisku 'Policz' w interface wtyczki,  obliczone zostanie pole powierzchni między punktami o wybranych wierzchołkach oraz w komunikatach pojawi się właściwy wynik.
Przykładowo:
```sh
Obliczenie pola powierzchni : Pole powierzchni figury o wierzchołkach w punktach o numerach: 819214.2.5002, 819214.2.5006, 819214.2.5007, 819214.2.5003 wynosi: 488283.8654 [m²]
```
 Numery punktu pobierane są na podstawie wartości atrybutu 'nr_punktu'.
Pole powierzchni obliczane jest TYLKO dla punktów w układzie PL-2000, których współrzędne 'x' i 'y' są opisane w tabeli atrybutów jako kolejno: 'x2000' 'y2000'. W innym wypadku zostanie ukazany komunikat o błędzie. 

### Uwagi oraz błędy 

- Ścieżka do folderu plugins nie musi być podobna jak w przykładzie, jest to zależne od wersji QGISA oraz systemu użytkownika.
- Atrybuty współrzędnych oraz wysokości punktów muszą być nazwane tak samo jak jest to napisane powyżej. W innym wypadku wtyczka nie zadziała.