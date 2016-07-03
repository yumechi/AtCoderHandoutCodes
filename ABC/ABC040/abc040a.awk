function abs(x) {
    return x > 0 ? x : -x
}

function min(x, y) {
    return x < y ? x : y
}

{
    print min($1 - $2, $2 - 1)
}
