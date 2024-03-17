# Totális derivált (derivált)

## Emlékeztető: 1 dimenzióban

### Definíció 1
$$A \in \mathbb{R}=f'(x_0) = \lim_{x \rightarrow x_0}{\frac{f(x)-f(x_0)}{x-x_0}}$$

### Definíció 2
$$A \in \mathbb{R} = f'(x_0)  \Leftrightarrow \frac{f(x)-f(x_0)}{x - x_0} - A = \varepsilon(x) \rightarrow 0$$

## Több dimenzióban

$f: \mathbb{R}^p \rightarrow \mathbb{R}$ függvény totálisan differenciálható $\underline{x}_0 \in \mathbb{R}^p$ pontban, ha 
$$\exists \underline{A} \in \mathbb{R}^p, \varepsilon: \mathbb{R}^p \rightarrow \mathbb{R}, \lim_{\underline{x} \rightarrow \underline{x}_0}{\varepsilon(\underline{x})}=0 \newline f(\underline{x}) = f(\underline{x}_0) + \underline{A} \cdot (\underline{x}-\underline{x}_0) + \varepsilon(\underline{x}) |\underline{x}-\underline{x}_0|, \forall x \in D_f$$
Ekkor: $$\underline{f'}(\underline{x}_0) := \underline{A}$$

## Egyenértékű definíció
Az $f'(\underline{x}_0)=\underline{A}$ állítás egyenértékű a következővel:
$$\lim_{\underline{x}\to \underline{x}_0} \frac{f(\underline{x})-f(\underline{x}_0)-\underline{A}\cdot(\underline{x}- \underline{x}_0)}{|\underline{x}- \underline{x}_0|}=0=\lim_{\underline{x}\to \underline{x}_0}\varepsilon(\underline{x})$$

### Feltételei

* $f$ [folytonos](./fuggveny-folytonossaga.md) $\underline{x}_0$-ban
* $f$ [parciális deriváltjai](./parcialis-derivalt.md) léteznek $\underline{x}_0$-ban
* Definíció szerinti határérték létezik és megfelel

## Szemléletesebb magyarázat

A totális derivált lényegében a függvény [érintősíkját](erintosik.md) írja le. Ahogy 1 dimenzióban a derivált a legjobb lináris közelítés volt, úgy több dimenzióban a totális derivált a legjobb lineáris közelítés.


