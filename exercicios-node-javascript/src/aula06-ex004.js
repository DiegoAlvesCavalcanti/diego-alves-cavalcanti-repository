var readlineSync = require('readline-sync');
let txt = readlineSync.question('Digite algo: ');

function isTitleCase(str) {
    return str.split(' ').every(word => /^[A-Z][a-z]*$/.test(word));
}
console.log(`O tipo primitivo desse valor é: ${typeof(txt)}`);
console.log(`Só tem espaços: ${txt == ''}`);
console.log(`É um número: ${!isNaN(txt)}`);
console.log(`É alfabético: ${/^[A-Za-z]+$/.test(txt)}`);
console.log(`É alfanumérico: ${/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$/.test(txt)}`);
console.log(`Está em maiúsculas: ${/[A-Z]/.test(txt)}`);
console.log(`Está em minúsculas: ${/[a-z]/.test(txt)}`);
console.log(`Está capitalizada?: ${isTitleCase(txt)}`);