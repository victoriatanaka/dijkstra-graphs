#!/bin/bash

# Aborta o script em caso de erro.
set -e

# Importa arquivo com funções auxiliares
source 'utils.sh'

# ------------------------------------------------------
p_info '-------------------------------------------------------------------'
p_info 'Rodando testes'
p_info '-------------------------------------------------------------------'
cd src
python main2.py ../graphs/dados.txt A Y
python main2.py ../graphs/dados.txt G Y
python main2.py ../graphs/dados.txt D U
python main2.py ../graphs/dados.txt Q J
python main2.py ../graphs/dados.txt V K
python main2.py ../graphs/dados.txt L H
python main2.py ../graphs/dados.txt T W
python main2.py ../graphs/dados.txt X K

p_ok "\nOK. Output gerado em /Desktop/caminhos.txt"



 

