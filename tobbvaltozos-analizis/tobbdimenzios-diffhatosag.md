# Többdimenziós diffhatóság

## Definíció 1
$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ függvény differenciálható, az $\underline{a} \in \text{int} D_f$ pontban ($\text{int} D_f$ a [belső pontok halmaza](./belso-pont.md)), ha $\exists A: \mathbb{R}^n \rightarrow \mathbb{R}^m$ [lineáris leképezés](./linearis-lekepezes.md) és $\underline{\varepsilon}: \mathbb{R}^n \rightarrow \mathbb{R}^m$ leképezés, amelyre $\lim_{\underline{x} \rightarrow \underline{a}}{\underline{\varepsilon} (\underline{x})} = \underline{0}$, és $\underline{f}(\underline{x}) = \underline{f}(\underline{a}) + A(\underline{x}-\underline{a}) + \underline{\varepsilon}(\underline{x})|\underline{x} - \underline{a}|$ $\forall \underline{x} \in D_f$. Ekkor $\underline{f}'(\underline{a}) = A$


## Definíció 2
$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ függvény differenciálható, az $\underline{a} \in \text{int} D_f$ pontban, ha $\underline{\underline{A}} \in \mathbb{R}^{m \times n}, \varepsilon$

$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ függvény differenciálható, az $\underline{a} \in \text{int} D_f$ pontban ($\text{int} D_f$ a [belső pontok halmaza](./belso-pont.md)), ha $\underline{\underline{A}} \in \mathbb{R}^{m \times n}$  mátrix és $\underline{\varepsilon}: \mathbb{R}^n \rightarrow \mathbb{R}^m$ leképezés, amelyre $\lim_{\underline{x} \rightarrow \underline{a}}{\underline{\varepsilon} (\underline{x})} = \underline{0}$, és $\underline{f}(\underline{x}) = \underline{f}(\underline{a}) + \underline{\underline{A}}(\underline{x}-\underline{a}) + \underline{\varepsilon}(\underline{x})|\underline{x} - \underline{a}|$ $\forall \underline{x} \in D_f$. Ekkor $\underline{f}'(\underline{a}) = A$
 (standard bázisban)

