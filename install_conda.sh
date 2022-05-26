MYPATH="/goinfre/$USER/miniconda3"
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH
$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle matplotlib seaborn
conda info --envs
Miniconda3-latest-Linux-x86_64.sh
