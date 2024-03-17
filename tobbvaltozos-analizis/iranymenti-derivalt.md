# Iránymenti derivált

Ugyanúgy ahogy a sima [parciális derviáltnál](parcialis-derivalt.md) egy adott $y=y_0$ egyenes mentén néztük úgy egy adott irány mentén is lehet.

## Definíció 2 dimenzióban
Tegyük fel, hogy $\underline{v} \in \mathbb{R}^2$ és $\underline{v} \neq \underline{0}$

Ekkor $f$ $\underline{v}$ irányú deriváltja az $(x_0, y_0)$ pontban 
$$f'_{\underline{v}}(x_0, y_0) = \lim_{t \rightarrow 0}{\frac{f((x_0, y_0) + t \frac{v}{|\underline{v}|}) - f(x_0, y_0)}{t}}$$

Lényegében megnézzük, hogy nagyon kicsit $v$ irányába mozdulunk a függvény [grafikonján](grafikon.md), akkor hogyan változik a függvényérték.

## Definíció $p$ dimenzióban
$f: \mathbb{R}^p \rightarrow \mathbb{R}$
$\underline{v} \in \mathbb{R}^p \backslash \{0\}$

$$f'_{\underline{v}}(\underline{x}_0) = \lim_{t \rightarrow 0}{\frac{f(\underline{x}_0 + t \frac{\underline{v}}{|\underline{v}|}) - f(\underline{x}_0)}{t}}$$

