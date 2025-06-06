# import streamlit as st
# import pandas as pd
# from datetime import datetime
# import yagmail
# from itens_classificados import itens_classificados

import streamlit as st
import pandas as pd
from datetime import datetime
import yagmail
from itens_classificados import itens_classificados
# from valores_unitarios import valores_unitarios




# 💵 Dicionário com valores unitários por item
valores_unitarios = {
   "492 - granola (KG)": 14.90,
   "495 - leite em po (KG)": 46.654,
   "496 - achocolatado (KG)": 32.5667,
   # "499 - açai(KG)": 21.2311,
   "499 - açai  (kg)": 21.2311,
   "574 - petit gateau (UN)": 20.90,
   "575 - calda de sorvete (KG)": 0.01,
   "597 - biscoito  (CX)": 4.98,
   "602 - bolacha maria/maizena(KG)": 0.00,
   "603 - geleia de frutas vermelhas (KG)": 0.00,
   "651 - cobertura chocolate (KG)": 34.50,
   "652 - cobertura morango (KG)": 18.90,
   "745 - mini cheesecake (CX)": 0.00,
   "335-ovos(UN)": 0.7726,
   "336 - salvia (KG)": 0.00,
   "337 - manjericao (KG)": 2.95,
   "338 - manjericao (KG)": 2.95,
   "339 - tomilho (KG)": 3.9895,
   "340 - louro (KG)": 80.687,
   "341 - hortela (UN)": 2.95,
   "342 - cenoura (KG)": 3.772,
   "343 - beterraba (UN)": 4.9503,
   "344 - berinjela (KG)": 6.8392,
   "454 - pimenta paprica doce (KG)": 14.4529,
   "455 - pimenta paprica defumada (KG)": 22.9823,
   "285 - presunto fatiado (KG)": 25.34,
"456 - pimenta paprica picante (KG)": 24.3007,
"461 - pimenta calabresa (KG)": 0.01,
"509 - aioli (KG)": 0.01,
"512 - salsinha verde (KG)": 2.95,
"520 - carne moida (KG)": 15.66,
"524 - peixe file (vilmar) (KG)": 1.00,
"569 - oleo algodao  balde (UN)": 10.12,
"697 - ovos de codorna (UN)": 27.06,
"781 - abacate (KG)": 18.66,
"824 - peixe inteiro (vilmar) (KG)": 0.00,
   
    "286 - peito peru (KG)": 51.54,
    "287 - copa (KG)": 12.07,
    "288 - salame (KG)": 81.12,
    "289 - presunto parma (KG)": 25.90,
    "294 - pao mini ciabata (KG)": 25.83,
    "295 - pao ciabata (KG)": 33.99,
    "297 - pao baguete 250g (KG)": 0.01,
    "302 - linguiça toscana frango (KG)": 10.14,
    "359 - carne de siri  (KG)": 42.88,
    "361 - marisco (KG)": 21.09,
    "362 - ostra (UN)": 0.00,
    "364 - camarao rosa (KG)": 1.00,
    "365 - camarao cinza (KG)": 56.94,
    "366 - lula (KG)": 21.40,
    "474 - salgadinho doritos (KG)": 0.00,
    "476 - lombo canadense (KG)": 0.00,
    "481 - pao italiano (KG)": 29.70,
    "482 - milho (KG)": 0.00,
    "484 - pao de queijo (KG)": 21.39,
    "493 - fermento quimico (KG)": 10.78,
    "494 - fermento biologico seco (KG)": 13.44,
    "505 - geleia de pimenta (KG)": 0.10,
    "513 - cebolinha verde (KG)": 2.95,
"514 - papel alumiun (UN)": 0.0147,
"521 - batata frita  (KG)": 12.998,
"534 - requeijao catupiry  (KG)": 28.89,
"622 - pao australiano (KG)": 20.371,
"623 - linguiça calabresa (KG)": 21.7961,
"624 - linguiça paio (KG)": 22.6917,
"690 - pao portugues (KG)": 18.8672,
"691 - pao fazenda (KG)": 26.5812,
"692 - pao de queijo com parmesao (KG)": 35.3712,
"693 - massa folhada (UN)": 14.9907,
"725 - ostra (UN)": 2.9513,
"779 - pao baguete 100g (KG)": 19.2893,
"780 - pao baguete 125g (KG)": 22.0247,
"783 - cafe soluvel (KG)": 21.6889,
"786 - pao de queijo doce (KG)": 30.7248,
"787 - pao de queijo rech catupiry (KG)": 37.2411,
"817 - linguiça toscana  (KG)": 27.1946,
"822 - camarao argentino (KG)": 55.9225,
"868 - camarao vennamei  VG (KG)": 44.9937,
"870 - pao mini couvert (KG)": 19.5427,
"933 - papel toalha (UN)": 2.6994,
"317 - cebola branca (KG)": 5.4028,
"318 - cebola roxa (KG)": 6.6212,
"319 - alho  (KG)": 21.538,
"320 - alho poro (UN)": 3.1028,
"321 - tomate salada (KG)": 6.3025,
"322 - tomate cereja (KG)": 14.8298,
"323 - tomate molho (KG)": 5.0733,
"325 - pimentao amarelo (KG)": 14.7813,
"326 - pimentao verde (KG)": 5.8755,
"327 - pimentao vermelho (KG)": 13.1528,
"328 - rucula (KG)": 13.0976,
"329 - alface americana (KG)": 8.7377,
"330 - alface roxa (KG)": 9.1755,
"331 - acelga (UN)": 6.7241,
"332 - pepino japones  (KG)": 6.8713,
"333 - repolho branco  (KG)": 4.7448,
"334 - repolho roxo (KG)": 7.9485,
"345 - abobrinha (KG)": 7.1131,
"346 - couve-flor (KG)": 10.3326,
"347 - couve manteiga (UN)": 5.5674,
"348 - brocolis  (KG)": 10.5839,
"349 - pimenta dedo de moca (KG)": 14.1054,
"350 - batata salsa baroa (KG)": 8.8216,
"351 - batata asterix (KG)": 5.4361,
"352 - fruta banana da terra (KG)": 6.6053,
"353 - fruta banana caturra (KG)": 4.7888,
"354 - fruta mamao papaia (KG)": 5.6339,
"355 - fruta mamao formosa (KG)": 5.1916,
"356 - fruta melancia (KG)": 3.4621,
"357 - fruta melao (KG)": 5.4573,
"358 - fruta maça (KG)": 6.9493,
"477 - fruta manga (KG)": 6.9028,
"483 - palmito (KG)": 30.0852,
"485 - champignon (KG)": 22.2437,
"488 - feijao branco (KG)": 9.3611,
"489 - feijao carioca (KG)": 7.7607,
"490 - linhaça dourada (KG)": 17.2536,
"527 - molho pesto (KG)": 25.1732,
"541 - molho alcaparas e mel  (KG)": 26.7635,
"544 - molho caeser (KG)": 20.6312,
"545 - crotons (KG)": 24.0226,
"619 - agriao (KG)": 7.3429,
"637 - cebola miuda conserva (KG)": 11.6247,
"639 - alecrim  (UN)": 1.5312,
"642 - fruta banana branca (KG)": 4.9779,
"664 - sache vinagre (UN)": 0.3257,
"687 - alface crespa (KG)": 8.9986,
"695 - vagem (KG)": 9.1447,
"775 - feijao fradinho (KG)": 8.7635,
"859 - linhaça marron (KG)": 13.7913,
"931 - pepino em conserva (KG)": 9.7758,
"931 - pepino em conserva (KG)": 9.7758,
"272 - manteiga  (KG)": 37.34,
"273 - creme de leite nata  45% (KG)": 28.95,
"291 - pao mini sovadinho (KG)": 15.5,
"292 - pao mini frances (KG)": 15.2,
"293 - pao fatiado tradicional (UN)": 11.75,
"480 - pao fatiado integral (UN)": 14.9,
"530 - molho mostarda iogurte (KG)": 27.85,
"749 - pao fatiado batata doce (UN)": 17.2,
"750 - pao fatiado caseiro (UN)": 18.6,
"8 - Agua s/gas (UN)": 2.49,
"12 - Agua c/gas (UN)": 3.1,
"13 - agua tonica lata (UN)": 3.9,
"15 - agua tonica zero lata (UN)": 4.2,
"16 - coca cola lata (UN)": 4.45,
"17 - coca zero lata (UN)": 4.5,
"18 - fanta laranja lata (UN)": 4.35,
"19 - guarana lata (UN)": 4.25,
"20 - guarana zero lata (UN)": 4.3,
"21 - sprite lata (UN)": 4.4,
"22 - schweppers citrus lata (UN)": 4.6,
"26 - energetico red bull lata (UN)": 7.95,
"27 - energetico red bull tropical lata (UN)": 8.2,
"192 - coco gelado  (UN)": 6.75,
"784 - guarana pet (UN)": 6.5,
"913 - energetico red bull sugar free (UN)": 8.15,
"153 - picole nestle moca cone (UN)": 5.95,
"154 - picole nestle prestigio (UN)": 5.9,
"155 - picole nestle classico ao leite (UN)": 5.85,
"156 - picole nestle baton (UN)": 5.75,
"157 - picole nestle chambinho morango (UN)": 5.8,
"158 - picole nestle diamante negro (UN)": 6.1,
"159 - picole nestle fine dentadura (UN)": 6.0,
"160 - picole nestle fine torcao (UN)": 6.05,
"161 - picole nestle fine tubes morango (UN)": 6.1,
"162 - picole nestle kit kat (UN)": 6.25,
"163 - picole nestle la fruta coco (UN)": 5.7,
"164 - picole nestle la fruta limao (UN)": 5.65,
"165 - picole nestle la fruta morango (UN)": 5.8,
"166 - picole nestle la fruta uva (UN)": 5.9,
"167 - picole nestle laka (UN)": 6.35,
"168 - picole nestle laka oreo (UN)": 6.5,
"169 - picole nestle mega alfajor (UN)": 6.75,
"170 - picole nestle mega cheesecake (UN)": 6.8,
"171 - picole nestle mega classico (UN)": 6.7,
"172 - picole nestle mega tres chocolates (UN)": 6.85,
"173 - picole nestle moca brigadeiro (UN)": 6.6,
"174 - picole nestle sonho de valsa (UN)": 6.65,
"175 - picole nestle oreo (UN)": 6.95,
"176 - picole nestle oreo cone (UN)": 6.9,
"177 - picole nestle sanduiche oreo (UN)": 7.0,
"568 - sorvete nestle pote creme (LT)": 23.9,
"730 - picole nestle fine tubes tutti frutti (UN)": 5.95,
"731 - picole nestle mega amendoas (UN)": 6.95,
"732 - picole nestle garoto bombom (UN)": 6.85,
"733 - picole nestle kitkat (UN)": 6.75,
"734 - picole nestle cone kitkat (UN)": 6.9,
"752 - picole nestle mega trufa branco (UN)": 6.85,
"899 - picole pote oreo bites (UN)": 24.9,
"909 - picole nestle la fruta maracuja (UN)": 5.9,
"910 - picole nestle mega pistache (UN)": 6.95,
"911 - picole nestle crocante (UN)": 6.8,
"119 - vinho tinto luigi bosca cabernet sauviginon (UN)": 95.0,
"120 - vinho tinto terranoble carmenere (UN)": 59.9,
"121 - vinho tinto claude val paul mas (UN)": 69.5,
"122 - vinho tinto intis cabernet sauviginon (UN)": 42.9,
"123 - vinho tinto la linda malbec (UN)": 75.0,
"124 - vinho tinto marques de montemor quinta da pansel (UN)": 88.0,
"125 - vinho tinto olapo melot los lirios (UN)": 57.0,
"126 - vinho tinto rey de copas tempranillo (UN)": 49.9,
"127 - vinho tinto villa cardeto sangiovese (UN)": 65.0,
"128 - vinho tinto terranoble cabernet sauvignon 375ml (UN)": 34.5,
"728 - vinho tinto alta yari malbec (UN)": 64.0,
"729 - vinho tinto sutil reserva carmenere (UN)": 66.9,
"821 - vinho tinto intis malbec (UN)": 44.0,
"890 - vinho tinto uko estate pinot noir (UN)": 78.5,
"891 - vinho tinto uko estate cabernet sauvignon (UN)": 79.0,
"892 - vinho tinto mister uko malbec (UN)": 82.0,
"893 - vinho tinto conclave nocturno cabernet franc (UN)": 90.0,
"914 - vinho tinto conclave nocturno malbec (UN)": 88.0,
"107 - vinho branco amalaya torrontes riesling (UN)": 69.0,
"108 - vinho branco fausto pizzato chardonnay (UN)": 89.9,
"110 - vinho branco intis sauvignon blanc (UN)": 44.9,
"111 - vinho branco la linda chardonnay (UN)": 74.0,
"112 - vinho branco marques de toledo (UN)": 59.0,
"113 - vinho branco muros antigos (UN)": 62.0,
"114 - vinho branco olapo chardonnay (UN)": 56.0,
"115 - vinho branco claude val paul mas gewustraminer (UN)": 71.0,
"116 - vinho branco thera sauvignon blanc (UN)": 82.5,
"117 - vinho branco vila cardeto pinot grigio (UN)": 67.0,
"118 - vinho branco terranoble chardonnay 375ml (UN)": 38.5,
"884 - vinho branco uko estate cherdonnay (UN)": 73.0,
"885 - vinho branco uko estate sauvignon blanc (UN)": 74.5,
"886 - vinho branco uko estate dulce (UN)": 75.0,
"887 - vinho branco fumata bianca sauvignon (UN)": 70.0,
"129 - vinho rose claude val paul mas (UN)": 68.0,
"130 - vinho rose las moras shyraz (UN)": 61.0,
"131 - vinho rose thera rose (UN)": 84.0,
"888 - vinho uko estate malbec rose (UN)": 72.0,
"889 - vinho conclave reserva rose (UN)": 79.5,
"102 - espumante bossa dem sec n2 (UN)": 49.9,
"103 - espumante bossa moscatel (UN)": 47.5,
"104 - espumante bossa brut (UN)": 51.0,
"105 - espumante fausto demi sec (UN)": 69.0,
"106 - espumante la linda extra brut (UN)": 89.9,
"894 - espumante cambiado dulce natural (UN)": 42.0,
"895 - espumante allegra rose extra brut (UN)": 58.0,
"912 - espumante chandon demi sec (UN)": 99.9,
"929 - espumante chandon brut (UN)": 104.9,
"28 - cerveja original 600ml (UN)": 7.49,
"29 - cerveja heineken long neck (UN)": 5.89,
"30 - cerveja corona long neck (UN)": 6.99,
"31 - balde/heineken long neck 10und (UN)": 58.9,
"32 - balde/corona long neck 10und (UN)": 64.9,
"33 - cerveja heineken long neck zero (UN)": 5.79,
# "773 - chop schornstein (UN)": 10.5,
"774 - cerveja heineken 600ml (UN)": 7.99,
"132 - garrafa aperol (UN)": 69.9,
"133 - garrafa cachaca (UN)": 12.9,
"134 - garrafa whisk jack daniels (UN)": 129.0,
"135 - garrafa martine rosso (UN)": 49.9,
"136 - garrafa jagermaister (UN)": 109.0,
"137 - garrafa gin tanqueray (UN)": 119.9,
"138 - garrafa tequila ouro (UN)": 99.0,
"139 - garrafa tequila prata (UN)": 97.5,
"140 - garrafa vodka absolut (UN)": 89.9,
"141 - garrafa vodka smirnoff (UN)": 29.9,
"142 - garrafa vodka ciroc (UN)": 149.0,
"143 - garrafa whisk ballantinnes 12 anos (UN)": 139.0,
"144 - garrafa whisk black label12 anos (UN)": 159.9,
"145 - garrafa whisk red label (UN)": 109.9,
"147 - combo smirnoff (UN)": 89.9,
"149 - garrafa campari (UN)": 42.9,
"150 - combo whisk jack daniels (UN)": 159.0,
"378 - garrafa bacardi carta blanca (UN)": 62.0,
"385 - garrafa gin gordons (UN)": 59.9,
"607 - garrafa amarula (UN)": 69.0,
"608 - garrafa licor 43 (UN)": 119.0,
"720 - garrafa whisk chivas 12 anos (UN)": 129.9,
"777 - garrafa gin bombay (UN)": 119.0,
"778 - garrafa rum montila branca (UN)": 27.9,
"71 - dose amarula (UN)": 9.0,
"73 - dose bacardi (UN)": 8.0,
"74 - dose campari (UN)": 7.5,
"75 - dose cachaça (UN)": 5.0,
"76 - dose gin tanqueray (UN)": 10.0,
"77 - dose jack daniels (UN)": 11.0,
"78 - dose jagermeister (UN)": 11.0,
"79 - dose licor 43 (UN)": 12.0,
"80 - dose steinhaeguer (UN)": 8.5,
"81 - dose tequila ouro (UN)": 9.0,
"82 - dose tequila prata (UN)": 8.5,
"83 - dose vodka absolut (UN)": 8.0,
"84 - dose vodka ciroc (UN)": 10.0,
"85 - dose vodka smirnoff (UN)": 6.0,
"86 - dose whisky 12 anos (UN)": 12.0,
"87 - dose whisky 8 anos (UN)": 9.0,
"193 - fruta limao taiti (KG)": 4.5,
"195 - polpa morango (KG)": 18.9,
"196 - polpa maracuja (KG)": 14.8,
"197 - fruta kiwi (KG)": 18.7,
"198 - polpa abacaxi (KG)": 9.9,
"199 - fruta laranja (KG)": 4.2,
"200 - fruta limao siciliano (KG)": 6.9,
"201 - anis estrelado (KG)": 59.0,
"202 - pimenta zinbro (KG)": 41.7,
"203 - pimenta rosa (KG)": 64.0,
"204 - hibisco (KG)": 39.5,
"205 - gelo cubo 5 kg (KG)": 8.0,
"206 - gelo escama (KG)": 7.5,
"207 - açucar refinado (branco) (KG)": 4.6,
"208 - gengibre (KG)": 6.9,
"209 - açucar organico (KG)": 5.9,
"210 - clara de ovo pastelrizada (LT)": 14.0,
"211 - capsula de gas co2 (UN)": 3.2,
"212 - agua c/gas 1.5 ltros (UN)": 4.9,
"213 - espumante salton brut (UN)": 32.0,
"214 - canudo bio (UN)": 0.35,
"379 - garrafa cointreau (UN)": 112.0,
"381 - garrafa steinhaeguer (UN)": 38.5,
"383 - garrafa sake (UN)": 34.0,
"384 - agua tonica 1.5 l (UN)": 6.0,
"386 - hibisco (KG)": 39.5,
"387 - agua s/gas 20 litros (LT)": 0.57,
"388 - xarope de gengibre (LT)": 22.9,
"389 - espuma moscow mule (LT)": 19.5,
"393 - polpa abacaxi com hortela (KG)": 12.9,
"398 - xarope de cramberry (UN)": 19.9,
"399 - xarope de franboesa (UN)": 19.9,
"400 - xarope de roma (UN)": 19.9,
"401 - xarope de cha verde (UN)": 19.9,
"402 - xarope de cha preto (UN)": 19.9,
"561 - garrfa de martine dry (UN)": 45.0,
"565 - fruta acerola (KG)": 11.3,
"566 - polpa mirtilho (KG)": 24.6,
"567 - canudo mexedor (UN)": 0.25,
"611 - xarope mix pessego e maracuja (ML)": 18.9,
"640 - ovo pastelrizada (LT)": 14.0,
"656 - xarope de frutas vermelhas (LT)": 21.5,
"661 - açucar sache (KG)": 6.9,
"683 - fruta laranja bahia (KG)": 4.8,
"686 - fruta maracuja (KG)": 7.6,
"688 - copo vidro (UN)": 2.5,
"696 - açucar confeitero (KG)": 7.3,
"710 - VASILHAME 20 LITROS (LT)": 12.0,
"715 - suco manguary maracuja (UN)": 5.8,
"721 - xarope cha verde (UN)": 19.9,
"722 - xarope cranberry (UN)": 19.9,
"723 - xarope framboesa (UN)": 19.9,
"726 - champanheira branca (UN)": 22.0,
"727 - saca rolha (UN)": 6.5,
"742 - licor creme cassis (UN)": 48.0,
"790 - polpa amora (KG)": 23.9,
"830 - emustab (KG)": 16.5,
"844 - canudo bio mexedor (UN)": 0.28,
"867 - espumante salton demi sec (UN)": 31.5,
"920 - xarope maçã verde (UN)": 19.9,
"925 - adoçante sache (KG)": 15.0,
"926 - adoçante (KG)": 18.0,
"100 - suco del valle uva (UN)": 4.5,
"101 - suco del valle pessego (UN)": 4.3,
"826 - saco de lixo (UN)": 0.65,
"827 - detergente (UN)": 2.2,
"828 - agua sanitaria (UN)": 1.9,
"834 - luva latex (UN)": 0.75,
"846 - alcool 70% (UN)": 3.6,
"853 - esfregao (UN)": 9.5,
"864 - esponja lava louça (UN)": 0.85,
"865 - bombril (UN)": 0.6,
"903 - touca descartavel (UN)": 0.2,
"905 - faca descartavel (UN)": 0.18,
"906 - colher descartavel (UN)": 0.18,
"907 - garfo descartavel (UN)": 0.18,
"927 - lustra moveis (UN)": 6.9,
"932 - desincrustante (UN)": 7.2,
"934 - plastico filme (UN)": 5.6,
"935 - esponja lava louça (UN)": 0.9,
"181 - cigarro marlboro (UN)": 9.0,
"182 - cigarro dunhill (UN)": 9.2,
"274 - queijo parmessao (KG)": 42.7,
"277 - queijo gorgonzola (KG)": 39.5,
"278 - queijo brie (KG)": 55.0,
"280 - cheddar (KG)": 28.9,
"281 - cream cheese (KG)": 27.5,
"283 - creme de leite (KG)": 10.5,
"284 - leite (LT)": 4.2,
"298 - file mignon (KG)": 68.9,
"299 - entrecot (KG)": 59.3,
"300 - coxa sobre coxa de frango (KG)": 10.7,
"301 - peito de frango (KG)": 14.5,
"303 - miolo da alcatra (KG)": 54.2,
"304 - costela bovina (KG)": 32.8,
"309 - carne seca (KG)": 49.7,
"310 - bacon (KG)": 28.3,
"311 - linguiça calabresa (KG)": 22.4,
"312 - linguiça paio (KG)": 21.9,
"313 - frango passarinho (KG)": 12.0,
"314 - picanha suina (KG)": 29.5,
"316 - costela suina (KG)": 26.7,
"450 - sal marinho fino (KG)": 3.2,
"451 - sal marinho grosso (KG)": 2.9,
"452 - pimenta do reino (KG)": 48.5,
"457 - cravo da india (KG)": 89.7,
"459 - canela em po (KG)": 38.0,
"460 - canela em pau (inteira) (KG)": 42.3,
"466 - açafrao da terra (KG)": 29.8,
"467 - hondashi (KG)": 98.2,
"478 - mandioca aipim (KG)": 3.9,
"487 - feijao preto (KG)": 5.2,
"503 - cogumelos paris (KG)": 39.9,
"504 - cogumelos funghi seco (KG)": 122.0,
"559 - caldo de galinha (KG)": 12.7,
"593 - pimenta do reino grao (KG)": 49.0,
"625 - panceta suina (KG)": 31.4,
"636 - queijo gouda (KG)": 49.2,
"655 - paleta musculo bovino (KG)": 35.7,
"699 - queijo ricota (KG)": 20.6,
"701 - coxao duro (KG)": 36.1,
"741 - sal refinado 1g (KG)": 2.8,
"818 - sal cebola/salsa (KG)": 12.5,
"908 - peito de frango defumado (KG)": 24.9,
"275 - queijo provolone (KG)": 44.6,
"368 - file de peixe linguado (KG)": 58.75,
"370 - file tilapia (KG)": 34.2,
"373 - bacalhau (KG)": 79.3,
"374 - pirarucu (KG)": 61.7,
"375 - banda tambaqui (KG)": 42.9,
"376 - costelinha de tambaqui (KG)": 45.5,
"377 - salmao (KG)": 89.0,
"403 - azeite de dende (ML)": 21.8,
"404 - azeite de oliva (ML)": 25.3,
"405 - amido de milho (KG)": 6.7,
"406 - tomate seco (KG)": 37.0,
"407 - azeitona preta (KG)": 18.4,
"408 - azeitona verde (KG)": 14.9,
"409 - ovo de codorna (KG)": 9.5,
"410 - vinagre aceto balsamico (ML)": 12.1,
"411 - shoyo (ML)": 9.3,
"412 - oleo de soja (ML)": 6.6,
"415 - leite de coco (ML)": 8.9,
"416 - leite de condensado (ML)": 10.5,
"417 - arroz parboilizado (KG)": 4.8,
"418 - arroz branco (KG)": 4.3,
"419 - arroz arboreo (KG)": 15.0,
"420 - massa espaguete (KG)": 5.9,
"421 - massa pene (KG)": 5.7,
"422 - massa linguine (KG)": 6.3,
"423 - massa nhoque (KG)": 9.0,
"424 - massa pastel (KG)": 7.2,
"425 - massa ravioli (KG)": 10.8,
"426 - castanha para (KG)": 68.2,
"427 - castanha de caju (KG)": 64.4,
"428 - mostarda em graos (KG)": 23.6,
"429 - nozes (KG)": 59.9,
"430 - damasco (KG)": 48.5,
"431 - fruta mirtilo (KG)": 35.0,
"432 - fruta amora (KG)": 34.0,
"434 - fruta framboesa (KG)": 36.0,
"435 - vinagre maça (ML)": 5.3,
"436 - vinagre de alcool branco (ML)": 3.2,
"437 - catchup (KG)": 7.5,
"438 - maionese (KG)": 8.2,
"439 - molho ingles (KG)": 11.7,
"440 - mel com favo (KG)": 29.5,
"441 - alcaparras (KG)": 43.6,
"442 - farinha de trigo (KG)": 4.0,
"444 - farinha de panko (KG)": 9.8,
"445 - farinha de mandioca (KG)": 5.1,
"446 - vinho tinto garrafao (ML)": 22.5,
"447 - vinho branco garrafao (ML)": 21.8,
"448 - garrafa conhaque (ML)": 27.6,
"462 - ajinomoto (KG)": 13.9,
"465 - açucar demerara (KG)": 6.4,
"470 - massa fettutine (KG)": 7.2,
"475 - vinagre de arroz (ML)": 6.9,
"491 - amendoas laminadas (KG)": 52.7,
"497 - fuba de milho (KG)": 4.8,
"508 - FAROFA (KG)": 6.1,
"531 - pao de alho (KG)": 12.3,
"532 - salada pratos (KG)": 7.0,
"533 - batata soute (KG)": 9.4,
"587 - chimichurry (KG)": 25.6,
"588 - cominho em po (KG)": 19.3,
"591 - noz moscada (KG)": 33.2,
"592 - pimenta do reino branca (KG)": 42.0,
"594 - file de pescada cambucu (KG)": 57.1,
"596 - mostarda dijon (UN)": 8.5,
"598 - salsao (UN)": 4.3,
"600 - batata lavada (KG)": 3.7,
"648 - fruta ameixa (KG)": 9.8,
"658 - jantar (UN)": 25.0,
"663 - polvo (KG)": 66.5,
"672 - alho em po a granel (KG)": 38.2,
"673 - cajun picante em po granel (KG)": 42.7,
"674 - cebola em po a granel (KG)": 25.9,
"676 - coentro em po a granel (KG)": 19.8,
"677 - lemon pepper em po a granel (KG)": 34.6,
"678 - fumaça em po a granel (KG)": 45.0,
"679 - manjerona em po a granel (KG)": 30.1,
"680 - salsa em po a granel (KG)": 28.3,
"681 - salvia em po a granel (KG)": 26.7,
"685 - lombo suino (KG)": 23.4,
"689 - file dourado (KG)": 48.6,
"698 - catchup (UN)": 4.2,
"706 - gema de ovo pasteurizada (UN)": 6.9,
"717 - file de costela porc ancho (KG)": 52.3,
"748 - mel fracionado (cafe) (UN)": 3.7,
"776 - file mignon suino (KG)": 36.5,
"782 - castanha do brasil media (KG)": 59.9,
"785 - massa papardeli (KG)": 12.0,
"788 - massa caseira (KG)": 10.7,
"815 - tainha fresca (KG)": 25.6,
"829 - acen bovino (KG)": 38.8,
"833 - flor comestivel (UN)": 2.9,
"835 - broto alface crespa (UN)": 1.75,
"836 - broto alface mimosa (UN)": 1.65,
"837 - broto alface lisa (UN)": 1.8,
"838 - broto cenoura (UN)": 1.9,
"839 - broto agriaõ (UN)": 1.95,
"840 - broto beterraba (UN)": 1.85,
"841 - broto coentro (UN)": 1.9,
"842 - broto mostarda (UN)": 1.9,
"845 - brocolis comun (UN)": 3.75,
"847 - broto rabanete (UN)": 1.7,
"848 - broto rucula (UN)": 1.8,
"849 - broto amaranto (UN)": 2.1,
"852 - arroz integral (KG)": 6.8,
"855 - file saithe bacalhau (KG)": 47.2,
"860 - massa lasanha/canelone (KG)": 12.9,
"866 - broto repolho (UN)": 1.6,
"869 - broto couve roxa (UN)": 1.85,
"896 - broto alface roxa (UN)": 1.75,
"897 - amaciante de carne (KG)": 18.6,
"917 - alho em flocos (KG)": 34.7,
"921 - mostarda (UN)": 4.2,
"937 - pitaia (KG)": 14.5,
"472 - cafe tradicional (KG)": 19.9,
"536 - polvilho azedo (KG)": 6.8,
"550 - manteiga fracionada (sache-cafe) (UN)": 0.45,
"552 - queijo coalho (KG)": 33.75,
"560 - adoçante (LT)": 9.8,
"582 - cream cheese fracionado (cafe) (UN)": 1.25,
"583 - geleias fracionadas (cafe) (UN)": 1.4,
"589 - gergelim branco (KG)": 22.3,
"590 - gergelim preto (KG)": 24.6,
"605 - fruta abacaxi (KG)": 6.25,
"609 - uva rubi (KG)": 7.75,
"616 - cha camomila (UN)": 2.15,
"617 - cha hortela (UN)": 2.05,
"628 - uva passa preta (KG)": 19.9,
"634 - povilho azedo (KG)": 6.8,
"654 - queijo mussarela fatiado (KG)": 33.2,
"665 - aroma artificial baunilha (ML)": 4.75,
"666 - chantily 1L (KG)": 14.9,
"667 - chocolate barra ao leite (KG)": 27.8,
"668 - chocolate em pó 50% (KG)": 22.7,
"669 - chocolate granulado (KG)": 19.6,
"670 - coco ralado (KG)": 18.2,
"671 - doce de leite (KG)": 15.9,
"675 - cha erva doce a granel (KG)": 28.5,
"694 - uva italia (KG)": 7.2,
"702 - chocolate barra branco (KG)": 28.4,
"708 - salsicha congelada (KG)": 12.1,
"709 - mortadela fatiada (KG)": 13.75,
"712 - mexedor para cafe (UN)": 0.1,
"718 - fruta figo (UN)": 1.6,
"743 - mini croissant chocolate (KG)": 24.3,
"744 - mini croissant frango/requeijao (KG)": 26.5,
"747 - mistura de bolo (UN)": 7.75,
"751 - mini croissant s/recheio (KG)": 23.8,
"753 - chia semente (UN)": 3.85,
"760 - mini croissant goiabada (KG)": 25.4,
"761 - mini couvert (KG)": 11.9,
"768 - cha cidreira (UN)": 2.10,
"769 - cha frutas vermelhas (UN)": 2.15,
"770 - mini coxinha de frango (KG)": 26.75,
"771 - mini bolinha de queijo (KG)": 25.95,
"819 - aroma baunilha (UN)": 4.60,
"831 - pao sete graos (UN)": 2.90,
"916 - nectarina (KG)": 9.45,
"930 - chocolate sonho de valsa (KG)": 34.2,
"939 - cha alecrim (UN)": 2.25,
"276 - queijo mussarela peça (KG)": 33.10,
"515 - molho tomate (KG)": 6.95,
"517 - demmi glass (KG)": 18.5,
"518 - molho bechamel (KG)": 15.6,
"519 - caldo legumes (LT)": 8.7,
"522 - oleo de carvao (LT)": 12.9,
"528 - burrata (UN)": 7.95,
"535 - bicarbonato de sodio (KG)": 9.15,
"537 - coca cola litros (UN)": 7.6,
"547 - fruta morango natural (KG)": 13.25,
"548 - molho roti madeira (KG)": 18.25,
"551 - linguiça bock (KG)": 23.75,
"554 - pao medieval (australiano) (KG)": 16.6,
"555 - pao mini brioche (KG)": 17.3,
"556 - peixe tamboriu (KG)": 29.9,
"557 - mozzarela de bufala (bolinha cerejinha) (KG)": 39.5,
"562 - coca cola zero 2 litros (UN)": 8.9,
"563 - guarana 2 litros (UN)": 7.45,
"585 - charque (KG)": 33.8,
"595 - grao de bico (KG)": 12.5,
"613 - fruta pera (KG)": 7.3,
"614 - abobora comum (KG)": 4.6,
"615 - linguiça blumenau (KG)": 26.5,
"618 - gergelim em pasta (UN)": 7.75,
"626 - kit feijoada (KG)": 31.9,
"629 - extrato de tomate (UN)": 3.45,
"630 - molho de salada lisa (UN)": 4.15,
"632 - suco de uva 1,5 (UN)": 6.8,
"633 - suco de laranja 5 litros (LT)": 18.9,
"635 - molho tare (LT)": 14.75,
"638 - aipim ou mandioca (KG)": 5.85,
"645 - pessego em caldas (UN)": 6.9,
"646 - sagu (KG)": 4.25,
"649 - massa conchiglioni (CX)": 9.95,
"650 - tapioca granulada (KG)": 7.1,
"653 - CHANPIGNON (KG)": 18.5,
"659 - arroz de sushi (KG)": 10.4,
"660 - massa talharin (KG)": 6.75,
"684 - mozzarela de bufala peça (KG)": 38.7,
"700 - manguari concentrado (UN)": 6.9,
"703 - mini risolis de carne (KG)": 25.4,
"704 - mini salsicha empanada (KG)": 22.6,
"705 - mini kibe com requeijao (KG)": 24.9,
"711 - guardanapo embalado (CX)": 12.95,
"713 - molho tabasco verde (UN)": 10.9,
"714 - molho tabasco vermelha (UN)": 10.9,
"716 - amendoin torrado (UN)": 4.7,
"719 - sache palito gental (UN)": 0.25,
"746 - bobina plastica (UN)": 5.8,
"754 - farinha de arroz (UN)": 7.3,
"759 - quiabo (KG)": 5.9,
"762 - espinafre (UN)": 3.85,
"763 - ervilha (KG)": 8.6,
"764 - abacaxi desidratado (KG)": 26.5,
"765 - laranja desidratada (KG)": 24.75,
"766 - limao desidratado (KG)": 24.9,
"767 - oregano (KG)": 9.25,
"856 - agar agar (UN)": 6.8,
"857 - flocos de arroz (KG)": 14.6,
"858 - gelatina em po (KG)": 18.3,
"861 - taça borone (UN)": 7.95,
"862 - pistache granel (KG)": 59.8,
"863 - chia granel (KG)": 17.4,
"883 - file de pescada(mistura)(KG)": 28.6,
"900 - copo long drink (UN)": 1.1,
"902 - copo cerveja (UN)": 1.15,
"915 - pessego amarelo (UN)": 3.2,
"918 - molho pimenta vermelha (UN)": 4.65,
"924 - dianteiro bovino (KG)": 27.5,
"928 - taca decanter (UN)": 15.0,
"936 - polenta pacote (KG)": 4.85,
"938 - taca vidro (UN)": 12.77,
"000 - Chopp (Litros)": 12.9,
"644 - taca vidro espumante (UN)": 12.77,
}

# # 📋 Opções de contagem
# opcoes_contagem = {
#     "1": "consumo_cafe_da_manha",
#     "2": "consumo_casamento_cozinha",
#     "3": "consumo_casamento_salao",
#     "4": "consumo_pre_wedding",
#     "5": "consumo_pos_wedding",
#     "6": "contagem_estoque"
# }

# st.title("📦 Contagem de Itens - Villa Sonali:")

# # 📌 Menu para objetivo
# escolha = st.selectbox("Selecione o objetivo da contagem:", list(opcoes_contagem.values()))
# objetivo = escolha

# # 📦 Organiza os itens por categoria
# categorias_estoque = {}
# for item, categoria in itens_classificados:
#     if categoria not in categorias_estoque:
#         categorias_estoque[categoria] = []
#     categorias_estoque[categoria].append(item)

# estoque = {}

# st.write("### 📋 Insira as quantidades dos itens:")

# # Interface de entrada para os itens
# # for categoria, itens in categorias_estoque.items():
# #     with st.expander(f"📂 {categoria.title()}"):
# #         for item in itens:
# #             quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=item)
# #             # quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=item)
# #             valor_unitario = valores_unitarios.get(item, 0.00)
# #             valor_total = round(quantidade * valor_unitario, 2)
# for categoria, itens in categorias_estoque.items():
#     with st.expander(f"📂 {categoria.title()}"):
#         for item in itens:
#             quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=item)
            
#             # 🔍 Remove espaços duplicados do nome do item antes de buscar o valor
#             item_normalizado = " ".join(item.split())
#             valor_unitario = valores_unitarios.get(item_normalizado, 0.00)
#             valor_total = round(quantidade * valor_unitario, 2)

#             st.text(f"💲 Valor unitário: R$ {valor_unitario:.2f} | Total: R$ {valor_total:.2f}")

#             if quantidade > 0:
#                 estoque[item] = {
#                     "Quantidade": quantidade,
#                     "Valor Unitário (R$)": valor_unitario,
#                     "Valor Total (R$)": valor_total
#                 }

# # 📁 Botão para gerar planilha
# if st.button("📥 Gerar Planilha e Enviar por Email"):
#     if not estoque:
#         st.warning("⚠️ Nenhum item com quantidade informada.")
#     else:
#         df = pd.DataFrame.from_dict(estoque, orient="index")
#         df.reset_index(inplace=True)
#         df.rename(columns={"index": "Item"}, inplace=True)

#         data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         nome_arquivo = f"{objetivo}_{data_hora}.xlsx"
#         df.to_excel(nome_arquivo, index=False)

#         # Envio de e-mail
#         try:
#             yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#             yag.send(
#                 to="ale.moreira@gmail.com",
#                 subject=f"📋 Relatório - {objetivo.replace('_', ' ').title()}",
#                 contents=f"Segue em anexo o controle de estoque referente a: {objetivo.replace('_', ' ').title()}",
#                 attachments=nome_arquivo
#             )
#             st.success(f"📧 Email enviado com sucesso! Planilha: `{nome_arquivo}`")
#         except Exception as e:
#             st.error(f"❌ Erro ao enviar e-mail: {e}")







# # aqui criei uma versão atualizada para zerar apos trocar o motivo da contagem

# # 📋 Opções de contagem
# opcoes_contagem = {
#     "1": "consumo_cafe_da_manha",
#     "2": "consumo_casamento_cozinha",
#     "3": "consumo_casamento_salao",
#     "4": "consumo_pre_wedding",
#     "5": "consumo_pos_wedding",
#     "6": "contagem_estoque",
#     "7": "consumo_funcionarios"
# }

# st.title("📦 Contagem de Itens - Villa Sonali")

# # 📌 Menu para objetivo
# escolha = st.selectbox("Selecione o objetivo da contagem:", list(opcoes_contagem.values()))
# objetivo = escolha

# # 📦 Organiza os itens por categoria
# categorias_estoque = {}
# for item, categoria in itens_classificados:
#     if categoria not in categorias_estoque:
#         categorias_estoque[categoria] = []
#     categorias_estoque[categoria].append(item)

# estoque = {}

# st.write("### 📋 Insira as quantidades dos itens:")

# # Interface de entrada para os itens com chave única por objetivo
# for categoria, itens in categorias_estoque.items():
#     with st.expander(f"📂 {categoria.title()}"):
#         for item in itens:
#             quantidade = st.number_input(
#                 f"{item}",
#                 min_value=0.0,
#                 step=0.1,
#                 key=f"{objetivo}_{item}"  # <- Chave única para cada objetivo
#             )

#             # 🔍 Remove espaços duplicados do nome do item antes de buscar o valor
#             item_normalizado = " ".join(item.split())
#             valor_unitario = valores_unitarios.get(item_normalizado, 0.00)
#             valor_total = round(quantidade * valor_unitario, 2)

#             # liberar esta linha abaixo quando quizer fazer T shoot do calculo da planilha e ver se está aparecendo no programa
#             # st.text(f"💲 Valor unitário: R$ {valor_unitario:.2f} | Total: R$ {valor_total:.2f}")

#             if quantidade > 0:
#                 estoque[item] = {
#                     "Quantidade": quantidade,
#                     "Valor Unitário (R$)": valor_unitario,
#                     "Valor Total (R$)": valor_total
#                 }

# # 📁 Botão para gerar planilha
# if st.button("📥 Gerar Planilha e Enviar por Email"):
#     if not estoque:
#         st.warning("⚠️ Nenhum item com quantidade informada.")
#     else:
#         df = pd.DataFrame.from_dict(estoque, orient="index")
#         df.reset_index(inplace=True)
#         df.rename(columns={"index": "Item"}, inplace=True)

#         data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         nome_arquivo = f"{objetivo}_{data_hora}.xlsx"
#         df.to_excel(nome_arquivo, index=False)

#         # Envio de e-mail
#         try:
#             yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#             yag.send(
#                 to="ale.moreira@gmail.com",
#                 subject=f"📋 Relatório - {objetivo.replace('_', ' ').title()}",
#                 contents=f"Segue em anexo o controle de estoque referente a: {objetivo.replace('_', ' ').title()}",
#                 attachments=nome_arquivo
#             )
#             st.success(f"📧 Email enviado com sucesso! Planilha: `{nome_arquivo}`")
#         except Exception as e:
#             st.error(f"❌ Erro ao enviar e-mail: {e}")




# # aqui mais uma versão, porem incluindo a pesquisa por item



# # 📋 Opções de contagem
# opcoes_contagem = {
#     "1": "consumo_cafe_da_manha",
#     "2": "consumo_casamento_cozinha",
#     "3": "consumo_casamento_salao",
#     "4": "consumo_pre_wedding",
#     "5": "consumo_pos_wedding",
#     "6": "contagem_estoque",
#     "7": "consumo_Almoço_funcionarios"
# }

# st.title("📦 Contagem de Itens - Villa Sonali")

# # Objetivo da contagem
# objetivo = st.selectbox("Selecione o objetivo da contagem:", list(opcoes_contagem.values()))

# # Campo de busca
# busca = st.text_input("🔎 Buscar item pelo nome ou código:")
# busca_normalizada = busca.strip().lower()

# # Organiza os itens por categoria
# categorias_estoque = {}
# for item, categoria in itens_classificados:
#     categorias_estoque.setdefault(categoria, []).append(item)

# estoque = {}

# st.write("### 📋 Insira as quantidades dos itens:")

# # Interface com busca
# for categoria, itens in categorias_estoque.items():
#     itens_filtrados = [item for item in itens if busca_normalizada in item.lower()] if busca_normalizada else itens
#     if not itens_filtrados:
#         continue

#     with st.expander(f"📂 {categoria.title()}"):
#         for item in itens_filtrados:
#             quantidade = st.number_input(
#                 f"{item}",
#                 min_value=0.0,
#                 step=0.1,
#                 key=f"{objetivo}_{item}"
#             )
        
# # )

#             item_normalizado = " ".join(item.split())
#             valor_unitario = valores_unitarios.get(item_normalizado, 0.00)
#             valor_total = round(quantidade * valor_unitario, 2)

#             if quantidade > 0:
#                 estoque[item] = {
#                     "Quantidade": quantidade,
#                     "Valor Unitário (R$)": valor_unitario,
#                     "Valor Total (R$)": valor_total
#                 }

       

# # Botão para gerar planilha e enviar
# if st.button("📥 Gerar Planilha e Enviar por Email"):
#     if not estoque:
#         st.warning("⚠️ Nenhum item com quantidade informada.")
#     else:
#         df = pd.DataFrame.from_dict(estoque, orient="index")
#         df.reset_index(inplace=True)
#         df.rename(columns={"index": "Item"}, inplace=True)

#         data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         nome_arquivo = f"{objetivo}_{data_hora}.xlsx"
#         df.to_excel(nome_arquivo, index=False)

#         try:
#             yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#             yag.send(
#                 to="ale.moreira@gmail.com",
#                 subject=f"📋 Relatório - {objetivo.replace('_', ' ').title()}",
#                 contents=f"Segue em anexo o controle de estoque referente a: {objetivo.replace('_', ' ').title()}",
#                 attachments=nome_arquivo
#             )
#             st.success(f"📧 Email enviado com sucesso! Planilha: `{nome_arquivo}`")
#         except Exception as e:
#             st.error(f"❌ Erro ao enviar e-mail: {e}")




# mais uma versao melhorando o anterior


# # Inicializa o estado da sessão para armazenar o estoque preenchido
# if 'estoque' not in st.session_state:
#     st.session_state.estoque = {}

# # Opções de contagem
# opcoes_contagem = {
#     "1": "consumo_cafe_da_manha",
#     "2": "consumo_casamento_cozinha",
#     "3": "consumo_casamento_salao",
#     "4": "consumo_pre_wedding",
#     "5": "consumo_pos_wedding",
#     "6": "contagem_estoque",
#     "7": "consumo_Almoco_funcionarios"
# }

# st.title("📦 Contagem de Itens - Villa Sonali")

# # Objetivo da contagem
# objetivo = st.selectbox("Selecione o objetivo da contagem:", list(opcoes_contagem.values()))

# # Campo de busca
# busca = st.text_input("🔎 Buscar item pelo nome ou código:")
# busca_normalizada = busca.strip().lower()

# # Organiza os itens por categoria
# categorias_estoque = {}
# for item, categoria in itens_classificados:
#     categorias_estoque.setdefault(categoria, []).append(item)

# st.write("### 📋 Insira as quantidades dos itens:")

# # Interface com busca
# for categoria, itens in categorias_estoque.items():
#     itens_filtrados = [item for item in itens if busca_normalizada in item.lower()] if busca_normalizada else itens
#     if not itens_filtrados:
#         continue

#     with st.expander(f"📂 {categoria.title()}"):
#         for item in itens_filtrados:
#             chave = f"{objetivo}_{item}"
#             quantidade = st.number_input(
#                 f"{item}",
#                 min_value=0.0,
#                 step=0.1,
#                 key=chave,
#                 value=st.session_state.estoque.get(item, {}).get("Quantidade", 0.0)
#             )

#             item_normalizado = " ".join(item.split())
#             valor_unitario = valores_unitarios.get(item_normalizado, 0.00)
#             valor_total = round(quantidade * valor_unitario, 2)

#             if quantidade > 0:
#                 st.session_state.estoque[item] = {
#                     "Quantidade": quantidade,
#                     "Valor Unitário (R$)": valor_unitario,
#                     "Valor Total (R$)": valor_total
#                 }
#             elif item in st.session_state.estoque:
#                 del st.session_state.estoque[item]

# # Botão para gerar planilha e enviar
# if st.button("📅 Gerar Planilha e Enviar por Email"):
#     if not st.session_state.estoque:
#         st.warning("⚠️ Nenhum item com quantidade informada.")
#     else:
#         df = pd.DataFrame.from_dict(st.session_state.estoque, orient="index")
#         df.reset_index(inplace=True)
#         df.rename(columns={"index": "Item"}, inplace=True)

#         data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         nome_arquivo = f"{objetivo}_{data_hora}.xlsx"
#         df.to_excel(nome_arquivo, index=False)

#         try:
#             yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#             yag.send(
#                 to="ale.moreira@gmail.com",
#                 subject=f"📋 Relatório - {objetivo.replace('_', ' ').title()}",
#                 contents=f"Segue em anexo o controle de estoque referente a: {objetivo.replace('_', ' ').title()}",
#                 attachments=nome_arquivo
#             )
#             st.success(f"📧 Email enviado com sucesso! Planilha: `{nome_arquivo}`")
#             st.session_state.estoque = {}  # Zera os dados após envio
#         except Exception as e:
#             st.error(f"❌ Erro ao enviar e-mail: {e}")










# Inicializa o estado da sessão para armazenar o estoque preenchido
if 'estoque' not in st.session_state:
    st.session_state.estoque = {}

# Opções de contagem
opcoes_contagem = {
    "1": "consumo_cafe_da_manha",
    "2": "consumo_casamento_cozinha",
    "3": "consumo_casamento_salao",
    "4": "consumo_pre_wedding",
    "5": "consumo_pos_wedding",
    "6": "contagem_estoque",
    "7": "Consumo_alimentação_funcionarios",
   "8": "Consumo_produtos_Uso_interno_etc"
}

st.title("\U0001F4E6 Contagem de Itens - Villa Sonali")

# Objetivo da contagem
objetivo = st.selectbox("Selecione o objetivo da contagem:", list(opcoes_contagem.values()))

# Campo de busca
busca = st.text_input("\U0001F50E Buscar item pelo nome ou código:")
busca_normalizada = busca.strip().lower()

# Organiza os itens por categoria
categorias_estoque = {}
for item, categoria in itens_classificados:
    categorias_estoque.setdefault(categoria, []).append(item)

st.write("### \U0001F4CB Insira as quantidades dos itens:")

# Interface com busca
for categoria, itens in categorias_estoque.items():
    itens_filtrados = [item for item in itens if busca_normalizada in item.lower()] if busca_normalizada else itens
    if not itens_filtrados:
        continue

    with st.expander(f"\U0001F4C2 {categoria.title()}"):
        for item in itens_filtrados:
            chave = f"{objetivo}_{item}"
            quantidade = st.number_input(
                f"{item}",
                min_value=0.0,
                step=0.1,
                key=chave,
                value=st.session_state.estoque.get(item, {}).get("Quantidade", 0.0)
            )

            item_normalizado = " ".join(item.split())
            valor_unitario = valores_unitarios.get(item_normalizado, 0.00)
            valor_total = round(quantidade * valor_unitario, 2)

            if quantidade > 0:
                st.session_state.estoque[item] = {
                    "Quantidade": quantidade,
                    "Valor Unitário (R$)": valor_unitario,
                    "Valor Total (R$)": valor_total
                }
            elif item in st.session_state.estoque:
                del st.session_state.estoque[item]

# ☕ Campo adicional para cafés vendidos
if objetivo == "consumo_cafe_da_manha":
    cafes_vendidos = st.number_input("☕ Número de cafés vendidos:", min_value=0, step=1)
else:
    cafes_vendidos = 0

# Botão para gerar planilha e enviar
if st.button("\U0001F4C5 Gerar Planilha e Enviar por Email"):
    if not st.session_state.estoque:
        st.warning("⚠️ Nenhum item com quantidade informada.")
    else:
        df = pd.DataFrame.from_dict(st.session_state.estoque, orient="index")
        df.reset_index(inplace=True)
        df.rename(columns={"index": "Item"}, inplace=True)

        valor_unitario_cafe = 40.0
        valor_total_cafe = cafes_vendidos * valor_unitario_cafe
        custo_total_itens = df["Valor Total (R$)"].sum()
        valor_liquido = valor_total_cafe - custo_total_itens

        # Inclui colunas extras se for café da manhã
        if objetivo == "consumo_cafe_da_manha":
            df["Número de Cafés Vendidos"] = cafes_vendidos
            df["Valor Recebido (R$)"] = valor_total_cafe
            df["Valor Líquido (R$)"] = valor_liquido

        data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"{objetivo}_{data_hora}.xlsx"
        df.to_excel(nome_arquivo, index=False)

        try:
            yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
            yag.send(
                to="ale.moreira@gmail.com",
                subject=f"\U0001F4CB Relatório - {objetivo.replace('_', ' ').title()}",
                contents=f"Segue em anexo o controle de estoque referente a: {objetivo.replace('_', ' ').title()}",
                attachments=nome_arquivo
            )
            st.success(f"\U0001F4E7 Email enviado com sucesso! Planilha: `{nome_arquivo}`")
            st.session_state.estoque = {}
        except Exception as e:
            st.error(f"❌ Erro ao enviar e-mail: {e}")


