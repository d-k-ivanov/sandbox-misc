var buttonP0 = require('@amperka/button')
  .connect(P0);

var servoP13 = require('@amperka/servo')
  .connect(P13);

var potA0 = require('@amperka/pot')
  .connect(A0);

function toInt(num){
  return Math.round(Number(num));
}

function play() {
  var level = toInt(potA0.read() * 178) + 1;
  var angle = (level);
  servoP13.write(angle);
  console.log('Level: ' + level + ' Angle: ' + angle);
}

//buttonP0.on('press', function() { servoP13.write(30); });
//buttonP0.on('release', function() { servoP13.write(150); });

setInterval(play, 20);

