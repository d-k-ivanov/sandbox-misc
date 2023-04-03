var ledP0 = require('@amperka/led').connect(P0);

var btnP3 = require('@amperka/button').connect(P7);

function pressButton() {
  ledP0.toggle();
}

function ledAutoFade () {
  ledP0.blink(1);
}

ledP0.turnOff();
btnP3.on('press', pressButton);
//btnP3.on('press', ledAutoFade);
