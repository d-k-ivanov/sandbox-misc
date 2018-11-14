var ledP0 = require('@amperka/led')
  .connect(P0)
  .turnOn();

var potA0 = require('@amperka/pot').connect(A0);

var sensorA5 = require('@amperka/light-sensor').connect(A5);

function updateBrightness() {
  var luxes = sensorA5.read('lx');
  //console.log("LX: " + luxes);
  var level = 1 - luxes / 50;
  //console.log("Lev0: " + level);
  var potLevel = potA0.read();
  //console.log("Lev1: " + potLevel);
  ledP0.brightness(level - potLevel);
  //TODO:more accurate values 
}

setInterval(updateBrightness, 10);

