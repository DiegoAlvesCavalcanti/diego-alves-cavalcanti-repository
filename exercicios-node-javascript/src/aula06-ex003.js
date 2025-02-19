var readlineSync = require('readline-sync');

let n1 = Number(readlineSync.question('Digite um número: '));
let n2 = Number(readlineSync.question('Digite outro número: '));
let s = n1 + n2;

console.log(`A soma entre ${n1} e ${n2} resulta em ${s}.`);
