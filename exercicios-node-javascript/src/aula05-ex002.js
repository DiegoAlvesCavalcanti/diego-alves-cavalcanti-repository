var readlineSync = require('readline-sync');

let nome = readlineSync.question('Digite o seu nome: ');
console.log(`É um prazer te conhecer, ${nome}!`);
console.log('É um prazer te conhecer,',nome,'!');
console.log('É um prazer te conhecer, '+nome+'!');