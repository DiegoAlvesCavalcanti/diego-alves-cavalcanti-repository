var readlineSync = require('readline-sync');

let nome = readlineSync.question('Qual o seu nome? -> ');
let idade = Number(readlineSync.question('Qual é a sua idade? -> '));
let peso = Number(readlineSync.question('Qual é o seu peso? -> '));

console.log(nome, idade, peso);