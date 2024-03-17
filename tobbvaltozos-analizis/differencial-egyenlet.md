# Differenciál egyenlet

[Egész jó segédlet](https://math.bme.hu/~konya/anal2/segedletek/diffegy.pdf)

A differenciálegyenletek olyan egyenletek, ahol az ismeretlen egy [diffható függvény](./totalis-diffhatosag.md) és az egyenlet a függvény és ennek deriváltjai között teremt kapcsolatot

## Típuselnevezések
- elsőrendű: azt jelenti, hogy a keresett függvénynek csak első deriváltja jelenik meg az egyenletben
- közönséges: olyan differenciálegyenlet, ami egy egyváltozós [diffható függvényre](./totalis-diffhatosag.md) van felírva
- explicit: Ha a derivált tag kifejezhető a többi taggal
- [egzakt](#egzakt-diffegyenletek)

## Elsőrendű közönséges explicit diffegyenletek
$y'=f(x,y)$ elsőrendű közönséges explicit [diffegyenlet](differencial-egyenlet.md), ha $f:D\to \mathbb{R}$ [folytonos függvény](fuggveny-folytonossaga.md), ahol $D\subseteq \mathbb{R}^2$ [tartomány](tartomany.md).
Ennek $y:I\to \mathbb{R}$ [diffható függvény](totalis-diffhatosag.md) megoldása, ha $y'(x)=f(x, y(x)),\  \forall x\in I$ ahol $I\in \mathbb{R}$ [nyílt intervallum](nyilt-halmaz.md).

## Szétválasztható változójú diffegyenletek
$y'= f(x) = g(x) \cdot h(x)$, ahol $g$ és $h$ [folytonos függvények](./fuggveny-folytonossaga.md)

### Megoldása
0. Ha $h(y)=0$ gyökei $y_1, y_2, \cdots$ akkor az $y=y_i$ függvény megoldása az egyenletnek, hiszen $y'=(y_i)'=0=h(y_i)$

1. Tegyük fel, hogy $h(y) \neq 0$
$$
\begin{alignat*}{3}
    y' = f(x, y) & = g(x) h(y) \\
    \frac{dy}{dx} &= g(x) h(y) \\
    dy &= g(x)h(y)dx \quad &&/ :h(y) \\
    \frac{1}{h(y)}dy &= g(x)dx \quad &&/ \int\\
    \int \frac{1}{h(y)}dy &= \int g(x)dx \\
    \widetilde{H}(y) &= G(x) + C \quad && (C \in \mathbb{R})
\end{alignat*}
$$
$\widetilde{H}(y)$-ból, meg jó esetben ki lehet fejezni az $y$-t, így megoldva a diffegyenletet.

## Egzakt diffegyenletek
### Definíció 1
$P, Q: \mathbb{R}^2 \rightarrow \mathbb{R}$ adott [folytonosan diffható](./folytonos-diffhatosag.md) függvények. Ekkor a $P(x, y)dx+Q(x,y)dy=0$ diffegyenlet egzakt, ha $\exists F: \mathbb{R}^2 \rightarrow \mathbb{R}$ kétszer [folytonosan diffható](./folytonos-diffhatosag.md), amelyre igaz, hogy $F'_x=P$ és $F'_y=Q$, tehát a [parciális deriváltjai](./parcialis-derivalt.md) megegyeznek $P$-vel és $Q$-val.

$$
\begin{alignat*}{3}
P(x, y)dx+Q(x,y)dy&=0 \quad &&/ :dx\\
P(x, y)+Q(x,y)\frac{dy}{dx}&=0 \\
P(x, y)+Q(x,y)y'(x)&=0 \quad &&/ \text{ ha } Q \neq 0 \\
y'(x) &= - \frac{P(x, y)}{Q(x, y)} \quad && \text{ }
\end{alignat*}
$$
Ezzel egy [explicit diffegyenletet](#elsőrendű-közönséges-explicit-diffegyenletek) kaptunk.

### Definíció 2
**Áll**.: Tfh.: $P, Q: \mathbb{R}^2 \rightarrow \mathbb{R}$ adott [folytonosan diffható](./folytonos-diffhatosag.md) függvények.
Ekkor $P(x, y)dx + Q(x, y)dy=0$ egzakt $\Leftrightarrow$ $P'_y=Q'_x$ $D$-n, feltéve, hogy $D$ [egyszeresen összefüggő tartomány](./egyszeresen-osszefuggo-tartomany.md)
**Biz**.: Csak a $\Rightarrow$ esetet bizonyítjuk
Ha egzakt, akkor $\exists F: \mathbb{R}^2 \rightarrow \mathbb{R}$ kétszer [folytonosan diffható](./folytonos-diffhatosag.md), amelyre $F'_x=P$ és $F'_y=Q$. Ekkor $P'_y=F''_{xy}$ és $Q'_x=F''_{yx}$. $F''_{xy}=F''_{yx}$ a [Young-tétel](./young-tetel.md) miatt.

### Megoldása
Ha $Pdx+Qdy=0$ [egzakt diffegyenlet](egzakt-diffegyenlet.md), és $F'_x=P,\ F'_y=Q$ akkor a [diffegyenlet](differencial-egyenlet.md) általános megoldása $F(x, y(x))=C \in \mathbb{R}$, azaz $F(x, y)$ szintvonalai által meghatározott $y(x)$ függvények.

**Bizonyítás:**
Az állítás feltétele:
$$F'_xdx+F'_ydy=0 \Leftrightarrow F'_x+F'_yy'=0$$
- Lemma: Ha $F:\mathbb{R}^2\to \mathbb{R}$ [totálisan diffható](totalis-diffhatosag.md), akkor $\frac{d}{dx}F(x, y(x))=F'_x+F'_yy'$. Biz.: Láncszabályból: $\frac{d}{dx}F(x(t), y(t))=F'_x\dot{x}+F'_y\dot{y}$

Tehát a diffegyenlet egyenértékű:
$$\frac{d}{dt}F(x, y(x))=0 \Leftrightarrow F(x, y(x))=C\in \mathbb{R}$$

## Majdnem egzakt diffegyenlet megoldása
**Kérdés**
Mi van azonban, ha a [diffegyenlet](./differencial-egyenlet.md) nem [egzakt](./differencial-egyenlet.md#egzakt-diffegyenletek), azaz $P'_y \neq Q'_x$?
[Jó videó a témáról](https://www.youtube.com/watch?v=u5NGfwNNqHw)

**Ötlet**.: Megpróbálunk keresni egy $\varphi (x, y)$ függvényt, úgy, hogy
$\textcolor{orange}{\varphi(x, y) P(x, y)}dx + \textcolor{green}{\varphi(x, y) Q(x,y)}dy = 0$ már egzakt.
$\textcolor{orange}{\widetilde{P}(x, y)}dx + \textcolor{green}{\widetilde{Q}(x,y)}dy = 0$

Tehát kell 
$$
\begin{alignat*}{2}
\widetilde{P}'_y &= \widetilde{Q}'_x \\
\varphi'_y \cdot P + \varphi \cdot P'_y &= \varphi'_x \cdot Q + \varphi \cdot Q'_x
\end{alignat*}
$$
Rossz hír: nehezebb megoldani, mint az eredetit. De [nem adjuk fel](https://www.youtube.com/watch?v=dQw4w9WgXcQ)!
Ötlet: Speciál alakú $\varphi(x, y)$ függvényekkel próbálkozunk.
Pl.: $$
\begin{alignat*}{3}
\varphi(x, y) &= m(x) \\
\varphi(x, y) &= m(y) \\
\varphi(x, y) &= m(x+y) \\ 
\varphi(x, y) &= m(xy) \\
\varphi(x, y) &= m(\frac{x}{y}) \\
\varphi(x, y) &= m(x^2+y^2) \\
\end{alignat*}
$$
Itt $m: \mathbb{R} \rightarrow \mathbb{R}$

**Áll**.: Tfh. $P, Q: \mathbb{R}^2 \rightarrow \mathbb{R}$ [folytonosan diffható](./folytonos-diffhatosag.md) egy $D \subseteq \mathbb{R}^2$ [egyszeresen összefüggő tartományon](./egyszeresen-osszefuggo-tartomany.md). Tfh. $P \neq 0$ $D$-n.
Ekkor $m(y)$ csak $y$-tól függő **integráló tényező** a $Pdx + Qdy = 0$ [diffegyenlethez](./differencial-egyenlet.md) $D$-n:
$\frac{Q'_x-P'_y}{P}dy$ csak $y$-tól függ, és $=m(y)=e^{\int{\frac{Q'_x-P'_y}{P}dy}}$

**Biz**.:
Ahhoz, hogy a $\varphi(x, y) P(x, y)dx + \varphi(x, y) Q(x,y)dy = 0$ [egzakt](#egzakt-diffegyenletek) legyen szükséges: $(m(y) P(x, y)dx)'_y = (m(y) Q(x,y)dy)'_x$
$$
\begin{alignat*}{3}
(m(y) P(x, y))'_y &= (m(y) Q(x,y))'_x \\
m(y)' P + m(y) P'_y &= m(y) Q'_x \\
m(y)' P &= m(y) (Q'_x - P'_y) \\
\frac{m(y)'}{m(y)} &= \frac{Q'_x - P'_y}{P}
\end{alignat*}
$$
Ha ez csak $y$-tól függő kifejezés, akkor

$$
\begin{alignat*}{3}
\frac{m(y)'}{m(y)} &= \frac{Q'_x - P'_y}{P} \\
\frac{1}{m} \frac{dm}{dy} &= \frac{Q'_x - P'_y}{P} \\
\int{\frac{1}{m} {dm}} &= \int{\frac{Q'_x - P'_y}{P}dy} \\
\ln|m| &= \int{\frac{Q'_x - P'_y}{P}dy} \\
m &= e^{\int{\frac{Q'_x - P'_y}{P}dy}}
\end{alignat*}
$$

