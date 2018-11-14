var lightSensorA2 = require('@amperka/light-sensor')
  .connect(A2);

var closed = false;
var level = 0;

function light_level() {
  var lx = lightSensorA2.read('lx').toFixed(2);
  var time = getTime().toFixed(0);
  console.log(time, 'sec', '->', lx, 'luxes');
}

setInterval(light_level, 1000);