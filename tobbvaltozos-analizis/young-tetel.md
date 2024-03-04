# Young-tétel

## Állítás

Ha $f$ kétszer [folytonosan diffható](folytonos-diffhatosag.md) (a deriváltja is [diffható](totalis-diffhatosag.md)) akkor $f''_{xy}=f''_{yx}$

### Eml.: Taylor polinom
$$T_n(x)=\sum_{i=0}^n{\frac{f^{(n)}(a)}{n!}(x-a)^n}$$

### Eml.: Lagrange maradéktag
Egy adott Taylor-polinom esetén:
$$f(x)=T_n(x)+R_n(x) = f(x_0)+(x-x_0)f'(x_0)+\frac{(x-x_0)^2}{2!}f''(x_0)+\cdots+\frac{(x-x_0)^n}{n!}f^{(n)}(x_0)+R_n$$
Ahol $R_n$ a Lagrange maradéktag. Ilyenkor létezik egy olyan $\tilde{x}$ $x_0$ és $x$ között, hogy a következő kifejezés igaz legyen:
$$R_n(x) = \frac{f^{(n+1)}(\tilde{x})}{(n+1)!}(x-x_0)^{n+1}$$

Tehát $n=1$-re fel lehet írni a következőt:
$$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{1}{2}f''(\tilde{x})(x-x_0)^2$$
$$f(x)-f(x_0)-f'(x_0)(x-x_0)=\frac{1}{2}f''(\tilde{x})(x-x_0)^2$$

## Bizonyítás

$$G(t)=\frac{1}{t^2}\left(\boxed{\textcolor{purple}{[f(x+t, y+t)-f(x,y+t)]}} - \boxed{\textcolor{green}{[f(x+t, y)-f(x, y)]}} \right)$$

$$\boxed{\textcolor{purple}{f(x+t, y+t)-f(x,y+t)}} = g(x+t)-g(x)=g'(x)(x+t-x)+\frac{1}{2}g''(\tilde{x})(x+t-x)^2=\boxed{\textcolor{purple}{f'_x(x, y+t)t+\frac{1}{2}f''_{xx}(\tilde{x}, y+t)t^2}}$$

$$f(x, y+t) := g(x) \newline
f'_x(x, y+t)=g'(x) \newline
f''_x(x, y+t)=g''(x)$$

Hasonlóan:
$$\boxed{\textcolor{green}{f(x+t, y)-f(x, y)}}=\boxed{\textcolor{green}{f'_x(x, y)t+\frac{1}{2}f''_{xx}(\tilde{\tilde{x}}, y)t^2}}$$

Feltéve, hogy $(x, y)$ fix
$$G(t)=\frac{\textcolor{purple}{f'_x(x,y+t)}-\textcolor{green}{f'_x(x,y)}}{t} + \frac{1}{2}\left(\textcolor{purple}{f''_{xx}(\tilde{x}, y+t)} - \textcolor{green}{f''_{xx}(\tilde{\tilde{x}}, y)} \right)$$

A [Lagrange-tételt](../analizis/lagrange-tetel.md) felhasználva:
$$g(y)=f'_x(x, y)$$
$$\frac{g(y+t)-g(y)}{t}=g'(\tilde{y})=\textcolor{orange}{f''_{xy}(x, \tilde{y})}$$


Ezt visszahelyettesítve
$$G(t)=\textcolor{orange}{f''_{xy}(x, \tilde{y})} + \frac{1}{2}\left(\textcolor{purple}{f''_{xx}(\tilde{x}, y+t)} - \textcolor{green}{f''_{xx}(\tilde{\tilde{x}}, y)} \right)$$

$$\lim_{t \rightarrow 0}G(t) = f''_{xy}(x, y)$$
Mivel 
$$\lim_{t \rightarrow 0}\frac{1}{2}\left(\textcolor{purple}{f''_{xx}(\tilde{x}, y+t)} - \textcolor{green}{f''_{xx}(\tilde{\tilde{x}}, y)} \right) = 0$$
Azért tart $0$-ba, mert mind $\tilde{x}$, mind $\tilde{\tilde{x}}$ az $x$ és $x+t$ közötti intervallumon helyezkednek el, így, ahogy $t$ tart $0$-ba úgy tartanak $x$-be.



Vegyük észre, hogy:
$$G(t)=\frac{1}{t^2}\left([f(x+t, y+t)-f(x+t,y)] -[f(x, y+t)-f(x, y)] \right)$$
Így a $G(t)$ függvényt nem változtattuk, azonban az $x$ és az $y$ szerepe felcserélődött így, ahogy $t \rightarrow 0$ úgy $G(t) \rightarrow f''_{yx}(x, y)$, ami így egyenlő kell leyen $f''_{xy}(x, y)$-al. Ezzel az állítást beláttuk.