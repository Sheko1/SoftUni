function solve(input, firstPie, secondPie) {
    let firstIndex = input.indexOf(firstPie);
    let secondIndex = input.lastIndexOf(secondPie);

    return input.slice(firstIndex, secondIndex  + 1);
}

console.log(solve([
    'Pumpkin Pie',
    'Key Lime Pie',
    'Cherry Pie',
    'Lemon Meringue Pie',
    'Sugar Cream Pie',], 'Key Lime Pie', 'Lemon Meringue Pie'))
