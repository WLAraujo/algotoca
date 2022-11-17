# **graphcol**

Projeto de Gradução no curso de Ciência da Computação (PGC) da UFABC. Visa ser um pacote Python com implementação de alguns algoritmos para o problema de coloração em grafos. O PGC é desenvolvido por Wesley Lima de Araujo e orientado pela Professora Doutora Carla Negri Lintzmayer. O projeto dá continuidade a um trabalho de Iniciação Científica (IC) já desenvolvido por aluno e orientadora sobre o mesmo tema, porém, o enfoque da IC era um estudo teórico.

Para desenvolvimento do pacote está sendo usada a ferramenta Poetry que automatiza uma parte considerável dos processos de criar e atualizar um pacote disponível no [PyPi](ttps://pypi.org/project/graphcol/). Para usar o pacote instale-o usando pip `pip install graphcol`.

Algoritmos já implementados no pacote:
* Algoritmos de coloração heurísticos gulosos:
   1. Guloso
   2. DSatur
   3. RLF
* Algoritmos de coloração metaheurísticos:
   1. Coloração Tabu
   2. Hill-Climbing
   3. Evolucionário Híbrido
   4. Colônia de Formigas

Algoritmos ainda a serem implementados:
* Algoritmos exatos
  1. Lawler
  2. Brown 

Controle semântico das versões: `x.y.z`, já avisando que não segue o versionamento semântico padrão. 
* `x` -> Versão major, passará a contar 1 na primeira entrega final da biblioteca (todos os algoritmos listados implementados).
* `y` -> Versão minor, alterada quando algum algoritmo/funcionalidade novo for implementado com sucesso
* `z` -> Versão patch, atualizada na correção de falhas e/ou adição de testes

Controle de versões:
* `0.2.1` -> Adição do algoritmo colônia de fôrmigas

## Publicação da biblioteca

Como já dito, estamos usando o framework Poetry para automatizar boa parte das atividades necessárias para a publicação do pacote. 

## Experimentos

Outra etapa do projeto de PGC é a realização de experimentos com os algoritmos implementados. Para realizar esses testes usaremos Jupyter Notebooks que encontram-se na pasta experimentos.

Os testes serão realizados sobre o benchmark do [DIMACS](https://mat.tepper.cmu.edu/COLOR/instances.html) que disponibiliza cerca de 80 instâncias do problema de coloração de grafos. Algumas dessas instâncias já possuem o número cromático do grafo.

Cada grafo encontra-se em arquivos de texto no padrão DIMACS para problemas de coloração de grafos. Na pasta de experimentos, basta executar o script `instancias.sh` que baixa e descompacta um `.tar` com as instâncias.

Para adicionar ambiente virtual como kernel dos notebooks:
1. Ative o ambiente virtual - `source experimentos_graphcol/bin/activate`
2. Adicione o ambiente virtual aos kernels - `python3 -m ipykernel install --user --name=experimentos_graphcol`
3. Installe os pacotes dependências - `pip install -f requirements.txt`
4. Abra o JupyterLab - `jupyter lab`
