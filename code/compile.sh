#!/usr/bin/env bash

export CLASSPATH=".:/home/user_change/antlr-4.8-complete.jar:$CLASSPATH"
alias antlr4='java -jar /home/user_change/antlr-4.8-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'

if [ -d sadbeep/temp ]; then
    rm -r sadbeep/temp;
fi

echo "Iniciando compilação"

cd sadbeep
antlr4 sadbeep.g4 -o temp

cd temp
javac *.java

echo "Compilação terminada"

echo "Iniciando testes..."

if [ -d ../../tests ]; then

    if [ -f ../../tests/working.sadbeep ]; then
        echo "Testando arquivo funcional"
        grun sadbeep parse -gui < ../../tests/working.sadbeep
    else
        echo "Arquivo funcional não encontrado. Abortando..."
    fi

    if [ -f ../../tests/fail.sadbeep ]; then
        echo "Testando arquivo não funcional"
        grun sadbeep parse -gui < ../../tests/fail.sadbeep
    else
        echo "Arquivo não funcional não encontrado. Abortando..."
    fi
else 
    echo "Diretório de testes não encontrado. Abortando..."    
fi

cd ../../
