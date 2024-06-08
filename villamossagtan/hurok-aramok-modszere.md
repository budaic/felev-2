# Hurok áramok módszere

A módszer a Kirchhoff törvényeken ([csomóponti](./kirchhoff-csomoponti-torvenye.md), [hurok](./kirchhoff-hurok-torvenye.md)) alapul. Segítségével bonyolultabb áramkörök is könnyen modellezhetőek. Áramforrást tartalmazó körök esetén nem alkalmazható.

Módszer lépései:
1. Azonosítjuk az áramkörnek azon hurkait, melyek nem tartalmaznak további hurkokat.
2. Mindegyik hurokhoz rendelünk egy hurok áramot, vagy az óramutató irányával megegyező, vagy azzal ellentétes irányban.
3. Mindegyik hurokra felírjuk [Kirchoff hurok törvényét](./kirchhoff-hurok-torvenye.md), a feszültségek helyére az [Ohm törvény](./ohm-torveny.md) segítségével a hurok áramokat írjuk.
4. Az egyenletrendszert megoldjuk a hurok áramokra.
5. A hurok áramok segítségével meghatározzuk az egyes ágakban folyó áramokat.
6. Az ágakban folyó áramok ismeretében az [Ohm törvény](./ohm-torveny.md) alkalmazásával meghatározzuk az áramköri elemeken eső feszültségeket.