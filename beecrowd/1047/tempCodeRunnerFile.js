const [startHour, startMin, endHour, endMin] = input.trim().split(' ');

const start = Number(startHour) * 60 + Number(startMin);
const end = Number(endHour) * 60 + Number(endMin);

const diff = end - start;
const hour = Math.floor(diff / 60);
const min = diff % 60;

let result = '';

if (diff === 0) {
  result = 'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)';  
} else if ((min >= 1 & hour === 0) || (hour >= 1 && hour < 24)) {
  result = `O JOGO DUROU ${hour} HORA(S) E ${min} MINUTO(S)`;  
} else {
  console.log(startHour, startMin, endHour, endMin);
}

if (result) console.log(result);