function solve(arr) {
    let result = [];

    for (let i = 0; i < arr.length; i ++) {
        if (arr[i] === 'add') {
            result.push(i + 1);
        }
        else if (arr[i] === 'remove') {
            result.pop();
        }
    }

    if (result.length === 0) {return 'Empty';}

    result = result.map(x => `${x}\n`);

    return result.join('');

}

console.log(solve(
    ['add',
        'add',
        'remove',
        'add',
        'add']
));
