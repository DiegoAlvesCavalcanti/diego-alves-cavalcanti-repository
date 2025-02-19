var readlineSync = require('readline-sync');

var nome = readlineSync.question('Qual é o seu nome? ');
console.log(`Olá ${nome}! prazer em te conhecer.`);