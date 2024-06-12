# Kapacitás

A kapacitás (C) vezető elrendezés töltéstároló képességét jellemzi.
$$V = V - V (\infty) = \int_P^\infty \textbf{E} d \textbf{l} \sim Q$$ 
$$V = \frac{1}{C} Q$$

**Jele**: C
**Mértékegysége**: [C] = farad = F = $\frac{C}{V}$

![alt text](./img/kapacitas.png)

## Mint áramköri elem
Villamos energiát tárol elektromos tér formájában.
Alkalmazása (kondenzátor): áramkörök feszültség- és áramviszonyainak beállítása váltakozóáramúesetben, villamos energia tárolás (szuperkapacitás), egyenáramú komponens leválasztásaváltakozóáramú jelről, meddő kompenzáció motoroknál, szűrő áramkörökben, híradástechnikában, stb.
Koncentrált paraméterű áramköri jelei:
![alt text](./img/kapacitas2.png)

**Feszültség-áram karakterisztikája tetszőleges időfüggő esetben**:
Egyenáramú esetben szakadás.
$$i = C \frac{du}{dt}$$

Ez a [differenciálegyenlet](../tobbvaltozos-analizis/differencial-egyenlet.html) szinuszos táplású esetben a [komplex időfüggvény](./komplex-idofuggveny.md) alkalmazásával lineárissá válik:

\[
\bm{i} = C \frac{d\bm{u}}{dt}
\]

A $\frac{d}{dt} = j\omega$ helyettesítéssel élve
\[
\bm{i} = j\omega C \bm{u}
\]

\[
\bm{u} = -\frac{j}{\omega C} \bm{i}
\]

[impedancia](./impedancia.md): $\bm{Z_C} = -\frac{j}{C \omega}$
[reaktancia](./reaktancia.md): $\bm{X_C} = \frac{1}{C \omega}$
[admittancia](./admittancia.md): $\bm{Y_C} = \frac{1}{\bm{Z_C}} = jC\omega$

![Vektorábrája](./vektorabra.md#kapacitás-vektorábrája)
