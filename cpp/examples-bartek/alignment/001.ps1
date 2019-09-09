if (Test-Path .\001.asm)    {Remove-Item -Path .\001.asm    -Force}
if (Test-Path .\001_14.asm) {Remove-Item -Path .\001_14.asm -Force}
if (Test-Path .\001_17.asm) {Remove-Item -Path .\001_17.asm -Force}
if (Test-Path .\001.exe)    {Remove-Item -Path .\001.exe    -Force}
if (Test-Path .\001_14.exe) {Remove-Item -Path .\001_14.exe -Force}
if (Test-Path .\001_17.exe) {Remove-Item -Path .\001_17.exe -Force}
if (Test-Path .\001.obj)    {Remove-Item -Path .\001.obj    -Force}
# cl /EHsc /std:c++14 001.cpp 
# cl /EHsc /std:c++17 001.cpp

g++ -std=c++14 001.cpp -S -o 001_14.asm
g++ -std=c++14 001.cpp -o 001_14.exe
g++ -std=c++17 001.cpp -S -o 001_17.asm
g++ -std=c++17 001.cpp -o 001_17.exe -v
# g++ 001.cpp -Wall -Wextra --std=c++14 -o 001.exe
# g++ 001.cpp -Wall -Wextra --std=c++17 -o 001.exe -v