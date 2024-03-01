# Iránymenti derivált

Ugyanúgy ahogy a sima [parciális derviáltnál](parcialis-derivalt.md) egy adott $y=y_0$ egyenes mentén néztük úgy egy adott irány mentén is lehet.

## Definíció 2 dimenzióban
Tegyük fel, hogy $\vec{v} \in \mathbb{R}^2$ és $\vec{v} \neq \vec{0}$

Ekkor $f$ $\vec{v}$ irányú deriváltja az $(x_0, y_0)$ pontban 
$$f'_{\vec{v}}(x_0, y_0) = \lim_{t \rightarrow 0}{\frac{f((x_0, y_0) + t \frac{v}{|\vec{v}|}) - f(x_0, y_0)}{t}}$$

Lényegében megnézzük, hogy nagyon kicsit $v$ irányába mozdulunk a függvény [grafikonján](grafikon.md), akkor hogyan változik a függvényérték.

## Definíció $p$ dimenzióban
$f: \mathbb{R}^p \rightarrow \mathbb{R}$
$\vec{v} \in \mathbb{R}^p \backslash \{0\}$

$$f'_{\vec{v}}(\vec{x_0}) = \lim_{t \rightarrow 0}{\frac{f(\vec{x_0} + t \frac{v}{|\vec{v}|}) - f(\vec{x_0})}{t}}$$

## Állítás
$f_{c\vec{v}}' = f_{\vec{v}}'$, ha $c > 0$

