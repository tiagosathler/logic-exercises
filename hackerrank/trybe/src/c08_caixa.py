"""Challenge 08 - Supermarket cashier"""
from collections import deque
from typing import List


def caixa(arg: int, seq: List[int]) -> int:
    """Uma atendente de supermercado deve lançar os valores
    dos produtos à medida que os passa no caixa.
    Eventualmente ele faz um lançamento errado e para
    invalidá-lo deve lançar o valor 0 (zero) para que
    o registro anterior não seja considerado.
    Na eventualidade de mais de um valor ser lançado errado
    consecutivamente o atendente lançará tantos valores zero
    quanto necessários para apagar os registros incorretos.
    Por exemplo, no lançamento: 1, 3, 5, 4, 0, 0, 7, 0, 0, 6
    serão considerados para a soma os valores 1 e 6,
     visto que os valores 3, 5, 4 e 7 foram anulados pelos zeros.
    Construa um algoritmo capaz de processar uma entrada de
    n números e apresentar na saída a SOMA DOS REGISTROS VÁLIDOS.

    Args:
        arg (int): any positive integer - number of operations
        seq (List[int]): input sequence

    Returns:
        int: sum of valid records
    """
    stack = deque()
    for i in range(0, arg):
        if seq[i] == 0:
            stack.pop()
        else:
            stack.append(seq[i])
    return sum(stack)


if __name__ == "__main__":
    INPUT = [10, 1, 3, 5, 4, 0, 0, 7, 0, 0, 6]
    N = INPUT[0]
    SEQ = INPUT[1:]
    result = caixa(N, SEQ)
    print(result)

    INPUT = [15, 1, 3, 0, 4, 0, 9, 7, 0, 0, 6, 0, 3, 10, 8, 0]
    N = INPUT[0]
    SEQ = INPUT[1:]
    result = caixa(N, SEQ)
    print(result)
