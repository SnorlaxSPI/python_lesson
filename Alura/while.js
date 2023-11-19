const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log("*********************************");
console.log("Bem vindo no jogo de adivinhação!");
console.log("*********************************");

const numeroSecreto = 42;
const totalDeTentativa = 3;
let rodada = 1;

function realizarRodada() {
  console.log(`Tentativa ${rodada} de ${totalDeTentativa}`);
  rl.question("Digite o seu número: ", (chuteStr) => {
    console.log(`Você digitou ${chuteStr}`);
    const chute = parseInt(chuteStr);
  
    const acertou = chute === numeroSecreto;
    const maior = chute > numeroSecreto;
    const menor = chute < numeroSecreto;
  
    if (acertou) {
      console.log("Você acertou");
      rl.close();
    } else {
      if (maior) {
        console.log("Você errou! O seu chute foi maior que o número secreto.");
      } else if (menor) {
        console.log("Você errou! O seu chute foi menor do que o número secreto.");
      }
      rodada++;
      if (rodada <= totalDeTentativa) {
        realizarRodada();
      } else {
        console.log("Fim do jogo");
        rl.close();
      }
    }
  });
}

realizarRodada();
