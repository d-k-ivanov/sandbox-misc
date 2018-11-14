var ledP0 = require('@amperka/led').connect(P0);
var buzP5 = require('@amperka/buzzer').connect(P5);
var btnP7 = require('@amperka/button').connect(P7);

btnP7.on('press', function() {
  ledP0.turnOn();
  buzP5.turnOn();
});

btnP7.on('release', function() {
  ledP0.turnOff();
  buzP5.turnOff();
});
