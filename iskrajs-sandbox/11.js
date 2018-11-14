var buttonP0 = require('@amperka/button')
  .connect(P0);

var ledP1 = require('@amperka/led')
  .connect(P1);

var buzzerP2 = require('@amperka/buzzer')
  .connect(P2)
  .frequency(50);

var servoP13 = require('@amperka/servo')
  .connect(P13)
  .write(90);

var potA0 = require('@amperka/pot')
  .connect(A0);

function toInt(num){
  return Math.round(Number(num));
}

var closed = false;
var level = 0;

function barrier_level() {
  level = toInt(potA0.read() * 89) + 1;
  console.log('Level: ' + level);
}

function barrier() { 
  closed = !closed;
  if (closed) {
    buzzerP2.beep(1, 0.5);
    ledP1.blink(1, 0.5);
    servoP13.write(0 + level);
  } else {
    buzzerP2.turnOff();
    ledP1.turnOff();
    servoP13.write(90 + level);
  }
}

buttonP0.on('press', barrier);

setInterval(barrier_level, 20);