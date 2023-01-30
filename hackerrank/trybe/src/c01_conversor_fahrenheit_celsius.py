"""
Challenge 01 - Conversor Fahrenheit-Celsius - fahrenheit_to_celsius

Para se converter uma temperatura medida em um termômetro em Fahrenheit
para escala Celsius, com a qual estamos acostumados no Brasil deve-se
usar a equação:
* C = (F - 32)/1,8, onde C é a temperatura em graus Celsius e F a
temperatura medida em Fahrenheit.

Construa um algoritmo que, ao receber um valor de temperatura medido
em Fahrenheit retorne a medida equivalente em Celsius.

Por exemplo, ao receber a leitura de 95ºF retorne 35,0
- Atenção para a saída em número de ponto flutuante.
"""


def fahrenheit_to_celsius(arg: float) -> float:
    """Converts Fahrenheit temperature to Celsius

    Args:
        arg (float): temperature in Fahrenheit

    Returns:
        float: temperature in Celsius
    """
    temperature_in_celsius = (arg - 32) / 1.8
    return round(temperature_in_celsius, 1)


if __name__ == "__main__":
    TEMP = 100.0
    ct = fahrenheit_to_celsius(TEMP)
    print(ct)
