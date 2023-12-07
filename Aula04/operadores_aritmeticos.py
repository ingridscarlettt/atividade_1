"""

OPERADORES ARITMÉTICOS EM PYTHON
+   ----------- Adição
-   ----------- Subtração
*   ----------- Multiplicação
/   ----------- Divisão
%   ----------- Mod(Resto)
**  ----------- Exponenciação
//  ----------- Divisão Truncada base exata
"""

a = 10;
b = 2;

print("(+)   ----------- Adição");
print(f"A soma de {a} + {b} é {a+b}");
print("A soma de {1} + {0} é {2}".format(b,a,a+b));
print("\n")

print("(-)   ----------- Subtração");
print(f"A diferença de {a} - {b} é {a-b} ");

print("(*)   ----------- Multiplicação");
print(f"O produto de {a} * {b} é {a*b} ");
print("\n");

print("(/)   ----------- Divisão");
print(f"O quoficiente de {a} / {b} é {(a/b):.0f} ");
print("\n");

print("(%)   ----------- Modulo");
print(f"O Modulo de {a} % {b} é {a%b} ");
print("\n");

print("(**)   ----------- Exponenciação:");
print(f"O valor  de {a} elevado a {b} potencia é igual a: {a**b} ");
print("\n");

print("(//)   ----------- Divisão Truncada:");
print(f"O valor da divisão {a} por {b} é igual a: {a//b} ");
print("\n");

