function solution(a, b) {
    const anb = String(a) + String(b)
    const ab2 = 2*a*b
    
    return anb >= ab2 ? Number(anb) : Number(ab2)

    
}