# felev-2
A BME Mechatronika Bsc második féléves jegyzetei Széles Tamás és Budai Csanád által.

# Tárgyak
* Mechatronika mérnök Bsc második félév (2022-es tanterv szerint)
    * [Többváltozós analízis mérnököknek](tobbvaltozos-analizis/0-tobbvaltozos-analizis.md) (emelt matekos G2)
    * [Szilárdságtan](szilardsagtan/0-szilardsagtan.md)
    * [Programozás alapjai](informatika-es-programozas-alapjai/0-informatika-es-programozas-alapjai.md)
    * [Ergonómia](tobbvaltozos-analizis/0-ergonomia.md)
    * [Elektronika I.](tobbvaltozos-analizis/0-elektronika-1.md)
    

# TODO
* Rendezni a szabványírás helyzetet
* [függvény folytonossága második definició](tobbvaltozos-analizis/fuggveny-folytonossaga.md#definíció-2) kérdéses, hogy $\geq$ kell, vagy $>$


# Írás szabvány

## Fájlrendszer
* targymappa
    * /img/
    * 0-targynev\.md
    * mas_fajlok.md

## Szabályok
* A fájlokban csak ékezet nélküli kis karaktereket hasznalunk kötőjellel elválasztva. (pl.: `0-tobbvaltozos-analizis.md`, `kulso-pont.md`)
* A tárgyaknál teljes név kell mindenhol ahol feljön
* Minden tárgynak kell egy külön mappa azon a mappán belül kell egy img mappa, ahová minden kép kerül.
* A 0-tárgy nevével jelzett .md fájlban lesznek az: (mind h1-el)
    1. tárgyhoz tartozó tartalomjegyzek 
    2. általános tudnivalók
    3. Definiciók/Tételek linkelve
    4. laborjegyzetek
    5. az előadás jegyzetek folytatólagosan egy nagy Előadások header alatt.
* A képletek írásához LaTeX kódot használunk (nem kézzel írott képleteket).
* A kézzel rajzolt/írt részek minimálisak legyenek a kereshetőség miatt.
* Amikor egy külön definíció/fogalom/tétel (valamilyen elkülönülő egység) jön fel annak külön .md filet kell csinálni a tantárgymappán belül
* Ha eszedbe jut, hogy egy fogalmat láttál már korábban, akkor linkeld be (nyugodtan lehet másik tárgy fogalmait is használni)