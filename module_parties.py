from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-94.95,80.97),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(-168.88,24.24),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-174.89,22.96),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(-168.88,24.24),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.89,22.96),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190.27,-26.94),[]),

  ("town_1","Munich",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.6673,-31.7728),[], 170),
  ("town_2","Donauworth",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.5517,-4.04044),[], 120),
  ("town_3","Amsterdam",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.207,47.6572),[], 80),
  ("town_4","Lyon",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.206,-85.1108),[], 290),
  ("town_5","Den_Haag",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.765,43.6168),[], 90),
  ("town_6","Paris",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.789,-8.89738),[], 155),
  ("town_7","Bordeaux",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.883,-80.0085),[], 240),
  
  ("town_8","London", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.303,62.3059),[], 175),
  ("town_9","Edinburgh",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.599,159.623),[], 90),
  ("town_10","Vienna",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.0209,-54.9977),[], 310),
  ("town_11","York",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.122,121.096),[], 150),
  ("town_12","Nurnberg", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.8398,-3.10152),[], 25),
  ("town_13","Glasgow",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.836,157.194),[], 60),
  ("town_14","Prague",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.87805,4.55023),[], 135),

  ("town_15","Groningen",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.1714,58.5642),[], 45),
  ("town_16","Brussels",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.587,21.5483),[], 0),
  ("town_17","Milan",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.093,-99.8262),[], 90),
  ("town_18","Stuttgart",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.5167,-22.895),[], 135),

  ("town_19","Madrid", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-274.221,-146.46),[], 45),
  ("town_20","Granada", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-270.885,-201.728),[], 270),
  ("town_21","Valencia", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-223.02,-174.912),[], 330),
  ("town_22","Leon", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-280.32,-103.959),[], 225),
  
  ("town_23","Palma", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.719,-180.81),[], 270),
  ("town_24","Barcelona", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.188,-150.784),[], 330),
  ("town_25","Toulon",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.616,-128.905),[], 290),
  ("town_26","Luxembourg",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.4595,4.05665),[], 155),
  ("town_27","Cherbourg",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.794,15.4998),[], 240),
  ("town_28","Trieste",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.42112,-106.208),[], 310),
  ("town_29","Ljubliana",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.5517,-96.6635),[], 90),
  ("town_30","Dublin",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.887,122.186),[], 150),
  ("town_31","Hamburg",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.588,56.9434),[], 135),
  #Denmark
  ("town_32","Kjoebenhavn",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.1529,84.3253),[], 320),
  ("town_33","Aalborg",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.6077,112.746),[], 180),
  ("town_34","Cristiania",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.9698,204.76),[], 35),
  #Sweden
  ("town_35","Rostock",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.4416,66.0698),[], 120),
  ("town_36","Stettin",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.96688,55.5957),[], 280),
  ("town_37","Gothenburg",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.6025,151.911),[], 235),
  ("town_38","Stockholm",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.001,192.05),[], 40),
  ("town_39","Abo",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.156,198.336),[], 80),
  ("town_40","Riga",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(144.297,123.325),[], 20),
  #Prussia
  ("town_41","Berlin",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.88546,43.4355),[], 90),
  ("town_42","Koenigsberg",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.3638,77.0971),[], 155),
  ("town_43","Memel",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.044,88.1464),[], 40),
  #French
  ("town_44","Besancon",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.758,-66.2757),[], 40),
  #HRE Additions
  ("town_45","Torino",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.546,-98.0758),[], 190),
  ("town_46","Brno",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.8459,-12.0636),[], 230),


  #Poland-Saxony-Lithuania
  ("town_47","Dresden",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.6676,34.3243),[], 10),
  ("town_48","Lodz",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.5778,44.9329),[], 80),
  ("town_49","Warsaw",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.3283,36.9978),[], 223),
  ("town_50","Vilnius",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.77,87.36),[], 133),
  #Russia
  ("town_51","Nizhiny_Novgorod",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(365.135,135.894),[], 120),
  ("town_52","Moskow",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(314.492,129.279),[], 280),
  ("town_53","Veliky_Novgorod",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(216.536,157.196),[], 235),
  ("town_54","Smolensk",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(227.392,89.6077),[], 40),
  ("town_55","Kiev",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197.688,15.6495),[], 80),
  ("town_56","Archangel",  icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(305.992,308.631),[], 20),
  #Spanish Habsburgs
  ("town_57","Cagliari",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.576,-232.958),[], 133),

  #HRE
  ("town_58","Naples",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.0394,-182.147),[], 190),
  ("town_59","Taranto",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.88031,-211.966),[], 230),
  ("town_60","Palermo",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.0969,-248.212),[], 190),
  ("town_61","Corunna",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-321.69,-69.9361),[], 133),
  
  #Ottoman Empire
  ("town_62","Istanbul",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190.267,-174.692),[], 250),
  ("town_63","Ankara",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274.978,-194.272),[], 150),
  ("town_64","Bursa",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(204.602,-200.627),[], 60),
  ("town_65","Bucharest",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.1,-98.6154),[], 20),
  ("town_66","Sofia",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.939,-147.292),[], 120),
  ("town_67","Belgrade",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.3657,-133.07),[], 230),
  ("town_68","Athens",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.891,-247.669),[], 150),
  ("town_69","Nicosia",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(277.315,-295.754),[], 140),
  
  #Poland Addition
  ("town_70","Lemberg",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.3294,1.5943),[], 140),
  #French Addition
  # ("town_71","Avignon",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.673,-108.233),[], 140),
  # ("town_72","Perpignan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.571,-133.627),[], 140),
  # ("town_73","Vichy",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.913,-77.0311),[], 140),
  # ("town_74","St. Etienne",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.079,-91.1177),[], 140),
  # ("town_75","Lourdes",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.234,-113.825),[], 140),
  # ("town_76","Le Mans",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-178.081,-24.533),[], 140),
  # ("town_77","Alencon",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.557,-10.5467),[], 140),
  # ("town_78","Roen",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.011,7.47634),[], 140),
  # ("town_79","Nancy",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.9788,-19.4391),[], 140),
  # #Great Britain Addition
  # ("town_80","Cork",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-271.05,104.135),[], 140),
  # ("town_81","Limerick",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-265.165,118.677),[], 140),
  # ("town_82","Southampton",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.411,47.4172),[], 140),
  # ("town_83","Canterbury",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148.858,48.8405),[], 140),
  # ("town_84","Exeter",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.431,56.016),[], 140),
  # ("town_85","Oxford",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.674,79.7767),[], 140),
  # ("town_86","Swansea",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.645,76.7679),[], 140),
  # ("town_87","Newcastle",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.107,137.144),[], 140),
  # ("town_88","Norwich",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.855,80.9416),[], 140),
  # #HRE Addition
  # ("town_89","Oldenburg",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.6315,57.7049),[], 140),
  # ("town_90","Erfurt",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.7236,26.465),[], 140),
  # ("town_91","Munster",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.4491,51.7694),[], 140),
  
#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Woerden_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.73,46.1097),[],50),
  ("castle_2","Pozsony_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.9672,-52.3101),[],75),
  ("castle_3","Plymouth_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-236.862,51.1815),[],100),
  ("castle_4","Dundee_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.228,149.459),[],180),
  ("castle_5","Ansbach_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.2061,-18.2946),[],90),
  ("castle_6","Tours_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.57,-36.7292),[],55),
  ("castle_7","Budapest_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.3822,-39.0506),[],45),
  ("castle_8","Belfast_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-229.552,144.112),[],30),
  ("castle_9","Nijmegen_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.5982,44.1434),[],100),
  ("castle_10","Schnelleberg_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.3595,32.9159),[],110),
  ("castle_11","Regensburg_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.845,-12.6693),[],75),
  ("castle_12","Augsburg_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.992,-29.1438),[],95),
  ("castle_13","Metz_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.9865,-4.49407),[],115),
  ("castle_14","Enschede_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.9798,49.1508),[],90),
  ("castle_15","Maastricht_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.5975,31.7443),[],235),
  ("castle_16","Breda_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.522,36.8457),[],45),
  ("castle_17","Linz_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.87046,-20.7951),[],15),
  ("castle_18","Nottingham_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.171,95.4672),[],300),
  ("castle_19","Inverness_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.386,191.187),[],280),
  ("castle_20","Liege_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.587,16.203),[],260),
  ("castle_21","Rotterdam_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.462,41.4852),[],260),
  ("castle_22","Koln_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.7265,14.7017),[],260),
  ("castle_23","Bourges_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.125,-52.9131),[],80),
  ("castle_24","Caen_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186.691,3.82614),[],260),
  ("castle_25","Dijon_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.666,-47.7922),[],260),
  ("castle_26","Strasbourg_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.033,-40.1815),[],260),
  ("castle_27","Brest_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-247.198,-2.12693),[],260),
  ("castle_28","Eindhoven_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.965,32.1995),[],260),

  ("castle_29","Liverpool_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.883,109.115),[],280),
  ("castle_30","Frankfurt_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.6166,14.7361),[],260),
  ("castle_31","Nantes_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.453,-33.9235),[],260),
  ("castle_32","Nurnberg_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.5185,-11.9797),[],260),
  ("castle_33","Utrecht_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.585,43.3232),[],80),
  ("castle_34","Landshut_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.6092,-24.2277),[],260),
  ("castle_35","Calais_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.807,28.7435),[],260),
  ("castle_36","Rosenheim_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.554,-34.8602),[],260),
  ("castle_37","Cardiff_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.157,75.4115),[],260),
  ("castle_38","Zagreb_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.4967,-107.428),[],260),
  ("castle_39","Arundel_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.546,44.7138),[],280),
  ("castle_40","Dusseldorf_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.5862,38.7311),[],260),

  ("castle_41","Burgos_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.185,-109.302),[],260),
  ("castle_42","Seville_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-303.156,-195.638),[],80),
  ("castle_43","Salamanca_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-301.285,-127.837),[],260),
  ("castle_44","Pamplona_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234.223,-116.787),[],260),
  ("castle_45","Cordoba_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-282.138,-191.291),[],260),
  ("castle_46","Santander_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-284.91,-90.9629),[],260),
  ("castle_47","Santiago_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-320.26,-76.3558),[],260),
  ("castle_48","Toledo_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-278.23,-152.675),[],260),
  
  ("castle_49","Graz_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.94195,-88.6392),[],175),
  ("castle_50","Debrecen_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.189,-41.1612),[],275),
  ("castle_51","Szeged_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.1227,-68.1444),[],55),
  ("castle_52","Bremen_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.6638,56.1351),[],25),
  ("castle_53","Hanover_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.1367,41.1665),[],15),
  ("castle_54","Gibraltar_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-302.014,-216.81),[],260),
  ("castle_55","Berkeley_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.016,76.1298),[],120),
  #Denmark
  ("castle_56","Flensburg_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.3348,76.0564),[],15),
  ("castle_57","Kiel_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.3561,68.2897),[],270),
  ("castle_58","Bergen_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.672,207.013),[],120),
  
  #Sweden
  ("castle_59","Malmo_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.2904,94.7743),[],215),
  ("castle_60","Jonkoping_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.3142,155.416),[],60),
  ("castle_61","Uppsala_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.9593,201.016),[],50),
  ("castle_62","Narva_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180.938,176.043),[],115),
  ("castle_63","Reval_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(144.092,174.881),[],100),
  ("castle_63_new","Ventspilis",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.66,119.67),[],100),
  #Prussia
  ("castle_64","Madgeburg_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.4556,38.7976),[],190),
  ("castle_65","Cottbus_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.16389,33.7329),[],50),
  ("castle_66","Halle_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.6984,32.5039),[],120),

  
  #HRE Addition
  ("castle_67","Olomouc_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.1535,-5.77538),[],120),
  ("castle_81","Messina_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.9333,-248.364),[],190),
  ("castle_82","Bari_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.48103,-201.344),[],50),
  ("castle_83","Pescara_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.6657,-168.016),[],120),
  
  #Poland-Saxony-Lithuania
  ("castle_68","Leipzig_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.20,33.51),[],235),
  ("castle_69","Danzig_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.0098,67.0746),[],45),
  ("castle_70","Krakow_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.4583,2.54989),[],15),
  ("castle_71","Grodno_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.451,57.4021),[],300),
  ("castle_72","Lublin_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.606,27.531),[],280),
  ("castle_73","Breslau_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.0152,37.3177),[],260),
  ("castle_73_new","Birzai",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(137.74,97.60),[],260),
  
  #Russia
  ("castle_74","Pskov_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(184.316,132.032),[],50),
  ("castle_75","Karkiv_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(244.235,15.4285),[],75),
  ("castle_76","Baturyn_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(210.547,23.7106),[],100),
  ("castle_77","Astrakhan_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(391.269,24.9854),[],180),
  ("castle_78","Kursk_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(265.069,73.3941),[],90),
  ("castle_79","Belgorod_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(239.803,24.0172),[],55),
  ("castle_80","Tver_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(301.644,142.664),[],260),
  
  #Great Britain Additions
  ("castle_84","Derry_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-244.011,156.099),[],260),
  ("castle_85","Waterford_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-255.45,102.075),[],100),
  ("castle_86","Stoke_on_Trent_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.733,105.293),[],25),
  ("castle_87","Carlisle_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.229,141.105),[],10),
  ("castle_88","Ness_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.549,230.157),[],60),
  ("castle_89","Kirkwall_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.5,218.634),[],50),
  
  #Ottoman Empire
  ("castle_90","Tarnovo_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128.415,-90.3177),[],160),
  ("castle_91","Varna_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.58,-131.386),[],55),
  ("castle_92","Skopje_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.4409,-156.89),[],285),
  ("castle_93","Podgorica_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.4877,-166.691),[],85),
  ("castle_94","Sarajevo_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.51,-142.157),[],185),
  ("castle_95","Rhodes_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.891,-275.242),[],30),
  ("castle_96","Heraklion_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.442,-299.097),[],125),
  ("castle_97","Khadjibey_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190.946,-48.6359),[],65),
  ("castle_98","Thessalonika_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.9219,-193.714),[],40),
  ("castle_99","Larissa_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.6816,-213.293),[],20),
  ("castle_100","Smyrna_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168.904,-236.941),[],40),
  ("castle_101","Antalya_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(233.87,-261.705),[],110),
  
  #Poland-Saxony-Lithuania Additions
  ("castle_102","Tarnopol_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156.357,7.37096),[],80),
  ("castle_103","Czernowitz_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.298,-11.0649),[],160),
  
  #Russian Additions
  ("castle_104","Poltava_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230.591,4.76604),[],65),
  ("castle_105","Chyhyryn_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.287,-6.82098),[],40), #Cossack - Keep in mind for rebellion
  ("castle_106","Voronezh_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(323.037,62.295),[],20),
  ("castle_107","Saratov_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(375.019,76.6663),[],40),
  ("castle_108","Khymelnitsky_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.461,4.12559),[],110), #Cossack
  
  #Great Britain Additions
  ("castle_109","Guernsey_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-215.035,18.0979),[],40),
  #HRE
  ("castle_110","Kassel_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.8931,30.2051),[],140),
  #Bavaria
  ("castle_111","Passau_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.0393,-20.8583),[],140),
  #French Additions
  ("castle_112","Troyes",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.931,-8.17736),[],140),
  ("castle_113","Biarritz",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.369,-98.1598),[],140),
  ("castle_114","Rennes",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.667,-18.8797),[],140),
  ("castle_115","Versailles",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.825,-9.28247),[],140),
  ("castle_116","Chaumont",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.632,-18.9871),[],140),
  # ("castle_117","Poitiers",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.789,-49.8279),[],140),
  # ("castle_118","Narbonne",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.608,-123.76),[],140),
  # ("castle_119","Albi",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.272,-97.677),[],140),
  # ("castle_120","Chartres",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.707,-17.3974),[],140),
  # ("castle_121","St. Malo",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.905,-9.7828),[],140),
  # ("castle_122","St. Lo",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.839,5.23971),[],140),
  # ("castle_123","Amiens",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.116,11.0034),[],140),
  # ("castle_124","Soissons",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.081,2.96082),[],140),
  # ("castle_125","Autun",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.751,-32.1348),[],140),
  # ("castle_126","Fontainebleu",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-134.456,-20.0314),[],140),
  # ("castle_127","Carcassone",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.11,-125.125),[],140),
  # #Great Britain Additions
  ("castle_128","Kinsale",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-276.097,101.636),[],140),
  ("castle_129","Drogheda",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-242.742,128.307),[],140),
  ("castle_130","Truro",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248.004,53.9391),[],140),
  ("castle_131","Dorchester",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.15,48.1733),[],140),
  ("castle_132","Cardigan",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-226.603,96.1582),[],140),
  # ("castle_133","Holyhead",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.081,119.185),[],140),
  # ("castle_134","Preston",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190.295,117.119),[],140),
  # ("castle_135","Colchester",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.011,62.5853),[],140),
  # ("castle_136","St. Andrews",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.07,167.97),[],140),
  # ("castle_137","Castlebar",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-276.921,143.825),[],140),
  # ("castle_138","Coventry",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.541,86.6451),[],140),
  # ("castle_139","Ipswich",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.202,67.6057),[],140),
  # ("castle_140","Torbay",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.345,51.2716),[],140),
  # ("castle_141","Cambridge",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.48,73.4845),[],140),
  # ("castle_142","Ayr",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.503,167.29),[],140),
  # #HRE Additions
  ("castle_143","Osnabruck",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.0652,45.3703),[],140),
  ("castle_144","Zwickau",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.9748,24.2356),[],140),
  ("castle_145","Fulda",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.0468,21.8657),[],140),
  ("castle_146","Krefeld",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.3581,26.303),[],140),
  ("castle_147","Gottingen",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.4823,35.8736),[],140),
  # ("castle_148","Saarbrucken",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.3676,-7.85993),[],140),
  
#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1", "Nantes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.95,-34.1434),[], 100),
  ("village_2", "Ramillies",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.943,-90.5578),[], 110),
  ("village_3", "Reims",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.192,-0.663814),[], 120),
  ("village_4", "Toulouse",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.607,-107.341),[], 130),
  ("village_5", "Kaisheim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.8644,-21.971),[], 170),
  ("village_6", "Strasbourg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.2329,-27.9398),[], 100),
  ("village_7", "Antwerp",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.117,33.348),[], 110),
  ("village_8", "Tapfheim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.3964,-22.7089),[], 120),
  ("village_9", "Leiden",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.778,46.2326),[], 130),
  ("village_10","Ingolstadt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.9459,-23.9683),[], 170),

  ("village_11","Salzburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.4468,-35.6554),[], 100),
  ("village_12","Den_Helder",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.345,56.1125),[], 110),
  ("village_13","Calais",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.856,29.7043),[], 120),
  ("village_14","Dundee",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.219,148.19),[], 130),
  ("village_15","Dijon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.659,-49.1046),[], 170),
  ("village_16","East Kilbride",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.403,154.591),[], 170),
  ("village_17","Belfast",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-229.668,141.606),[], 35),
  ("village_18","Portsmouth",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.957,40.5609),[], 170),
  ("village_19","Liverpool",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.292,107.292),[], 170),
  ("village_20","Roslyn",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.247,164.037),[], 170),

  ("village_21","Scarborough",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.238,111.431),[], 100),
  ("village_22","Dumfries",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.077,143.104),[], 110),
  ("village_23","Assen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.0114,57.0475),[], 120),
  ("village_24","Alkmaar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.046,52.1),[], 130),
  ("village_25","Innsbruck",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.4151,-47.8618),[], 170),
  ("village_26","Maastricht",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.9178,29.9742),[], 170),
  ("village_27","Drachten",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.1998,57.8),[], 170),
  ("village_28","Pozsony",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.6629,-25.6554),[], 170),
  ("village_29","Augsburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.5711,-30.0423),[], 170),

  ("village_30","Wettstetten",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.1513,-24.4981),[], 170),
  ("village_31","Hochstadt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.9976,1.11683),[], 100),
  ("village_32","Liege",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.451,15.2311),[], 110),
  ("village_33","Marseilles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.073,-122.458),[], 120),
  ("village_34","Caen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-185.358,2.80491),[], 130),
  ("village_35","Blenheim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.8683,-21.1606),[], 170),
  ("village_36","Schnellenberg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.4292,38.8317),[], 170),
  ("village_37","Bergamo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.9806,-94.8058),[], 170),
  ("village_38","La_Rochelle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.954,-51.5584),[], 170),
  ("village_39","Enschede",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.3395,47.8264),[], 170),
  ("village_40","Breda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.013,35.194),[], 170),

  ("village_41","Frankfurt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.8484,13.6843),[], 100),
  ("village_42","Como",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.405,-95.0474),[], 110),
  ("village_43","Durlach",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.6889,-21.065),[], 120),
  ("village_44","Pilsen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.87484,1.14696),[], 130),
  ("village_45","Linz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.16436,-19.5926),[], 170),
  ("village_46","Zwolle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.9668,49.1438),[], 170),
  ("village_47","Leeuwarden",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.911,59.4896),[], 170),
  ("village_48","Orleans",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.463,-27.6848),[], 170),
  ("village_49","Berwick",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.891,156.772),[], 10),
  ("village_50","Inverness",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.192,192.431),[], 170),

  ("village_51","Rosenheim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.5225,-36.1512),[], 100),
  ("village_52","Koln",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.5974,14.0499),[], 110),
  ("village_53","Bourges",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.428,-53.8981),[], 120),
  ("village_54","Metz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.6583,-6.00758),[], 130),
  ("village_55","Tours",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.37,-38.9938),[], 170),
  ("village_56","Oberglauheim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.9486,-20.903),[], 170),
  ("village_57","Ostend",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.677,34.7285),[], 170),
  ("village_58","Kilmarnock",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.413,155.271),[], 170),
  ("village_59","Utrecht",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.762,42.0382),[], 170),
  ("village_60","Limoges",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.155,-59.1815),[], 170),

  ("village_61","Huttenbach",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.6692,0.183478),[], 100),
  ("village_62","Leeds",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.781,117.547),[], 100),
  ("village_63","Brest",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-245.505,-3.18475),[], 100),
  ("village_64","Eindhoven",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.675,30.7873),[], 100),
  ("village_65","Grenoble",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.808,-92.033),[], 100),
  ("village_66","Dunfermline",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.489,162.669),[], 100),
  ("village_67","Cardiff",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.373,74.8346),[], 100),
  ("village_68","Rotterdam",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.928,40.2454),[], 100),
  ("village_69","Regensburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.8244,-14.6734),[], 100),
  ("village_70","Woerden",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.841,44.462),[], 100),

  ("village_71","Oudenaarde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.906,27.4147),[], 20),
  ("village_72","Troyes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.224,-8.94773),[], 60),
  ("village_73","Hoorn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.012,53.3503),[], 100),
  ("village_74","Margate",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.084,49.0956),[], 15),
  ("village_75","Budapest",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.0314,-40.8204),[], 10),
  ("village_76","Heilbronn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.6556,-18.9394),[], 35),
  ("village_77","Landshut",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.0151,-25.4037),[], 160),
  ("village_78","Arnhem",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.5573,46.2656),[], 180),
  ("village_79","Ameland",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.4483,14.5436),[], 0),
  ("village_80","Ansbach",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.9935,-19.8134),[], 40),

  ("village_81","Buxheim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.0939,-14.8487),[], 20),
  ("village_82","Namur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.776,18.8035),[], 60),
  ("village_83","Le Havre",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.925,6.0192),[], 55),
  ("village_84","Hilversum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.271,46.3472),[], 15),
  ("village_85","Nottingham",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.128,94.5707),[], 10),
  ("village_86","Aberdeen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-169.345,183.185),[], 35),
  ("village_87","Plymouth",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-236.07,50.0027),[], 160),
  ("village_88","Zagreb",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.5354,-108.821),[], 180),
  ("village_89","Dusseldorf",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.9333,36.2863),[], 0),
  ("village_90","Nijmegen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.7609,42.5452),[], 40),

  ("village_91","Getafe",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-277.233,-148.435),[], 20),
  ("village_92","Guadalajara",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.501,-140.798),[], 60),
  ("village_93","Arranjuez",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-272.573,-150.019),[], 55),
  ("village_94","Burgos",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-265.347,-111.054),[], 15),
  ("village_95","La Zubia",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-270.017,-203.364),[], 10),
  ("village_96","Santiago_de_Compostela",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-319.133,-77.5527),[], 35),
  ("village_97","Atarfe",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-272.7,-199.635),[], 160),
  ("village_98","Torremolinos",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-282.829,-209.288),[], 180),
  ("village_99","Gijon",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-303.23,-72.8106),[], 0),
  ("village_100","Oviedo",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-283.891,-83.1233),[], 40),

  ("village_101","Cassabermeja",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-278.922,-208.548),[], 20),
  ("village_102","Seville",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-303.653,-197.321),[], 60),
  ("village_103","Velez-Malaga",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-273.913,-209.247),[], 55),
  ("village_104","Salamanca",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-300.679,-128.962),[], 15),
  ("village_105","Pamplona",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-233.84,-118.475),[], 10),
  ("village_106","Santander",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-283.881,-94.8148),[], 35),
  ("village_107","Toledo",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-279.599,-154.15),[], 160),
  ("village_108","Cordoba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-284.129,-192.065),[], 180),
  ("village_109","Torrent",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-225.181,-175.581),[], 0),
  ("village_110","Sagunto",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-221.57,-172.429),[], 40),
  
  ("village_111","Ibiza",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.452,-186.111),[], 20),
  ("village_112","Sa_Pobla",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-188.597,-175.892),[], 60),
  ("village_113","Menorca",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.819,-171.975),[], 55),
  
  ("village_114","Cadiz",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-309.809,-206.46),[], 60),
  ("village_115","Gibraltar",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-301.302,-218.396),[], 55),
  
  ("village_116","Wexford",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248.007,106.17),[], 172),
  ("village_117","Shannon",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-278.16,122.339),[], 150),
  ("village_118","Dundalk",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.284,132.126),[], 120),
  ("village_119","Manchester",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-188.318,110.295),[], 100),
  ("village_120","Ipswich",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.948,63.5316),[], 150),
  ("village_121","Birmingham",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.772,93.2129),[], 120),
  ("village_122","Bristol",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.568,70.6696),[], 100),
  ("village_123","Girona",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.019,-147.774),[], 15),
  ("village_124","Saragossa",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-228.753,-136.654),[], 10),
  ("village_125","Tarragona",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.226,-154.412),[], 35),
  ("village_126", "Evenos",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.385,-124.957),[], 100),
  ("village_127", "La_Garde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.254,-127.649),[], 110),
  ("village_128", "Olioules",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.458,-127.576),[], 120),
  
  ("village_129", "Kirchberg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.8967,10.9733),[], 100),
  ("village_130", "Strassen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.6412,7.67604),[], 110),
  ("village_131", "Cessange",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.6667,1.45659),[], 120),
  
  ("village_132", "Tourlaville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.241,14.1534),[], 100),
  ("village_133", "La_Glacerie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.107,13.536),[], 110),
  ("village_134", "Nouanville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.875,16.189),[], 120),
  
  ("village_135","Udine",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.1076,-94.966),[], 100),
  ("village_136","Treviso",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.4794,-101.82),[], 110),
  ("village_137","Bolzano",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.9356,-90.7092),[], 120),
  
  ("village_138","Moribor",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2321,-94.2383),[], 100),
  ("village_139","Rijeka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.9343,-118.991),[], 110),
  ("village_140","Klagenfurt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.527537,-71.4187),[], 120),
  
  ("village_141","Stade",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.2411,60.1935),[], 100),
  ("village_142","Ahrensburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.7247,59.5623),[], 110),
  ("village_143","Hartberg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.2762,-68.8226),[], 120),
  
  ("village_144","Mako",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.485,-54.1919),[], 100),
  ("village_145","Zeven",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.5965,54.3966),[], 110),
  ("village_146","Braunschweig",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.1258,46.9523),[], 120),
  #New as of 0.180
  #Denmark/Norway
  ("village_147","Oedense",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.9735,81.6472),[], 80),
  ("village_148","Frederikshavn",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.125,107.174),[], 80),
  ("village_149","Skagen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.6108,120.062),[], 135),
  
  ("village_150","Esbjerg",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.1571,94.8617),[], 120),
  ("village_151","Kristiansand",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.3041,176.089),[], 200),
  ("village_152","Stavanger",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.614,178.762),[], 80),
  ("village_153","Kiel",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.0472,67.1795),[], 220),
  ("village_154","Flensberg",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.9076,74.8849),[], 120),
  ("village_155","Bergen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.767,203.84),[], 220),
  #Sweden
  ("village_156","Butzow",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.7985,60.88),[], 180),
  ("village_157","Stralsund",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.11995,65.6563),[], 280),
  ("village_158","Sassnitz",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.8055,68.651),[], 35),
  
  ("village_159","Falkensee",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.0349,46.7147),[], 20),
  ("village_160","Pasewalk",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.493578,55.1104),[], 120),
  ("village_161","Halmstad",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.8929,125.384),[], 180),
  
  ("village_162","Boras",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.3132,154.305),[], 245),
  ("village_163","Mariehamn",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.7264,191.475),[], 45),
  ("village_164","Upplands_Vasby",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.6765,196.101),[], 70),
  
  ("village_165","Vasteras",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.8614,194.655),[], 90),
  ("village_166","Helsingfors",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(137.093,188.584),[], 120),
  ("village_167","Hanko",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.727,189.632),[], 70),
  ("village_168","Ogre",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.645,119.86),[], 320),
  ("village_169","Trakai",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.316,77.3314),[], 80),
  ("village_170","Valmira",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.95,114.14),[], 30),
  ("village_171","Lund",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.0975,97.3885),[], 230),
  ("village_172","Filipstad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.1165,196.836),[], 30),
  ("village_173","Orebro",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.8454,190.307),[], 130),
  ("village_173_new","Kuldiga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.01,109.58),[], 130),
  
  
  #Prussia
  ("village_174","Potsdam",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.40974,40.6131),[], 95),
  ("village_175","Oranienburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.24629,47.2108),[], 45),
  ("village_176","Zimmerbude",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.1624,79.4747),[], 220),
  ("village_177","Neuhausen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.4461,75.0959),[], 240),
  ("village_178","Libau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.414,99.675),[], 65),
  ("village_179","Krottingen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.47,93.29),[], 30),
  ("village_180","Magdeberg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.9243,37.5523),[], 30),
  ("village_181","Cottbus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.85393,32.347),[], 30),
  ("village_182","Halle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.3998,35.0926),[], 30),
  ("village_182_new","Tisit",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.08,81.58),[], 30),
  
  #France Additions
  ("village_183","Montbeliard",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.219,-62.0003),[], 130),
  ("village_184","Vesoul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.084,-57.8867),[], 150),
  
  #HRE Additions
  ("village_185","Castellemonte",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.7049,-92.5798),[], 40),
  ("village_186","Novara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.3113,-99.8135),[], 110),
  ("village_187","Vyskov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.7876,-9.34508),[], 55),
  ("village_188","Jihlava",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.2462,-8.534),[], 140),
  ("village_189","Zlin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.5029,-12.1103),[], 300),
  ("village_190","Olomouc",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.3978,-6.64193),[], 15),
  
  ("village_191","Salerno",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.1715,-191.93),[], 40),
  ("village_192","Benevento",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.7524,-179.401),[], 110),
  ("village_193","Potenza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.2122,-188.853),[], 55),
  ("village_194","Lecce",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.8679,-218.747),[], 140),
  ("village_195","Brindisi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.6312,-211.256),[], 300),
  ("village_196","Agrigento",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.6893,-261.287),[], 15),
  ("village_197","Ragusa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.5379,-266.41),[], 55),
  ("village_198","Messina",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.1564,-249.791),[], 140),
  ("village_199","Bari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.92906,-202.672),[], 300),
  ("village_200","Pescara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.3358,-169.722),[], 15),
  
  #Poland-Saxony-Lithuania
  ("village_201","Bischofswerda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.13971,33.49),[], 40),
  ("village_202","Neustadt_in_Sachsen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.59218,31.4201),[], 110),
  ("village_203","Kutno",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.5164,48.5344),[], 55),
  ("village_204","Tomaszow-Mazowiecki",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.4272,42.3053),[], 140),
  ("village_205","Radom",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.6756,31.3592),[], 300),
  ("village_206","Siedlce",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.6756,31.3592),[], 15),
  ("village_207","Lublin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.938,26.1815),[], 40),
  ("village_208","Plock",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.4979,52.6564),[], 110),
  ("village_209","Kaunas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.21,89.73),[], 55),
  ("village_210","Siauliai",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.15,97.12),[], 140),
  ("village_211","Leipzig",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.92,32.82),[], 300),
  ("village_212","Elbing ",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.1104,65.2522),[], 15),
  ("village_213","Krakow",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.195,0.741454),[], 15),
  ("village_214","Breslau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.2693,36.0985),[], 40),
  ("village_215","Grodno",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131.763,56.7148),[], 55),
  #Russia
  ("village_216", "Vladimir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(331.666,132.4),[], 100),
  ("village_217", "Ivanovo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(345.064,146.075),[], 110),
  ("village_218", "Balashika",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(319.13,130.364),[], 120),
  ("village_219", "Korolyov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(316.675,132.969),[], 130),
  ("village_220", "Khimki",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(309.947,132.307),[], 170),
  ("village_221", "Podolsk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(313.624,121.062),[], 100),
  ("village_222", "Tikhvin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(226.546,184.115),[], 110),
  ("village_223", "Gatchina",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.661,183.115),[], 120),
  ("village_224", "Yartsevo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(240.798,95.6114),[], 130),
  ("village_225", "Demidov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(218.892,101.79),[], 170),

  ("village_226","Bryansk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(242.806,77.1454),[], 100),
  ("village_227","Boyarka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.296,12.2127),[], 110),
  ("village_228","Buzova",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(188.496,14.5425),[], 120),
  ("village_229","Novodvinsk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.268,302.843),[], 130),
  ("village_230","Severodvinsk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(299.963,307.464),[], 170),
  ("village_231","Pskov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(183.957,129.786),[], 170),
  ("village_232","Karkiv",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(245.803,13.6348),[], 35),
  ("village_233","Baturyn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(211.824,21.7893),[], 170),
  ("village_234","Astrakhan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(384.668,22.6962),[], 170),
  ("village_235","Kursk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(264.956,70.5649),[], 170),

  ("village_236","Belgorod",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(239.071,22.1095),[], 100),
  ("village_237","Tver",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(304.691,143.1),[], 110),
  #Spanish Habsburgs Addition
  ("village_238","Sassari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.258,-201.682),[], 110),
  #Great Britain Additions
  ("village_239","Derry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.966,154.631),[], 170),
  ("village_240","Waterford",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-257.961,103.646),[], 170),
  ("village_241","Stoke_on_Trent",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190.749,103.63),[], 35),
  ("village_242","Carlisle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-188.497,139.707),[], 170),
  ("village_243","Ness",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.159,228.397),[], 170),
  ("village_244","Kirkwall",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-169.096,220.82),[], 170),
  #Spanish Bourbon Additions
  ("village_245","Lugo",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-311.969,-71.2992),[], 170),
  ("village_246","Foz",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-308.258,-70.0696),[], 200),
  ("village_247","Pontecesco",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-323.897,-71.757),[], 200),
  
  #Ottoman Empire
  ("village_248","Kavakli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(184.255,-172.235),[], 270),
  ("village_249","Corlu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170.788,-173.124),[], 120),
  ("village_250","Vize",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(164.304,-159.417),[], 30),
  
  ("village_251","Kazan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(271.582,-185.667),[], 50),
  ("village_252","Bala",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(282.097,-204.019),[], 140),
  ("village_253","Nicea",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(213.565,-188.145),[], 80),
  
  ("village_254","Kestel",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(208.271,-200.757),[], 150),
  ("village_255","Yalova",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200.856,-187.461),[], 40),
  ("village_256","Calugareni",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.889,-102.881),[], 180),
  
  ("village_257","Calarasi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.951,-99.7318),[], 175),
  ("village_258","Giurgiu",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.5,-109.555),[], 180),
  ("village_259","Vratsa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.986,-138.516),[], 10),
  
  ("village_260","Pernik",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.1307,-150.128),[], 225),
  ("village_261","Smederevo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.852,-134.71),[], 80),
  ("village_262","Novi_Sad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.5536,-127.574),[], 175),
  
  ("village_263","Zografou",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.567,-245.075),[], 330),
  ("village_264","Larnaca",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280.374,-303.89),[], 225),
  ("village_265","Limossol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(269.211,-312.602),[], 240),
  
  ("village_266","Tarnovo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.564,-114.757),[], 100),
  ("village_267","Varna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.183,-129.16),[], 140),
  ("village_268","Skopje",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.7165,-158.345),[], 350),
  
  ("village_269","Podgorica",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.1608,-164.623),[], 130),
  ("village_270","Sarajevo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.8542,-143.938),[], 190),
  ("village_271","Rhodes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(193.396,-277.616),[], 250),
  
  ("village_272","Heraklion",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(144.544,-301.024),[], 50),
  ("village_273","Khadjibey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192.098,-46.8584),[], 320),
  ("village_274","Thessalonika",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.9361,-195.145),[], 110),
  
  ("village_275","Larissa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.4215,-214.981),[], 150),
  ("village_276","Smyrna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170.2,-239.452),[], 220),
  ("village_277","Alanya",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(242.886,-263.292),[], 210),
  
  #Spanish Bourbon Additions
  ("village_278","Melilla",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-253.054,-258.227),[], 210),

  #Polish Additions
  ("village_279","Tarnopol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.399,5.87191),[], 210),
  ("village_280","Czernowitz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.753,-13.0312),[], 210),
  ("village_281","Horodok",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.89,2.67436),[], 10),
  ("village_282","Rudky",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.3759,-4.11363),[], 145),
  ("village_283","Olesko",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.333,6.19832),[], 160),
  
  #Russian Additions
  ("village_284","Poltava",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(231.397,7.03065),[], 210),
  ("village_285","Chyhyryn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(213.898,-8.22251),[], 210),
  ("village_286","Voronezh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(323.496,59.7752),[], 10),
  ("village_287","Saratov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(371.428,74.5591),[], 145),
  ("village_288","Khymelnitsky",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.118,2.31851),[], 160),
  
  #Great Britain
  ("village_289","Jersey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.272,9.21869),[], 160),
  
  #HRE Addition
  ("village_290","Debrecen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.3831,-43.438),[], 160),
  ("village_291","Luneburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.7151,51.8243),[], 160),
  ("village_292","Budweis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.65823,-8.28598),[], 160),
  #Bavaria
  ("village_293","Passau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.1665,-22.6083),[], 120),
  #HRE
  ("village_294","Kassel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.521,28.7988),[], 120),
  #French Addition
  ("village_295","Pau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.638,-105.069),[], 120),
  ("village_296","Auch",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.541,-104.306),[], 120),
  ("village_297","Dax",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-226.16,-94.496),[], 120),
  ("village_298","Le Boulou",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.27,-138.316),[], 120),
  ("village_299","Foix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.768,-127.309),[], 120),
  
  # ("village_300","Limoux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186.467,-129.598),[], 120),
  # ("village_301","Agde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.909,-120.965),[], 120),
  # ("village_302","Nimes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.492,-110.529),[], 120),
  # ("village_303","Montpellier",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.141,-115.911),[], 120),
  # ("village_304","Ruffec",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.416,-58.5673),[], 120),
  
  # ("village_305","Le Puy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.348,-95.2283),[], 120),
  # ("village_306","Ambert",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.014,-90.2509),[], 120),
  # ("village_307","Commentry",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.215,-77.8385),[], 120),
  # ("village_308","Riom",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.701,-86.4675),[], 120),
  # ("village_309","Bressuire",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.372,-61.5274),[], 120),
  
  # ("village_310","Guer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-215.854,-24.0777),[], 120),
  # ("village_311","Erquy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.775,-8.89435),[], 120),
  # ("village_312","Louplande",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.838,-29.2423),[], 120),
  # ("village_313","Conlie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186.027,-20.8276),[], 120),
  # ("village_314","Carrouges",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-184.613,-9.53258),[], 120),
  
  # ("village_315","Mamers",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.127,-11.4905),[], 120),
  # ("village_316","Granville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.41,-1.98257),[], 120),
  # ("village_317","Bayeux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.707,6.12552),[], 120),
  # ("village_318","Evreux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.758,3.307),[], 120),
  # ("village_319","Fecamp",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.153,12.6834),[], 120),
  
  # ("village_320","Plaisir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.14,-9.29652),[], 120),
  # ("village_321","Troul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.9925,-22.5409),[], 120),
  # ("village_322","Luneville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.521,28.7988),[], 120),
  # ("village_323","Laon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.761,7.51223),[], 120),
  # ("village_324","Montauban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.466,-93.1734),[], 120),
  
  # ("village_325","Cahors",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186.561,-79.867),[], 120),
  # ("village_326","Agen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.368,-97.9464),[], 120),
  # ("village_327","Bergerac",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.508,-83.8424),[], 120),
  # ("village_328","Angouleme",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.997,-64.4434),[], 120),
  # ("village_329","Royan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-215.327,-60.5222),[], 120),
  
  # ("village_330","Brive-la-Gaillarde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.261,-64.5447),[], 120),
  # ("village_331","Gueret",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.775,-52.2528),[], 120),
  # ("village_332","Colmar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.5486,-34.2109),[], 120),
  # ("village_333","Haguenau",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.676,-21.8264),[], 120),
  # ("village_334","Mulhouse",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.6846,-53.1532),[], 120),
  # #Great Britian Addition
  ("village_335","Killarney",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-286.62,109.624),[], 120),
  ("village_337","Listowel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-285.079,117.289),[], 120),
  ("village_338","Killkenny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.403,115.208),[], 120),
  ("village_339","Westport",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-279.607,140.923),[], 120),
  ("village_340","Strandhill",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-257.904,144.939),[], 120),
  
  # ("village_341","Ballymote",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-253.84,137.665),[], 120),
  # ("village_342","Kilybegs",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-253.366,152.949),[], 120),
  # ("village_343","Portlaoise",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-252.897,124.163),[], 120),
  # ("village_344","Portdown",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.121,141.406),[], 120),
  # ("village_345","Galway",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-268.252,129.851),[], 120),
  
  # ("village_346","Sennen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-255.877,52.0864),[], 120),
  # ("village_347","St Agnes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.261,58.3915),[], 120),
  # ("village_348","Wadebridge",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-221.329,64.0664),[], 120),
  # ("village_349","Bath",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.006,65.3964),[], 120),
  # ("village_350","Crawley",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.049,54.3302),[], 120),
  
  # ("village_351","Reading",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.489,61.9013),[], 120),
  # ("village_352","Swindon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.904,67.5901),[], 120),
  # ("village_353","Bournemouth",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.896,45.702),[], 120),
  # ("village_354","Carmarthen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.478,90.3717),[], 120),
  # ("village_355","Fishguard",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234.089,96.0327),[], 120),
  
  # ("village_356","Llanelli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.125,80.9926),[], 120),
  # ("village_357","Wolwerhampton",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.214,87.6716),[], 120),
  # ("village_358","Southport",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.591,114.28),[], 120),
  # ("village_359","Blackpool",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.114,118.282),[], 120),
  # ("village_360","Bolton",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.191,113.722),[], 120),
  
  # ("village_361","Bradford",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.14,-9.29652),[], 120),
  # ("village_362","Northfield",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.912,87.7769),[], 120),
  # ("village_363","Boston",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.129,83.82),[], 120),
  # ("village_364","Skegness",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.995,90.7797),[], 120),
  # ("village_365","Docking",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.293,85.3813),[], 120),
  
  # ("village_366","Cromer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.937,86.8882),[], 120),
  # ("village_367","Lowestoft",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.446,73.7177),[], 120),
  # ("village_368","Diss",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.78,71.9685),[], 120),
  # ("village_369","Grimsby",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.943,102.917),[], 120),
  # ("village_370","Middlesbrough",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.313,129.135),[], 120),
  
  # ("village_371","Castletown",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.465,130.852),[], 120),
  # ("village_372","Prestwick",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.186,171.56),[], 120),
  # ("village_373","Greenock",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.206,183.922),[], 120),
  # ("village_374","Portree",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.459,204.337),[], 120),
  # ("village_375","Ullapool",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.888,210.328),[], 120),
  # #HRE Addition
  ("village_376","Essen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.9256,27.9211),[], 120),
  ("village_377","Bielefeld",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.0011,43.6725),[], 120),
  ("village_378","Norden",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.0902,61.9213),[], 120),
  ("village_379","Rheine",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.6033,37.2915),[], 120),
  ("village_380","Wangerland",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.6584,61.8608),[], 120),
  
  # ("village_381","Travemunde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.5379,61.8592),[], 120),
  # ("village_382","Wismar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.4827,60.4583),[], 120),
  # ("village_383","Schwerin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.7117,53.2254),[], 120),
  # ("village_384","Bergedorf",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.9456,56.0051),[], 120),
  # ("village_385","Stendal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.6577,45.9044),[], 120),
  
  # ("village_386","Celle",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.1601,41.9098),[], 120),
  # ("village_387","Paderborn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.8813,31.8557),[], 120),
  # ("village_388","Baden Baden",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.3126,-28.9934),[], 120),
  # ("village_389","Freiburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.3679,-34.8699),[], 120),
  # ("village_390","Karlsruhe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.1022,-2.35786),[], 120),
  
  # ("village_391","Tubingen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.204,-26.8703),[], 120),
  # ("village_392","Reutlingen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.165,-26.6596),[], 120),
  # ("village_393","Ulm",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.9204,-30.7292),[], 120),
  # ("village_394","Mayrhofen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.5917,-51.2817),[], 120),
  # ("village_395","Vocklabruck",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.13538,-34.2006),[], 120),
  
  # ("village_396","Bad ischl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.02984,-38.0973),[], 120),
  # ("village_397","Armstetten",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.66164,-54.0451),[], 120),
  # ("village_398","Sankt Polten",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.60047,-54.8844),[], 120),
  # ("village_399","St Martin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.37249,-66.417),[], 120),
  # ("village_400","Pressburg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.0806,-56.6461),[], 120),
  
  ("salt_mine","Tunis_Barbary_Port",icon_village_c|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.547,-287.273),[]),
  ("four_ways_inn","Mostaghanem",icon_town|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.048,-276.128),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.355,-287.937),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234.76,-287.644),[]),
  ("dhorak_keep","Algiers_Port",icon_town|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.696,-275.915),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-272.63,-140.015),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.99,-2.73515),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.197,67.6445),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.02,44.2816),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.6527,-36.962),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.5223,-61.5339),[], 100),
  



#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(361.541,-270.671),[], -44.8),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(376.54,-263.12),[], 4.28),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(356.561,-272.07),[], 64.5),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(364.74,-269.507),[], -2.13),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(377.467,-270.982),[], 21.5),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(356.567,-275.834),[], -73.5),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(360.184,-273.371),[], -64),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(366.494,-271.996),[], 1.72),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(374.275,-272.336),[], -33.76),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(380.742,-272.286),[], -44.07),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(388.014,-262.401),[], 81.3),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(354.93,-278.2),[], -35.5),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(354.811,-285.62),[], -17.7),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(366.836,-285.839),[], 66.6),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-160.174,46.8659),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(229.78,43.4425),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(334.692,208.397),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(179.468,90.2532),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-215.256,-129.212),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-298.88,-212.9),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-120.307,-276.098),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(263.904,-229.479),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(360.318,-290.143),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(365.663,-298.604),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(371.781,-289.625),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(377.922,-287.754),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(373.821,-299.12),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(376.041,-302.376),[(trp_looter,15,0)]),  
  ]
