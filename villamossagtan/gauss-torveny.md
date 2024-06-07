# Gauss törvény

**Fizikai értelme**: az elektrosztatikus tér forrásai a nyugvó villamos töltések
**Matematikai formula** diszkrét töltéseloszlás esetén:
$$\oint_A \textbf{D} d \textbf{A} = \sum_{i=1}^n Q_i$$

$A$ : tetszőleges, zárt felület
$Q_i$ : az A felület által behatárolt térfogatban lévő töltések.

**Matematikai formula** folytonos töltéseloszlás esetén:
$$\oint_A \textbf{D} d \textbf{A} = \int_V \rho_V dV$$

$A$ : tetszőleges, zárt felület
$V$ : az $A$ által határolt térfogat
$\rho_V$ : a térfogati töltéssűrűség (a térfogategységben található töltésmennyiség)

**Matematikai formula** differenciális alak:
$$div \textbf{D} = \boldsymbol{\nabla} \cdot \textbf{D} = \frac{\partial{D_x}}{\partial x} + \frac{\partial{D_y}}{\partial y} + \frac{\partial{D_z}}{\partial z} = \rho_V$$

$\textbf{D}$ : [eltolási vektor](./eltolasi-vektor.md)
$div \textbf{D}$ : $\textbf{D}$ [divergenciája](../tobbvaltozos-analizis/divergencia.md)

**Szemléletesen**:
Egy tartományból kilépő [fluxus](./villamos-ter-fluxusa.md) - tehát az [erővonalak](./villamos-erovonal.md) száma - az ott levő töltésekkel arányos.