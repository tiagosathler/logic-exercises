function numbersGenerator(args) {
    const { maxDigit, numDigits, sum } = args;
    const magnitude = numDigits - 1;

    if (maxDigit * numDigits < sum) {
        return [null]
    }

    const numbers = [];

    let digit = maxDigit; // 7

    // maxNumber
    {
        const number = Array(numDigits).fill(0);
        number[0] = digit // 7
        let remainder = sum - number[0]
        for (let d = 1; d <= magnitude; d++) {
            let n = maxDigit;
            if (remainder >= n) {
                number[d] = n;
                remainder -= n;
            } else {
                while (remainder <= n) {
                    if (remainder >= n) {
                        number[d] = n;
                        remainder -= n;
                        break;
                    }
                    n -= 1;
                }
            }
        }
        numbers.push(number)
    }

    return numbers;
}


function main() {
    const MAX_DIGIT = 9
    const NUM_DIGITS = 4
    const SUM = 21
    
    const numbers = numbersGenerator({ maxDigit: MAX_DIGIT, numDigits: NUM_DIGITS, sum: SUM })
    numbers.forEach((n) => console.log(n))
}

main();