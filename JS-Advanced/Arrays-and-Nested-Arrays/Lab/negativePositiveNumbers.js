function solve(numbers) {
    numbers.sort(a => {
        if (a < 0) {
            return -1;
        }
        else {
            return 0;
        }
    })

    numbers.forEach(x => console.log(x));
}

solve([3, -2, 0, -1]);
