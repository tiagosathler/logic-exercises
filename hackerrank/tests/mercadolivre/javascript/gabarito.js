function numbersGenerator(maxDigit) {
    const resultList = [];
    let maxNumber = ""
    
    for (let i = 0; i < 4; i++) {
        maxNumber += maxDigit.toString()
    }
    
    maxNumber = Number(maxNumber)
    
    
    for (let number = 1000; number <= maxNumber; number++) {
        const numberStr = number.toString()
        
        let sum = 0;
        for (digit of numberStr) {
            if (Number(digit) <= maxDigit) {
                sum += Number(digit)
            }
        }
        
        if (sum === 21) {
            resultList.push(number)
        }
    }
    
    return resultList.length ? resultList : [null]
}


function main() {
    // Dado um input de 'maxDigit' - um dígito de 1 a 9,
    // encontre todas as combinações possíveis para gerar números de 4 dígitos ("xxxx"),
    // cuja soma desses quatro DÍGITOS seja IGUAL a 21 E que todos sejam quaisquer dígitos
    // igual ou menor que 'maxDigit'

    // Se não houver solução imprima 'null'
    
    const input = "9"
    const maxDigit = Number(input);
    const numbers = numbersGenerator(maxDigit);
    
    numbers.forEach((number) => {
        console.log(number)
    })
}

main();

/*
    EXEMPLO:
        input = "6"
        
        saída (stdout ou console.log):
            3666
            4566
            4656
            4665
            5466
            5556
            5565
            5646
            5655
            5664
            6366
            6456
            6465
            6546
            6555
            6564
            6636
            6645
            6654
            6663
        
        (ou seja, todos estes números são compostos por dígitos menor ou igual a 'maxDigit' e a soma deles é 21)
*/