# Rotáció

Tegyük fel, hogy $\underline{v} : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ [totálisan diffható](./totalis-diffhatosag.md) és $\underline{v}'(\underline{r}) = D\underline{v}$.
Ekkor 
$
\begin{aligned}
    \text{rot } \mathbf{v}(\mathbf{r}) &= (\nabla \times \mathbf{v})(\mathbf{r}) = 
    \begin{vmatrix}
        \hat{\imath} & \hat{\jmath} & \hat{k} \\
        \partial_1 & \partial_2 & \partial_3 \\
        v_1 & v_2 & v_3 
    \end{vmatrix} 
    &= \begin{pmatrix}
        \partial_2 v_3 - \partial_3 v_2 \\
        \partial_3 v_1 - \partial_1 v_3 \\
        \partial_1 v_2 - \partial_2 v_1
    \end{pmatrix}
\end{aligned}$

## Rotáció koorsz. fgtlen értelmezése

Tfh: \( v : \mathbb{R}^3 \to \mathbb{R}^3 \) folyt diffható.

Legyen \( |n| = 1 \), \(\gamma_{n,\varepsilon}\), \( r_0 \) középpontú, \(\varepsilon\) sugarú körvonal \( n \) a körlap síkjának normálisa.

Ekkor \( \oint_{\gamma_{n,\varepsilon}} v \, d\mathbf{r} = \iint_{F_{n,\varepsilon}} \text{rot} \mathbf{v} \, dA \)

Ekkor \( n \cdot \text{rot} \mathbf{v}(r_0) = \lim_{\varepsilon \to 0} \frac{\iint_{F_{n,\varepsilon}} \text{rot} \mathbf{v} \, dA}{\varepsilon^2 \pi} = \lim_{\varepsilon \to 0} \frac{\oint_{\gamma_{n,\varepsilon}} v \, d\mathbf{r}}{\varepsilon^2 \pi} \)


ugyanis: \( n \cdot \text{rot} \mathbf{v}(r_0) = \lim_{\varepsilon \to 0} \frac{\iint_{F_{n,\varepsilon}} \text{rot} \mathbf{v} \cdot n \, dA}{\varepsilon^2 \pi} \) integrálás középérték tétele 2 dim-ban.

Amilyen \( n \)-re max, arra mutat \(\text{rot}\mathbf{v}\).
