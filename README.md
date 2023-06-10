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
Po zaznaczeniu dwóch punktów na tej samej warstwie oblicza różnicę wysokości między nimi.
W wiadomości wynikowej wyświetlane są numery punktów wykorzystanych do obliczeń. Program przyjmuje wartości do obliczeń zawsze w tej samej kolejności, takiej samej w jakiej wymienione są numery punktów. aby uzyskać odwrotne przewyższenie należy przyjąć obliczoną wartość z odwrotnym znakiem.
Obsługiwane są wysokości podane w systemach:
- PL-EVRF2007
- PL-KRON86
których atrybuty są opisane w tabeli atrybutów jako kolejno: "h_plevrf2007nh" i "h_plkron86nh".
W przypadku gdy nazwa atrybutu wysokości jest inna 