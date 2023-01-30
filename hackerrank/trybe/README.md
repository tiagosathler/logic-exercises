# Desafios de algoritmos

Desafios de algoritmos aplicados pela [Trybe](https://www.betrybe.com/) durante o curso de Desenvolvimento Web no dia 12 / 11 / 2021.

<br>

1. [x] 1. **[Conversor Fahrenheit-Celsius](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c01_conversor_fahrenheit_celsius.py):**

Para se converter uma temperatura medida em um termômetro em Fahrenheit para escala Celsius, com a qual estamos acostumados no Brasil deve-se usar a equação:

$$ C = {F - 32 \over 1,8} $$

Onde C é a temperatura em graus Celsius e F a temperatura medida em Fahrenheit.

Construa um algoritmo que, ao receber um valor de temperatura medido em Fahrenheit retorne a medida equivalente em Celsius.

Por exemplo, ao receber a leitura de 95ºF retorne 35,0.
> Atenção para a saída em número de ponto flutuante.

<br>

2. [x] 2. **[Diferença](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c02_difference.py):**

Dado um número **X**, retorne a diferença entre X e 10 de forma que o resultado seja sempre um valor positivo.

Isto é:

* se X < 10, faça 10 - X - exemplo: X = 3 ==> 7 (10 - 3)
* se X > 10, faça X - 10 - exemplo: X = 15 ==> 5 (15 - 10)

<br>

3. [x] 3. **[Contagem regressiva](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c03_count_down.py):**

Dado um número **X** construa um programa que retorne a contagem regressiva no formato X...X-1...X-2...0!!!

*Exemplo:*

* X = 10 ==> 10...9...8...7...6...5...4...3...2...1...0!!!

<br>

4. [x] 4. **[Múltiplos de 3 ou 5](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c04_multiples_of_3_or_5.py):**

Construa um algoritmo que encontre a soma de todos os números naturais múltiplos de **3** ou **5** menores que um dado número **N**.

*Exemplo:*

* Quando listamos todos os números naturais menores que 10 que são múltiplos de 3 ou 5 temos: 3, 5, 6 e 9. A soma desses números é 3 + 5 + 6 + 9 = 23.

<br>

5. [x] 5. **[Números pares da série de Fibonacci](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c05_even_fibonacci_numbers.py):**

Uma série de *Fibonacci* iniciando com os números 1 e 2, do terceiro elemento em diante calcula-se o próximo elemento como a soma do dois anteriores, sucessivamente.

Dessa forma, os 10 primeiros elementos dessa série são: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

A soma dos números pares menores que 100 daquela série é 44.

Calcule a soma dos números pares entre os elementos da série que sejam menores que um dado número **N**.

> Algumas referências apontam a série de Fibonacci começando em 0. Nesse caso a serie seria: 0, 1, 1, 2, 3, 5, ... Para efeito dessa atividade considere a série iniciando em "1, 2".

<br>

6. [x] 6. **[Enésimo Primo](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c06_nth_prime.py):**

Um número primo é um número natural que é divisível exclusivamente por 1 e por ele mesmo.

Construa um algoritmo capaz de calcular o enésimo número primo para um dado número **N**.

*Exemplo:*

* N = 6 ==> tem-se os 6 primeiros números primos:  2, 3, 5, 7, 11, 13, onde 13 é o sexto número primo.

> O número 1 não é considerado um número primo.

<br>

7. [x] 7. **[Maior divisor primo](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c07_largest_prime_factor.py):**

Números primos são aqueles que são divisíveis exclusivamente por 1 e eles mesmos.

Os divisores primos de 13195, por exemplo, são 5, 7, 13 e 29.

Encontre o maior divisor primo de um dado número.

<br>

8. [x] 8. **[Caixa de supermercado](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c08_supermarket_cashier.py):**

Uma atendente de supermercado deve lançar os valores dos produtos à medida que os passa no caixa.

Eventualmente ele faz um lançamento errado e para invalidá-lo deve lançar o valor 0 (zero) para que o registro anterior não seja considerado.

Na eventualidade de mais de um valor ser lançado errado consecutivamente o atendente lançará tantos valores zero quanto necessários para apagar os registros incorretos.

Por exemplo, no lançamento: 1, 3, 5, 4, 0, 0, 7, 0, 0, 6 serão considerados para a soma os valores 1 e 6, visto que os valores 3, 5, 4 e 7 foram anulados pelos zeros.

Construa um algoritmo capaz de processar uma entrada de **n** números e apresentar na saída a *SOMA DOS REGISTROS VÁLIDOS*.

Considere a entrada do algoritmo sendo uma lista da seguinte forma: [n<sub>1</sub>, n<sub>2</sub>, n<sub>3</sub>, n<sub>4</sub>, n<sub>5</sub>, ... n<sub>x</sub>].

No exemplo acima a entrada seria [1, 3, 5, 4, 0, 0, 7, 0, 0, 6].

> Caso você analise os dados do teste aberto verá que a entrada é: 10, 1, 3, 5, 4, 0, 0, 7, 0, 0, 6. Mas apenas a lista [1, 3, 5, 4, 0, 0, 7, 0, 0, 6] é passada para a função que você irá construir.

<br>

9. [x] 9. **[Menor múltiplo](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c09_smallest_multiple.py):**

O menor número divisível por todos os números de 1 a 10 é **2520**.

Crie um algoritmo capaz de calcular o menor número divisível por todos os números de 1 a um dado número.

<br>

10. [x] 10. **[Diferença das somas dos quadrados e quadrados da soma](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c10_sum_square_difference.py):**

O quadrado da soma dos **n** primeiros números é dado por:

* square_of_sum = (1 + 2 + 3 ... + n)²

A soma dos quadrados dos primeiros **n** números naturais é dada por:

* sum_of_square = (1² + 2² + 3² + ... + n²)

Dado um número natural **N**, calcule a diferença entre o quadrado da soma e a soma dos quadrados dos *n* primeiros números naturais

<br>

11. [x] 11. **[Cadeias de quadrados de dígitos](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c11_square_digit_chain.py):**

Uma cadeia de números é gerada a partir da soma dos quadrados dos dígitos do número anterior até ue o número formado já esteja presente nessa cadeia.

Por exemplo:

* 44 - 32 - 13 - 10 - 1 - 1
    Explicação:
    4² + 4² = 32
    3² + 2² = 13
    1² + 3² = 10
    1² + 0² = 1
    1² = 1

* 85 - 89 - 175 - 42 - 20 - 4 - 16 - 37 - 58 - 89 ...

Qualquer cadeia que chegue a um número repetido ficará presa em um lopping infinito entre a primeira ocorrência desse número e a segunda ocorrência dele.

No caso do 1, a partir da primeira ocorrência, todos os números serão 1.

No caso do 89, uma vez que ele seja atingido, a sequência será eternamente a mesma que até alcançar 89 novamente.

Construa um algoritmo capaz de contar quantas cadeias terminarão em 89 considerando cadeias que se iniciem com todos os números menores que um dado número **N**.

<br>

12. [x] 12. **[Números de Lychrel](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c12_lychrel_numbers.py):**

*Números palíndromos* podem se lidos da esquerda para direita ou da direita para esquerda com o mesmo resultado.

Se pegarmos o número 47 e o somarmos ao seu reverso, 74, temos 47 + 74 = 121, que é um número palíndromo.

Nem todos os os números geram palíndromos de forma tão rápida quanto 47.

*Exemplo ==> 349:*

* 349 + 943 = 1292,
* 1292 + 2921 = 4213
* 4213 + 3124 = 7337 (é palíndromo)

Ou seja, o número **349** levou **3 interações** para gerar um palíndromo pelas somas dos resultados com seu reverso.

Apesar de não ser formalmente provado, acredita-se que números como 196 jamais gerarão um palíndromo pelas somas dos resultados de seus resultados como os respectivos reversos.

Um número que não gera palíndromos a partir desse processo é chamado de **Número de Lychrel**.

Acredita-se que para qualquer número abaixo de 10.000:

* gerará um palíndromo a partir da soma dos resultados com seus
reversos até a 50a iteração;

* não será possível gerar um palíndromo nem mesmo com todo o
poder computacional disponível do mundo.

Construa um algoritmo capaz de identificar a quantidade de números de Lychrel menores que um dado número N < 10.000.

<br>

13. [x] 13. **[Soma dos dígitos](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c13_digits_sum.py):**

Escreva um programa capaz de encontrar quantos números entre 0 e 1000 têm a a soma dos seus dígitos igual a um dado número **S**.

*Exemplo:*

* para S = 26 temos 3 números, 899, 989 e 998, cujas somas dos algarismos é igual a S.

<br>

14. [x] 14. **[Maior Produto Palíndromo](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c14_largest_palindrome_product.py):**

Um número palíndromo tem a o mesmo valor sendo ser lido da direita para a esquerda ou da esquerda para direita, por exemplo: 11, 212, 3773, 1034301..

O maior número palíndromo resultado do produto de dois números de **2 dígitos** é **9009** (*91 x 91*)

Encontre o maior número palíndromo resultado do produto de dois números com um determinado número de **dígitos**.

<br>

15. [x] 15. **[Poligramas](https://github.com/tiagosathler/logic-exercises/blob/master/hackerrank/trybe/src/c15_polygram.py):**

Duas palavras **A** e **B** são anagramas entre si se podemos transformar a palavra A na palavra B apenas trocando de posição as letras da palavra A.

*Exemplos de anagramas:*

* **duetos** e **estudo**

* **bba** e **bab**

Vamos chamar de poligrama uma palavra que consiste na concatenação de duas ou mais palavras que são anagramas entre si.

A primeira dessas palavras é chamada de raiz do poligrama.

*Exemplo de poligrama:*

* **bbabab** é um poligrama com raiz **bba**, pois ela é a concatenação dos anagramas **bba** e **bab**.

Dada uma palavra, escreva um programa que determine se ela é um poligrama.

Caso a palavra seja um poligrama, o programa deve retornar a raiz dele.

Caso contrário deve retornar uma string vazia.
