# Teljesítményfajták szinuszos hálózatokban

Emlékeztető: [teljesítmény](./teljesitmeny.md)

## Pillanatérték teljesítmény
**Jele**: p
Az áram és a feszültség pillanatértékeinek szorzata, mely időben változik. $p = ui$
**Mértékegysége**: watt (W)

## Komplex teljesítmény
**Jele**: $\bm{S}$
$\bm{S} = \bm{U}\bm{I^*} = I^2\bm{Z} = \frac{U^2}{\bm{Z*}}$
**Mértékegysége** volt-amper (VA)

## Hatásos teljesítmény
**Jele**: P
A pillanatérték preiódusidőre vett átlaga, ez az a teljesítmény, amit a villamos berendezés átlagosan elfogyaszt, ezt méri a villanyóra is.
Bizonyítható, hogy $P=\text{Re}(\bm{S})$, mely akár valós függvényes alakba is írható: $P=UIcos(\varphi_Z)$. 
**Mértékegysége**: watt (W).
Tiszta ohmos fogyasztó esetén a komplex teljesítménynek csak valós része van, tehát $P=UI=S$, a teljes betáplált villamos teljesítmény elfogyasztásra kerül. Amennyiben a fogyasztónk tisztán reaktív (induktív, vagy kapacitív), akkor a komplex teljesítmény csak képzetes résszel rendelkezik, $P=0$. Reaktív áramköri elem átlagban nem fogyaszt, egyik félperiódusban energiát vesz fel (fogyasztó), amit a másik féperiódusban visszatáplál a hálózatba (termelő).

## Meddő teljesítmény
**Jele**: $Q$
A reaktív áramköri elemek teljesítményviszonyainak jellemzésére szolgál. A hálózatból felvett, vagy annak visszaadott teljesítmény maximumával egyezik meg.
Bizonyítható, hogy $Q=\text{Im}(\bm{S})$, mely akár valós függvényes alakba is írható: $Q = UI\sin(\varphi_Z)$.
**Mértékegysége**: volt-amper-reaktív (var)
A meddő teljesítmény induktív esetben pozitív, kapacitív esetben negatív.
Tiszta ohmos fogyasztó esetén a komplex teljesítménynek csak valós része van, tehát $Q=0$. Amennyiben a fogyasztónk tisztán reaktív (induktív, vagy kapacitív), akkor a komplex teljesítmény csak képzetes résszel rendelkezik, melynek nagysága, $Q=UI=S$

## Látszólagos teljesítmény
**Jele**: $S$
A komplex teljesítmény abszolút értéke, $S=UI$.
**Mértékegysége**: volt-amper (VA)
Ez az a teljesítmény, amire a berendezést (vezetékeket) méretezni kell, mert a vezetékeket mind az átlagban elfogyasztott, mind pedig a reaktív komponensek által időszakosan felvett/visszaadott teljesítményeknek megfelelő áramok egyaránt terhelik.


## Teljesítményfajták közötti összefüggés
$$S^2 = P^2+Q^2$$
Vektorábrán Pithagorasz tétel szerint látszik.

## Teljesítménytényező
$\cos(\varphi_Z)$
Megmutatja, mennyire reaktív, vagy ohmos a fogasztónk. Tiszta ohmos esetben $\cos(\varphi_Z) = 1$, tiszta reaktív esetben pedig, $\cos(\varphi_Z) = 0$
Az áramszolgáltató nem szereti, ha a teljesítménytényező kisebb, mint az 1-hez közeli érték, mert habár a reaktív komponens átlagban nem fogyaszt, a villanyóra azt nem méri, de az időszakos energia kivétel/visszaadás időszakosan terheli a hálózatot.
Ha egy berendezés [impedanciája](./impedancia.md) nem tiszta ohmos (villanymotorok esetén induktív jellegű), meddő kompenzációt alkalmaznak a meddő teljesítmény-komponens kinullázására, így a teljesítménytényező 1 körüli érték lesz. Induktív jellegű esetben például kapacitás beiktatásával lehet ezt elérni.