var ledP0 = require('@amperka/led')
  .connect(P0)
  .turnOn();

var sensorA5 = require('@amperka/light-sensor').connect(A5);

function updateBrightness() {
  var luxes = sensorA5.read('lx');
  var level = 1 - luxes / 50;
  ledP0.brightness(level);
}

setInterval(updateBrightness, 10);

