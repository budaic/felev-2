# 1. Labor

## Mérési feladatok megoldása

### Felkészülési kérdések
1. **Mi a kombinációs hálózat definíciója?**
[Kombinációs hálózat](./kombinacios-halozat.md)

2. **Hány lehetséges függvény állítható elő n bemeneti változó esetén?**
Talán $2^{2^n}$

3. **Adja meg a DeMorgan azonosságokat 2 változó esetére.**
[De Morgan azonosságok](../analizis/de-morgan-azonossagok.md)

4. **Mit jelent az, hogy egy bemenet ponált vagy negált?**
[ponált](./ponalt.md), [negált](./negalt.md)

5. **Mit jelent az, hogy egy bemenet vagy kimenet aktív 0 vagy aktív 1 szintű? Hogyan látható ez a jel megnevezéséből?**
[aktív szint](./aktiv-szint.md), talán van egy vonás felette (negálás jele)

6. **Írja fel a 2-bemenetű ÉS, VAGY és KIZÁRÓ VAGY kapuk igazságtáblázatát.**
[és](./logikai-es.md), [vagy](./logikai-vagy.md), [kizáró vagy](./logikai-kizaro-vagy.md)


7. **Hogyan rendelhetők hozzá a logikai szintek az egyes feszültségszintekhez?**
A logikai 1 a magasabb feszültségszintnek felel meg, a logikai 0 az alacsonyabbnak.

8. **Hogyan valósítható meg egy [inverter](./logikai-nem.md) egy [NEMÉS](./nemes.md) vagy egy [NEMVAGY](./nemvagy.md) kapuból?**
Mindkét kapunál a két bemenetre ugyanazt kötjük és így egy [invertert](./logikai-nem.md) kapunk.


9. **Mi az összefüggés az ANTIVALENCIA (KIZÁRÓ VAGY) és EKVIVALENCIA függvény között. Igazolja állítását.**
Egymás [negáltjai](./negalt.md). 
[Kizáró vagy](./logikai-kizaro-vagy.md): $\overline{A}B + A\overline{B}$
Ekvivalencia: $AB + \overline{A} \cdot \overline{B}$
Kizáró vagy [negálva](./negalt.md): $\overline{\overline{A}B + A\overline{B}}$
Ha ezt a [De Morgan azonosságot](../analizis/de-morgan-azonossagok.md) felhasználva kibontjuk: $\overline{\overline{A}B} \cdot \overline{A\overline{B}} = (\overline{\overline{A}} + \overline{B}) \cdot (\overline{A} + \overline{\overline{B}})$. Most a disztributivitást használjuk ki: $A\overline{A} + \overline{B}\cdot\overline{A}+AB+\overline{B}B$. Mivel a [Boole-algebra axiómáiból](boole-algebra-axiomai.md) következik, hogy bármilyen logikai változó vagy igaz, vagy hamis, ezért $A\overline{A}$ és $\overline{B}{B}$ mindenképp hamis. Így marad $\overline{B} \cdot \overline{A} + AB$, ami pont az ekvivalencia.

10. **Mi a funkciója egy kódoló áramkörnek. Milyen jellegű bemenetei és kimenetei vannak?**
A dekóderrel éppen ellentétesen működik a kódoló áramkör, melynek bemenetei közül csak egy aktív és a kimenetein az aktív bemenetnek megfelelő binárisan kódolt érték nyerhető.

11. **Hány bit szükséges ahhoz, ha nemcsak számjegyeket, hanem betűket és írásjeleket is kódolni kívánunk?**
8 bit

12. **Mi a funkciója egy dekódoló áramkörnek. Milyen jellegű bemenetei és kimenetei vannak?**
A dekódoló áramkörök bemenetére bináris információ érkezik, míg a kimenetén csak bemeneti bináris értéknek megfelelő sorszámú kimeneten jelenik meg aktív jel, aktív érték. Az aktív 1 kimenetű változatnál az adott kimenet 1 értékű, ha a bemeneten az adott kimenet indexének (sorszámának) megfelelő érték van és 0, ha ez nem teljesül, míg az aktív 0 kimenetű változatnál az adott kimenet 0 értékű, ha a bemeneten az adott kimenet indexének (sorszámának) megfelelő érték van és 1, ha ez nem teljesül. Minden más kimenet ilyenkor inaktív (előző esetben 0, míg utóbbi esetben 1). A 22. ábra egy aktív 1 kimenetű „1 a 4-ből” (4 lehetséges bemeneti kombináció és mindig 1 aktív értékű kimenet) dekódoló áramkört és igazság táblázatát mutatja be (bemenetek: $I_0$-$I_1$,  kimenetek: $O_0$-$O_3$).

13. **Mondjon példát átkódoló áramkörre. Nevezze meg a bemeneteit és a kimeneteit.**
A gyakorlatban előfordul még az itt fel nem tüntetett ú.n átkódoló áramkör is, melynek mind bemenete, mind kimenete 4-bites bináris kód.  Ilyen lehet például egy NBCD - "3-többletes Gray kód" konverter (átkódoló), melynek bemenetére az NBCD kódnak megfelelő kódok érkeznek, míg minden bemeneti értéknél az illető decimális számnak megfelelő 3-többletes Gray kód jelenik meg a kimenetén.

14. **Mi az a multiplexer? Hány vezérlő bemenet szükséges egy multiplexernél n bemenet esetén?**
A harmadik, gyakran használt áramkörök az ú.n. multiplexerek. Ennek több bemenete van és csak egy kimenete. Erre a kimenetre a bemenetek közül csak annak a jele kerül ki, amelyet az ú.n. vezérlő bemenetekkel kiválasztottunk. Megkülönböztetésül előbbi bemeneteket szokás adat bemenetnek, utóbbiakat vezérlő bemeneteknek nevezni. A 24. ábrán egy 4-bemenetű multiplexer (MUX) és igazság táblázata látható. A vezérlő bemenetek kódolva tartalmazzák a kiválasztandó adatbemenet sorszámát, így n adatbemenet esetén a vezérlő bemenetek szükséges száma $\log_2(n)$. Így 4 kimenet esetén 2 vezérlő bemenetre van szükség.

15. **Mi az a demultiplexer? Hány vezérlő bemenet szükséges egy demultiplexernél n kimenet esetén?**
A harmadik, gyakran használt áramkörök az ú.n. multiplexerek. Ennek több bemenete van és csak egy kimenete. Erre a kimenetre a bemenetek közül csak annak a jele kerül ki, amelyet az ú.n. vezérlő bemenetekkel kiválasztottunk. Megkülönböztetésül előbbi bemeneteket szokás adat bemenetnek, utóbbiakat vezérlő bemeneteknek nevezni. A 24. ábrán egy 4-bemenetű multiplexer (MUX) és igazság táblázata látható. A vezérlő bemenetek kódolva tartalmazzák a kiválasztandó adatbemenet sorszámát, így n adatbemenet esetén a vezérlő bemenetek szükséges száma log2(n). Így 4 kimenet esetén 2 vezérlő bemenetre van szükség.
