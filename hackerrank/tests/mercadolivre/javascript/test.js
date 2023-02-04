function xablau(maxDigit) {
    const MAX = 21
    const arr = [maxDigit]
    let acc = MAX - arr[0]
    for (let i=1; i<4; i++) {
        let div = Math.floor(acc / (4 - i))
        
        do {
            if (div < maxDigit) {
                arr[i] = div
            }
        }
        while (div > maxDigit) {
            if (div < maxDigit) {
                arr[i] = div
            }
            div -= 1
        }
        acc -= arr[i]
    }
    console.log(acc)
    // const responses = [arr.reverse()]
    // let response = true
    // while (response) {
        
    // }
    return arr
}

console.log(xablau(6))
