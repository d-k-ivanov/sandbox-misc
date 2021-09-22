($python = Get-Command python.exe | Select-Object -ExpandProperty Definition); python.exe -m virtualenv -p $python venv
.\\venv\\Scripts\\activate.ps1
python -m pip install --upgrade pip
python -m pip install --upgrade jupyter
python -m pip install --upgrade Keras
python -m pip install --upgrade matplotlib
python -m pip install --upgrade nltk
python -m pip install --upgrade numpy
python -m pip install --upgrade numpy-stl
python -m pip install --upgrade pandas
python -m pip install --upgrade ray[default]
python -m pip install --upgrade seaborn
python -m pip install --upgrade sklearn
python -m pip install --upgrade tensorflow
# python -m pip install --upgrade powershell_kernel
# python -m powershell_kernel.install
