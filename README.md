# Projeto Data Science

Os arquivos do projeto podem ser encontrados no Github à partir do seguinte link ***https://github.com/wheeout/ProjetoDS***

# Tema e dataset

O conjunto de dados foi obtido do Kaggle
(https://www.kaggle.com/ncaa/academic-scores). É intitulado **Academic Scores for NCAA Athletic Programs** e contém todas as pontuações acadêmicas da equipe atlética da Divisão 1 da NCAA de 2004 a 2014. O **National Collegiate Athletic Association** ou **NCAA** é uma associação composta de 1281 instituições, conferências, organizações e indivíduos que organizam a maioria dos programas de esporte universitário nos Estados Unidos.O conjunto de dados tem 6.511 linhas por 57 colunas. Cada linha contém os dados de uma única equipe atlética em cada instituição acadêmica. Os dados em cada linha incluem a pontuação APR das equipes atléticas, porcentagem de elegibilidade e taxa de retenção de 2004 a 2014, bem como sua pontuação APR de 4 anos, porcentagem de elegibilidade de 4 anos e taxa de retenção de 4 anos. Cada linha também contém as conferências atléticas das equipes. Cada aluno-atleta individual da equipe calcula a pontuação APR de uma equipe. Um aluno-atleta ganha 1 ponto por permanecer na escola ou se formar e 1 ponto por permanecer elegível (http://www.ncaa.org/about/what-apr). A pontuação de elegibilidade das equipes é calculada pela porcentagem de alunos-atletas da equipe que são elegíveis para jogar em todos os jogos da temporada esportiva. Um jogador pode se tornar inelegível devido a notas baixas e/ou reprovação nas aulas. Assim, um maior percentual de elegibilidade indica uma maior quantidade de alunos-atletas na equipe passando nas aulas. A taxa de retenção de uma equipe é calculada pelo fato de cada aluno-atleta da equipe se formar ou permanecer na escola. Assim, uma taxa de retenção mais alta indica uma porcentagem maior de alunos-atletas que permanecem na escola ou se formam em cada equipe.



# Codificando e limpando os dados

 - "School ID", "School Type" e "Sport Code" não tiveram impacto na
   análise. Todos os esportes que eram da divisão 2 ou da divisão 3
   foram removidos. Não havia dados suficientes em D2 ou D3, e é por
   isso que foi decidido removê-los para torná-lo um estudo de divisão
 - Houve vários casos em que os dados não estavam presentes. Nesses
   casos, os dados foram listados como “-99”. Como a intenção era
   possivelmente fazer dados de séries temporais, quaisquer pontos de
   dados ausentes distorceriam os resultados. Assim, os valores -99
   foram convertidos para NaN e então removidos do quadro de dados.
 - A partir daqui, os dados foram agrupados de três maneiras diferentes.
   Em cada forma, foi feita a média de todos os valores com base em como
   eles foram agrupados.
   
	 - Por Conferência: Os valores foram agrupados por conferência atlética.
	   Isso me deu uma ideia de quais conferências atléticas, como um todo,
	   eram academicamente melhores do que outras conferências.
	 - Por Escola: Os valores foram agrupados por instituição acadêmica.
	   Isso me deu uma ideia de quais atletas das escolas tiveram o melhor
	   desempenho acadêmico em todos os esportes.
	 - Por esporte: Os valores foram agrupados por esporte. Isso me deu uma
	   ideia de quais esportes, em geral, tinham o melhor desempenho
	   acadêmico. Isso significava, por exemplo, que o desempenho acadêmico
	   de cada time de futebol da escola era medido em relação a outro
	   esporte – por exemplo, o futebol feminino.
	   
 - Decidi que os dados mais interessantes se enquadravam no agrupamento
   por escola. Eu queria ver quais escolas, em média, tinham as melhores
   pontuações APR. Eu também queria ver quais escolas tinham as piores
   pontuações APR. Então, peguei as 10 instituições com as melhores
   pontuação APR e as 10 instituições com as piores pontuação APR e criei
   seus próprios quadros de dados.
 - Eu queria ver se as 10 melhores escolas da APR progrediram muito de
   2004 a 2014 e também se as 10 piores escolas da APR progrediram ou
   diminuíram de 2004 a 2014.
 - Mesclei as 10 piores e as 10 melhores escolas APR para criar um
   quadro de dados das 10 melhores e piores escolas ARP.
 - A partir daqui, criei um gráfico de dispersão comparando cada uma das
   pontuações de APR de 2004 da instituição com suas pontuações de APR
   de 2014.
   
	 - Como você pode ver no gráfico, as escolas com alto APR estão
	   agrupadas no canto, com pouca diferença entre 2004 e 2014.
	 - Enquanto isso, aqueles com pontuações baixas de APR estão localizados
	   no canto inferior esquerdo (como esperado), mas muito dispersos, o
	   que significa que algumas instituições mudaram para melhor e ainda
	   estavam entre as 10 últimas, enquanto a pontuação de APR de algumas
	   instituições piorou.
 - A partir daqui, decidi adicionar outro elemento ao gráfico. O tamanho
   do ponto no gráfico também indicava a porcentagem de elegibilidade de
   uma determinada instituição acadêmica. Assim, é mostrada uma
   correlação entre as pontuações da APR e a porcentagem de
   elegibilidade, porque todas as 10 melhores instituições têm um ponto
   maior do que as 10 últimas instituições.
 - Usei o pacote seaborn para representar graficamente os dados.
 - Em seguida, eu queria olhar mais para os dados da conferência. Decidi
   que há muitas conferências, 33 para ser exato, para agrupar por
   conferências. Então, eu os agrupei pelas “Conferências Power 5” que
   inclui o ACC, o Pac-12, o Big-12, o Big Ten e o SEC. Essas
   conferências são as mais proeminentes em termos atléticos, então eu
   queria ver como elas se comparam nas avaliações acadêmicas. Além
   disso, incluí a Ivy League neste agrupamento, considerando que a Ivy
   League é conhecida por seu sucesso acadêmico.
 - Em seguida, fundi meus dois conjuntos de dados para visualizar as
   pontuações da APR ao longo do tempo. Isso foi muito útil,
   considerando que não consegui plotar os dados como uma série temporal
   antes de fundir os dados.
 - Por fim, limpei todos os meus conjuntos de dados renomeando os nomes
   das colunas para que fossem facilmente legíveis quando fossem
   colocados nos gráficos.

## Resultados

O primeiro gráfico ***(arquivo Graph_1.png)*** ilustra a relação entre as 10 melhores instituições acadêmicas e as 10 piores instituições acadêmicas com base em sua “Pontuação APR ao longo de 4 anos”. A figura mostra um conjunto de pontos de dados no canto superior direito, todas as 10 principais instituições com pontos grandes e altas pontuações APR, indicando consistência com o sucesso acadêmico, bem como correlação com a porcentagem de elegibilidade. Uma pontuação de APR mais alta e mais consistente parece correlacionada com uma porcentagem de elegibilidade mais alta. Por outro lado, as 10 piores instituições são inconsistentes de 2004 a 2014 e também parecem correlacionadas com uma porcentagem de elegibilidade mais baixa.

O segundo gráfico ***(arquivo Graph_2.png)*** mostra a diferença na progressão entre as 10 melhores e as 10 piores instituições de 2004 a 2014, incluindo sua pontuação APR em cada um dos 10 anos. Este gráfico confirma nossa suposição do gráfico anterior de que as 10 melhores instituições APR têm pontuações APR consistentemente altas, enquanto as 10 piores instituições são inconsistentes em suas pontuações APR. Embora as cores possam ser um pouco difíceis de distinguir às vezes, o objetivo é destacar os grupos como um todo, em vez de olhar para instituições específicas.

O terceiro gráfico ***(arquivo Graph_3.png)*** mostra a progressão de 2004 a 2014 das “Conferências Power 5”, bem como das escolas da Ivy League. As linhas no gráfico representam a pontuação média da APR por conferência em cada um dos anos. Como você pode ver, houve um grande aumento de 2004 a 2014 nas pontuações do APR como um todo para cada uma das Conferências Power 5, enquanto as escolas da Ivy League permaneceram consistentemente altas em média ao longo dos 10 anos. As escolas power 5 fecharam a lacuna entre elas e as escolas da Ivy League, o que, esperançosamente, implica um maior compromisso com os acadêmicos do atletismo universitário como um todo.

Por fim, o quarto gráfico ***(arquivo Graph_4.png)*** ilustra a distribuição de cada uma das equipes atléticas individuais em cada uma das conferências. Cada ponto de dados representa cada equipe atlética em cada uma das conferências “Pontuação APR ao longo de 4 anos”, que obtém uma média da pontuação APR de cada equipe ao longo de 4 anos. A partir deste gráfico, podemos ver o grau de parentesco entre as equipes em cada conferência, bem como a diferença na pontuação média e total da APR entre as 6 conferências selecionadas.

