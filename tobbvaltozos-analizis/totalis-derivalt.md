# Totális derivált (derivált)

## 1 dimenzióban

### Definíció 1
$A \in \mathbb{R}=f'(x_0) = \lim_{x \rightarrow x_0}{\frac{f(x)-f(x_0)}{x-x_0}}$

### Definíció 2
$A \in \mathbb{R} = f'(x_0)  \Leftrightarrow \frac{f(x)-f(x_0)}{x - x_0} - A = \varepsilon(x) \rightarrow 0$

## Több dimenzióban

$f: \mathbb{R}^p \rightarrow \mathbb{R}$ függvény totálisan diffható $\vec{x_0} \in \mathbb{R}^p$ pontban, ha $\exists \vec{A} \in \mathbb{R}^p, \varepsilon: \mathbb{R}^p \rightarrow \mathbb{R} : \lim_{\vec{x} \rightarrow \vec{x_0}}{\varepsilon(\vec{x})}=0$ és létezik $f(\vec{x}) = f(\vec{x_0}) + \vec{A} \cdot (\vec{x}-\vec{x_0}) + \varepsilon(\vec{x}) |\vec{x}-\vec{x_0}|, \forall x \in D_f$
Ekkor $\vec{f'}(\vec{x_0}) := \vec{A}$