let nome = "Rafael";
let sobrenome = "da Silva";
let nomeCompleto = ("Meu nome é: ", nome + " " + sobrenome);
console.log(nomeCompleto); // Meu nome é: Rafael da Silva

let templateString =`Meu nome é: ${nome},
meu sobrenome é: ${sobrenome}`;
console.log(templateString);// Meu nome é: Rafael da Silva

let numA1 = 5;
let numB1 = 9;
let soma = `A soma de ${numA1} e ${numB1} é ${numA1 +numB1}`;
console.log(soma);
/*Acesse o site OneCompiler (link em anexo) e crie uma função que recebe dois números 
como parâmetros e imprime quatro frases no terminal (a partir de template strings) 
demonstrando as quatro operações básicas aplicadas a ambos números. Exemplo:

4 + 5 = 9
4 - 5 = -1
4 x 5 = 20
4 / 5 = 0.8  */

let numA = 4;
let numB = 5;
function operacoesBasicas(numA, numB){
    let soma = `Valor de A: ${numA} + Valor de B: ${numB} = Soma: ${numA+numB}`;
    console.log(soma);
    let subtrair = `Valor de A: ${numA} - Valor de B: ${numB} = Subtração: ${numA-numB}`;
    console.log(subtrair);
    let multiplicação = `Valor de A: ${numA} * Valor de B: ${numB} = Multiplicação: ${numA * numB}`;
    console.log(multiplicação);
    let divisão = `Valor de A: ${numA} / Valor de B: ${numB} = Divisão:  ${numA/numB}`;
    console.log(divisão);
}
operacoesBasicas(numA, numB);


