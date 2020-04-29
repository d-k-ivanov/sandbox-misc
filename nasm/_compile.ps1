
# $InstallPaths = @(
#     'C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2019\Preview'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2017\Community'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools'
#     'C:\Program Files (x86)\Microsoft Visual Studio\2017\Preview'
# )

# foreach($InstallPath in $InstallPaths) {
#     $DevShell = (Join-Path "$InstallPath" 'Common7\Tools\Microsoft.VisualStudio.DevShell.dll')
#     if (Test-Path "$DevShell") {
#         Import-Module "$DevShell"
#         $curDir = Get-Location
#         Enter-VsDevShell -VsInstallPath "$InstallPath" -StartInPath "$curDir" -DevCmdArguments -arch=x86
#         break
#     }
# }

If (Test-Path ./001.obj) {
    Remove-Item -Force 001.obj
}

If (Test-Path ./001.exe) {
    Remove-Item -Force 001.exe
}

& nasm.exe -f win32 001.asm
# & nasm.exe -f win64 001.asm

link /subsystem:console /nodefaultlib /largeaddressaware:no /entry:main 001.obj kernel32.lib
