**graphcol**
============

Projeto de Gradução no curso de Ciência da Computação (PGC) da UFABC.
Visa ser um pacote Python com implementação de alguns algoritmos para o
problema de coloração em grafos. O PGC é desenvolvido por Wesley Lima de
Araujo e orientado pela Professora Doutora Carla Negri Lintzmayer. O
projeto dá continuidade a um trabalho de Iniciação Científica (IC) já
desenvolvido por aluno e orientadora sobre o mesmo tema, porém, o
enfoque da IC era um estudo teórico.

Para desenvolvimento do pacote está sendo usada a ferramenta
`Poetry <https://python-poetry.org/>`__ que automatiza uma parte
considerável dos processos de criar e atualizar um pacote disponível no
`PyPi <ttps://pypi.org/project/graphcol/>`__. Para usar o pacote
instale-o usando pip ``pip install graphcol``.

Algoritmos já implementados no pacote: \* Algoritmos de coloração
heurísticos gulosos: 1. Guloso 2. DSatur 3. RLF \* Algoritmos de
coloração metaheurísticos: 1. Coloração Tabu 2. Hill-Climbing 3.
Evolucionário Híbrido 4. Colônia de Formigas \* Algoritmos exatos: 1.
Lawler

Controle semântico das versões: ``x.y.z``, já avisando que não segue o
versionamento semântico padrão. \* ``x`` -> Versão major, passará a
contar 1 na primeira entrega final da biblioteca (todos os algoritmos
listados implementados). \* ``y`` -> Versão minor, alterada quando algum
algoritmo/funcionalidade novo for implementado com sucesso \* ``z`` ->
Versão patch, atualizada na correção de falhas e/ou adição de testes

Controle de versões: \* ``0.4.0`` -> Implementação do DSatur exato,
testes pré-lançamento oficial

Publicação da biblioteca
------------------------

Como já dito, estamos usando o framework Poetry para automatizar boa
parte das atividades necessárias para a publicação do pacote.

Seguem os principais comandos usados na publicação de uma nova versão do
pacote: 1. ``poetry check`` (Verifica se o .toml do projeto está OK) 2.
``poetry build`` (Builda os arquivos .tar.gz e .whl da versão) 3.
``poetry publish`` (Publica o pacote no PyPi)

Testes
------

Para realização dos testes unitários dos algoritmos utilizamos a
ferramenta pytest que fornece diversas funcionalidades para facilitar o
teste de funções e classes implementadas na linguagem Python.

Os testes realizados aqui visavam assegurar o bom funcionamento dos
algoritmos implementados através da validação da qualidade da solução.
Por exemplo, o algoritmo DSatur tem garantia matemática que para grafos
bipartidos o resultado devolvido é exato, então sua implementação é
testada com alguns grafos bipartidos e se nenhum deles foge desse
resultado. Também temos algumas das heurísticas que apresentam garantia
que o resultado devolvido é sempre uma solução viável, esse é outro
teste que realizamos.

Até o momento as seguintes implementações possuem testes unitários sobre
instâncias de grafos: \* Guloso \* DSatur \* RLF \* TabuCol \*
Hill-Climbing \* Evolucionário \* Colônia

Para entender melhor os testes veja as definições dos casos nos arquivos
dentro da pasta ``teste``. São os arquivos com nome começando em
``test_``.

Experimentos
------------

Outra etapa do projeto de PGC é a realização de experimentos com os
algoritmos implementados. Para realizar esses testes usaremos Jupyter
Notebooks que encontram-se na pasta experimentos.

Os testes serão realizados sobre o benchmark do
`DIMACS <https://mat.tepper.cmu.edu/COLOR/instances.html>`__ que
disponibiliza cerca de 80 instâncias do problema de coloração de grafos.
Algumas dessas instâncias já possuem o número cromático do grafo. Dentre
essas instâncias disponibilizadas nesse branchmark 20 foram escolhidas
para realização dos experimentos com os algoritmos implementados na
biblioteca. As instâncias usadas encontram-se na pasta
``experimentos -> instancias``

Cada grafo encontra-se em arquivos de texto no padrão DIMACS para
problemas de coloração de grafos. Na pasta de experimentos, basta
executar o script ``instancias.sh`` que baixa e descompacta um ``.tar``
com as instâncias.

Para adicionar ambiente virtual como kernel dos notebooks: 1. Ative o
ambiente virtual - ``source experimentos_graphcol/bin/activate`` 2.
Adicione o ambiente virtual aos kernels -
``python3 -m ipykernel install --user --name=experimentos_graphcol`` 3.
Installe os pacotes dependências - ``pip install -f requirements.txt``
4. Abra o JupyterLab - ``jupyter lab``
