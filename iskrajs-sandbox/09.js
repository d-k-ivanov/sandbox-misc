//Termenvox
var buttonP0 = require('@amperka/button')
  .connect(P0);

var buzzerP5 = require('@amperka/buzzer')
  .connect(P5)
  .turnOff();

var potA0 = require('@amperka/pot')
  .connect(A0);

var sensorA1= require('@amperka/light-sensor')
  .connect(A1);

function toInt(num){
  return Math.round(Number(num));
}

function play() {
  var luxes = toInt(sensorA1.read('lx') * 100);
  var level = toInt(potA0.read() * 7) + 1;
  var freq = (luxes * level);
  buzzerP5.frequency(freq);
  console.log('Level: ' + luxes + ' Level: ' + level + ' Frequency: ' + freq);
  //console.log('LS: ' + freq);
}

buttonP0.on('press', function() { buzzerP5.toggle(); });

setInterval(play, 10);

