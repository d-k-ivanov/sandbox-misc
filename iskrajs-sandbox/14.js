var termometerA4 = require('@amperka/thermometer')
  .connect(A4);

var units = 0;
var temp = 'undef';

function set_celsius() {
  units = 0;
}

function set_farengheit() {
  units = 1;
}

function set_kelvin() {
  units = 2;
}

function show_temperature() {
  var celsius = termometerA4.read('C');
  var farengheit = celsius * 1.8 + 32;
  var kelvin = celsius + 273.15;
  switch (units) {
    case 1:
      temp = farengheit.toFixed(1) + ' °F';
      break;
    case 2:
      temp = kelvin.toFixed(1) + ' °K';
      break;
    default:
      temp = celsius.toFixed(1) + ' °C';
  }
  var site = '<!DOCTYPE html>'                                       +
  '<html>'                                                           +
  '<head>'                                                           +
  '<style>'                                                          +
  '   .button {'                                                     +
  '       background-color: #555555;'                                +
  '       border: none;'                                             +
  '       color: white;'                                             +
  '       padding: 10px 10px;'                                       +
  '       text-align: center;'                                       +
  '       text-decoration: none;'                                    +
  '       display: inline-block;'                                    +
  '       font-size: 16px;'                                          +
  '       }'                                                         +
  '</style>'                                                         +
  '</head>'                                                          +
  '<body>'                                                           +
  '   <div>'                                                         +
  '       <button class="button" type="buttonC" onclick="set_celsius()">Celsius</button>'      +
  '       <button class="button" type="buttonF" onclick="set_farengheit()>Farengheit</button>' +
  '       <button class="button" type="buttonK" onclick="set_kelvin()">Kelvin</button>'        +
  '   </div>'                                                        +
  '   <div style="font-size: 0.5em">'                                +
  '       Temperature:'                                              +
  '   </div>'                                                        +
  '   <div>'                                                         +
        temp                                                         +
  '   </div>'                                                        +
  '</body>'                                                          +
  '</html>'                                                          +
  '';
  console.log(site);
}

setInterval(show_temperature, 3000);



