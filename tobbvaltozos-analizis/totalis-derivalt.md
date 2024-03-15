# Totális derivált (derivált)

## Emlékeztető: 1 dimenzióban

### Definíció 1
$$A \in \mathbb{R}=f'(x_0) = \lim_{x \rightarrow x_0}{\frac{f(x)-f(x_0)}{x-x_0}}$$

### Definíció 2
$$A \in \mathbb{R} = f'(x_0)  \Leftrightarrow \frac{f(x)-f(x_0)}{x - x_0} - A = \varepsilon(x) \rightarrow 0$$

## Több dimenzióban

$f: \mathbb{R}^p \rightarrow \mathbb{R}$ függvény totálisan differenciálható $\vec{x_0} \in \mathbb{R}^p$ pontban, ha 
$$\exists \vec{A} \in \mathbb{R}^p, \varepsilon: \mathbb{R}^p \rightarrow \mathbb{R}, \lim_{\vec{x} \rightarrow \vec{x_0}}{\varepsilon(\vec{x})}=0 \newline f(\vec{x}) = f(\vec{x_0}) + \vec{A} \cdot (\vec{x}-\vec{x_0}) + \varepsilon(\vec{x}) |\vec{x}-\vec{x_0}|, \forall x \in D_f$$
Ekkor: $$\vec{f'}(\vec{x_0}) := \vec{A}$$

## Egyenértékű definíció
Az $f'(\vec{x}_0)=\vec{A}$ állítás egyenértékű a következővel:
$$\lim_{\vec{x}\to \vec{x}_0} \frac{f(\vec{x})-f(\vec{x}_0)-\vec{A}\cdot(\vec{x}- \vec{x}_0)}{|\vec{x}- \vec{x}_0|}=0=\lim_{\vec{x}\to \vec{x}_0}\varepsilon(\vec{x})$$

### Feltételei

* $f$ [folytonos](./fuggveny-folytonossaga.md) $\vec{x_0}$-ban
* $f$ [parciális deriváltjai](./parcialis-derivalt.md) léteznek $\vec{x_0}$-ban
* Definíció szerinti határérték létezik és megfelel

## Szemléletesebb magyarázat

A totális derivált lényegében a függvény [érintősíkját](erintosik.md) írja le. Ahogy 1 dimenzióban a derivált a legjobb lináris közelítés volt, úgy több dimenzióban a totális derivált a legjobb lineáris közelítés.


