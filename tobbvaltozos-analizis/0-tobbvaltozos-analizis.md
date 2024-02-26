# Többváltozós analízis

# Tartalomjegyzék
1. [Általános tudnivalók](#általános-tudnivalók)
2. [Jelölések](#jelölések)
3. [Definíciók](#definiciók)
4. [Tételek, állítások](#tételek-állítások)
5. [Előadások](#előadások) \
    5.1. [1. Előadás](#1-előadás)
    5.2. [2. Előadás](#2-előadás)


# Általános tudnivalók

# Jelölések
$\mathbb{R}^p$ - $p$ dimenziós valós tér \
$A^C$ - $A$ halmaz komplementere \
$\text{ext } A$ - $A$ halmaz [külső pontjainak](kulso-pont.md) halmaza \
$\text{int } A$ - $A$ halmaz [belső pontjainak](belso-pont.md) halmaza \
$\partial A$ - $A$ halmaz [határpontjainak](hatarpont.md) halmaza \
$\bar{A}$ - $A$ halmaz [lezártja](halmaz-lezartja.md) \
$\text{graph } f$ - $f$ [grafikonja](grafikon.md) \
$\gamma_c$ - $f$ függvény $c$-hez tartozó [szintvonala](szintvonal.md) \
$\Gamma_c$ - $f$ függvény $c$-hez tartozó [kontúrvonala](konturvonal.md) \
$|\vec{x}|$ - $\vec{x}$ hossza \
$d(\vec{x}, \vec{y})=|\vec{x}-\vec{y}|$ - $\vec{x}$ és $\vec{y}$ távolsága

# Definíciók
* [Pont környezete](kornyezet.md)
* [Belső pont, belső ponthalmaz](belso-pont.md)
* [Külső pont, külső ponthalmaz](kulso-pont.md)
* [Határpont, határponthalmaz](hatarpont.md)
* [Nyílt halmaz](nyilt-halmaz.md)
* [Zárt halmaz](zart-halmaz.md)
* [Halmaz lezártja](halmaz-lezartja.md)
* [Izolált pont](izolalt-pont.md)
* [Torlódási pont](torlodasi-pont.md)
* [Összefüggőség](osszefuggoseg.md)
* [Tartomány](tartomany.md)
* [Korlátos halmaz](korlatos-halmaz.md)
* [Sorozat határértéke](sorozat-hatarerteke.md)
* [Konvergens sorozat](konvergens-sorozat.md)
* [Függvény határértéke](fuggveny-hatarerteke.md)
* [Függvény folytonossága](fuggveny-folytonossaga.md)
* [Korlátos sorozat](korlatos-sorozat.md)
* [Grafikon](grafikon.md)
* [Kontúrvonal](konturvonal.md)
* [Szintvonal](szintvonal.md)
* [Két út módszer](ket-ut-modszer.md)
* [Parciális derivált](parcialis-derivalt.md)
* [Young tétel](young-tetel.md)
* [Iránymenti derivált](iranymenti-derivalt.md)
* [Érintősík](erintosik.md)
* [Totális derivált](totalis-derivalt.md)
* [Gradiens vektor](gradiens-vektor.md)


# Tételek, állítások
* [+ random allitasok kellenek, amiket felirtunk?]
* [Bolzano-Weierstrass tétel](bolzano-weierstrass.md)

# Előadások
---
## 1. előadás

> ### Félév tematikája
* Többváltozós függvények: $f:\mathbb{R}^p \rightarrow \mathbb{R}$
* Térgörbék: $f:\mathbb{R}\rightarrow \mathbb{R}^p$
* Felületek: $f:\mathbb{R}^2\rightarrow \mathbb{R}^p$
* Vektormezők:  $f:\mathbb{R}^p\rightarrow \mathbb{R}^q$
* Függvénysorozatok/sorok, hatványsorok, Fourier-sorok
* Komplex függvénytani bevezető

> ### $\mathbb{R}^p$ tér topológiája
**Jelölés**: $\vec{x} \in \mathbb{R}^p$

**Def**.: 
* [Pont környezete](kornyezet.md)
* [Belső pontok](belso-pont.md)
* [Külső pontok](kulso-pont.md)
* [Határpontok](hatarpont.md)
* [Nyílt halmaz](nyilt-halmaz.md)
* [Zárt halmaz](zart-halmaz.md)
* [Halmaz lezártja](halmaz-lezartja.md)

**Áll**.: 
* $\text{int } A\subseteq A \subseteq \bar{A}$
* [$\text{ext }A$](kulso-pont.md) mindig [nyílt](nyilt-halmaz.md)
* [$\partial A$](hatarpont.md) mindig [zárt](zart-halmaz.md)
* [$\text{int } A$](belso-pont.md), [$\text{ext } A$](kulso-pont.md), [$\partial A$](hatarpont.md) páronként diszjunkt halmazok
* $ \text{int } \ A \cup \text{ ext } A \ \cup \partial A = \mathbb{R}^p $, ha $A \subseteq \mathbb{R}^p$ 

**Példa**: $A=[0;1) \text{ esetén}$
* $\text{int } A = (0; 1)$
* $\text{ext } A = (-\infty; 0) \cup (1; \infty)$
* $\partial A = \{0; 1\}$
* $\bar{A} = [0; 1]$

**Példa**: $A = \{(x, y)\in \mathbb{R}^2: 0<x^2+y^2<1\}$ esetén
* $\text{int } A = A$
* $\text{ext } A = \{ x^2+y^2>1 \}$
* $\partial A = \{ x^2+y^2=1\}\cup \{(0, 0)\}$

**Def**.: 
* [Izolált pont](izolalt-pont.md)
* [Torlódási pont](torlodasi-pont.md)

**Példa**: $A=\{ \frac{1}{n}:n\in \mathbb{N}^p \}$-nak $0$-ban van [torlódási pontja](torlodasi-pont.md)

**Példa**: $A=(0;1]$-nak a [torlódási pontjai](torlodasi-pont.md) $[0;1]$

**Áll**.:
* Véges sok [nyílt halmaz](nyilt-halmaz.md) metszete nyílt
* Akárhány [nyílt halmaz](nyilt-halmaz.md) uniója nyílt
* Véges sok [zárt halmaz](zart-halmaz.md) uniója zárt
* Akárhány [zárt halmaz](zart-halmaz.md) metszete zárt

**Def**.: 
* [Összefüggő halmaz](osszefuggoseg.md)
* [Tartomány](tartomany.md)
* [Korlátos halmaz](korlatos-halmaz.md)

**Példa**: 
* $(1; 3]$ összefüggő
* $A=(0;1) \cup (1;3]$ nem összefüggő, hiszen $B=(0; 1), C=(1; 4)$

**Def**.:
* [Sorozat határértéke](sorozat-hatarerteke.md)
* [Konvergens sorozat](konvergens-sorozat.md)



* [Függvény határértéke](fuggveny-hatarerteke.md)
* [Függvény folytonossága](fuggveny-folytonossaga.md)

**Áll**.: $\lim{\vec{x}_n}=A \Leftrightarrow \forall i<p: (\vec{x}_n)_i\to A_i$

**Példa**:
$\lim_{n\to \infty} \left( \frac{n-1}{n}, \left( 1+\frac{1}{n}\right)^n\right) = (1, e)$

**Áll**.: 
* [Bolzano-Weierstrass tétel](../analizis/bolzano-weierstrass-tetel.md): $\forall$ [korlátos sorozatnak](korlatos-sorozat.md) $\exists$ [konvergens](konvergens-sorozat.md) [részsorozata](../analizis/reszsorozat.md)
* $\mathbb{R}^p$-ben is igaz, hogy $\forall$ [Cauchy sorozat](../analizis/cauchy-sorozat.md) [konvergens](konvergens-sorozat.md)


> ### Kétváltozós függvények

**Def**.:
* [Grafikon](grafikon.md)
* [Kontúrvonal](konturvonal.md)
* [Szintvonal](szintvonal.md)

**Példa**: $f(x, y) = \sqrt{x^2+y^2} = z$, Mi lehet ez?

**Medoldás**:
* Szintvonalak: $\sqrt{x^2+y^2}=c$ - minden szintvonal kör
* Síkmetszés $[x,\ z]$ síkkal, (ekkor $y=0$): $\sqrt{x^2}=|x|=z$
* Tehát minden vízszintes szintvonal kör, és az egyik függőleges egy abszolútérték, így ez egy forgáskúp lesz.

---

## 2. előadás

**Példa**: $\lim_{(x,y)\rightarrow(0,0)}\frac{2xy}{x^2+y^2} = \lim_{(x,y)\rightarrow(0,0)} f(x,y)$

**Def**.:
* [Két út módszer](ket-ut-modszer.md)
* [Parciális derivált](parcialis-derivalt.md)
* [Young tétel](young-tetel.md)
* [Iránymenti derivált](iranymenti-derivalt.md)
* [Érintősík](erintosik.md)
* [Totális derivált](totalis-derivalt.md)

**Áll**.:
$f$ [totálisan diffható](totalis-derivalt.md) $x_0$ pontban és $f'(\vec{x_0})=\vec{A} \Leftrightarrow \lim_{\vec{x} \rightarrow \vec{x_0}}{\frac{f(\vec{x})-f(\vec{x_0}) - \vec{A}(\vec{x}-\vec{x_0})}{|\vec{x}-\vec{x_0|}}} = 0$

**Def**.:
* [Gradiens vektor](gradiens-vektor.md)

**Áll**.:
Tegyük fel, hogy $f$ [totálisan diffható](totalis-derivalt.md) $\vec{x_0}$ pontban $f: \mathbb{R}^p \rightarrow \mathbb{R}$. Ekkor:
    1. $f$ [folytonos](fuggveny-folytonossaga.md) $\vec{x_0}$-ban 
    2. $f$ [iránymenti deriváltjai](iranymenti-derivalt.md) léteznek az $\vec{x_0}$-ban és $f_{\vec{v}}' = \vec{f'}(\vec{x_0}) \cdot \frac{\vec{v}}{|\vec{v}|} = \vec{\nabla} f(\vec{x_0})\frac{\vec{v}}{|\vec{v}|}$
    3. $\vec{f'} = \vec{\nabla} f(x_0)$ [totálisan diffható](totalis-derivalt.md) $f \Rightarrow f$ [parciális deriváltjai](parcialis-derivalt.md) is léteznek.

---

## 3. előadás

**Def**.:
* [Totális differenciálhatóság](totalis-diffhatosag.md)
* [Folytonos differenciálhatóság](folytonos-diffhatosag.md)

**Áll**.: Ha $f$ [differenciálható](totalis-diffhatosag.md) $\vec{x}_0$ akkor:
* $f$ [folytonos](fuggveny-folytonossaga.md) $\vec{x}_0$-ban
* $f$ [parciális deriváltjai](parcialis-derivalt.md) $\exists$-nek, és $\vec{f}'(\vec{x}_0)=^{\text{áll}} \vec{\nabla}f(\vec{x}_0)=^{\text{def}} \left( f'_{x_1}(\vec{x}_0), f'_{x_2}(\vec{x}_0), f'_{x_3}(\vec{x}_0) \right)$ 
* $f$ [iránymenti deriváltjai](iranymenti-derivalt.md) $\exists$-nek, és: $f'_{\vec{v}}(\vec{x}_0)=\vec{\nabla}f(\vec{x}_0)\cdot \frac{\vec{v}}{|\vec{v}|}$, ahol $\vec{v}\in \mathbb{R}^p\setminus \{0\}$

**Áll**.: Ha $f$ [folytonosan differenciálható](folytonos-diffhatosag.md), akkor [totálisan differenciálható](totalis-diffhatosag.md).

**Áll**.: Ha $f$ kétszer [folytonosan diffható](folytonos-diffhatosag.md) akkor $f''_{xy}=f''_{yx}$, ez a [Young tétel](young-tetel.md)
