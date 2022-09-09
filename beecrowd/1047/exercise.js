// https://www.beecrowd.com.br/judge/pt/problems/view/1047
// Tempo de Jogo com Minutos

const fs = require("fs");
const input = fs.readFileSync("./dev/stdin", "utf8");
const [startHour, startMin, endHour, endMin] = input.trim().split(" ");

const start = Number(startHour) * 60 + Number(startMin);
const end = Number(endHour) * 60 + Number(endMin);

let diff = end - start;

if (diff < 0) {
  diff += 24 * 60;
}

const hour = Math.floor(diff / 60);
const min = diff % 60;

let result = "";

if (diff === 0) {
  console.log("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)");
} else {
  console.log(`O JOGO DUROU ${hour} HORA(S) E ${min} MINUTO(S)`);
}
