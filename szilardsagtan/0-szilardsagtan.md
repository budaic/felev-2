# Szilárságtan

# Tartalomjegyzék
1. [Általános tudnivalók](#általános-tudnivalók)
2. [Jelölések](#jelölések)
3. [Definíciók](#definiciók)
4. [Tételek, állítások](#tételek-állítások)
5. [Előadások](#előadások) \
    5.1 [1. Előadás](#1-előadás)

# Általános tudnivalók

Dr. Kossa Attila
mm.bme.hu/~kossa/

Statika - merev testek
Sziltan - deformálható testek

Cél: deformáció és feszültségek számítása

Téma: Lineárisan rugalmas anyagok, kis alakváltozások, rudak, gerendák

## Hasznos lehet
* Gyakorlati anyagok példatár - Teamsen - nyomtassuk ki, vigyük gyakorlatra
* Konzultáció lehet, gyakvezzel egyeztetve.
* Alkalmazott mechanika szakosztály youtube videók
* A diákat Moodle-re tölti fel
* Muttnyánszky Ádám: Szilárdságtan 1981
* Csernák pdf - valahol fenn van
* Efficient engineer

## Követelmények
* Gyakorlati órák 70%-a - katalógus van
* Vizsga van:
    * Írásbeli 100 pont (40 min)
    * Szóbeli: fakultatív + infok a prezentáción?
* HF: 04.08., 05.13. - kötelező, valami python van benne
* ZH 04.25. - féléves anyag 2/3-a (50 pont)

# Előadásokok

## 1. Előadás

Statika - merev testek
Sziltan - deformálható testek

Cél: deformáció és feszültségek számítása

Téma: Lineárisan rugalmas anyagok, kis alakváltozások, rudak, gerendák

### [Rudak gerendák feszültségi állapota](rudak-gerendak-feszultsegi-allapota.md)

## 2. Előadás

### Másodrendű nyomaték

Hajlítás, nyírás, csavarás igénybevételnél

Keresztmetszethez tartozó tisztán geometriai mennyiség
Mindig csak síkidomra számítjuk (a vizsgált rúd keresztmetszete pl)
Súlypontszámítás ismerete elengedhetetlen

Koordináta rendszerben tetszőleges síkidomot nagyon kicsi felületelemekkel közelítem

Terület közelítése: 
$A \approx \sum_0^n \Delta A$

ennek a határértéke ($n \rightarrow \infty$) lesz a terület

$A = lim_{n \rightarrow \infty}{\sum_0^n{\Delta A}} = \int_{(A)}{dA}$

Felírjuk a távolságát mindkét tengelytől, a tengelyre számított másodrendű nyomaték alatt a tengelytávolság négyzetösszegét értjük
**Tengerlyre számított** másodrendű nyomaték
Jelölés: $I_x$

$I_x = \int_{(A)}{y^2dA}$
$I_y = \int_{(A)}{x^2dA}$

Minél nagyobb a másodrendű nyomaték annál kisebb a deformáció (azonos erőre)

**Tengelypárra számított** másodrendű nyomaték
$I_{xy} = \int_{(A)}{xydA}$

Fontos megfigyelés: $I_x$ biztosan nagyobb mint 0.
$I_x > 0 = [m^4]$
$I_y > 0 = [m^4]$
$I_{xy} \in \mathbb{R} = [m^4]$


**Ez három független mennyiség !!**

Számítható a pontra számított (poláris) másodrendű nyomaték
$I_p = \int_{(A)}{r^2dA} = \int_{(A)}{(x^2 + y^2)dA}$
$I_p = I_y + I_x$
nem független mennyiség

Ha az egyik tengely szimmetriatengely, akkor biztosan $I_{xy} = 0$

A súlyponti (súlyponton átmenő) tengelyekre számított másodrendű nyomaték kifejezetten fontos.

**Példa**:
Téglalap keresztmetszet, illesztem a súlypontjához a tengelyeket (Origó a keresztmetszet súlypontja). Szélessége: $a$. Magassága: $b$.

$I_x = \int_{(A)}{y^2dA}$
$dA = dx dy$
$\int_{-b/2}^{b/2}{\int_{-a/2}^{a/2}{y^2dx}dy}$

$I_x = \int_{-b/2}^{b/2}{(ay^2)dy}$
$I_x = a[\frac{y^3}{3}]_{-b/2}^{b/2} = \frac{ab^3}{12}$

$I_y = b[\frac{x^3}{3}]_{-a/2}^{a/2} = \frac{ba^3}{12}$

Itt mivel $x$ és $y$ is szimmetriatengely:

$I_{xy} = 0$

Összetett keresztmetszet (síkidom) esetén: 
Össze lehet adni egy közös koordinátarendszer esetén az egyes primitív síkidomok másodrendű nyomatékait (a terület előjeles figyelembe vételével). 

**Steiner-tétel** (párhuzamos tengelyek tétele)
$I_\xi = I_x + t^2A$
$I_\xi > I_x$

!!Csak akkor alkalmazható, ha a két párhuzamos tengely közül az egyik a súlyponton halad keresztül!!

**Tengelypár esetén**
$I_{\xi \eta} = I_{xy} + rt \cdot A$

Hogyan találom meg azt a tengelyt, amelyre a legnagyobb a másodrendű nyomaték

> ### Főmásodrendű nyomatékok

Koordinátarendszer elforgatása
Nem kell fejből tudni sem zhn sem vizsgán.
Levezetés a ppt-ben

#TODO megcsinálni ezt a pptből

Főirányok helyzetére adódik





