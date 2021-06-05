function solve(text) {
    let wordsArray = text.match(/\w+/g);

    return wordsArray.join(', ').toLocaleUpperCase();
}

console.log(solve('Hi, how are you?'));