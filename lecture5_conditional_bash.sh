#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then #diferente de py, semicolon e then são necessários
	echo "Everything ok"
else
	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi #fi seria um ponto final no conditional fi é if ao contrário

#os conditionals são baseados em exit status, onde se verifica o output de 0 (True) e another number (Error) 1, 2, 3....

#Test -- verifica se um comando é avaliado como True (0) or False (1)

if test -n "$PATH"; then echo "Your path is not empty"; fi
# -n -- checa se a variável está vazia ou não

#in another way

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

#brackets representa o Test, mas ela precisa estar num espaçamento antes e depois de fechar

#Test é um comando que avalia as condições de saída e verifica se há uma saída de status de 0 quando o condicional é verdadeiro, ou de 1, se é falso. 

#Em Bash, um "test" é um comando embutido usado para realizar avaliações condicionais. Ele permite que você teste condições, como igualdade de strings, comparação numérica, verificação de existência de arquivos e diretórios, entre outras.

#O comando "test" é frequentemente usado em conjunto com estruturas de controle condicional, como "if", "while" e "for", para tomar decisões com base em condições específicas.

#A sintaxe básica do comando "test" é:

#bash

#test condição; ou

#[ condição ]

#Por exemplo, para verificar se uma variável chamada "x" é igual a 5, você pode usar:

bash

if [ $x -eq 5 ]; then
  echo "x é igual a 5"
fi

#Aqui estão alguns exemplos de operadores comuns usados com o comando "test":

   # -eq: verifica se dois números são iguais.
   # -ne: verifica se dois números são diferentes.
   # -gt: verifica se um número é maior que outro.
   # -lt: verifica se um número é menor que outro.
   # -z: verifica se uma string é vazia.
   # -f: verifica se um arquivo existe e é regular.
   # -d: verifica se um diretório existe.
   
   
