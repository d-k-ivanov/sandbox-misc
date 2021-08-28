($python = Get-Command python.exe | Select-Object -ExpandProperty Definition); python.exe -m virtualenv -p $python venv
.\\venv\\Scripts\\activate.ps1
python -m pip install --upgrade pip
python -m pip install --upgrade jupyter
python -m pip install --upgrade numpy
python -m pip install --upgrade pandas
python -m pip install --upgrade matplotlib
# python -m pip install --upgrade powershell_kernel
# python -m powershell_kernel.install
