#!/usr/bin/env zsh

typeset -A repo_de

while read linha; do
    itens=("${(s/,/)linha}")
    repo_de[$itens[1]]=$itens[2]
done < $1

