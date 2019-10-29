#!/usr/bin/env python
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import networkx as nx

get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
G=nx.Graph()


labels = {}
GREX = 'G-Rex'
PEEKABOO = 'Peekaboo'
LIQUID_STRANGER = 'Liquid Stranger'
SPACE_JESUS = 'Space Jesus'
CLOZEE = 'Clozee'
CALCIUM = 'Calcium'
SFAM='SFAM'
TVBOO='Tvboo'
QUAVIUSBLACK='Quaviusblack'
MERSIV='Mersiv'
CHILL_BOBBY='Chill Bobby'
LUZCID='LUZCID'
CHAMPAIGNE_DRIP='Chambaigne Drip'
INZO='Inzo'
LEO_NAPIER='Leo Napier'
BLOOKAH='Blookah'
STRATUS='Stratus'
DIRT_MONKEY='Dirt Monkey'
LAIKA_BEATS='Laika Beats'
KNAT_TURNER='Knat Turner'
LSDREAM='LSDREAM'
MEREDITH_BULL='Meredith Bull'
HYDRALIX='Hydralix'
KRISCHVN='Krischvn'
LEOTRIX='Leotrix'
FREDDY_TODD='Freddy Todd'
OF_THE_TREES='Of The Trees'
BLACK_CARL='BLACK CARL'
TYNAN='TYNAN'
MR_BILL='Mr.Bill'
ZEBBLER_ENCANTI_EXPERIENCE='Zebbler Encanti Experience'
COMET='COM3t'
KTRL='KTRL'
KAYOH='Kayoh'
LEAH_CULVER='Lear Culver'
VARIEN='Varien'
SARAH_HUDSON='Sarah Hudson'
STUCA='STUCA'
TRE_JUSTICE='Tre Justice'
ROXAS='Roxas'
SHANGHAI_DOOM='Shanghai Doom'
CHEE='Chee'
VERN_KNOWS='Vern Knows'
DION_TIMMER='Dion Timmer'
CRYSTALLINE='Crystalline'
LEN_X='Len X'
EAZYBAKED='EAZYBAKED'
G_SPACE='G-Space'
BLEEP_BLOOP='Bleep Bloop'
DUBLOADZ='Dubloadz'
TOP_SHELF='Top $helf'
SHLUMP='Shlump'
TRIPZY_LEARY='Tripzy Leary'
GDUBZ='GDubz'
GIOMETRIC='Giometric'
TOADFACE='Toadface'
YHETI='Yheti'
DMVU='DMVU'
AKAMU='Akamu'
BORNI='Born I'
MEGAN_HAMILTOM='Megan Hamilton'
DIGITAL_ETHOS='Digital Ethos'
TAYLR_RENEE='Taylr Renee'
DOC='DOC'
FLY='Fly'
WAX_FUTURE='Wax Future'
NOTE='Note'
JONATHAN_SANTOS='Jonathan Santos'
BIG_CHOCOLATE='Big Chocolate'
DJ_TWO_STACKS='Dj Two Stacks'
NANOPULSE='Nanopulse'










       

G.add_edge(PEEKABOO, CALCIUM)
G.add_edge(SFAM, QUAVIUSBLACK)
G.add_edge(SFAM,MERSIV)
G.add_edge(QUAVIUSBLACK,MERSIV)
G.add_edge(SFAM,TVBOO)
G.add_edge(CHILL_BOBBY,MERSIV)
G.add_edge(CHAMPAIGNE_DRIP,LUZCID)
G.add_edge(INZO,LEO_NAPIER)
G.add_edge(BLOOKAH,INZO)
G.add_edge(BLOOKAH,LEO_NAPIER)
G.add_edge(STRATUS,INZO)
G.add_edge(DIRT_MONKEY,PEEKABOO)
G.add_edge(LAIKA_BEATS,KNAT_TURNER)
G.add_edge(LAIKA_BEATS,MERSIV)
G.add_edge(KNAT_TURNER,MERSIV)
G.add_edge(LSDREAM,MEREDITH_BULL)
G.add_edge(HYDRALIX,KRISCHVN)
G.add_edge(HYDRALIX,LEOTRIX)
G.add_edge(FREDDY_TODD,OF_THE_TREES)
G.add_edge(BLACK_CARL,FREDDY_TODD)
G.add_edge(GREX,TYNAN)
G.add_edge(ZEBBLER_ENCANTI_EXPERIENCE,MR_BILL)
G.add_edge(COMET,LSDREAM)
G.add_edge(KTRL,LSDREAM)
G.add_edge(KAYOH,LSDREAM)
G.add_edge(LEAH_CULVER,LSDREAM)
G.add_edge(CHAMPAIGNE_DRIP,LSDREAM)
G.add_edge(VARIEN,LSDREAM)
G.add_edge(SARAH_HUDSON,LSDREAM)
G.add_edge(ROXAS,TYNAN)
G.add_edge(SFAM,TYNAN)
G.add_edge(TYNAN,SHANGHAI_DOOM)
G.add_edge(CHEE,LIQUID_STRANGER)
G.add_edge(CLOZEE,LIQUID_STRANGER)
G.add_edge(LIQUID_STRANGER,VERN_KNOWS)
G.add_edge(DION_TIMMER,LIQUID_STRANGER)
G.add_edge(CHAMPAIGNE_DRIP,CRYSTALLINE)
G.add_edge(LEN_X,CHAMPAIGNE_DRIP)
G.add_edge(GREX,PEEKABOO)
G.add_edge(EAZYBAKED,G_SPACE)
G.add_edge(LIQUID_STRANGER, BLEEP_BLOOP)
G.add_edge(LIQUID_STRANGER,FREDDY_TODD)
G.add_edge(GREX,DUBLOADZ)
G.add_edge(GREX,TOP_SHELF)
G.add_edge(LIQUID_STRANGER,SHLUMP)
G.add_edge(TRIPZY_LEARY,GDUBZ)
G.add_edge(GDUBZ,GIOMETRIC)
G.add_edge(TRIPZY_LEARY,GIOMETRIC)
G.add_edge(TOADFACE,SFAM)
G.add_edge(YHETI,DMVU)
G.add_edge(YHETI,TOADFACE)
G.add_edge(TOADFACE,DMVU)
G.add_edge(AKAMU,TOADFACE)
G.add_edge(OF_THE_TREES,TOADFACE)
G.add_edge(EAZYBAKED,TOADFACE)
G.add_edge(DIRT_MONKEY,LUZCID)
G.add_edge(LUZCID,TRE_JUSTICE)
G.add_edge(LUZCID,BORNI)
G.add_edge(MEGAN_HAMILTOM,LUZCID)
G.add_edge(DIGITAL_ETHOS,SPACE_JESUS)
G.add_edge(TAYLR_RENEE,LSDREAM)
G.add_edge(SARAH_HUDSON,LSDREAM)
G.add_edge(FREDDY_TODD,OF_THE_TREES)
G.add_edge(FLY,DOC)
G.add_edge(FLY,ZEBBLER_ENCANTI_EXPERIENCE)
G.add_edge(DOC,ZEBBLER_ENCANTI_EXPERIENCE)
G.add_edge(SPACE_JESUS,DIRT_MONKEY)
G.add_edge(NOTE,FREDDY_TODD)
G.add_edge(FREDDY_TODD,JONATHAN_SANTOS)
G.add_edge(LIQUID_STRANGER,MR_BILL)
G.add_edge(BIG_CHOCOLATE,DJ_TWO_STACKS)
G.add_edge(NANOPULSE,LIQUID_STRANGER)
G.add_edge(SPACE_JESUS,LIQUID_STRANGER)











































pos = nx.spring_layout(G)


nx.draw_networkx_nodes(G, pos, nodelist=[PEEKABOO, CALCIUM] ,node_size=10,
                   alpha=0.8)



nx.draw_networkx_nodes(G, pos, nodelist=[SFAM, QUAVIUSBLACK] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SFAM] ,node_size=70,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LSDREAM] ,node_size=100,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LIQUID_STRANGER] ,node_size=100,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TOADFACE] ,node_size=90,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[FREDDY_TODD] ,node_size=70,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LUZCID] ,node_size=70,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[MERSIV] ,node_size=80,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[GREX] ,node_size=60,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CHAMPAIGNE_DRIP] ,node_size=50,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TYNAN] ,node_size=50,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[DIRT_MONKEY] ,node_size=40,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[INZO] ,node_size=40,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[PEEKABOO] ,node_size=40,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[QUAVIUSBLACK,MERSIV] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SFAM,MERSIV] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SFAM,TVBOO] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CHILL_BOBBY,MERSIV] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CHAMPAIGNE_DRIP,LUZCID] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[INZO,LEO_NAPIER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[BLOOKAH,INZO] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[BLOOKAH,LEO_NAPIER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[STRATUS,INZO] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[DIRT_MONKEY,PEEKABOO] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LAIKA_BEATS,KNAT_TURNER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LAIKA_BEATS,MERSIV] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[KNAT_TURNER,MERSIV] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LSDREAM,MEREDITH_BULL] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[HYDRALIX,KRISCHVN] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[HYDRALIX,LEOTRIX] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[FREDDY_TODD,OF_THE_TREES] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[BLACK_CARL,FREDDY_TODD] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[GREX,TYNAN] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[ZEBBLER_ENCANTI_EXPERIENCE,MR_BILL] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[COMET,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[KTRL,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[KAYOH,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LEAH_CULVER,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CHAMPAIGNE_DRIP,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[VARIEN,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SARAH_HUDSON,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[ROXAS,TYNAN] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SFAM,TYNAN] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TYNAN,SHANGHAI_DOOM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CHEE,LIQUID_STRANGER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CLOZEE,LIQUID_STRANGER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LIQUID_STRANGER,VERN_KNOWS] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[DION_TIMMER,LIQUID_STRANGER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[CHAMPAIGNE_DRIP,CRYSTALLINE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LEN_X,CHAMPAIGNE_DRIP] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[GREX,PEEKABOO] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[EAZYBAKED,G_SPACE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LIQUID_STRANGER, BLEEP_BLOOP] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LIQUID_STRANGER,FREDDY_TODD] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[GREX,DUBLOADZ] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[GREX,TOP_SHELF] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LIQUID_STRANGER,SHLUMP] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TRIPZY_LEARY,GDUBZ] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[GDUBZ,GIOMETRIC] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TRIPZY_LEARY,GIOMETRIC] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TOADFACE,SFAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[YHETI,DMVU] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[YHETI,TOADFACE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TOADFACE,DMVU] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[AKAMU,TOADFACE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[OF_THE_TREES,TOADFACE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[EAZYBAKED,TOADFACE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[DIRT_MONKEY,LUZCID] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LUZCID,TRE_JUSTICE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LUZCID,BORNI] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[MEGAN_HAMILTOM,LUZCID] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[DIGITAL_ETHOS,SPACE_JESUS] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[TAYLR_RENEE,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SARAH_HUDSON,LSDREAM] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[FREDDY_TODD,OF_THE_TREES] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[FLY,DOC] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[FLY,ZEBBLER_ENCANTI_EXPERIENCE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[DOC,ZEBBLER_ENCANTI_EXPERIENCE] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SPACE_JESUS,DIRT_MONKEY] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[NOTE,FREDDY_TODD] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[FREDDY_TODD,JONATHAN_SANTOS] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[LIQUID_STRANGER,MR_BILL] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[BIG_CHOCOLATE,DJ_TWO_STACKS] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[NANOPULSE,LIQUID_STRANGER] ,node_size=10,
                   alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=[SPACE_JESUS,LIQUID_STRANGER] ,node_size=10,
                   alpha=0.8)



nx.draw_networkx_labels(G, pos, font_size=5, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.8, edge_color='r')


# In[ ]:




