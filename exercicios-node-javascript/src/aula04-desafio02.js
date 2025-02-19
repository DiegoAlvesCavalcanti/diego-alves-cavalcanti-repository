var readlineSync = require('readline-sync');

let dia = readlineSync.question('Dia = ');
let mes = readlineSync.question('Mês = ');
let ano = readlineSync.question('Ano = ');

console.log(`Você nasceu no dia ${dia} do mês ${mes} de ${ano}.`);