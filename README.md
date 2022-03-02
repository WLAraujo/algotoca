# algotoca

A ALGOTOCA visa ser uma biblioteca de algoritmos implementados pelo Laboratório de Teoria da computação, Otimização, Combinatória e Algoritmos (TOCA) da Universidade Federal do ABC (UFABC).

Atualmente, a biblioteca é o Trabalho de Conclusão de Curso de um aluno da gradução que é membro do laboratório. O TCC do aluno consiste em implementar algoritmos para coloração de grafos, tema já trabalhado pelo aluno em uma Iniciação Científica.

A biblioteca é construída e publicada usando o poetry, uma ferramenta de isolamento de ambientes e deploy de pacotes no pip. A algotoca está disponível no pip através do comando `pip install algotoca`. A biblioteca ainda está em fase primária de desenvolvimento e tem expectativa de lançamento de sua versão 1.0 em 2023.

Passos para instalação do poetry (https://python-poetry.org/docs/master/#installing-with-the-official-installer):
1. curl -sSL https://install.python-poetry.org | python3 -
2. export PATH="/$HOME/.local/bin:$PATH
3. poetry --version

Algoritmos já implementados no pacote:
1. Algoritmos de coloração heurísticos gulosos:
   1. Guloso
   2. DSatur
   3. RLF