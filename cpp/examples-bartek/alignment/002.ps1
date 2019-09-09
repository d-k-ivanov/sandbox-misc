if (Test-Path .\002.asm) {Remove-Item -Path .\002.asm -Force}
if (Test-Path .\002.exe) {Remove-Item -Path .\002.exe -Force}
if (Test-Path .\002.obj)  {Remove-Item -Path .\002.obj  -Force}
if (Test-Path .\0022.asm) {Remove-Item -Path .\0022.asm -Force}
if (Test-Path .\0022.exe) {Remove-Item -Path .\0022.exe -Force}

cl  /std:c++17 002.cpp /EHsc
cl  /std:c++17 002.cpp /EHsc /Fa /c
g++ -std=c++17 002.cpp -S -o 0022.asm -Wall -Wextra 
g++ -std=c++17 002.cpp -o 0022.exe -v -Wall -Wextra 
# g++ 002.cpp -Wall -Wextra --std=c++17 -o 002.exe -v