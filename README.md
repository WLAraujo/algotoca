# graphcol

Projeto de Gradução no curso de Ciência da Computação (PGC) da UFABC. Visa ser um pacote Python com implementação de alguns algoritmos para o problema de coloração em grafos. O PGC é desenvolvido por Wesley Lima de Araujo e orientado pela Professora Doutora Carla Negri Lintzmayer. O projeto dá continuidade a um trabalho de Iniciação Científica (IC) já desenvolvido por aluno e orientadora sobre o mesmo tema, porém, o enfoque da IC era um estudo teórico.

Para desenvolvimento do pacote está sendo usada a ferramenta Poetry que automatiza uma parte considerável dos processos de criar e atualizar um pacote disponível no PyPi. PAra usar o pacote instale-o usando pip `pip install graphcol`.

Algoritmos já implementados no pacote:
* Algoritmos de coloração heurísticos gulosos:
   1. Guloso
   2. DSatur
   3. RLF
* Algoritmos de coloração metaheurísticos:
   1. Coloração Tabu
   2. Hill-Climbing
   3. Evolucionário Híbrido

Algoritmos ainda a serem implementados:
* Algoritmos metaheurísticos
  1. Colônia de Formigas
* Algoritmos exatos
  1. Lawler
  2. Brown 

Controle semântico das versões: `x.y.z`, já avisando que não segue o versionamento semântico padrão. 
* `x` -> Versão major, passará a contar 1 na primeira entrega final da biblioteca (todos os algoritmos listados implementados).
* `y` -> Versão minor, alterada quando algum algoritmo/funcionalidade novo for implementado com sucesso
* `z` -> Versão patch, atualizada na correção de falhas e/ou adição de testes

Controle de versões:
* `0.2.0` -> Mudança de nome da biblioteca (reset das versões) + Alterações no código de hill-climbing + Adição de testes do hill-climbing