# Ezt majd szét kell szedni ezt a doksit

### DEF: Elsőrendű közönséges explicit diffegyenlet
$y'=f(x,y)$ elsőrendű közönséges explicit [diffegyenlet](differencial-egyenlet.md), ha $f:D\to \mathbb{R}$ [folytonos függvény](fuggveny-folytonossaga.md), ahol $D\subseteq \mathbb{R}^2$ [tartomány](tartomany.md)
Ennek $y:I\to \mathbb{R}$ [diffható függvény](totalis-diffhatosag.md) megoldása, ha $y'(x)=f(x, y(x)),\  \forall x\in I$ ahol $I\in \mathbb{R}$ [nyílt intervallum](nyilt-halmaz.md).

### Példa
Tfh $f(x, y)=-\frac{P(x,y)}{Q(x,y)}$. Tfh $D\subseteq\mathbb{R}^2$ [tartományon](tartomany.md) $Q\neq0$. Ekkor:
$$y'=-\frac{P(x,y)}{Q(x,y)} \newline
Qy'=-P \newline
P+qy'=0 \newline
P+Q\frac{dy}{dx}=0
$$
Azaz formálisan átírva:
$$Pdx+Qdy=0 $$

### DEF: Egzakt diffegyenlet
$Pdx+Qdy=0$ Egzakt diffegyenlet, ha $\exists F:D\to \mathbb{R}$ kétszer [folytonosan diffható](folytonos-diffhatosag.md) függvény: $F'_x=P,\ F'_y=Q$ a $D\subseteq \mathbb{R}^2$ [tartományon](tartomany.md).

### Állítás
Ha $Pdx+Qdy=0$ [egzakt diffegyenlet](egzakt-diffegyenlet.md), és $F'_x=P,\ F'_y=Q$ akkor a [diffegyenlet](differencial-egyenlet.md) általános megoldása $F(x, y(x))=C \in \mathbb{R}$, azaz $F(x, y)$ szintvonalai által meghatározott $y(x)$ függvények.

### Bizonyítás
Az állítás feltétele:
$$F'_xdx+F'_ydy=0 \Leftrightarrow F'_x+F'_yy'=0$$
- Lemma: Ha $F:\mathbb{R}^2\to \mathbb{R}$ [totálisan diffható](totalis-diffhatosag.md), akkor $\frac{d}{dx}F(x, y(x))=F'_x+F'_yy'$. Biz.: Láncszabályból: $\frac{d}{dx}F(x(t), y(t))=F'_x\dot{x}+F'_y\dot{y}$

Tehát a diffegyenlet egyenértékű:
$$\frac{d}{dt}F(x, y(x))=0 \Leftrightarrow F(x, y(x))=C\in \mathbb{R}$$