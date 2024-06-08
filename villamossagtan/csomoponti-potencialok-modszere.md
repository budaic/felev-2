# Csomóponti potenciálok módszere

A módszer a Kirchhoff törvényeken ([csomóponti](./kirchhoff-csomoponti-torvenye.md), [hurok](./kirchhoff-hurok-torvenye.md)) alapul. Segítségével bonyolultabb áramkörök is könnyen modellezhetőek.

Módszer lépései:
1. Kiválasztunk egy csomópontot (ahol két vagy több áramköri elem találkozik) a körben, melynek [potenciálját](./villamos-potencial.md) nullának vesszük. A többi csomópont [potenciálját](./villamos-potencial.md) ehhez viszonyítjuk.
2. Elnevezzük a további csomópontok [potenciálját](./villamos-potencial.md) ($V_1, V_2, V_3, \dots$) Először a ránézésre meghatározható csomópontok [potenciáljait](./villamos-potencial.md) határozzuk meg.
3. Először a meghatározható csomópontok [potenciáljait](./villamos-potencial.md) határozzuk meg.
4. A többi csomópontra alkalmazzuk [Kirchhoff csomóponti törvényét](./kirchhoff-csomoponti-torvenye.md), az áramok helyére az [Ohm törvény](./ohm-torveny.md) segítségével beírjuk a csomóponti [potenciálokat](./villamos-potencial.md). Feszültségforrások kapcsai esetén a két kapocs [potenciáljának](./villamos-potencial.md) különbsége egyenlő a [feszültséggel](./feszultseg.md), ez további egyenleteket eredményez a csomóponti [potenciálokra](./villamos-potencial.md) vonatozóan.
5. A kapott egyenletrendszert megoldjuk a csomóponti [potenciálokra](./villamos-potencial.md).
6. A kapott [potenciálokból](./villamos-potencial.md) meghatározzuk az áramkörökön eső [feszültségeket](./feszultseg.md).
7. [Ohm törvényének](./ohm-torveny.md) meghatározzuk az egyes ágakban folyó áramokat.