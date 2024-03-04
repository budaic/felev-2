# Negyedik labor

```cpp
#include <stdio.h>

#define AL 65

int main() {
	char a2 = 66;
	printf("az a2 karakter erteke: %c\n", a2);

	int ka = AL;
	printf("ka erteke: %i\n", ka);
	printf("ka erteke oktalisan: %o\n", ka);
	printf("ka erteke hexadecimalisan: 0x%x\n", ka);

	double Ludolph = (double) 339 / 108;
	printf("pi=%8.2f\n", Ludolph);
	printf("pi=%08.2f\n", Ludolph);
	printf("pi=%8e\n", Ludolph);
	printf("pi=%8g\n", Ludolph);

    scanf_s("%lf", &valami_double);
    printf("d= %g mm\n", d);

    printf("fejes csapszeg atmeroje [mm] d= ");
    double d;
    scanf_s("%lf", &d);
    printf("d= %g mm\n", d);
    double ker = d*Ludolph;
    printf("kerulet: %f\n", ker);

    printf("fejes csapszeg hossza l= ");
    double l;
    scanf_s("%lf", &l);
    // vas surusege = 7.847*10^3
    double suruseg = 7847.0; // kg/m^3

    double d_m = d / 1000;
    double l_m = l / 1000;

    double v = d_m*d_m/4*Ludolph*l_m;
    double tomeg = suruseg * v;
    printf("tomege: %g\n", tomeg);

	return 0;
}
```

```cpp
#include <stdio.h>
#define _USE_MATH_DEFINES // M_PI, ezt a math.h elott kell beirni
#include <math.h>

int main() {
    int i = 1, j = 2;
    double f = i/j
    printf("%i / %i = %g\n", i, j, f);
    printf("pi = %g\n", M_PI);
    printf("4*atan(1) = %g\n", 4 * atan(1));
    printf("e = %17.15f\n", M_E);
    double le = log10(2.7);

    printf("le=%g\n", le);

    byte acc = 0;
    printf("acc=0x%02x", acc);
    return 0;
}


```