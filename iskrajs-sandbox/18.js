
var irrP7 = require('@amperka/ir-receiver').connect(P7);
var ledP1 = require('@amperka/led').connect(P1);

var powerCode = null;

function ledToggle(code, repeat)
{
    if (repeat)
    {
        return;
    }

  if (powerCode === null)
    {
        powerCode = code;
    }

    if (code === powerCode)
    {
        ledP1.toggle();
    }
}

function ledAutoFade ()
{
    ledP1.blink(1);
}

ledP1.turnOff();
irrP7.on('receive', ledToggle);
