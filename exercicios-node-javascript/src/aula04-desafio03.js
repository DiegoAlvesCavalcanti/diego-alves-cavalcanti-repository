var readlineSync = require('readline-sync');

let first_number = Number(readlineSync.question('Digite o primeiro número: '));
let second_number = Number(readlineSync.question('Digite o segundo número: '));

let result = first_number + second_number;

console.log(`A soma é: ${result}`);