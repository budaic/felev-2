# L'Hospital

## L'H $\frac{0}{0}$ 
Tegyük fel, hogy $f$ és $g$ diffható és $g, g' \neq 0$ $b \in \mathbb{R}$ pont egy környezetében, kivéve esetleg $b$-ben, és $\lim_{x \to b}f(x)=\lim_{x \to b}g(x)=0$ és $\lim_{x \to b}\frac{f'(x)}{g'(x)}$ létezik (véges, vagy végtelen is lehet). Ekkor $\lim_{x \to b}\frac{f(x)}{g(x)} = \lim_{x \to b}\frac{f'(x)}{g'(x)}$.
### Bizonyítás
[Cauchy-tétel](cauchy-tetel.md) segítségével bal és jobb határértékkel

## L'H $\frac{\infty}{\infty}$ 
Tegyük fel, hogy $f$ és $g$ diffható és $g, g' \neq 0$ $b \in \mathbb{R}$ pont egy környezetében, kivéve esetleg $b$-ben, és $\lim_{x \to b}|f(x)|=\lim_{x \to b}|g(x)|=\infty$ és $\lim_{x \to b}\frac{f'(x)}{g'(x)}$ létezik (véges, vagy végtelen is lehet). Ekkor $\lim_{x \to b}\frac{f(x)}{g(x)} = \lim_{x \to b}\frac{f'(x)}{g'(x)}$.

### Bizonyítás
[Jól elmondja](https://www.youtube.com/watch?v=Vx56JfwE5U8&ab_channel=MichaelPenn)
[Cauchy-tétel](cauchy-tetel.md)
NEM lehet az első bizonyítás segítségével csak reciprokokat venni és úgy bizonyítani, mert akkor fel kéne tenni azt is, hogy $\lim_{x \to b}\frac{f(x)}{g(x)}$ létezik és véges, amit nem tehetünk meg.
![[img/Pasted image 20240108130230.png]]
![[img/Pasted image 20240108130249.png]]
![[img/Pasted image 20240108130305.png]]
## L'H $\rightarrow \infty$ $\frac{0}{0}$ 

## Bizonyítás
Itt már működik a reciprokvételes helyettesítés
![[img/Pasted image 20240108133321.png]]
