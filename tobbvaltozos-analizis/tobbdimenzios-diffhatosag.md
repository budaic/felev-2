# Többdimenziós diffhatóság

## Definíció 1
$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ függvény differenciálható, az $\vec{a} \in \text{int} D_f$ pontban ($\text{int} D_f$ a [belső pontok halmaza](./belso-pont.md)), ha $\exists A: \mathbb{R}^n \rightarrow \mathbb{R}^m$ [lineáris leképezés](./linearis-lekepezes.md) és $\vec{\varepsilon}: \mathbb{R}^n \rightarrow \mathbb{R}^m$ leképezés, amelyre $\lim_{\vec{x} \rightarrow \vec{a}}{\vec{\varepsilon} (\vec{x})} = \vec{0}$, és $\vec{f}(\vec{x}) = \vec{f}(\vec{a}) + A(\vec{x}-\vec{a}) + \vec{\varepsilon}(\vec{x})|\vec{x} - \vec{a}|$ $\forall \vec{x} \in D_f$. Ekkor $\vec{f}'(\vec{a}) = A$


## Definíció 2
$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ függvény differenciálható, az $\vec{a} \in \text{int} D_f$ pontban, ha $\underline{\underline{A}} \in \mathbb{R}^{m \times n}, \varepsilon$

$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ függvény differenciálható, az $\vec{a} \in \text{int} D_f$ pontban ($\text{int} D_f$ a [belső pontok halmaza](./belso-pont.md)), ha $\underline{\underline{A}} \in \mathbb{R}^{m \times n}$  mátrix és $\vec{\varepsilon}: \mathbb{R}^n \rightarrow \mathbb{R}^m$ leképezés, amelyre $\lim_{\vec{x} \rightarrow \vec{a}}{\vec{\varepsilon} (\vec{x})} = \vec{0}$, és $\vec{f}(\vec{x}) = \vec{f}(\vec{a}) + \underline{\underline{A}}(\vec{x}-\vec{a}) + \vec{\varepsilon}(\vec{x})|\vec{x} - \vec{a}|$ $\forall \vec{x} \in D_f$. Ekkor $\vec{f}'(\vec{a}) = A$
 (standard bázisban)

