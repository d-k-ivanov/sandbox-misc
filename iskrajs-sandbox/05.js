var ledP0 = require('@amperka/led')
  .connect(P0)
  .turnOn();

var light = true;

var potA0 = require('@amperka/pot').connect(A0);

var btnP7 = require('@amperka/button').connect(P7);

function updateBrightness() {
  var potLevel = potA0.read();
  ledP0.brightness(potLevel);
}

function toggleDimmer() {
  if (light) {
    console.log("Ligts are turned off!");
    light = false;
  } else {
    console.log("Ligts are turned on!");
    light = true;
  }
  console.log("Brightness level: " + potA0.read());
  ledP0.toggle();
}

btnP7.on('press', toggleDimmer);

setInterval(updateBrightness, 10);

