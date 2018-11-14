var buttonP0 = require('@amperka/button')
  .connect(P0);

var buzzerP5 = require('@amperka/buzzer')
  .connect(P5)
  .turnOff();

var potA0 = require('@amperka/pot')
  .connect(A0);

function synth() {
  var freq = 20 + 20000 * potA0.read();
  buzzerP5.frequency(freq);
  console.log('Frequency: ' + freq);
}

buttonP0.on('press', function() { buzzerP5.toggle(); });
setInterval(synth, 10);

