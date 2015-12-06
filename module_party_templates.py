from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,escorted_merchant_personality,[(trp_cattle,80,120)]),
#Criminals

("looters", "Looters", icon_axeman|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_looter,3,45)] ),
("manhunters", "Police Patrol", icon_gray_knight, 0, fac_manhunters, soldier_personality, [(trp_manhunter,9,40),(trp_mounted_patrol,1,10)] ),
("forest_bandits","Highwaymen",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_forest_bandit,4,42)]),
("taiga_bandits", "Rebel Uskoci", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_taiga_bandit,12,130)] ),
("steppe_bandits", "Illegal Trade Smugglers", icon_khergit|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_steppe_bandit,15,60)] ),
("sea_raiders", "Monarchist Agitators", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_sea_raider,20,150)] ),
("mountain_bandits", "Jacobite Rebels", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_mountain_bandit,15,200),(trp_scottish_rebel_leader,1,4)] ),
("desert_bandits", "Slavic Bandits", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_desert_bandit,4,50)] ),
("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
("merchant_caravan", "Merchant Caravan", icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party, 0, fac_commoners, escorted_merchant_personality, [(trp_caravan_master,1,1),(trp_caravan_guard,5,35)] ),
("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
("runaway_serfs","Runaway Peasants",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),

("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),

("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,45)]),
("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

#("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_french_regiment_du_roi_recruit,5,10),(trp_french_de_la_marine_recruit,4,7),(trp_regiment_surbeck_recruit,4,7)] ),
#("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_garde_suisses_recruit,5,8),(trp_french_grenadier_recruit,7,10),(trp_french_officer,1,1),(trp_royal_italien_recruit,5,7),(trp_gardes_francaises_recruit,5,8)] ),
#("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_french_regiment_lorraine_recruit,3,5),(trp_french_royal_carabinier_recruit,4,6),(trp_french_drummer,1,1),(trp_french_standard_bearer,1,1),(trp_regiment_clare_recruit,7,10)] ),

#("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,5,10),(trp_british_churchill_regiment_recruit,2,4)] ),
#("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_british_webb_regiment_recruit,2,4),(trp_british_howe_regiment_recruit,2,4),(trp_british_marlborough_regiment_recruit,1,2)] ),
#("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_british_welch_fusiliers_recruit,2,3),(trp_british_officer,1,2),(trp_british_duke_of_schomberg_regiment_recruit,1,2),(trp_british_drummer,1,1),(trp_british_standard_bearer,1,1)] ),

#("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_austrian_wuerttemburg_regiment_recruit,3,5),(trp_austrian_wetzel_regiment_recruit,2,9),(trp_hessen_schopping_regiment_recruit,1,1),(trp_savoy_pikeline_recruit,2,3),(trp_savoy_rehbinder_recruit,1,2),(trp_savoy_dragoon_recruit,1,1)] ),
#("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,1,1),(trp_austrian_grenadier_recruit,1,2),(trp_austrian_officer,1,1),(trp_hessen_prinz_wilhem_regiment_recruit,1,1),(trp_hessen_erbprinz_regiment_recruit,1,1),(trp_hessen_leibguard_recruit,1,1)] ),
#("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_austrian_regiment_von_deutschmeister_recruit,2,4),(trp_austrian_standard_bearer,1,1),(trp_austrian_drummer,1,1),(trp_wurttenberg_prince_cavalry_recruit,1,2),(trp_savoy_grenadier_recruit,1,3),(trp_savoy_desportes_recruit,1,3)] ),

#("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bavaria_leib_regiment_recruit,6,11),(trp_bavaria_karthausen_recruit,2,4),(trp_bavaria_grenadier_guard_recruit,2,4)] ),
#("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_bavaria_maffey_recruit,2,5),(trp_bavria_kurzprinz_recruit,3,4),(trp_bavaria_grenadier_guard_recruit,1,2)] ),
#("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_bavaria_prince_phillipe_recruit,5,9),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_drummer,1,1)] ),

#("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,5,10),(trp_dutch_oranje_gelderland_recruit,2,4)]),
#("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_dutch_zweeds_recruit,7,10),(trp_dutch_nassau_recruit,2,4)] ),
#("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_dutch_opstad_recruit,2,3),(trp_dutch_cuirassier_recruit,1,2),(trp_dutch_blue_guard_recruit,2,5),(trp_dutch_standard_bearer,1,1),(trp_dutch_drummer,1,1)] ),

#("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bourbon_diputacio_recruit,6,12),(trp_bourbon_aragon_recruit,2,4)] ),
#("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_bourbon_asturias_recruit,2,4),(trp_bourbon_colorados_recruit,4,7),(trp_bourbon_walloon_recruit,2,4)] ),
#("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,5,6),(trp_bourbon_royal_guards_recruit,1,1),(trp_bourbon_drummer,1,1)] ),

#("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_danish_militia_recruit,5,10),(trp_danish_funen_recruit,2,4),(trp_danish_first_recruit,2,3),(trp_danish_life_dragoon_recruit,1,1)] ),
#("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_danish_funen_recruit,3,6),(trp_danish_marine_recruit,2,4),(trp_danish_sjallandska_recruit,2,4),(trp_danish_prince_christian_recruit,1,3)] ),
#("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_danish_prince_charles_recruit,2,4),(trp_danish_grenadier_recruit,2,3),(trp_danish_drummer,1,1),(trp_danish_standard_bearer,1,1),(trp_danish_livegardet_till_hast_recruit,1,2),(trp_danish_ungerska_drongera_recruit,1,2)] ),

#("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swedish_alvsborg_recruit,5,10),(trp_swedish_jonkoping_recruit,2,4),(trp_swedish_pommerska_recruit,1,4),(trp_swedish_dal_recruit,1,4),(trp_swedish_pikeman_recruit,1,15)] ),
#("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swedish_narke_varmlands_recruit,2,5),(trp_swedish_sodermanlands_recruit,2,5),(trp_swedish_nyland_recruit,1,5),(trp_swedish_drummer,1,1),(trp_swedish_standard_bearer,1,1)] ),
#("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swedish_uppland_recruit,2,8),(trp_swedish_nv_tremannigar_recruit,1,4),(trp_swedish_grenadier_recruit,1,4),(trp_swedish_mellins_estlandska_recruit,1,4),(trp_swedish_officer,1,2),(trp_swedish_skanska_recruit,1,4)] ),

#("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,5,7),(trp_prussia_anhalt_dessau_recruit,4,12),(trp_prussia_anhalt_zerbst_recruit,4,6)] ),
#("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_zerbst_recruit,2,5),(trp_prussia_grenadier_garde_recruit,2,5),(trp_prussia_markgraf_recruit,2,6),(trp_prussia_potsdam_giant_recruit,2,5),(trp_prussia_leibregiment_recruit,2,6),(trp_prussia_officer,1,1)] ),
#("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,2,4),(trp_prussia_standard_bearer,1,1),(trp_prussia_drummer,1,1),(trp_prussia_wartensleben_recruit,1,5),(trp_prussia_leibregiment_cavalry_recruit,1,6),(trp_prussia_cuirassier_recruit,1,7)] ),

#("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_habsburg_guerilla_recuit,5,10),(trp_habsburg_muntaya_recruit,2,4),(trp_habsburg_diputacio_recruit,2,4),(trp_habsburg_barcelona_recruit,2,4),(trp_habsburg_immaculado_recruit,2,3)] ),
#("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_habsburg_eulalia_recruit,7,10),(trp_habsburg_nostra_senyora_recruit,2,4),(trp_habsburg_grenadier_recruit,1,3),(trp_habsburg_san_narciso_recruit,1,3),(trp_habsburg_nostra_del_roser_recruit,1,3),(trp_habsburg_mallorca_recruit,1,3)] ),
#("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_habsburg_officer,2,3),(trp_habsburg_nebot_dragoon_recruit,1,2),(trp_habsburg_de_la_fe_dragoon_recruit,2,5),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_drummer,1,1),(trp_habsburg_san_miguel_recruit,3,5)] ),

#("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_polish_thielau_recruit,6,11),(trp_polish_musketeer_recruit,2,4),(trp_polish_fusilier_recruit,1,2),(trp_polish_saxon_officer,1,1),(trp_polish_arquebusier_cavalry_recruit,1,1)] ),
#("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_polish_grenadier_recruit,2,5),(trp_polish_steinau_recruit,3,4),(trp_polish_pistoris_recruit,1,2),(trp_polish_kuprinz_recruit,2,3),(trp_polish_polinishce_garde_recruit,2,3),(trp_polish_sachische_garde_recruit,2,3)] ),
#("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_polish_goltz_dragoon_recruit,2,3),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_drummer,1,1),(trp_polish_guard_dragoon_recruit,3,4),(trp_polish_officer,1,1),(trp_polish_hussar_recruit,2,4)] ),

#("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_russia_strelets_recruit,6,12),(trp_russia_st_petersburg_recruit,2,4),(trp_russia_cossacks_recruit,2,5),(trp_russia_butyrsky_recruit,2,5),(trp_russia_kampenhausen_recruit,1,3)] ),
#("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_russia_narvsky_recruit,2,4),(trp_russia_semenovksy_recruit,4,7),(trp_russia_moskovsky_recruit,2,4),(trp_russia_standard_bearer,1,1),(trp_russia_ingermanlandski_recruit,3,7),(trp_russia_drummer,1,1)] ),
#("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_russia_nizhnynovgorodsky_recruit,2,6),(trp_russia_preobrazhenksy_recruit,1,5),(trp_russia_officer,1,3),(trp_russia_kroptov_recruit,2,6),(trp_russia_cossack_cavalry_recruit,2,6),(trp_russia_preobrazhenksy_grenadier_recruit,3,5)] ),

#("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ottoman_bashi_bazouk_recruit,6,12),(trp_ottoman_palestinian_recruit,2,4),(trp_ottoman_ackinci_recruit,2,5),(trp_ottoman_artillery_recruit,2,5),(trp_ottoman_bimbasha_recruit,1,1),(trp_ottoman_aleppo_recruit,1,1)] ),
#("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_ottoman_albanian_levy_recruit,2,4),(trp_ottoman_solak_recruit,4,7),(trp_ottoman_mameluke_recruit,2,4),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_bulgarian_recruit,3,7),(trp_ottoman_drummer,1,1)] ),
#("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_ottoman_wallachian_recruit,2,6),(trp_ottoman_azap_recruit,1,5),(trp_ottoman_cebelu_recruit,1,3),(trp_ottoman_sipahi_recruit,2,6),(trp_ottoman_janissary_recruit,2,6),(trp_ottoman_kapikulu_recruit,3,5)] ),



#Cavalry Reinforcements by Faction
#French
("french_cavalry_party_1", "{!}french_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,10,70),(trp_mounted_patrol,4,7),(trp_mercenary_horseman,4,6),(trp_mercenary_cavalry,2,4),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_2", "{!}french_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_french_royal_carabinier_recruit,10,60),(trp_french_royal_carabinier_experienced,4,7),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_3", "{!}french_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,10,60),(trp_french_mousquetaires_de_la_garde_veteran,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_4", "{!}french_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_french_royal_carabinier_recruit,10,70),(trp_irish_recruit,4,7),(trp_mercenary_horseman,4,6),(trp_mercenary_cavalry,2,4),(trp_scottish_mercenary_1,3,8),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_5", "{!}french_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,10,70),(trp_mounted_patrol,4,7),(trp_mercenary_horseman,4,6),(trp_mercenary_cavalry,2,4),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_6", "{!}french_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_french_royal_carabinier_recruit,10,60),(trp_manhunter,4,7),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_7", "{!}french_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_french_royal_carabinier_recruit,10,60),(trp_french_mousquetaires_de_la_garde_recruit,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_french_cavalry_officer,1,1)] ),
("french_cavalry_party_8", "{!}french_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,10,70),(trp_irish_recruit,4,7),(trp_mercenary_horseman,4,6),(trp_mercenary_cavalry,2,4),(trp_scottish_mercenary_1,3,8),(trp_french_cavalry_officer,1,1)] ),


#British
("british_cavalry_party_1", "{!}british_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,10,70),(trp_british_orkneys_regiment_recruit,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_british_cavalry_officer,1,1)] ),
("british_cavalry_party_2", "{!}british_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_british_duke_of_schomberg_regiment_recruit,10,70),(trp_british_dragoon_recruit,4,17),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,4,7),(trp_british_cavalry_officer,1,1)] ),
("british_cavalry_party_3", "{!}british_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,10,40),(trp_mercenary_swordsman,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_british_cavalry_officer,1,1),(trp_danish_tavern,1,3)] ),
("british_cavalry_party_4", "{!}british_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,10,40),(trp_mounted_patrol,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_british_cavalry_officer,1,1),(trp_british_corporal,1,3)] ),
("british_cavalry_party_5", "{!}british_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,10,70),(trp_mounted_patrol,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_british_cavalry_officer,1,1)] ),
("british_cavalry_party_6", "{!}british_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_british_duke_of_schomberg_regiment_recruit,10,70),(trp_british_dragoon_recruit,4,17),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,4,7),(trp_british_cavalry_officer,1,1)] ),
("british_cavalry_party_7", "{!}british_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,10,40),(trp_mercenary_swordsman,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_british_cavalry_officer,1,1),(trp_danish_tavern,1,3)] ),
("british_cavalry_party_8", "{!}british_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,10,40),(trp_mounted_patrol,4,17),(trp_mercenary_horseman,4,7),(trp_mercenary_cavalry,4,7),(trp_british_cavalry_officer,1,1),(trp_british_corporal,1,3)] ),


#HRE
("hre_cavalry_party_1", "{!}hre_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,10,40),(trp_austrian_hussar_green,14,27),(trp_mercenary_horseman,4,7),(trp_hessen_light_horse_recruit,14,18),(trp_austrian_cavalry_officer,1,1),(trp_savoy_dragoon_recruit,1,10)] ),
("hre_cavalry_party_2", "{!}hre_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_savoy_house_guard_recruit,10,40),(trp_savoy_house_guard_experienced,14,27),(trp_mercenary_horseman,4,7),(trp_savoy_dragoon_recruit,14,18),(trp_savoy_cavalry_officer,1,1)] ),
("hre_cavalry_party_3", "{!}hre_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_hessen_light_horse_recruit,10,40),(trp_wurttenberg_prince_cavalry_recruit,14,27),(trp_mercenary_horseman,4,7),(trp_savoy_cavalry_officer,1,1),(trp_austrian_cavalry_officer,1,2),(trp_savoy_dragoon_recruit,1,10)] ),
("hre_cavalry_party_4", "{!}hre_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_austrian_cuirassier_recruit,10,40),(trp_austrian_cuirassier_experienced,14,18),(trp_austrian_cavalry_officer,1,1),(trp_austrian_hussar_recruit,1,10)] ),
("hre_cavalry_party_5", "{!}hre_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,10,40),(trp_austrian_cuirassier_recruit,14,27),(trp_mercenary_horseman,4,7),(trp_hessen_light_horse_recruit,14,18),(trp_austrian_cavalry_officer,1,1),(trp_savoy_dragoon_recruit,1,10)] ),
("hre_cavalry_party_6", "{!}hre_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_austrian_cuirassier_recruit,10,40),(trp_wurttenberg_prince_cavalry_recruit,14,27),(trp_mercenary_horseman,4,7),(trp_hessen_light_horse_recruit,14,18),(trp_savoy_cavalry_officer,1,1),(trp_savoy_dragoon_recruit,1,10)] ),
("hre_cavalry_party_7", "{!}hre_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,10,40),(trp_wurttenberg_prince_cavalry_recruit,14,27),(trp_mercenary_horseman,4,7),(trp_savoy_cavalry_officer,1,1),(trp_austrian_cavalry_officer,1,2),(trp_savoy_dragoon_recruit,1,10)] ),
("hre_cavalry_party_8", "{!}hre_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_austrian_cuirassier_recruit,14,18),(trp_austrian_cavalry_officer,1,1),(trp_hessen_erbprinz_regiment_recruit,1,10)] ),

#Bavarian
("bavarian_cavalry_party_1", "{!}bavarian_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,10,60),(trp_mounted_patrol,14,27),(trp_mercenary_horseman,4,7),(trp_bavaria_dragoon_experienced,14,18),(trp_bavaria_cavalry_officer,1,1),(trp_bavaria_dragoon_hardened,1,10)] ),
("bavarian_cavalry_party_2", "{!}bavarian_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_bavaria_grenadier_guard_recruit,10,40),(trp_bavaria_grenadier_guard_green,14,27),(trp_mounted_patrol,4,7),(trp_bavaria_grenadier_guard_experienced,14,18),(trp_bavaria_cavalry_officer,1,1),(trp_bavaria_grenadier_recruit,1,10)] ),
("bavarian_cavalry_party_3", "{!}bavarian_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,10,40),(trp_mounted_patrol,14,27),(trp_mercenary_horseman,4,7),(trp_bavaria_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("bavarian_cavalry_party_4", "{!}bavarian_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_bavaria_grenadier_guard_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_swiss_recruit,14,18),(trp_bavaria_cavalry_officer,1,1),(trp_bavaria_corporal,1,10)] ),
("bavarian_cavalry_party_5", "{!}bavarian_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,10,60),(trp_mounted_patrol,14,27),(trp_mercenary_horseman,4,7),(trp_swiss_recruit,14,18),(trp_bavaria_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("bavarian_cavalry_party_6", "{!}bavarian_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_bavaria_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("bavarian_cavalry_party_7", "{!}bavarian_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,10,40),(trp_mounted_patrol,14,27),(trp_mercenary_horseman,4,7),(trp_bavaria_cavalry_officer,1,1)] ),
("bavarian_cavalry_party_8", "{!}bavarian_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_swiss_recruit,14,18),(trp_bavaria_cavalry_officer,1,1),(trp_bavaria_corporal,1,10)] ),


#United Provinces/Dutch
("dutch_cavalry_party_1", "{!}dutch_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,10,60),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_dutch_van_massou_green,14,18),(trp_dutch_cavalry_officer,1,1),(trp_dutch_musketeer_recruit,1,10)] ),
("dutch_cavalry_party_2", "{!}dutch_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_dutch_cuirassier_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_dutch_cuirassier_green,14,18),(trp_dutch_cavalry_officer,1,1),(trp_dutch_cuirassier_experienced,1,10)] ),
("dutch_cavalry_party_3", "{!}dutch_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,10,40),(trp_dutch_van_massou_green,14,27),(trp_mercenary_horseman,4,7),(trp_dutch_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("dutch_cavalry_party_4", "{!}dutch_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_dutch_cuirassier_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_mercenary_swordsman,14,18),(trp_dutch_cavalry_officer,1,1),(trp_dutch_corporal,1,10)] ),
("dutch_cavalry_party_5", "{!}dutch_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,10,60),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,14,18),(trp_dutch_cavalry_officer,1,1),(trp_dutch_musketeer_recruit,1,10)] ),
("dutch_cavalry_party_6", "{!}dutch_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_dutch_cuirassier_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_dutch_cuirassier_experienced,14,18),(trp_dutch_cavalry_officer,1,1),(trp_musketeer_1,1,10)] ),
("dutch_cavalry_party_7", "{!}dutch_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,10,40),(trp_dutch_van_massou_green,14,27),(trp_mercenary_horseman,4,7),(trp_dutch_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("dutch_cavalry_party_8", "{!}dutch_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_dutch_cuirassier_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_dutch_cuirassier_experienced,14,18),(trp_dutch_cavalry_officer,1,1),(trp_dutch_corporal,1,10)] ),

#Spanish Bourbons
("spanish_bourbon_cavalry_party_1", "{!}spanish_bourbon_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,10,60),(trp_bourbon_mosquetero_guardia_green,14,18),(trp_bourbon_cavalry_officer,1,1)] ),
("spanish_bourbon_cavalry_party_2", "{!}spanish_bourbon_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_bourbon_royal_guards_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_bourbon_royal_guards_experienced,4,7),(trp_bourbon_royal_guards_green,14,18),(trp_bourbon_cavalry_officer,1,1)] ),
("spanish_bourbon_cavalry_party_3", "{!}spanish_bourbon_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,10,40),(trp_bourbon_mosquetero_guardia_green,14,27),(trp_irish_recruit,4,7),(trp_bourbon_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("spanish_bourbon_cavalry_party_4", "{!}spanish_bourbon_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_bourbon_royal_guards_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_bourbon_royal_guards_experienced,14,18),(trp_bourbon_cavalry_officer,1,1),(trp_mounted_patrol,1,10)] ),
("spanish_bourbon_cavalry_party_5", "{!}spanish_bourbon_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,10,60),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,14,18),(trp_bourbon_cavalry_officer,1,1),(trp_pikeman_recruit,1,10)] ),
("spanish_bourbon_cavalry_party_6", "{!}spanish_bourbon_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_bourbon_royal_guards_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_bourbon_walloon_recruit,14,18),(trp_bourbon_cavalry_officer,1,1),(trp_musketeer_1,1,10)] ),
("spanish_bourbon_cavalry_party_7", "{!}spanish_bourbon_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,10,40),(trp_bourbon_mosquetero_guardia_green,14,27),(trp_irish_recruit,4,7),(trp_bourbon_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("spanish_bourbon_cavalry_party_8", "{!}spanish_bourbon_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_bourbon_royal_guards_recruit,10,40),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_mercenary_swordsman,14,18),(trp_bourbon_cavalry_officer,1,1),(trp_bourbon_corporal,1,10)] ),

#Danish 
("danish_cavalry_party_1", "{!}danish_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,10,60),(trp_danish_life_dragoon_green,14,27),(trp_mercenary_horseman,4,7),(trp_danish_life_dragoon_experienced,14,18),(trp_danish_cavalry_officer,1,1)] ),
("danish_cavalry_party_2", "{!}danish_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_danish_ungerska_drongera_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_danish_ungerska_drongera_green,14,18),(trp_danish_cavalry_officer,1,1),(trp_danish_ungerska_drongera_experienced,1,10)] ),
("danish_cavalry_party_3", "{!}danish_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_danish_livegardet_till_hast_recruit,10,40),(trp_danish_livegardet_till_hast_green,14,27),(trp_danish_livegardet_till_hast_experienced,4,7),(trp_danish_cavalry_officer,1,1),(trp_danish_livegardet_till_hast_elite,1,10)] ),
("danish_cavalry_party_4", "{!}danish_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_danish_ungerska_drongera_recruit,10,40),(trp_danish_ungerska_drongera_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_mercenary_swordsman,14,18),(trp_danish_cavalry_officer,1,1),(trp_danish_sjallandska_recruit,1,10)] ),
("danish_cavalry_party_5", "{!}danish_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_danish_ungerska_drongera_recruit,10,60),(trp_mercenary_cavalry,14,27),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,14,18),(trp_danish_cavalry_officer,1,1),(trp_hired_blade,1,10)] ),
("danish_cavalry_party_6", "{!}danish_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_danish_militia_recruit,14,18),(trp_danish_cavalry_officer,1,1),(trp_hired_blade,1,10)] ),
("danish_cavalry_party_7", "{!}danish_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_danish_livegardet_till_hast_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_mounted_patrol,4,7),(trp_danish_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("danish_cavalry_party_8", "{!}danish_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,10,40),(trp_danish_life_dragoon_green,14,27),(trp_mercenary_horseman,4,7),(trp_mercenary_swordsman,14,18),(trp_danish_cavalry_officer,1,1),(trp_mounted_patrol,1,10)] ),

#Swedish 
("swedish_cavalry_party_1", "{!}swedish_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_swedish_pommerska_recruit,10,60),(trp_swedish_pommerska_elite,14,27),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,14,18),(trp_swedish_cavalry_officer,1,1),(trp_swedish_pommerska_green,1,10)] ),
("swedish_cavalry_party_2", "{!}swedish_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_swedish_nyland_recruit,10,40),(trp_swedish_nyland_green,14,27),(trp_swedish_nyland_experienced,4,7),(trp_swedish_nyland_hardened,14,18),(trp_swedish_cavalry_officer,1,1),(trp_swedish_nyland_veteran,1,10)] ),
("swedish_cavalry_party_3", "{!}swedish_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_swedish_karelska_recruit,10,40),(trp_swedish_karelska_green,14,27),(trp_swedish_karelska_experienced,4,7),(trp_swedish_cavalry_officer,1,1),(trp_swedish_karelska_veteran,1,10)] ),
("swedish_cavalry_party_4", "{!}swedish_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_swedish_skanska_recruit,10,40),(trp_swedish_skanska_green,14,27),(trp_mercenary_horseman,4,7),(trp_swedish_karelska_veteran,14,18),(trp_swedish_cavalry_officer,1,1),(trp_swedish_pikeman_recruit,1,10)] ),
("swedish_cavalry_party_5", "{!}swedish_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_swedish_drabant_garde_recruit,10,60),(trp_swedish_drabant_garde_green,14,27),(trp_mercenary_horseman,4,7),(trp_swedish_drabant_garde_veteran,14,18),(trp_swedish_cavalry_officer,1,1),(trp_swedish_drabant_garde_experienced,1,10)] ),
("swedish_cavalry_party_6", "{!}swedish_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_swedish_nyland_recruit,10,40),(trp_swedish_nyland_green,14,27),(trp_mounted_patrol,4,7),(trp_swedish_alvsborg_recruit,14,18),(trp_swedish_cavalry_officer,1,1),(trp_swedish_nyland_experienced,1,10)] ),
("swedish_cavalry_party_7", "{!}swedish_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_swedish_pommerska_recruit,10,40),(trp_swedish_pommerska_elite,14,27),(trp_mercenary_horseman,4,7),(trp_swedish_cavalry_officer,1,1),(trp_swedish_drabant_garde_recruit,1,10)] ),
("swedish_cavalry_party_8", "{!}swedish_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_swedish_skanska_recruit,10,40),(trp_mounted_patrol,14,27),(trp_mercenary_horseman,4,7),(trp_mercenary_swordsman,14,18),(trp_swedish_cavalry_officer,1,1),(trp_swedish_dal_recruit,1,10)] ),

#Prussian 
("prussian_cavalry_party_1", "{!}prussian_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,10,60),(trp_prussia_portail_cavalry_elite,14,27),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,14,18),(trp_prussia_cavalry_officer,1,1),(trp_prussia_portail_cavalry_green,1,10)] ),
("prussian_cavalry_party_2", "{!}prussian_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_prussia_wartensleben_recruit,10,40),(trp_prussia_wartensleben_veteran,14,27),(trp_mounted_patrol,4,7),(trp_prussia_markgraf_recruit,14,18),(trp_prussia_cavalry_officer,1,1),(trp_prussia_wartensleben_experienced,1,10)] ),
("prussian_cavalry_party_3", "{!}prussian_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_prussia_leibregiment_cavalry_recruit,10,40),(trp_prussia_leibregiment_cavalry_green,14,27),(trp_prussia_leibregiment_cavalry_veteran,4,7),(trp_prussia_cavalry_officer,1,1),(trp_prussia_leibregiment_cavalry_experienced,1,10)] ),
("prussian_cavalry_party_4", "{!}prussian_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_prussia_cuirassier_recruit,10,40),(trp_prussia_cuirassier_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_prussia_cuirassier_experienced,14,18),(trp_prussia_cavalry_officer,1,1),(trp_prussia_cuirassier_green,1,10)] ),
("prussian_cavalry_party_5", "{!}prussian_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_prussia_wartensleben_recruit,10,60),(trp_prussia_wartensleben_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_mounted_patrol,14,18),(trp_prussia_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("prussian_cavalry_party_6", "{!}prussian_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,10,40),(trp_prussia_portail_cavalry_elite,14,27),(trp_mounted_patrol,4,7),(trp_prussia_anhalt_zerbst_recruit,14,18),(trp_prussia_cavalry_officer,1,1),(trp_prussia_portail_cavalry_green,1,10)] ),
("prussian_cavalry_party_7", "{!}prussian_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_prussia_cuirassier_recruit,10,40),(trp_prussia_cuirassier_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_prussia_cavalry_officer,1,1),(trp_mercenary_cavalry,1,10)] ),
("prussian_cavalry_party_8", "{!}prussian_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,10,40),(trp_prussia_portail_cavalry_green,14,27),(trp_mercenary_horseman,4,7),(trp_prussia_portail_cavalry_experienced,14,18),(trp_prussia_cavalry_officer,1,1),(trp_prussia_cuirassier_green,1,10)] ),

#Habsburg Spanish 
("spanish_habsburg_cavalry_party_1", "{!}spanish_habsburg_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_recruit,10,60),(trp_habsburg_nebot_dragoon_veteran,14,27),(trp_mercenary_horseman,14,17),(trp_habsburg_guerilla_recuit,1,8),(trp_habsburg_cavalry_officer,1,1),(trp_habsburg_nebot_dragoon_green,1,5)] ),
("spanish_habsburg_cavalry_party_2", "{!}spanish_habsburg_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_habsburg_de_la_fe_dragoon_green,10,40),(trp_habsburg_de_la_fe_dragoon_recruit,14,27),(trp_mounted_patrol,4,7),(trp_habsburg_cavalry_officer,1,1),(trp_mercenary_horseman,1,10)] ),
("spanish_habsburg_cavalry_party_3", "{!}spanish_habsburg_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_habsburg_san_miguel_recruit,10,40),(trp_habsburg_san_miguel_green,14,27),(trp_mercenary_horseman,4,7),(trp_habsburg_cavalry_officer,1,1),(trp_habsburg_guerilla_recuit,1,10)] ),
("spanish_habsburg_cavalry_party_4", "{!}spanish_habsburg_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_recruit,10,40),(trp_habsburg_nebot_dragoon_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_mercenary_swordsman,14,18),(trp_habsburg_cavalry_officer,1,1),(trp_habsburg_guerilla_recuit,1,10)] ),
("spanish_habsburg_cavalry_party_5", "{!}spanish_habsburg_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_habsburg_de_la_fe_dragoon_recruit,10,60),(trp_habsburg_de_la_fe_dragoon_green,14,27),(trp_mercenary_horseman,14,17),(trp_habsburg_guerilla_recuit,1,8),(trp_habsburg_cavalry_officer,1,1),(trp_habsburg_de_la_fe_dragoon_veteran,1,5)] ),
("spanish_habsburg_cavalry_party_6", "{!}spanish_habsburg_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_elite,10,40),(trp_habsburg_nebot_dragoon_recruit,14,27),(trp_mounted_patrol,4,7),(trp_habsburg_cavalry_officer,1,1),(trp_mercenary_horseman,1,10)] ),
("spanish_habsburg_cavalry_party_7", "{!}spanish_habsburg_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_recruit,10,40),(trp_habsburg_de_la_fe_dragoon_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_habsburg_cavalry_officer,1,1),(trp_habsburg_guerilla_recuit,1,10)] ),
("spanish_habsburg_cavalry_party_8", "{!}spanish_habsburg_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_habsburg_san_miguel_recruit,10,40),(trp_habsburg_san_miguel_veteran,14,27),(trp_mercenary_horseman,4,7),(trp_habsburg_san_miguel_green,14,18),(trp_habsburg_cavalry_officer,1,1),(trp_habsburg_guerilla_recuit,1,10)] ),

#Polish
("polish_cavalry_party_1", "{!}polish_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_polish_dragoon_recruit,10,60),(trp_polish_dragoon_green,14,27),(trp_mercenary_horseman,4,7),(trp_polish_hussar_recruit,14,18),(trp_polish_cavalry_officer,1,1),(trp_slave_driver,1,10)] ),
("polish_cavalry_party_2", "{!}polish_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_polish_goltz_dragoon_recruit,10,40),(trp_polish_goltz_dragoon_green,14,27),(trp_mounted_patrol,4,7),(trp_polish_goltz_dragoon_experienced,14,18),(trp_polish_saxon_cavalry_officer,1,1),(trp_slave_crusher,1,10)] ),
("polish_cavalry_party_3", "{!}polish_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_polish_saxon_cuirassier_recruit,10,40),(trp_polish_saxon_cuirassier_green,14,27),(trp_mercenary_horseman,4,7),(trp_polish_saxon_cavalry_officer,1,1),(trp_polish_saxon_cuirassier_experienced,1,10)] ),
("polish_cavalry_party_4", "{!}polish_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_polish_hussar_recruit,10,40),(trp_polish_hussar_green,14,27),(trp_polish_hussar_veteran,4,7),(trp_polish_hussar_experienced,14,18),(trp_polish_cavalry_officer,1,1),(trp_slave_master,1,10)] ),
("polish_cavalry_party_5", "{!}polish_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_polish_arquebusier_cavalry_recruit,10,60),(trp_polish_arquebusier_cavalry_green,14,27),(trp_mercenary_horseman,4,7),(trp_polish_arquebusier_cavalry_experienced,14,18),(trp_polish_cavalry_officer,1,1),(trp_polish_hussar_green,1,10)] ),
("polish_cavalry_party_6", "{!}polish_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_polish_cuirassier_recruit,10,40),(trp_polish_cuirassier_green,14,27),(trp_polish_hussar_recruit,4,7),(trp_polish_cuirassier_experienced,14,18),(trp_polish_cavalry_officer,1,1),(trp_slave_crusher,1,10)] ),
("polish_cavalry_party_7", "{!}polish_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_polish_goltz_dragoon_recruit,10,40),(trp_polish_saxon_cuirassier_green,14,27),(trp_mercenary_horseman,4,7),(trp_polish_saxon_cavalry_officer,1,1),(trp_polish_goltz_dragoon_green,1,10)] ),
("polish_cavalry_party_8", "{!}polish_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_polish_guard_dragoon_recruit,10,40),(trp_polish_guard_dragoon_green,14,27),(trp_mercenary_horseman,4,7),(trp_polish_guard_dragoon_experienced,14,18),(trp_polish_cavalry_officer,1,1),(trp_slave_master,1,10)] ),

#Russian
("russian_cavalry_party_1", "{!}russian_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_russia_moskovsky_recruit,10,60),(trp_russia_moskovsky_green,14,27),(trp_russia_moskovsky_veteran,4,7),(trp_russia_cavalry_officer,1,1),(trp_russia_moskovsky_experienced,1,10)] ),
("russian_cavalry_party_2", "{!}russian_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_russia_ingermanlandski_recruit,10,40),(trp_russia_ingermanlandski_green,14,27),(trp_russia_ingermanlandski_experienced,4,7),(trp_russia_cossack_cavalry_recruit,14,18),(trp_russia_cavalry_officer,1,1),(trp_slave_crusher,1,10)] ),
("russian_cavalry_party_3", "{!}russian_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_russia_cossack_cavalry_recruit,10,40),(trp_russia_cossack_cavalry_green,14,27),(trp_slave_driver,4,7),(trp_russia_cavalry_officer,1,1),(trp_russia_cossack_cavalry_experienced,1,10)] ),
("russian_cavalry_party_4", "{!}russian_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_russia_kroptov_recruit,10,60),(trp_russia_kroptov_green,14,27),(trp_russia_kroptov_experienced,4,7),(trp_russia_cavalry_officer,1,1),(trp_slave_master,1,10)] ),
("russian_cavalry_party_5", "{!}russian_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_russia_cossack_cavalry_recruit,10,60),(trp_russia_moskovsky_green,14,27),(trp_slave_crusher,4,7),(trp_russia_cavalry_officer,1,1),(trp_slave_driver,1,20)] ),
("russian_cavalry_party_6", "{!}russian_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_russia_cossack_cavalry_recruit,10,40),(trp_mercenary_horseman,14,27),(trp_slave_crusher,4,7),(trp_russia_moskovsky_recruit,14,18),(trp_russia_cavalry_officer,1,1),(trp_slave_crusher,1,10)] ),
("russian_cavalry_party_7", "{!}russian_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_russia_ingermanlandski_elite,10,40),(trp_russia_kroptov_green,14,27),(trp_slave_driver,4,7),(trp_russia_cavalry_officer,1,1),(trp_russia_moskovsky_recruit,1,10)] ),
("russian_cavalry_party_8", "{!}russian_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_russia_cossack_cavalry_recruit,10,60),(trp_russia_moskovsky_recruit,14,27),(trp_mercenary_horseman,4,7),(trp_russia_cavalry_officer,1,1),(trp_slave_master,1,10)] ),

#Ottoman
("ottoman_cavalry_party_1", "{!}ottoman_cavalry_party_1", 0, 0, fac_commoners, 0, [(trp_ottoman_ackinci_recruit,10,60),(trp_ottoman_mameluke_recruit,14,27),(trp_ottoman_ackinci_veteran,4,7),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_militia_5,1,10)] ),
("ottoman_cavalry_party_2", "{!}ottoman_cavalry_party_2", 0, 0, fac_commoners, 0, [(trp_ottoman_mameluke_recruit,10,40),(trp_ottoman_mameluke_veteran,14,27),(trp_ottoman_mameluke_elite,4,7),(trp_ottoman_aleppo_recruit,14,18),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_militia_6,1,10)] ),
("ottoman_cavalry_party_3", "{!}ottoman_cavalry_party_3", 0, 0, fac_commoners, 0, [(trp_ottoman_cebelu_recruit,10,40),(trp_ottoman_kapikulu_veteran,14,27),(trp_ottoman_ackinci_recruit,4,7),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_militia_6,1,10)] ),
("ottoman_cavalry_party_4", "{!}ottoman_cavalry_party_4", 0, 0, fac_commoners, 0, [(trp_ottoman_sipahi_recruit,10,60),(trp_ottoman_sipahi_veteran,14,27),(trp_ottoman_kapikulu_veteran,4,7),(trp_ottoman_cavalry_officer,1,1)] ),
("ottoman_cavalry_party_5", "{!}ottoman_cavalry_party_5", 0, 0, fac_commoners, 0, [(trp_ottoman_aleppo_recruit,10,60),(trp_ottoman_aleppo_green,14,27),(trp_ottoman_ackinci_veteran,4,7),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_aleppo_veteran,1,10)] ),
("ottoman_cavalry_party_6", "{!}ottoman_cavalry_party_6", 0, 0, fac_commoners, 0, [(trp_ottoman_mameluke_recruit,10,40),(trp_ottoman_mameluke_veteran,14,27),(trp_ottoman_mameluke_elite,4,7),(trp_ottoman_ackinci_recruit,14,18),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_militia_6,1,10)] ),
("ottoman_cavalry_party_7", "{!}ottoman_cavalry_party_7", 0, 0, fac_commoners, 0, [(trp_ottoman_kapikulu_green,10,40),(trp_ottoman_kapikulu_veteran,14,27),(trp_ottoman_kapikulu_recruit,4,7),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_militia_6,1,10)] ),
("ottoman_cavalry_party_8", "{!}ottoman_cavalry_party_8", 0, 0, fac_commoners, 0, [(trp_ottoman_sipahi_green,10,60),(trp_ottoman_sipahi_recruit,14,27),(trp_ottoman_cebelu_recruit,4,7),(trp_ottoman_cavalry_officer,1,1),(trp_ottoman_militia_5,1,10)] ),


#Infantry Reinforcement Templates by Faction - 8 per faction

#French
("french_infantry_party_1", "{!}french_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_french_regiment_du_roi_recruit,40,80),(trp_french_regiment_du_roi_veteran,20,40),(trp_french_regiment_du_roi_elite,4,6),(trp_french_standard_bearer,1,1),(trp_french_corporal,1,3),(trp_french_drummer,1,1)] ),
("french_infantry_party_2", "{!}french_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_regiment_surbeck_recruit,30,60),(trp_regiment_surbeck_veteran,40,70),(trp_irish_recruit,4,7),(trp_french_standard_bearer,1,1),(trp_french_officer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_3", "{!}french_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_garde_suisses_recruit,40,60),(trp_garde_suisses_veteran,40,60),(trp_french_grenadier_recruit,4,7),(trp_french_standard_bearer,1,1),(trp_french_officer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_4", "{!}french_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_gardes_francaises_recruit,60,70),(trp_irish_recruit,20,30),(trp_gardes_francaises_veteran,25,65),(trp_french_standard_bearer,1,1),(trp_french_corporal,1,8),(trp_french_drummer,1,1)] ),
("french_infantry_party_5", "{!}french_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_french_grenadier_recruit,40,70),(trp_swiss_recruit,20,50),(trp_french_grenadier_veteran,20,30),(trp_french_standard_bearer,1,1),(trp_french_sergeant,1,3),(trp_french_drummer,1,1)] ),
("french_infantry_party_6", "{!}french_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_french_de_la_marine_recruit,20,60),(trp_musketeer_1,40,80),(trp_scottish_mercenary_1,4,7),(trp_french_standard_bearer,1,1),(trp_french_officer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_7", "{!}french_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_regiment_clare_recruit,40,60),(trp_regiment_clare_veteran,25,60),(trp_mercenary_swordsman,4,7),(trp_french_standard_bearer,1,1),(trp_french_officer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_8", "{!}french_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_regiment_surbeck_recruit,50,70),(trp_irish_recruit,20,50),(trp_royal_italien_recruit,40,60),(trp_french_corporal,2,4),(trp_french_standard_bearer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_9", "{!}french_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_french_regiment_la_reine_recruit,40,80),(trp_french_regiment_la_reine_elite,20,40),(trp_swiss_recruit,4,6),(trp_french_standard_bearer,1,1),(trp_french_corporal,1,3),(trp_french_drummer,1,1)] ),
("french_infantry_party_10", "{!}french_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_royal_italien_recruit,30,60),(trp_royal_italien_green,40,70),(trp_scottish_mercenary_1,4,7),(trp_french_standard_bearer,1,1),(trp_french_officer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_11", "{!}french_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_french_regiment_lorraine_recruit,40,60),(trp_french_regiment_lorraine_green,40,60),(trp_french_grenadier_recruit,4,7),(trp_french_standard_bearer,1,1),(trp_french_officer,1,1),(trp_french_drummer,1,1)] ),
("french_infantry_party_12", "{!}french_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_french_de_la_marine_recruit,80,100),(trp_french_de_la_marine_veteran,20,30),(trp_mercenary_swordsman,5,10),(trp_french_standard_bearer,1,1),(trp_french_corporal,1,8),(trp_french_drummer,1,1)] ),

#British
("british_infantry_party_1", "{!}british_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,40,80),(trp_british_orkneys_regiment_experienced,20,40),(trp_mercenary_swordsman,4,6),(trp_british_standard_bearer,1,1),(trp_british_corporal,1,3),(trp_british_drummer,1,1)] ),
("british_infantry_party_2", "{!}british_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_british_churchill_regiment_recruit,30,60),(trp_british_churchill_regiment_veteran,40,70),(trp_british_churchill_regiment_elite,4,7),(trp_british_standard_bearer,1,1),(trp_british_officer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_3", "{!}british_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_british_webb_regiment_recruit,40,60),(trp_british_webb_regiment_veteran,40,60),(trp_mercenary_swordsman,4,7),(trp_british_standard_bearer,1,1),(trp_british_officer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_4", "{!}british_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_british_welch_fusiliers_recruit,60,70),(trp_british_welch_fusiliers_experienced,20,30),(trp_british_welch_fusiliers_elite,25,65),(trp_british_standard_bearer,1,1),(trp_british_corporal,1,8),(trp_british_drummer,1,1)] ),
("british_infantry_party_5", "{!}british_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_british_howe_regiment_recruit,40,70),(trp_british_howe_regiment_experienced,20,50),(trp_british_grenadier_guard_recruit,20,30),(trp_british_standard_bearer,1,1),(trp_british_corporal,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_6", "{!}british_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_british_marlborough_regiment_recruit,20,60),(trp_british_marlborough_regiment_veteran,40,80),(trp_british_standard_bearer,1,1),(trp_british_grenadier_1st_foot_guard_recruit,20,30),(trp_british_officer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_7", "{!}british_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_british_grenadier_1st_foot_guard_recruit,40,60),(trp_british_grenadier_1st_foot_guard_veteran,25,60),(trp_mercenary_swordsman,4,7),(trp_british_standard_bearer,1,1),(trp_british_officer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_8", "{!}british_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_british_grenadier_guard_recruit,50,70),(trp_british_grenadier_guard_veteran,20,50),(trp_mercenary_swordsman,40,60),(trp_british_corporal,2,4),(trp_british_standard_bearer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_9", "{!}british_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_mercenary_swordsman,40,70),(trp_hired_blade,20,50),(trp_british_grenadier_guard_recruit,20,30),(trp_british_standard_bearer,1,1),(trp_british_corporal,1,1),(trp_militia_drummer,1,1)] ),
("british_infantry_party_10", "{!}british_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_british_churchill_regiment_recruit,20,60),(trp_pikeman_recruit,40,80),(trp_british_standard_bearer,1,1),(trp_british_grenadier_1st_foot_guard_recruit,20,30),(trp_british_officer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_11", "{!}british_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_british_howe_regiment_recruit,40,60),(trp_british_grenadier_1st_foot_guard_veteran,25,60),(trp_mercenary_swordsman,4,7),(trp_british_standard_bearer,1,1),(trp_british_officer,1,1),(trp_british_drummer,1,1)] ),
("british_infantry_party_12", "{!}british_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,50,70),(trp_british_grenadier_guard_recruit,20,50),(trp_british_orkneys_regiment_green,40,60),(trp_british_corporal,2,4),(trp_british_standard_bearer,1,1),(trp_british_drummer,1,1)] ),

#HRE
("hre_infantry_party_1", "{!}hre_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_austrian_wuerttemburg_regiment_recruit,40,80),(trp_austrian_wuerttemburg_regiment_green,20,40),(trp_austrian_grenadier_recruit,4,6),(trp_austrian_standard_bearer,1,1),(trp_austrian_sergeant,1,3),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_2", "{!}hre_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_austrian_wetzel_regiment_recruit,30,60),(trp_austrian_wetzel_regiment_veteran,40,70),(trp_austrian_wetzel_regiment_elite,4,7),(trp_austrian_standard_bearer,1,1),(trp_austrian_officer,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_3", "{!}hre_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_savoy_pikeline_recruit,40,60),(trp_savoy_rehbinder_recruit,40,60),(trp_savoy_pikeline_veteran,4,7),(trp_savoy_standard_bearer,1,1),(trp_savoy_sergeant,1,3),(trp_savoy_drummer,1,1)] ),
("hre_infantry_party_4", "{!}hre_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_savoy_grenadier_recruit,60,70),(trp_savoy_desportes_recruit,20,30),(trp_savoy_desportes_green,25,65),(trp_savoy_standard_bearer,1,1),(trp_savoy_sergeant,1,8),(trp_savoy_drummer,1,1)] ),
("hre_infantry_party_5", "{!}hre_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_hessen_schopping_regiment_recruit,40,70),(trp_hessen_schopping_veteran,20,50),(trp_mercenary_swordsman,20,30),(trp_austrian_standard_bearer,1,1),(trp_austrian_corporal,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_6", "{!}hre_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_austrian_regiment_von_deutschmeister_recruit,20,60),(trp_austrian_regiment_von_deutschmeister_veteran,40,80),(trp_austrian_standard_bearer,1,1),(trp_austrian_grenadier_recruit,20,30),(trp_austrian_officer,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_7", "{!}hre_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_austrian_grenadier_recruit,40,60),(trp_hessen_leibguard_recruit,25,60),(trp_austrian_grenadier_veteran,4,7),(trp_austrian_standard_bearer,1,1),(trp_austrian_officer,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_8", "{!}hre_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_hessen_erbprinz_regiment_recruit,50,70),(trp_hessen_erbprinz_veteran,20,50),(trp_mercenary_swordsman,40,60),(trp_austrian_corporal,2,4),(trp_austrian_standard_bearer,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_9", "{!}hre_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_hessen_prinz_wilhem_regiment_recruit,40,70),(trp_hessen_schopping_veteran,20,50),(trp_austrian_wetzel_regiment_recruit,20,30),(trp_austrian_standard_bearer,1,1),(trp_austrian_corporal,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_10", "{!}hre_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_savoy_grenadier_recruit,20,60),(trp_savoy_grenadier_experienced,40,80),(trp_savoy_standard_bearer,1,1),(trp_savoy_pikeline_recruit,20,30),(trp_savoy_sergeant,1,1),(trp_savoy_drummer,1,1)] ),
("hre_infantry_party_11", "{!}hre_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_hessen_leibguard_recruit,40,60),(trp_hessen_leibguard_veteran,25,60),(trp_austrian_grenadier_recruit,4,7),(trp_austrian_standard_bearer,1,1),(trp_austrian_officer,1,1),(trp_austrian_drummer,1,1)] ),
("hre_infantry_party_12", "{!}hre_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_austrian_wetzel_regiment_recruit,50,70),(trp_austrian_grenadier_recruit,20,50),(trp_mercenary_swordsman,40,60),(trp_austrian_corporal,2,4),(trp_austrian_standard_bearer,1,1),(trp_austrian_drummer,1,1)] ),

#Bavaria
("bavarian_infantry_party_1", "{!}bavarian_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_bavaria_leib_regiment_recruit,40,80),(trp_bavaria_leib_regiment_experienced,20,40),(trp_mercenary_swordsman,4,6),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_corporal,1,3),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_2", "{!}bavarian_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_bavaria_karthausen_recruit,30,60),(trp_bavaria_karthausen_experienced,40,70),(trp_bavaria_grenadier_recruit,4,7),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_officer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_3", "{!}bavarian_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_bavaria_maffey_recruit,40,60),(trp_bavaria_maffey_experienced,40,60),(trp_swiss_recruit,4,7),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_corporal,1,3),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_4", "{!}bavarian_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_bavria_kurzprinz_recruit,60,70),(trp_bavria_kurzprinz_experienced,20,30),(trp_bavria_kurzprinz_elite,25,65),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_corporal,1,8),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_5", "{!}bavarian_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_bavaria_leib_regiment_recruit,40,70),(trp_bavaria_leib_regiment_hardened,20,50),(trp_mercenary_swordsman,20,30),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_corporal,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_6", "{!}bavarian_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_bavaria_grenadier_recruit,20,60),(trp_bavaria_grenadier_green,40,80),(trp_bavaria_standard_bearer,1,1),(trp_musketeer_2,20,30),(trp_bavaria_officer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_7", "{!}bavarian_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_bavria_kurzprinz_recruit,40,60),(trp_bavria_kurzprinz_green,25,60),(trp_swiss_recruit,4,7),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_officer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_8", "{!}bavarian_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_bavaria_karthausen_recruit,50,70),(trp_bavaria_karthausen_green,20,50),(trp_bavaria_karthausen_veteran,40,60),(trp_bavaria_corporal,2,4),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_9", "{!}bavarian_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_bavaria_maffey_recruit,40,70),(trp_bavaria_maffey_experienced,20,50),(trp_bavaria_grenadier_recruit,20,30),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_corporal,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_10", "{!}bavarian_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_bavaria_karthausen_hardened,20,60),(trp_bavaria_karthausen_recruit,40,80),(trp_bavaria_standard_bearer,1,1),(trp_musketeer_2,20,30),(trp_bavaria_officer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_11", "{!}bavarian_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_bavaria_leib_regiment_recruit,40,60),(trp_bavaria_leib_regiment_green,25,60),(trp_bavaria_leib_regiment_experienced,4,7),(trp_bavaria_standard_bearer,1,1),(trp_bavaria_officer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_infantry_party_12", "{!}bavarian_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_bavaria_maffey_recruit,50,70),(trp_mercenary_swordsman,20,50),(trp_hired_blade,40,60),(trp_bavaria_corporal,2,4),(trp_bavaria_standard_bearer,1,1),(trp_militia_drummer,1,1)] ),

#Dutch
("dutch_infantry_party_1", "{!}dutch_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,40,80),(trp_dutch_musketeer_green,20,40),(trp_dutch_musketeer_veteran,4,6),(trp_dutch_standard_bearer,1,1),(trp_dutch_corporal,1,3),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_2", "{!}dutch_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_dutch_oranje_gelderland_recruit,30,60),(trp_dutch_oranje_gelderland_green,40,70),(trp_dutch_oranje_gelderland_experienced,4,7),(trp_dutch_standard_bearer,1,1),(trp_dutch_officer,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_3", "{!}dutch_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_dutch_zweeds_recruit,40,60),(trp_dutch_zweeds_green,40,60),(trp_dutch_zweeds_experienced,4,7),(trp_dutch_standard_bearer,1,1),(trp_dutch_corporal,1,3),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_4", "{!}dutch_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_dutch_nassau_recruit,60,70),(trp_dutch_nassau_green,20,30),(trp_dutch_nassau_exprienced,25,65),(trp_dutch_standard_bearer,1,1),(trp_dutch_corporal,1,8),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_5", "{!}dutch_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_dutch_opstad_recruit,40,70),(trp_dutch_opstad_green,20,50),(trp_dutch_opstad_experienced,20,30),(trp_dutch_standard_bearer,1,1),(trp_dutch_corporal,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_6", "{!}dutch_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_dutch_blue_guard_recruit,20,60),(trp_dutch_blue_guard_green,40,80),(trp_dutch_standard_bearer,1,1),(trp_dutch_blue_guard_experienced,20,30),(trp_dutch_officer,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_7", "{!}dutch_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_dutch_grenadier_recruit,40,60),(trp_dutch_grenadier_green,25,60),(trp_dutch_musketeer_recruit,4,7),(trp_dutch_standard_bearer,1,1),(trp_dutch_officer,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_8", "{!}dutch_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,50,70),(trp_musketeer_1,20,50),(trp_mercenary_swordsman,40,60),(trp_dutch_corporal,2,4),(trp_dutch_standard_bearer,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_9", "{!}dutch_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,40,70),(trp_mercenary_swordsman,20,50),(trp_dutch_musketeer_veteran,20,30),(trp_dutch_standard_bearer,1,1),(trp_dutch_corporal,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_10", "{!}dutch_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_dutch_nassau_recruit,20,60),(trp_dutch_nassau_green,40,80),(trp_dutch_standard_bearer,1,1),(trp_dutch_grenadier_green,20,30),(trp_dutch_officer,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_11", "{!}dutch_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_dutch_zweeds_recruit,40,60),(trp_dutch_zweeds_green,25,60),(trp_mercenary_swordsman,4,7),(trp_dutch_standard_bearer,1,1),(trp_dutch_officer,1,1),(trp_dutch_drummer,1,1)] ),
("dutch_infantry_party_12", "{!}dutch_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_dutch_nassau_recruit,50,70),(trp_dutch_nassau_green,20,50),(trp_mercenary_swordsman,40,60),(trp_dutch_corporal,2,4),(trp_dutch_standard_bearer,1,1),(trp_dutch_drummer,1,1)] ),

#Spanish Bourgons
("spanish_bourbon_infantry_party_1", "{!}spanish_bourbon_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_bourbon_diputacio_recruit,40,80),(trp_bourbon_diputacio_green,20,40),(trp_bourbon_diputacio_experienced,4,6),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_corporal,1,3),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_2", "{!}spanish_bourbon_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_bourbon_aragon_recruit,30,60),(trp_bourbon_aragon_green,40,70),(trp_bourbon_grenadier_recruit,4,7),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_officer,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_3", "{!}spanish_bourbon_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_bourbon_castile_recuit,40,60),(trp_bourbon_castile_green,40,60),(trp_bourbon_castile_experienced,4,7),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_corporal,1,3),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_4", "{!}spanish_bourbon_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_bourbon_asturias_recruit,60,70),(trp_bourbon_asturias_green,20,30),(trp_bourbon_asturias_experienced,25,65),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_corporal,1,8),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_5", "{!}spanish_bourbon_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_bourbon_colorados_recruit,40,70),(trp_bourbon_colorados_green,20,50),(trp_bourbon_colorados_exprienced,20,30),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_corporal,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_6", "{!}spanish_bourbon_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_bourbon_walloon_recruit,20,60),(trp_bourbon_walloon_green,40,80),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_walloon_experienced,20,30),(trp_bourbon_officer,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_7", "{!}spanish_bourbon_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_bourbon_castile_recuit,40,60),(trp_bourbon_grenadier_recruit,25,60),(trp_mercenary_swordsman,4,7),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_officer,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_8", "{!}spanish_bourbon_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_bourbon_asturias_recruit,50,70),(trp_watchman,20,50),(trp_bourbon_asturias_green,40,60),(trp_bourbon_corporal,2,4),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_9", "{!}spanish_bourbon_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_bourbon_grenadier_recruit,40,70),(trp_irish_recruit,20,50),(trp_pikeman_recruit,20,30),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_corporal,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_10", "{!}spanish_bourbon_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_bourbon_aragon_recruit,20,60),(trp_bourbon_aragon_green,40,80),(trp_bourbon_standard_bearer,1,1),(trp_mercenary_swordsman,20,30),(trp_bourbon_officer,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_11", "{!}spanish_bourbon_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_bourbon_diputacio_recruit,40,60),(trp_bourbon_diputacio_green,25,60),(trp_mercenary_swordsman,4,7),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_officer,1,1),(trp_bourbon_drummer,1,1)] ),
("spanish_bourbon_infantry_party_12", "{!}spanish_bourbon_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_bourbon_colorados_recruit,50,70),(trp_musketeer_1,20,50),(trp_bourbon_colorados_green,40,60),(trp_bourbon_corporal,2,4),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_drummer,1,1)] ),

#Danish
("danish_infantry_party_1", "{!}danish_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_danish_militia_recruit,40,80),(trp_danish_militia_green,20,40),(trp_danish_militia_experienced,4,6),(trp_danish_standard_bearer,1,1),(trp_danish_corporal,1,3),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_2", "{!}danish_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_danish_first_recruit,30,60),(trp_danish_first_green,40,70),(trp_danish_first_hardened,4,7),(trp_danish_standard_bearer,1,1),(trp_danish_officer,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_3", "{!}danish_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_danish_funen_recruit,40,60),(trp_danish_funen_veteran,40,60),(trp_danish_funen_experienced,4,7),(trp_danish_standard_bearer,1,1),(trp_danish_corporal,1,3),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_4", "{!}danish_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_danish_marine_recruit,60,70),(trp_danish_marine_green,20,30),(trp_danish_marine_veteran,25,65),(trp_danish_standard_bearer,1,1),(trp_danish_corporal,1,8),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_5", "{!}danish_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_danish_sjallandska_recruit,40,70),(trp_danish_sjallandska_green,20,50),(trp_danish_sjallandska_experienced,20,30),(trp_danish_standard_bearer,1,1),(trp_danish_corporal,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_6", "{!}danish_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_danish_prince_christian_recruit,20,60),(trp_danish_prince_christian_green,40,80),(trp_danish_standard_bearer,1,1),(trp_danish_grenadier_recruit,20,30),(trp_danish_officer,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_7", "{!}danish_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_danish_prince_charles_recruit,40,60),(trp_danish_prince_charles_experienced,25,60),(trp_danish_grenadier_recruit,4,7),(trp_danish_standard_bearer,1,1),(trp_danish_officer,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_8", "{!}danish_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_danish_life_guard_recruit,50,70),(trp_danish_life_guard_green,20,50),(trp_danish_grenadier_veteran,40,60),(trp_danish_corporal,2,4),(trp_danish_standard_bearer,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_9", "{!}danish_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_danish_grenadier_recruit,40,70),(trp_danish_funen_recruit,20,50),(trp_danish_funen_veteran,20,30),(trp_danish_standard_bearer,1,1),(trp_danish_corporal,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_10", "{!}danish_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_danish_militia_recruit,20,60),(trp_mercenary_swordsman,40,80),(trp_danish_standard_bearer,1,1),(trp_swiss_recruit,20,30),(trp_danish_officer,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_11", "{!}danish_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_danish_grenadier_recruit,40,60),(trp_danish_grenadier_veteran,25,60),(trp_mercenary_swordsman,4,7),(trp_danish_standard_bearer,1,1),(trp_danish_officer,1,1),(trp_danish_drummer,1,1)] ),
("danish_infantry_party_12", "{!}danish_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_danish_sjallandska_recruit,50,70),(trp_danish_sjallandska_green,20,50),(trp_danish_militia_recruit,40,60),(trp_danish_corporal,2,4),(trp_danish_standard_bearer,1,1),(trp_danish_drummer,1,1)] ),

#Swedish
("swedish_infantry_party_1", "{!}swedish_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_swedish_alvsborg_recruit,40,80),(trp_swedish_alvsborg_veteran,20,40),(trp_swedish_alvsborg_elite,4,6),(trp_swedish_standard_bearer,1,1),(trp_swedish_corporal,1,3),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_2", "{!}swedish_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_swedish_jonkoping_recruit,30,60),(trp_swedish_jonkoping_veteran,40,70),(trp_swedish_pikeman_recruit,4,7),(trp_swedish_standard_bearer,1,1),(trp_swedish_officer,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_3", "{!}swedish_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_swedish_dal_recruit,40,60),(trp_swedish_dal_veteran,40,60),(trp_swedish_pikeman_recruit,4,7),(trp_swedish_standard_bearer,1,1),(trp_swedish_corporal,1,3),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_4", "{!}swedish_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_swedish_narke_varmlands_recruit,60,70),(trp_swedish_narke_varmlands_veteran,20,30),(trp_swedish_grenadier_recruit,25,65),(trp_swedish_standard_bearer,1,1),(trp_swedish_corporal,1,8),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_5", "{!}swedish_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_swedish_sodermanlands_recruit,40,70),(trp_swedish_sodermanlands_veteran,20,50),(trp_swedish_pikeman_recruit,20,30),(trp_swedish_standard_bearer,1,1),(trp_swedish_corporal,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_6", "{!}swedish_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_swedish_uppland_recruit,20,60),(trp_swedish_uppland_veteran,40,80),(trp_swedish_standard_bearer,1,1),(trp_swedish_uppland_elite,20,30),(trp_swedish_officer,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_7", "{!}swedish_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_swedish_nv_tremannigar_recruit,40,60),(trp_swedish_grenadier_recruit,25,60),(trp_swedish_nv_tremannigar_experienced,4,7),(trp_swedish_standard_bearer,1,1),(trp_swedish_officer,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_8", "{!}swedish_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_swedish_mellins_estlandska_recruit,50,70),(trp_swedish_mellins_estlandska_veteran,20,50),(trp_swedish_pikeman_recruit,40,60),(trp_swedish_corporal,2,4),(trp_swedish_standard_bearer,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_9", "{!}swedish_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_swedish_narke_varmlands_recruit,40,70),(trp_swedish_narke_varmlands_veteran,20,50),(trp_swedish_pikeman_recruit,20,30),(trp_swedish_standard_bearer,1,1),(trp_swedish_corporal,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_10", "{!}swedish_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_swedish_uppland_recruit,20,60),(trp_swedish_uppland_veteran,40,80),(trp_swedish_standard_bearer,1,1),(trp_swedish_pikeman_recruit,20,30),(trp_swedish_officer,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_11", "{!}swedish_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_swedish_dal_recruit,40,60),(trp_swedish_grenadier_recruit,25,60),(trp_mercenary_swordsman,4,7),(trp_swedish_standard_bearer,1,1),(trp_swedish_officer,1,1),(trp_swedish_drummer,1,1)] ),
("swedish_infantry_party_12", "{!}swedish_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_swedish_sodermanlands_recruit,50,70),(trp_swedish_sodermanlands_veteran,20,50),(trp_swedish_grenadier_recruit,40,60),(trp_swedish_corporal,2,4),(trp_swedish_standard_bearer,1,1),(trp_swedish_drummer,1,1)] ),

#Prussian
("prussian_infantry_party_1", "{!}prussian_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,40,80),(trp_prussia_markgraf_green,20,40),(trp_prussia_markgraf_experienced,4,6),(trp_prussia_standard_bearer,1,1),(trp_prussia_corporal,1,3),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_2", "{!}prussian_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_dessau_recruit,30,60),(trp_prussia_anhalt_dessau_green,40,70),(trp_prussia_grenadier_garde_recruit,4,7),(trp_prussia_standard_bearer,1,1),(trp_prussia_officer,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_3", "{!}prussian_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_zerbst_recruit,40,60),(trp_prussia_anhalt_zerbst_veteran,40,60),(trp_prussia_grenadier_garde_recruit,4,7),(trp_prussia_standard_bearer,1,1),(trp_prussia_corporal,1,3),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_4", "{!}prussian_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_prussia_grenadier_garde_recruit,60,70),(trp_prussia_grenadier_garde_veteran,20,30),(trp_prussia_grenadier_garde_elite,25,65),(trp_prussia_standard_bearer,1,1),(trp_prussia_corporal,1,8),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_5", "{!}prussian_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_prussia_potsdam_giant_recruit,40,70),(trp_prussia_potsdam_giant_veteran,20,50),(trp_prussia_potsdam_giant_elite,20,30),(trp_prussia_standard_bearer,1,1),(trp_prussia_corporal,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_6", "{!}prussian_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_prussia_leibregiment_recruit,20,60),(trp_prussia_leibregiment_veteran,40,80),(trp_prussia_standard_bearer,1,1),(trp_prussia_grenadier_garde_recruit,20,30),(trp_prussia_officer,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_7", "{!}prussian_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_prussia_grenadier_garde_recruit,40,60),(trp_swiss_recruit,25,60),(trp_mercenary_swordsman,4,7),(trp_prussia_standard_bearer,1,1),(trp_prussia_officer,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_8", "{!}prussian_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,50,70),(trp_prussia_markgraf_green,20,50),(trp_mercenary_swordsman,40,60),(trp_prussia_corporal,2,4),(trp_prussia_standard_bearer,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_9", "{!}prussian_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_dessau_recruit,40,70),(trp_prussia_anhalt_dessau_green,20,50),(trp_mercenary_swordsman,20,30),(trp_prussia_standard_bearer,1,1),(trp_prussia_corporal,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_10", "{!}prussian_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_zerbst_recruit,20,60),(trp_prussia_anhalt_zerbst_veteran,40,80),(trp_prussia_standard_bearer,1,1),(trp_prussia_potsdam_giant_recruit,20,30),(trp_prussia_officer,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_11", "{!}prussian_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,40,60),(trp_prussia_markgraf_green,25,60),(trp_mercenary_swordsman,4,7),(trp_prussia_standard_bearer,1,1),(trp_prussia_officer,1,1),(trp_prussia_drummer,1,1)] ),
("prussian_infantry_party_12", "{!}prussian_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_zerbst_recruit,50,70),(trp_prussia_anhalt_zerbst_veteran,20,50),(trp_swiss_recruit,40,60),(trp_prussia_corporal,2,4),(trp_prussia_standard_bearer,1,1),(trp_prussia_drummer,1,1)] ),

#Habsburg Spanish
("spanish_habsburg_infantry_party_1", "{!}spanish_habsburg_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_habsburg_guerilla_recuit,40,80),(trp_mercenary_swordsman,20,40),(trp_habsburg_guerilla_experienced,4,6),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_corporal,1,3),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_2", "{!}spanish_habsburg_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_habsburg_muntaya_recruit,30,60),(trp_habsburg_muntaya_veteran,40,70),(trp_habsburg_muntaya_elite,4,7),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_officer,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_3", "{!}spanish_habsburg_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_habsburg_diputacio_recruit,40,60),(trp_habsburg_diputacio_veteran,40,60),(trp_habsburg_grenadier_recruit,4,7),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_corporal,1,3),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_4", "{!}spanish_habsburg_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_habsburg_barcelona_recruit,60,70),(trp_habsburg_barcelona_veteran,20,30),(trp_habsburg_guerilla_recuit,25,65),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_corporal,1,8),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_5", "{!}spanish_habsburg_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_habsburg_immaculado_recruit,40,70),(trp_habsburg_immaculado_veteran,20,50),(trp_habsburg_guerilla_recuit,20,30),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_corporal,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_6", "{!}spanish_habsburg_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_habsburg_eulalia_recruit,20,60),(trp_habsburg_eulalia_veteran,40,80),(trp_habsburg_guerilla_recuit,20,30),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_officer,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_7", "{!}spanish_habsburg_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_habsburg_nostra_senyora_recruit,40,60),(trp_habsburg_nostra_senyora_veteran,25,60),(trp_mercenary_swordsman,4,7),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_officer,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_8", "{!}spanish_habsburg_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_habsburg_san_narciso_recruit,50,70),(trp_habsburg_san_narciso_experienced,20,50),(trp_habsburg_grenadier_recruit,40,60),(trp_habsburg_corporal,2,4),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_9", "{!}spanish_habsburg_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_habsburg_nostra_del_roser_recruit,40,70),(trp_habsburg_nostra_del_roser_green,20,50),(trp_mercenary_swordsman,20,30),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_corporal,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_10", "{!}spanish_habsburg_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_habsburg_mallorca_recruit,20,60),(trp_habsburg_mallorca_green,40,80),(trp_habsburg_guerilla_recuit,20,30),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_officer,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_11", "{!}spanish_habsburg_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_habsburg_grenadier_recruit,40,60),(trp_habsburg_grenadier_experienced,25,60),(trp_habsburg_guerilla_recuit,4,7),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_officer,1,1),(trp_habsburg_drummer,1,1)] ),
("spanish_habsburg_infantry_party_12", "{!}spanish_habsburg_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_habsburg_guerilla_recuit,50,70),(trp_musketeer_1,20,50),(trp_mercenary_swordsman,40,60),(trp_habsburg_corporal,2,4),(trp_habsburg_standard_bearer,1,1),(trp_habsburg_drummer,1,1)] ),

#Polish
("polish_infantry_party_1", "{!}polish_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_polish_thielau_recruit,40,80),(trp_polish_thielau_veteran,20,40),(trp_polish_thielau_elite,4,6),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_sergeant,1,3),(trp_polish_saxon_drummer,1,1)] ),
("polish_infantry_party_2", "{!}polish_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_polish_musketeer_recruit,30,60),(trp_polish_musketeer_veteran,40,70),(trp_polish_musketeer_elite,4,7),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_officer,1,1),(trp_polish_drummer,1,1)] ),
("polish_infantry_party_3", "{!}polish_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_polish_fusilier_recruit,40,60),(trp_polish_fusilier_veteran,40,60),(trp_polish_grenadier_recruit,4,7),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_corporal,1,3),(trp_polish_drummer,1,1)] ),
("polish_infantry_party_4", "{!}polish_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_polish_grenadier_recruit,60,70),(trp_polish_grenadier_veteran,20,30),(trp_mercenary_swordsman,25,65),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_corporal,1,8),(trp_polish_drummer,1,1)] ),
("polish_infantry_party_5", "{!}polish_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_polish_steinau_recruit,40,70),(trp_polish_steinau_veteran,20,50),(trp_polish_grenadier_recruit,20,30),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_sergeant,1,1),(trp_polish_saxon_drummer,1,1)] ),
("polish_infantry_party_6", "{!}polish_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_polish_pistoris_recruit,20,60),(trp_polish_pistoris_veteran,40,80),(trp_mercenary_swordsman,20,30),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_officer,1,1),(trp_polish_saxon_drummer,1,1)] ),
("polish_infantry_party_7", "{!}polish_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_polish_kuprinz_recruit,40,60),(trp_polish_kuprinz_green,25,60),(trp_polish_sachische_garde_recruit,4,7),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_sergeant,1,1),(trp_polish_drummer,1,1)] ),
("polish_infantry_party_8", "{!}polish_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_polish_sachische_garde_recruit,50,70),(trp_polish_sachische_garde_veteran,20,50),(trp_polish_grenadier_recruit,40,60),(trp_polish_saxon_sergeant,2,4),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_drummer,1,1)] ),
("polish_infantry_party_9", "{!}polish_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_polish_polinishce_garde_recruit,40,70),(trp_polish_polinishce_garde_green,20,50),(trp_polish_grenadier_recruit,20,30),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_sergeant,1,1),(trp_polish_drummer,1,1)] ),
("polish_infantry_party_10", "{!}polish_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_polish_thielau_recruit,20,60),(trp_polish_thielau_veteran,40,80),(trp_mercenary_swordsman,20,30),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_officer,1,1),(trp_polish_saxon_drummer,1,1)] ),
("polish_infantry_party_11", "{!}polish_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_polish_musketeer_recruit,40,60),(trp_polish_musketeer_veteran,25,60),(trp_mercenary_swordsman,4,7),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_officer,1,1),(trp_polish_drummer,1,1)] ),
("polish_infantry_party_12", "{!}polish_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_polish_steinau_recruit,50,70),(trp_polish_sachische_garde_recruit,20,50),(trp_pikeman_recruit,40,60),(trp_polish_saxon_sergeant,2,4),(trp_polish_saxon_standard_bearer,1,1),(trp_polish_saxon_drummer,1,1)] ),

#Russian
("russian_infantry_party_1", "{!}russian_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_russia_strelets_recruit,40,80),(trp_russia_strelets_veteran,20,40),(trp_russia_strelets_elite,4,6),(trp_russia_standard_bearer,1,1),(trp_russia_corporal,1,3),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_2", "{!}russian_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_russia_st_petersburg_recruit,50,90),(trp_russia_st_petersburg_veteran,40,70),(trp_russia_artillery_recruit,4,7),(trp_russia_standard_bearer,1,1),(trp_russia_officer,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_3", "{!}russian_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_russia_cossacks_recruit,40,60),(trp_russia_cossacks_veteran,40,60),(trp_mercenary_swordsman,4,7),(trp_russia_standard_bearer,1,1),(trp_russia_corporal,1,3),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_4", "{!}russian_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_russia_butyrsky_recruit,60,70),(trp_russia_butyrsky_veteran,20,30),(trp_russia_butyrsky_elite,25,65),(trp_russia_standard_bearer,1,1),(trp_russia_corporal,1,8),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_5", "{!}russian_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_russia_narvsky_recruit,40,70),(trp_russia_narvsky_veteran,20,50),(trp_russia_preobrazhenksy_grenadier_recruit,20,30),(trp_russia_standard_bearer,1,1),(trp_russia_sergeant,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_6", "{!}russian_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_russia_semenovksy_recruit,20,60),(trp_russia_semenovksy_veteran,40,80),(trp_pikeman_recruit,20,30),(trp_russia_standard_bearer,1,1),(trp_russia_officer,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_7", "{!}russian_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_russia_kampenhausen_recruit,40,60),(trp_russia_kampenhausen_veteran,25,60),(trp_russia_strelets_recruit,4,7),(trp_russia_standard_bearer,1,1),(trp_russia_officer,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_8", "{!}russian_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_russia_nizhnynovgorodsky_recruit,50,70),(trp_russia_nizhnynovgorodsky_veteran,20,50),(trp_russia_nizhnynovgorodsky_green,40,60),(trp_russia_sergeant,2,4),(trp_russia_standard_bearer,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_9", "{!}russian_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_russia_preobrazhenksy_recruit,40,70),(trp_russia_preobrazhenksy_experienced,20,50),(trp_russia_preobrazhenksy_grenadier_recruit,20,30),(trp_russia_standard_bearer,1,1),(trp_russia_sergeant,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_10", "{!}russian_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_russia_narvsky_recruit,20,60),(trp_russia_narvsky_green,40,80),(trp_russia_cossacks_recruit,20,30),(trp_russia_standard_bearer,1,1),(trp_russia_officer,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_11", "{!}russian_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_russia_kampenhausen_recruit,40,60),(trp_russia_kampenhausen_veteran,25,60),(trp_russia_cossacks_recruit,4,7),(trp_russia_standard_bearer,1,1),(trp_russia_officer,1,1),(trp_russia_drummer,1,1)] ),
("russian_infantry_party_12", "{!}russian_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_russia_st_petersburg_recruit,50,70),(trp_russia_st_petersburg_veteran,20,50),(trp_russia_preobrazhenksy_grenadier_recruit,40,60),(trp_russia_sergeant,2,4),(trp_russia_standard_bearer,1,1),(trp_russia_drummer,1,1)] ),

#Ottoman
("ottoman_infantry_party_1", "{!}ottoman_infantry_party_1", 0, 0, fac_commoners, 0, [(trp_ottoman_bashi_bazouk_recruit,40,80),(trp_ottoman_bashi_bazouk_veteran,20,40),(trp_ottoman_solak_recruit,4,6),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_corporal,1,3),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_2", "{!}ottoman_infantry_party_2", 0, 0, fac_commoners, 0, [(trp_ottoman_palestinian_recruit,30,60),(trp_ottoman_palestinian_veteran,40,70),(trp_ottoman_artillery_recruit,4,7),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_officer,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_3", "{!}ottoman_infantry_party_3", 0, 0, fac_commoners, 0, [(trp_ottoman_albanian_levy_recruit,40,60),(trp_ottoman_albanian_levy_experienced,40,60),(trp_ottoman_bashi_bazouk_recruit,4,7),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_corporal,1,3),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_4", "{!}ottoman_infantry_party_4", 0, 0, fac_commoners, 0, [(trp_ottoman_solak_recruit,60,70),(trp_ottoman_solak_experienced,20,30),(trp_ottoman_bimbasha_recruit,25,65),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_corporal,1,8),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_5", "{!}ottoman_infantry_party_5", 0, 0, fac_commoners, 0, [(trp_ottoman_leventi_recruit,40,70),(trp_ottoman_leventi_experienced,20,50),(trp_ottoman_bashi_bazouk_recruit,20,30),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_sergeant,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_6", "{!}ottoman_infantry_party_6", 0, 0, fac_commoners, 0, [(trp_ottoman_bulgarian_recruit,20,60),(trp_ottoman_bulgarian_green,40,80),(trp_ottoman_solak_recruit,20,30),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_officer,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_7", "{!}ottoman_infantry_party_7", 0, 0, fac_commoners, 0, [(trp_ottoman_wallachian_recruit,40,60),(trp_ottoman_wallachian_green,25,60),(trp_ottoman_militia_1,4,7),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_officer,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_8", "{!}ottoman_infantry_party_8", 0, 0, fac_commoners, 0, [(trp_ottoman_azap_recruit,50,70),(trp_ottoman_azap_green,20,50),(trp_ottoman_militia_1,40,60),(trp_ottoman_sergeant,2,4),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_9", "{!}ottoman_infantry_party_9", 0, 0, fac_commoners, 0, [(trp_ottoman_janissary_recruit,40,70),(trp_ottoman_janissary_experienced,20,50),(trp_ottoman_janissary_hardened,20,30),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_sergeant,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_10", "{!}ottoman_infantry_party_10", 0, 0, fac_commoners, 0, [(trp_ottoman_bashi_bazouk_recruit,20,60),(trp_ottoman_solak_recruit,40,80),(trp_ottoman_militia_1,20,30),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_officer,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_11", "{!}ottoman_infantry_party_11", 0, 0, fac_commoners, 0, [(trp_ottoman_bulgarian_recruit,40,60),(trp_ottoman_wallachian_recruit,25,60),(trp_ottoman_janissary_recruit,4,7),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_officer,1,1),(trp_ottoman_drummer,1,1)] ),
("ottoman_infantry_party_12", "{!}ottoman_infantry_party_12", 0, 0, fac_commoners, 0, [(trp_ottoman_bashi_bazouk_recruit,50,70),(trp_ottoman_azap_recruit,20,50),(trp_ottoman_militia_1,40,60),(trp_ottoman_sergeant,2,4),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_drummer,1,1)] ),

#French Town
("french_town_party_1", "{!}french_town_party_1", 0, 0, fac_commoners, 0, [(trp_french_regiment_du_roi_recruit,40,80),(trp_french_de_la_marine_recruit,20,40),(trp_watchman,1,10),(trp_irish_recruit,1,10),(trp_swiss_recruit,1,30),(trp_pikeman_recruit,1,10)] ),
("french_town_party_2", "{!}french_town_party_2", 0, 0, fac_commoners, 0, [(trp_french_regiment_lorraine_recruit,50,90),(trp_french_regiment_la_reine_recruit,40,70),(trp_royal_italien_recruit,4,7),(trp_french_standard_bearer,1,5),(trp_jacobite_villager,1,5),(trp_french_drummer,1,1)] ),
("french_town_party_3", "{!}french_town_party_3", 0, 0, fac_commoners, 0, [(trp_regiment_surbeck_recruit,40,60),(trp_regiment_clare_recruit,40,60),(trp_mercenary_swordsman,4,7),(trp_french_grenadier_recruit,1,10),(trp_french_corporal,1,3),(trp_french_drummer,1,5)] ),
("french_town_party_4", "{!}french_town_party_4", 0, 0, fac_commoners, 0, [(trp_gardes_francaises_recruit,60,70),(trp_french_mousquetaires_de_la_garde_recruit,2,30),(trp_garde_suisses_recruit,25,65),(trp_hired_blade,1,10),(trp_french_corporal,1,8),(trp_french_royal_carabinier_recruit,1,10)] ),

#British Town
("british_town_party_1", "{!}british_town_party_1", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,40,80),(trp_watchman,20,40),(trp_danish_tavern,4,6),(trp_british_welch_fusiliers_recruit,1,10),(trp_hired_blade,1,30),(trp_british_drummer,1,3)] ),
("british_town_party_2", "{!}british_town_party_2", 0, 0, fac_commoners, 0, [(trp_british_churchill_regiment_recruit,50,90),(trp_british_webb_regiment_recruit,40,70),(trp_british_welch_fusiliers_recruit,4,7),(trp_british_grenadier_guard_recruit,1,20),(trp_british_officer,1,1),(trp_pikeman_recruit,1,10)] ),
("british_town_party_3", "{!}british_town_party_3", 0, 0, fac_commoners, 0, [(trp_british_howe_regiment_recruit,40,60),(trp_british_marlborough_regiment_recruit,40,60),(trp_british_grenadier_1st_foot_guard_recruit,4,7),(trp_british_standard_bearer,1,7),(trp_british_corporal,1,30),(trp_hired_blade,1,10)] ),
("british_town_party_4", "{!}british_town_party_4", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,60,70),(trp_british_duke_of_schomberg_regiment_recruit,20,30),(trp_mercenary_swordsman,25,65),(trp_british_grenadier_1st_foot_guard_recruit,1,10),(trp_militia_corporal,1,8),(trp_militia_drummer,1,2)] ),

#HRE Town
("hre_town_party_1", "{!}hre_town_party_1", 0, 0, fac_commoners, 0, [(trp_austrian_wuerttemburg_regiment_recruit,40,80),(trp_swiss_recruit,20,40),(trp_savoy_pikeline_recruit,4,16),(trp_watchman,5,50),(trp_austrian_corporal,1,5),(trp_austrian_drummer,1,5)] ),
("hre_town_party_2", "{!}hre_town_party_2", 0, 0, fac_commoners, 0, [(trp_austrian_wetzel_regiment_recruit,50,90),(trp_austrian_regiment_von_deutschmeister_recruit,40,70),(trp_austrian_grenadier_recruit,4,15),(trp_savoy_rehbinder_recruit,5,25),(trp_savoy_desportes_recruit,1,15),(trp_savoy_grenadier_recruit,1,15)] ),
("hre_town_party_3", "{!}hre_town_party_3", 0, 0, fac_commoners, 0, [(trp_hessen_prinz_wilhem_regiment_recruit,40,60),(trp_hessen_erbprinz_regiment_recruit,40,60),(trp_hessen_schopping_regiment_recruit,4,15),(trp_hessen_leibguard_recruit,5,15),(trp_savoy_sergeant,1,3),(trp_austrian_standard_bearer,1,5)] ),
("hre_town_party_4", "{!}hre_town_party_4", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,60,70),(trp_austrian_cuirassier_recruit,20,30),(trp_hessen_light_horse_recruit,25,65),(trp_savoy_standard_bearer,1,5),(trp_austrian_villager,1,8),(trp_savoy_drummer,1,5)] ),

#Bavarian Town
("bavarian_town_party_1", "{!}bavarian_town_party_1", 0, 0, fac_commoners, 0, [(trp_bavaria_leib_regiment_recruit,40,80),(trp_bavria_kurzprinz_recruit,20,40),(trp_swiss_recruit,4,6),(trp_mercenary_swordsman,1,10),(trp_musketeer_1,1,10),(trp_bavaria_drummer,1,1)] ),
("bavarian_town_party_2", "{!}bavarian_town_party_2", 0, 0, fac_commoners, 0, [(trp_bavaria_karthausen_recruit,50,90),(trp_bavaria_leib_regiment_recruit,40,70),(trp_watchman,4,7),(trp_bavaria_standard_bearer,1,2),(trp_bavaria_officer,1,1),(trp_bavaria_drummer,1,1)] ),
("bavarian_town_party_3", "{!}bavarian_town_party_3", 0, 0, fac_commoners, 0, [(trp_bavaria_maffey_recruit,40,60),(trp_bavaria_grenadier_recruit,40,60),(trp_mercenary_swordsman,4,7),(trp_bavaria_standard_bearer,1,3),(trp_bavaria_corporal,1,3),(trp_watchman,1,20)] ),
("bavarian_town_party_4", "{!}bavarian_town_party_4", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,60,70),(trp_bavaria_grenadier_guard_recruit,20,30),(trp_bavaria_prince_phillipe_recruit,25,65),(trp_mercenary_horseman,1,10),(trp_bavaria_corporal,1,8),(trp_swiss_recruit,1,10)] ),

#Dutch Town
("dutch_town_party_1", "{!}dutch_town_party_1", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,40,80),(trp_dutch_oranje_gelderland_recruit,20,40),(trp_watchman,4,60),(trp_dutch_zweeds_recruit,1,10),(trp_dutch_corporal,1,10),(trp_dutch_drummer,1,6)] ),
("dutch_town_party_2", "{!}dutch_town_party_2", 0, 0, fac_commoners, 0, [(trp_dutch_nassau_recruit,50,90),(trp_dutch_opstad_recruit,40,70),(trp_dutch_blue_guard_recruit,5,20),(trp_dutch_standard_bearer,1,5),(trp_dutch_officer,1,1),(trp_dutch_grenadier_recruit,1,10)] ),
("dutch_town_party_3", "{!}dutch_town_party_3", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,40,60),(trp_dutch_zweeds_recruit,40,60),(trp_mercenary_swordsman,4,70),(trp_watchman,1,15),(trp_dutch_nassau_recruit,1,30),(trp_dutch_drummer,1,1)] ),
("dutch_town_party_4", "{!}dutch_town_party_4", 0, 0, fac_commoners, 0, [(trp_dutch_oranje_gelderland_recruit,60,70),(trp_dutch_van_massou_recruit,20,30),(trp_dutch_cuirassier_recruit,25,65),(trp_dutch_nassau_recruit,1,10),(trp_dutch_corporal,1,8),(trp_dutch_grenadier_recruit,5,30)] ),

#Bourbon Spanish Town
("bourbon_town_party_1", "{!}bourbon_town_party_1", 0, 0, fac_commoners, 0, [(trp_bourbon_diputacio_recruit,40,80),(trp_bourbon_aragon_recruit,20,40),(trp_bourbon_castile_recuit,5,40),(trp_bourbon_standard_bearer,1,6),(trp_bourbon_corporal,1,8),(trp_bourbon_drummer,1,10)] ),
("bourbon_town_party_2", "{!}bourbon_town_party_2", 0, 0, fac_commoners, 0, [(trp_bourbon_asturias_recruit,50,90),(trp_bourbon_colorados_recruit,40,70),(trp_dutch_grenadier_recruit,4,7),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_officer,1,1),(trp_militia_drummer,1,1)] ),
("bourbon_town_party_3", "{!}bourbon_town_party_3", 0, 0, fac_commoners, 0, [(trp_bourbon_walloon_recruit,40,60),(trp_bourbon_grenadier_recruit,40,60),(trp_mercenary_swordsman,5,70),(trp_militia_corporal,1,10),(trp_watchman,1,3),(trp_mercenary_crossbowman,1,5)] ),
("bourbon_town_party_4", "{!}bourbon_town_party_4", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,60,70),(trp_bourbon_royal_guards_recruit,20,30),(trp_irish_recruit,25,65),(trp_musketeer_1,1,10),(trp_bourbon_corporal,1,8),(trp_pikeman_recruit,1,20)] ),

#Danish Town
("danish_town_party_1", "{!}danish_town_party_1", 0, 0, fac_commoners, 0, [(trp_danish_militia_recruit,40,80),(trp_danish_first_recruit,20,40),(trp_danish_grenadier_recruit,5,25),(trp_mercenary_swordsman,1,10),(trp_danish_corporal,1,10),(trp_danish_drummer,1,10)] ),
("danish_town_party_2", "{!}danish_town_party_2", 0, 0, fac_commoners, 0, [(trp_danish_funen_recruit,50,90),(trp_danish_marine_recruit,40,70),(trp_danish_prince_charles_recruit,5,25),(trp_danish_standard_bearer,1,10),(trp_danish_officer,1,3),(trp_militia_drummer,1,1)] ),
("danish_town_party_3", "{!}danish_town_party_3", 0, 0, fac_commoners, 0, [(trp_danish_sjallandska_recruit,40,60),(trp_danish_prince_christian_recruit,40,60),(trp_mercenary_swordsman,5,25),(trp_danish_life_guard_recruit,5,25),(trp_watchman,1,30),(trp_musketeer_1,1,10)] ),
("danish_town_party_4", "{!}danish_town_party_4", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,60,70),(trp_danish_ungerska_drongera_recruit,20,30),(trp_danish_livegardet_till_hast_recruit,25,65),(trp_danish_funen_recruit,1,10),(trp_watchman,1,8),(trp_pikeman_recruit,1,10)] ),

#Swedish Town
("swedish_town_party_1", "{!}swedish_town_party_1", 0, 0, fac_commoners, 0, [(trp_swedish_jonkoping_recruit,40,80),(trp_swedish_alvsborg_recruit,20,40),(trp_swedish_pikeman_recruit,4,60),(trp_swedish_standard_bearer,1,10),(trp_swedish_corporal,1,10),(trp_swedish_drummer,1,10)] ),
("swedish_town_party_2", "{!}swedish_town_party_2", 0, 0, fac_commoners, 0, [(trp_swedish_dal_recruit,50,90),(trp_swedish_narke_varmlands_recruit,40,70),(trp_swedish_sodermanlands_recruit,5,26),(trp_swedish_mellins_estlandska_recruit,1,1),(trp_swedish_officer,1,3),(trp_militia_drummer,1,1)] ),
("swedish_town_party_3", "{!}swedish_town_party_3", 0, 0, fac_commoners, 0, [(trp_swedish_uppland_recruit,40,60),(trp_swedish_nv_tremannigar_recruit,40,60),(trp_mercenary_swordsman,6,25),(trp_musketeer_1,1,10),(trp_watchman,1,30),(trp_swedish_drabant_garde_recruit,1,1)] ),
("swedish_town_party_4", "{!}swedish_town_party_4", 0, 0, fac_commoners, 0, [(trp_swedish_pommerska_recruit,60,70),(trp_swedish_nyland_recruit,20,30),(trp_swedish_grenadier_recruit,25,65),(trp_swedish_karelska_recruit,1,1),(trp_swedish_skanska_recruit,1,8),(trp_pikeman_sergeant,1,10)] ),

#Prussian Town
("prussian_town_party_1", "{!}prussian_town_party_1", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,40,80),(trp_prussia_anhalt_dessau_recruit,20,40),(trp_watchman,5,30),(trp_prussia_standard_bearer,1,8),(trp_prussia_corporal,1,8),(trp_prussia_drummer,1,6)] ),
("prussian_town_party_2", "{!}prussian_town_party_2", 0, 0, fac_commoners, 0, [(trp_prussia_anhalt_zerbst_recruit,50,90),(trp_prussia_grenadier_garde_recruit,40,70),(trp_prussia_anhalt_dessau_recruit,5,25),(trp_prussia_markgraf_recruit,1,10),(trp_prussia_officer,1,2),(trp_militia_drummer,1,1)] ),
("prussian_town_party_3", "{!}prussian_town_party_3", 0, 0, fac_commoners, 0, [(trp_prussia_potsdam_giant_recruit,40,60),(trp_prussia_leibregiment_recruit,40,60),(trp_mercenary_swordsman,5,20),(trp_watchman,1,10),(trp_militia_corporal,1,3),(trp_swiss_recruit,1,10)] ),
("prussian_town_party_4", "{!}prussian_town_party_4", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,60,70),(trp_prussia_wartensleben_recruit,20,30),(trp_prussia_leibregiment_cavalry_recruit,25,65),(trp_prussia_cuirassier_recruit,1,10),(trp_swiss_recruit,1,8),(trp_pikeman_recruit,1,10)] ),

#Habsburg Spanish Town
("habsburg_town_party_1", "{!}habsburg_town_party_1", 0, 0, fac_commoners, 0, [(trp_habsburg_guerilla_recuit,40,80),(trp_habsburg_muntaya_recruit,20,40),(trp_habsburg_diputacio_recruit,4,6),(trp_mercenary_swordsman,1,10),(trp_habsburg_corporal,1,8),(trp_habsburg_drummer,1,5)] ),
("habsburg_town_party_2", "{!}habsburg_town_party_2", 0, 0, fac_commoners, 0, [(trp_watchman,50,90),(trp_habsburg_barcelona_recruit,40,70),(trp_habsburg_immaculado_recruit,5,25),(trp_habsburg_standard_bearer,1,10),(trp_habsburg_officer,1,2),(trp_habsburg_eulalia_recruit,1,20)] ),
("habsburg_town_party_3", "{!}habsburg_town_party_3", 0, 0, fac_commoners, 0, [(trp_habsburg_nostra_senyora_recruit,40,60),(trp_habsburg_grenadier_recruit,40,60),(trp_habsburg_san_narciso_recruit,4,17),(trp_habsburg_nostra_del_roser_recruit,1,10),(trp_habsburg_mallorca_recruit,1,30),(trp_habsburg_guerilla_recuit,10,30)] ),
("habsburg_town_party_4", "{!}habsburg_town_party_4", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_recruit,60,70),(trp_habsburg_de_la_fe_dragoon_recruit,20,30),(trp_habsburg_san_miguel_recruit,25,65),(trp_habsburg_mallorca_recruit,1,10),(trp_watchman,1,38),(trp_habsburg_san_narciso_recruit,1,10)] ),

#Polish Town
("polish_town_party_1", "{!}polish_town_party_1", 0, 0, fac_commoners, 0, [(trp_polish_thielau_recruit,40,80),(trp_polish_grenadier_recruit,20,40),(trp_watchman,4,60),(trp_slave_driver,1,10),(trp_polish_corporal,1,6),(trp_polish_saxon_drummer,1,3)] ),
("polish_town_party_2", "{!}polish_town_party_2", 0, 0, fac_commoners, 0, [(trp_polish_musketeer_recruit,50,90),(trp_polish_pistoris_recruit,40,70),(trp_polish_kuprinz_recruit,4,7),(trp_polish_sachische_garde_recruit,1,10),(trp_pikeman_recruit,1,20),(trp_polish_cuirassier_recruit,1,10)] ),
("polish_town_party_3", "{!}polish_town_party_3", 0, 0, fac_commoners, 0, [(trp_polish_fusilier_recruit,40,60),(trp_polish_steinau_recruit,40,60),(trp_polish_polinishce_garde_recruit,10,20),(trp_polish_saxon_standard_bearer,1,10),(trp_slaver_chief,1,3),(trp_polish_drummer,1,3)] ),
("polish_town_party_4", "{!}polish_town_party_4", 0, 0, fac_commoners, 0, [(trp_polish_grenadier_recruit,60,70),(trp_polish_dragoon_recruit,20,30),(trp_polish_hussar_recruit,25,65),(trp_watchman,1,10),(trp_polish_saxon_sergeant,1,8),(trp_polish_goltz_dragoon_recruit,1,10)] ),

#Russian Town
("russian_town_party_1", "{!}russian_town_party_1", 0, 0, fac_commoners, 0, [(trp_russia_strelets_recruit,40,120),(trp_russia_st_petersburg_recruit,20,40),(trp_russia_cossacks_recruit,15,60),(trp_russia_standard_bearer,1,5),(trp_russia_corporal,1,8),(trp_russia_drummer,1,5)] ),
("russian_town_party_2", "{!}russian_town_party_2", 0, 0, fac_commoners, 0, [(trp_russia_narvsky_recruit,50,90),(trp_russia_butyrsky_recruit,40,70),(trp_russia_artillery_recruit,4,7),(trp_russia_nizhnynovgorodsky_recruit,1,1),(trp_russia_officer,1,10),(trp_pikeman_recruit,1,1)] ),
("russian_town_party_3", "{!}russian_town_party_3", 0, 0, fac_commoners, 0, [(trp_russia_semenovksy_recruit,40,60),(trp_russia_kampenhausen_recruit,40,60),(trp_watchman,1,70),(trp_slave_driver,5,25),(trp_russia_preobrazhenksy_grenadier_recruit,1,3),(trp_militia_drummer,1,1)] ),
("russian_town_party_4", "{!}russian_town_party_4", 0, 0, fac_commoners, 0, [(trp_russia_cossack_cavalry_recruit,60,70),(trp_russia_ingermanlandski_recruit,20,30),(trp_serbian_irregular,25,65),(trp_russia_preobrazhenksy_recruit,1,1),(trp_russia_moskovsky_recruit,1,8),(trp_russia_kroptov_recruit,1,1)] ),

#Ottoman Town
("ottoman_town_party_1", "{!}ottoman_town_party_1", 0, 0, fac_commoners, 0, [(trp_ottoman_bashi_bazouk_recruit,40,80),(trp_ottoman_palestinian_recruit,20,40),(trp_ottoman_leventi_recruit,4,6),(trp_ottoman_standard_bearer,1,1),(trp_ottoman_corporal,1,10),(trp_ottoman_drummer,1,5)] ),
("ottoman_town_party_2", "{!}ottoman_town_party_2", 0, 0, fac_commoners, 0, [(trp_ottoman_albanian_levy_recruit,50,90),(trp_ottoman_solak_recruit,40,70),(trp_ottoman_artillery_recruit,5,26),(trp_ottoman_bimbasha_recruit,1,30),(trp_ottoman_officer,1,5),(trp_ottoman_militia_4,1,15)] ),
("ottoman_town_party_3", "{!}ottoman_town_party_3", 0, 0, fac_commoners, 0, [(trp_ottoman_bulgarian_recruit,40,60),(trp_ottoman_janissary_recruit,40,60),(trp_ottoman_wallachian_recruit,5,30),(trp_ottoman_azap_recruit,1,20),(trp_ottoman_militia_1,1,30),(trp_ottoman_sipahi_recruit,1,1)] ),
("ottoman_town_party_4", "{!}ottoman_town_party_4", 0, 0, fac_commoners, 0, [(trp_ottoman_ackinci_recruit,60,70),(trp_ottoman_mameluke_recruit,20,30),(trp_ottoman_cebelu_recruit,25,65),(trp_ottoman_aleppo_recruit,1,10),(trp_ottoman_militia_1,10,80),(trp_serbian_irregular,1,10)] ),

#Castle Parties
#French Castle
("french_castle_party_1", "{!}french_castle_party_1", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,40,80),(trp_manhunter,20,40),(trp_mercenary_horseman,15,40),(trp_french_standard_bearer,1,10),(trp_french_corporal,1,10),(trp_french_drummer,1,10)] ),
("french_castle_party_2", "{!}french_castle_party_2", 0, 0, fac_commoners, 0, [(trp_french_royal_carabinier_recruit,50,90),(trp_mercenary_horseman,40,70),(trp_jacobite_villager_2,14,30),(trp_irish_recruit,1,10),(trp_french_officer,1,5),(trp_french_cavalry_officer,1,10)] ),
("french_castle_party_3", "{!}french_castle_party_3", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,40,60),(trp_mercenary_horseman,40,60),(trp_french_royal_carabinier_recruit,4,7),(trp_watchman,1,1),(trp_militia_cavalry_officer,1,10),(trp_militia_drummer,1,1)] ),
("french_castle_party_4", "{!}french_castle_party_4", 0, 0, fac_commoners, 0, [(trp_french_regiment_du_roi_recruit,60,70),(trp_french_regiment_lorraine_recruit,20,30),(trp_french_grenadier_recruit,25,65),(trp_watchman,5,30),(trp_irish_recruit,1,8),(trp_swiss_recruit,1,10)] ),

#British Castle
("british_castle_party_1", "{!}british_castle_party_1", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,40,80),(trp_russia_strelets_veteran,20,40),(trp_hired_blade,5,25),(trp_british_standard_bearer,1,10),(trp_british_corporal,1,8),(trp_british_drummer,1,10)] ),
("british_castle_party_2", "{!}british_castle_party_2", 0, 0, fac_commoners, 0, [(trp_british_duke_of_schomberg_regiment_recruit,50,90),(trp_constable_1,40,70),(trp_danish_tavern,5,10),(trp_watchman,1,40),(trp_british_officer,1,1),(trp_militia_drummer,1,10)] ),
("british_castle_party_3", "{!}british_castle_party_3", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,40,60),(trp_british_duke_of_schomberg_regiment_recruit,40,60),(trp_mercenary_swordsman,4,7),(trp_mercenary_horseman,5,25),(trp_militia_cavalry_officer,1,8),(trp_mercenary_cavalry,1,10)] ),
("british_castle_party_4", "{!}british_castle_party_4", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,60,70),(trp_british_welch_fusiliers_recruit,20,30),(trp_british_grenadier_1st_foot_guard_recruit,25,65),(trp_watchman,1,10),(trp_british_howe_regiment_recruit,1,28),(trp_british_dragoon_recruit,1,20)] ),

#HRE Castle
("hre_castle_party_1", "{!}hre_castle_party_1", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,40,80),(trp_hessen_light_horse_recruit,20,40),(trp_hessen_erbprinz_regiment_recruit,5,15),(trp_austrian_standard_bearer,1,2),(trp_austrian_corporal,1,3),(trp_austrian_drummer,1,1)] ),
("hre_castle_party_2", "{!}hre_castle_party_2", 0, 0, fac_commoners, 0, [(trp_austrian_cuirassier_recruit,50,90),(trp_russia_st_petersburg_veteran,40,70),(trp_wurttenberg_prince_cavalry_recruit,30,50),(trp_savoy_standard_bearer,1,3),(trp_austrian_cavalry_officer,1,1),(trp_savoy_drummer,1,1)] ),
("hre_castle_party_3", "{!}hre_castle_party_3", 0, 0, fac_commoners, 0, [(trp_savoy_dragoon_recruit,40,60),(trp_savoy_house_guard_recruit,40,60),(trp_mercenary_swordsman,5,25),(trp_austrian_wuerttemburg_regiment_recruit,1,10),(trp_savoy_cavalry_officer,1,3),(trp_savoy_officer,1,1)] ),
("hre_castle_party_4", "{!}hre_castle_party_4", 0, 0, fac_commoners, 0, [(trp_savoy_desportes_recruit,60,70),(trp_savoy_pikeline_recruit,20,30),(trp_watchman,25,65),(trp_musketeer_1,5,10),(trp_savoy_sergeant,1,8),(trp_austrian_officer,1,1)] ),

#Bavarian Castle
("bavarian_castle_party_1", "{!}bavarian_castle_party_1", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,40,80),(trp_bavaria_prince_phillipe_recruit,20,40),(trp_bavaria_karthausen_recruit,5,25),(trp_bavaria_standard_bearer,1,10),(trp_bavaria_corporal,1,8),(trp_bavaria_drummer,1,10)] ),
("bavarian_castle_party_2", "{!}bavarian_castle_party_2", 0, 0, fac_commoners, 0, [(trp_bavaria_grenadier_guard_recruit,50,90),(trp_bavaria_dragoon_recruit,40,70),(trp_bavaria_prince_phillipe_recruit,5,25),(trp_swiss_recruit,1,15),(trp_bavaria_officer,1,12),(trp_bavaria_maffey_recruit,1,10)] ),
("bavarian_castle_party_3", "{!}bavarian_castle_party_3", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,40,60),(trp_bavaria_grenadier_guard_recruit,40,60),(trp_mercenary_swordsman,5,25),(trp_pikeman_recruit,1,10),(trp_musketeer_1,1,30),(trp_bavaria_cavalry_officer,1,12)] ),
("bavarian_castle_party_4", "{!}bavarian_castle_party_4", 0, 0, fac_commoners, 0, [(trp_bavaria_maffey_recruit,60,70),(trp_bavaria_grenadier_recruit,20,30),(trp_bavaria_leib_regiment_recruit,25,65),(trp_watchman,1,40),(trp_musketeer_2,1,28),(trp_mercenary_horseman,5,30)] ),

#Dutch Castle
("dutch_castle_party_1", "{!}dutch_castle_party_1", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,40,80),(trp_dutch_cuirassier_recruit,20,40),(trp_pikeman_recruit,5,25),(trp_dutch_standard_bearer,1,10),(trp_dutch_corporal,1,8),(trp_dutch_drummer,1,10)] ),
("dutch_castle_party_2", "{!}dutch_castle_party_2", 0, 0, fac_commoners, 0, [(trp_dutch_cuirassier_recruit,50,90),(trp_dutch_van_massou_recruit,40,70),(trp_hired_blade,5,25),(trp_mercenary_horseman,1,20),(trp_dutch_officer,1,12),(trp_watchman,1,40)] ),
("dutch_castle_party_3", "{!}dutch_castle_party_3", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,40,60),(trp_dutch_cuirassier_recruit,40,60),(trp_mercenary_swordsman,5,26),(trp_dutch_staff_sergeant,1,10),(trp_militia_cavalry_officer,1,3),(trp_militia_drummer,1,5)] ),
("dutch_castle_party_4", "{!}dutch_castle_party_4", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,60,70),(trp_dutch_grenadier_recruit,20,30),(trp_dutch_zweeds_recruit,25,65),(trp_dutch_blue_guard_recruit,1,15),(trp_dutch_cavalry_officer,1,8),(trp_musketeer_1,1,10)] ),

#Bourbon Spanish Castle
("bourbon_castle_party_1", "{!}bourbon_castle_party_1", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,40,80),(trp_bourbon_royal_guards_recruit,20,40),(trp_mercenary_horseman,5,26),(trp_bourbon_standard_bearer,1,10),(trp_bourbon_corporal,1,3),(trp_bourbon_drummer,1,10)] ),
("bourbon_castle_party_2", "{!}bourbon_castle_party_2", 0, 0, fac_commoners, 0, [(trp_bourbon_royal_guards_recruit,50,90),(trp_bourbon_mosquetero_guardia_recruit,40,70),(trp_mercenary_horseman,5,27),(trp_musketeer_1,1,10),(trp_bourbon_officer,1,1),(trp_militia_drummer,1,5)] ),
("bourbon_castle_party_3", "{!}bourbon_castle_party_3", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,40,60),(trp_mercenary_horseman,40,60),(trp_mercenary_swordsman,5,25),(trp_caravan_guard,1,10),(trp_militia_cavalry_officer,1,3),(trp_swiss_recruit,1,15)] ),
("bourbon_castle_party_4", "{!}bourbon_castle_party_4", 0, 0, fac_commoners, 0, [(trp_bourbon_colorados_recruit,60,70),(trp_bourbon_castile_recuit,20,30),(trp_bourbon_diputacio_recruit,25,65),(trp_watchman,1,30),(trp_bourbon_cavalry_officer,1,8),(trp_irish_recruit,1,15)] ),

#Danish Castle
("danish_castle_party_1", "{!}danish_castle_party_1", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,40,80),(trp_danish_ungerska_drongera_recruit,20,40),(trp_mercenary_horseman,5,25),(trp_danish_standard_bearer,1,1),(trp_danish_corporal,1,5),(trp_danish_drummer,1,15)] ),
("danish_castle_party_2", "{!}danish_castle_party_2", 0, 0, fac_commoners, 0, [(trp_danish_ungerska_drongera_recruit,50,90),(trp_danish_life_dragoon_experienced,40,70),(trp_danish_militia_recruit,5,27),(trp_mercenary_horseman,5,26),(trp_danish_officer,1,2),(trp_militia_drummer,1,15)] ),
("danish_castle_party_3", "{!}danish_castle_party_3", 0, 0, fac_commoners, 0, [(trp_danish_ungerska_drongera_green,40,60),(trp_danish_livegardet_till_hast_recruit,40,60),(trp_mercenary_swordsman,4,7),(trp_watchman,1,25),(trp_danish_cavalry_officer,1,3),(trp_danish_tavern,1,20)] ),
("danish_castle_party_4", "{!}danish_castle_party_4", 0, 0, fac_commoners, 0, [(trp_danish_first_recruit,60,70),(trp_danish_sjallandska_recruit,20,30),(trp_danish_funen_recruit,25,65),(trp_danish_grenadier_recruit,1,25),(trp_pikeman_recruit,1,8),(trp_musketeer_1,1,10)] ),

#Swedish Castle
("swedish_castle_party_1", "{!}swedish_castle_party_1", 0, 0, fac_commoners, 0, [(trp_swedish_pommerska_recruit,40,80),(trp_swedish_pommerska_green,20,40),(trp_swedish_pikeman_recruit,5,25),(trp_swedish_standard_bearer,1,10),(trp_swedish_corporal,1,5),(trp_swedish_drummer,1,5)] ),
("swedish_castle_party_2", "{!}swedish_castle_party_2", 0, 0, fac_commoners, 0, [(trp_swedish_nyland_recruit,50,90),(trp_swedish_karelska_recruit,40,70),(trp_swedish_pommerska_recruit,4,7),(trp_swedish_dal_recruit,4,25),(trp_swedish_officer,1,2),(trp_militia_drummer,1,5)] ),
("swedish_castle_party_3", "{!}swedish_castle_party_3", 0, 0, fac_commoners, 0, [(trp_swedish_skanska_recruit,40,60),(trp_swedish_drabant_garde_recruit,40,60),(trp_mercenary_swordsman,4,7),(trp_swedish_pommerska_recruit,1,1),(trp_swedish_cavalry_officer,1,3),(trp_musketeer_1,1,10)] ),
("swedish_castle_party_4", "{!}swedish_castle_party_4", 0, 0, fac_commoners, 0, [(trp_swedish_narke_varmlands_recruit,60,70),(trp_swedish_nv_tremannigar_recruit,20,30),(trp_watchman,25,65),(trp_swedish_grenadier_recruit,1,20),(trp_mercenary_horseman,1,35),(trp_pikeman_recruit,1,30)] ),

#Prussian Castle
("prussian_castle_party_1", "{!}prussian_castle_party_1", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,40,80),(trp_prussia_wartensleben_recruit,20,40),(trp_prussia_cavalry_officer,1,10),(trp_prussia_standard_bearer,1,10),(trp_prussia_corporal,1,3),(trp_prussia_drummer,1,10)] ),
("prussian_castle_party_2", "{!}prussian_castle_party_2", 0, 0, fac_commoners, 0, [(trp_prussia_leibregiment_cavalry_recruit,50,90),(trp_prussia_cuirassier_recruit,40,70),(trp_mercenary_horseman,5,25),(trp_pikeman_recruit,1,10),(trp_prussia_officer,1,1),(trp_militia_drummer,1,1)] ),
("prussian_castle_party_3", "{!}prussian_castle_party_3", 0, 0, fac_commoners, 0, [(trp_prussia_cuirassier_recruit,40,60),(trp_prussia_wartensleben_recruit,40,60),(trp_mercenary_swordsman,5,25),(trp_watchman,5,25),(trp_mercenary_cavalry,1,15),(trp_slave_driver,1,10)] ),
("prussian_castle_party_4", "{!}prussian_castle_party_4", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,60,70),(trp_prussia_anhalt_zerbst_recruit,20,30),(trp_prussia_anhalt_dessau_recruit,25,65),(trp_musketeer_1,5,25),(trp_swiss_recruit,1,20),(trp_pikeman_recruit,1,10)] ),

#Habsburg Spanish Castle
("habsburg_castle_party_1", "{!}habsburg_castle_party_1", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_recruit,40,80),(trp_habsburg_de_la_fe_dragoon_recruit,20,40),(trp_habsburg_san_miguel_recruit,4,6),(trp_habsburg_standard_bearer,1,10),(trp_habsburg_corporal,1,8),(trp_habsburg_drummer,1,10)] ),
("habsburg_castle_party_2", "{!}habsburg_castle_party_2", 0, 0, fac_commoners, 0, [(trp_habsburg_de_la_fe_dragoon_recruit,50,90),(trp_habsburg_nebot_dragoon_recruit,40,70),(trp_watchman,5,25),(trp_mercenary_horseman,5,25),(trp_habsburg_officer,1,5),(trp_militia_drummer,1,1)] ),
("habsburg_castle_party_3", "{!}habsburg_castle_party_3", 0, 0, fac_commoners, 0, [(trp_habsburg_san_miguel_recruit,40,60),(trp_habsburg_de_la_fe_dragoon_recruit,40,60),(trp_mercenary_swordsman,4,7),(trp_caravan_guard,5,25),(trp_mercenary_horseman,1,30),(trp_irish_recruit,1,10)] ),
("habsburg_castle_party_4", "{!}habsburg_castle_party_4", 0, 0, fac_commoners, 0, [(trp_habsburg_guerilla_recuit,60,70),(trp_habsburg_muntaya_recruit,20,30),(trp_habsburg_grenadier_recruit,25,65),(trp_mercenary_horseman,1,10),(trp_habsburg_cavalry_officer,1,8),(trp_pikeman_recruit,1,1)] ),

#Polish Castle
("polish_castle_party_1", "{!}polish_castle_party_1", 0, 0, fac_commoners, 0, [(trp_polish_dragoon_recruit,40,80),(trp_polish_goltz_dragoon_recruit,20,40),(trp_polish_hussar_recruit,5,25),(trp_polish_saxon_standard_bearer,1,10),(trp_polish_corporal,1,5),(trp_polish_drummer,1,5)] ),
("polish_castle_party_2", "{!}polish_castle_party_2", 0, 0, fac_commoners, 0, [(trp_polish_guard_dragoon_recruit,50,90),(trp_polish_cuirassier_recruit,40,70),(trp_pikeman_recruit,4,20),(trp_mercenary_horseman,5,25),(trp_polish_saxon_cavalry_officer,1,1),(trp_polish_saxon_drummer,1,5)] ),
("polish_castle_party_3", "{!}polish_castle_party_3", 0, 0, fac_commoners, 0, [(trp_polish_arquebusier_cavalry_recruit,40,60),(trp_polish_hussar_recruit,40,60),(trp_polish_saxon_cuirassier_recruit,4,7),(trp_watchman,5,25),(trp_polish_cavalry_officer,1,3),(trp_militia_drummer,1,1)] ),
("polish_castle_party_4", "{!}polish_castle_party_4", 0, 0, fac_commoners, 0, [(trp_polish_grenadier_recruit,60,70),(trp_polish_musketeer_recruit,20,30),(trp_polish_pistoris_recruit,25,65),(trp_slave_driver,5,30),(trp_polish_saxon_sergeant,1,8),(trp_polish_thielau_recruit,1,10)] ),

#Russian Castle
("russian_castle_party_1", "{!}russian_castle_party_1", 0, 0, fac_commoners, 0, [(trp_russia_moskovsky_recruit,40,80),(trp_russia_ingermanlandski_recruit,20,40),(trp_russia_cossack_cavalry_recruit,5,25),(trp_russia_standard_bearer,1,5),(trp_russia_corporal,1,4),(trp_russia_drummer,1,5)] ),
("russian_castle_party_2", "{!}russian_castle_party_2", 0, 0, fac_commoners, 0, [(trp_russia_cossack_cavalry_experienced,50,90),(trp_russia_moskovsky_green,40,70),(trp_russia_artillery_recruit,5,25),(trp_militia_cavalry_officer,1,1),(trp_russia_officer,1,3),(trp_militia_drummer,1,5)] ),
("russian_castle_party_3", "{!}russian_castle_party_3", 0, 0, fac_commoners, 0, [(trp_russia_kroptov_recruit,40,60),(trp_russia_cossack_cavalry_veteran,40,60),(trp_mercenary_swordsman,5,25),(trp_mercenary_horseman,1,25),(trp_slave_driver,1,3),(trp_russia_cavalry_officer,1,1)] ),
("russian_castle_party_4", "{!}russian_castle_party_4", 0, 0, fac_commoners, 0, [(trp_russia_strelets_recruit,60,90),(trp_russia_st_petersburg_recruit,20,30),(trp_russia_semenovksy_recruit,25,65),(trp_russia_cossacks_recruit,1,20),(trp_russia_narvsky_recruit,1,18),(trp_watchman,1,25)] ),

#Ottoman Castle
("ottoman_castle_party_1", "{!}ottoman_castle_party_1", 0, 0, fac_commoners, 0, [(trp_ottoman_ackinci_recruit,40,80),(trp_ottoman_cebelu_recruit,20,40),(trp_ottoman_kapikulu_recruit,4,25),(trp_ottoman_standard_bearer,1,10),(trp_ottoman_corporal,1,8),(trp_ottoman_drummer,1,10)] ),
("ottoman_castle_party_2", "{!}ottoman_castle_party_2", 0, 0, fac_commoners, 0, [(trp_ottoman_ackinci_recruit,50,90),(trp_ottoman_aleppo_recruit,40,70),(trp_ottoman_militia_1,5,25),(trp_ottoman_militia_6,1,1),(trp_ottoman_officer,1,3),(trp_ottoman_azap_recruit,1,15)] ),
("ottoman_castle_party_3", "{!}ottoman_castle_party_3", 0, 0, fac_commoners, 0, [(trp_ottoman_mameluke_recruit,40,60),(trp_ottoman_sipahi_recruit,40,60),(trp_ottoman_bashi_bazouk_recruit,10,40),(trp_ottoman_bulgarian_recruit,1,1),(trp_ottoman_cavalry_officer,1,3),(trp_ottoman_wallachian_recruit,1,25)] ),
("ottoman_castle_party_4", "{!}ottoman_castle_party_4", 0, 0, fac_commoners, 0, [(trp_serbian_irregular,60,70),(trp_ottoman_janissary_recruit,20,30),(trp_ottoman_solak_recruit,25,65),(trp_ottoman_artillery_recruit,2,15),(trp_ottoman_militia_5,1,15),(trp_ottoman_bimbasha_recruit,1,14)] ),

#European Militias
("european_militia_1", "{!}european_militia_1", 0, 0, fac_commoners, 0, [(trp_watchman,2,10),(trp_caravan_guard,5,20),(trp_militia_corporal,4,6),(trp_mercenary_swordsman,1,1),(trp_mercenary_horseman,10,30),(trp_militia_drummer,1,1)] ),
("european_militia_2", "{!}european_militia_2", 0, 0, fac_commoners, 0, [(trp_caravan_guard,5,20),(trp_watchman,4,7),(trp_militia_corporal,4,15),(trp_mercenary_swordsman,1,5),(trp_mercenary_horseman,1,5),(trp_militia_drummer,1,1)] ),
("european_militia_3", "{!}european_militia_3", 0, 0, fac_commoners, 0, [(trp_caravan_guard,4,30),(trp_watchman,4,6),(trp_militia_corporal,4,7),(trp_militia_drummer,1,1),(trp_mercenary_swordsman,1,30),(trp_mercenary_horseman,1,10)] ),


#Ottoman Militias
("ottoman_militia_1", "{!}ottoman_militia_1", 0, 0, fac_commoners, 0, [(trp_ottoman_militia_1,2,10),(trp_ottoman_militia_2,5,20),(trp_ottoman_militia_3,4,6),(trp_ottoman_militia_4,1,1),(trp_ottoman_militia_6,10,30),(trp_ottoman_janissary_recruit,1,2)] ),
("ottoman_militia_2", "{!}ottoman_militia_2", 0, 0, fac_commoners, 0, [(trp_ottoman_militia_1,5,20),(trp_ottoman_militia_3,4,7),(trp_ottoman_militia_6,4,15),(trp_ottoman_militia_4,1,5),(trp_ottoman_militia_2,1,5),(trp_ottoman_janissary_recruit,1,10)] ),
("ottoman_militia_3", "{!}ottoman_militia_3", 0, 0, fac_commoners, 0, [(trp_ottoman_militia_2,4,30),(trp_ottoman_militia_1,4,6),(trp_ottoman_militia_3,4,7),(trp_ottoman_militia_6,1,1),(trp_ottoman_solak_recruit,1,30),(trp_ottoman_albanian_levy_recruit,1,10)] ),

#Town recruits
("french_town_recruits_1", "{!}french_town_recruits_1", 0, 0, fac_commoners, 0, [(trp_french_de_la_marine_recruit,1,5),(trp_french_regiment_lorraine_recruit,1,5),(trp_french_regiment_du_roi_recruit,1,10),(trp_french_regiment_la_reine_recruit,1,10),(trp_royal_italien_recruit,1,5), (trp_regiment_surbeck_recruit,1,5)] ),
("french_town_recruits_2", "{!}french_town_recruits_2", 0, 0, fac_commoners, 0, [(trp_french_standard_bearer,1,1),(trp_french_grenadier_recruit,1,10),(trp_garde_suisses_recruit,1,5),(trp_gardes_francaises_recruit,1,5),(trp_french_drummer,1,1), (trp_french_corporal,1,5)] ),
("french_town_recruits_3", "{!}french_town_recruits_3", 0, 0, fac_commoners, 0, [(trp_french_de_la_marine_recruit,1,5),(trp_french_regiment_lorraine_recruit,1,5),(trp_french_regiment_du_roi_recruit,1,10),(trp_french_regiment_la_reine_recruit,1,10),(trp_royal_italien_recruit,1,5), (trp_regiment_surbeck_recruit,1,5)] ),
("british_town_recruits_1", "{!}british_town_recruits_1", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,1,10),(trp_british_churchill_regiment_recruit,1,5),(trp_british_webb_regiment_recruit,1,10),(trp_british_welch_fusiliers_recruit,1,5),(trp_british_howe_regiment_recruit,1,5),(trp_british_marlborough_regiment_recruit,1,3)] ),
("british_town_recruits_2", "{!}british_town_recruits_2", 0, 0, fac_commoners, 0, [(trp_british_grenadier_1st_foot_guard_recruit,1,5),(trp_british_grenadier_guard_recruit,1,5),(trp_british_drummer,1,1),(trp_british_standard_bearer,1,1),(trp_british_corporal,1,5),(trp_danish_tavern,1,4)] ),
("british_town_recruits_3", "{!}british_town_recruits_3", 0, 0, fac_commoners, 0, [(trp_british_orkneys_regiment_recruit,1,10),(trp_british_churchill_regiment_recruit,1,5),(trp_british_webb_regiment_recruit,1,10),(trp_british_welch_fusiliers_recruit,1,5),(trp_british_howe_regiment_recruit,1,5),(trp_british_marlborough_regiment_recruit,1,3)] ),
("hre_town_recruits_1", "{!}hre_town_recruits", 0, 0, fac_commoners, 0, [(trp_austrian_wuerttemburg_regiment_recruit,1,5),(trp_austrian_wetzel_regiment_recruit,1,5),(trp_austrian_regiment_von_deutschmeister_recruit,1,5),(trp_austrian_grenadier_recruit,1,3),(trp_hessen_prinz_wilhem_regiment_recruit,1,3),(trp_hessen_erbprinz_regiment_recruit,1,3)] ),
("hre_town_recruits_2", "{!}hre_town_recruits", 0, 0, fac_commoners, 0, [(trp_hessen_schopping_regiment_recruit,1,3),(trp_hessen_leibguard_recruit,1,3),(trp_savoy_pikeline_recruit,1,10),(trp_savoy_rehbinder_recruit,1,10),(trp_savoy_desportes_recruit,1,5),(trp_savoy_grenadier_recruit,1,5)] ),
("hre_town_recruits_3", "{!}hre_town_recruits", 0, 0, fac_commoners, 0, [(trp_austrian_drummer,1,1),(trp_austrian_standard_bearer,1,1),(trp_savoy_standard_bearer,1,1),(trp_savoy_drummer,1,1),(trp_austrian_corporal,1,5),(trp_savoy_sergeant,1,3)] ),
("bavarian_town_recruits_1", "{!}bavarian_town_recruits", 0, 0, fac_commoners, 0, [(trp_bavaria_leib_regiment_recruit,1,10), (trp_bavaria_karthausen_recruit,1,5), (trp_bavaria_maffey_recruit,1,5)] ),
("bavarian_town_recruits_2", "{!}bavarian_town_recruits", 0, 0, fac_commoners, 0, [(trp_bavria_kurzprinz_recruit,1,5),(trp_bavaria_grenadier_recruit,1,5)] ),
("bavarian_town_recruits_3", "{!}bavarian_town_recruits", 0, 0, fac_commoners, 0, [(trp_bavaria_standard_bearer,1,1),(trp_bavaria_drummer,1,1),(trp_bavaria_corporal,1,5)] ),
("dutch_town_recruits_1", "{!}dutch_town_recruits", 0, 0, fac_commoners, 0, [(trp_dutch_musketeer_recruit,1,10),(trp_dutch_oranje_gelderland_recruit,1,5),(trp_dutch_zweeds_recruit,1,5)] ),
("dutch_town_recruits_2", "{!}dutch_town_recruits", 0, 0, fac_commoners, 0, [(trp_dutch_nassau_recruit,1,5),(trp_dutch_opstad_recruit,1,5),(trp_dutch_blue_guard_recruit,1,5)] ),
("dutch_town_recruits_3", "{!}dutch_town_recruits", 0, 0, fac_commoners, 0, [(trp_dutch_grenadier_recruit,1,5),(trp_dutch_standard_bearer,1,1),(trp_dutch_drummer,1,1),(trp_dutch_corporal,1,5)] ),
("bourbon_town_recruits_1", "{!}bourbon_town_recruits", 0, 0, fac_commoners, 0, [(trp_bourbon_diputacio_recruit,1,10),(trp_bourbon_aragon_recruit,1,5),(trp_bourbon_castile_recuit,1,5)] ),
("bourbon_town_recruits_2", "{!}bourbon_town_recruits", 0, 0, fac_commoners, 0, [(trp_bourbon_asturias_recruit,1,5),(trp_bourbon_colorados_recruit,1,5),(trp_bourbon_walloon_recruit,1,5),(trp_bourbon_corporal,1,5)] ),
("bourbon_town_recruits_3", "{!}bourbon_town_recruits", 0, 0, fac_commoners, 0, [(trp_bourbon_grenadier_recruit,1,5),(trp_bourbon_standard_bearer,1,1),(trp_bourbon_drummer,1,1)] ),
("danish_town_recruits_1", "{!}danish_town_recruits", 0, 0, fac_commoners, 0, [(trp_danish_militia_recruit,1,10),(trp_danish_first_recruit,1,5),(trp_danish_funen_recruit,1,5),(trp_danish_drummer,1,1)] ),
("danish_town_recruits_2", "{!}danish_town_recruits", 0, 0, fac_commoners, 0, [(trp_danish_marine_recruit,1,5),(trp_danish_sjallandska_recruit,1,5),(trp_danish_prince_christian_recruit,1,5),(trp_danish_standard_bearer,1,1)] ),
("danish_town_recruits_3", "{!}danish_town_recruits", 0, 0, fac_commoners, 0, [(trp_danish_prince_charles_recruit,1,5),(trp_danish_grenadier_recruit,1,5),(trp_danish_life_guard_recruit,1,5),(trp_danish_corporal,1,5)] ),
("swedish_town_recruits_1", "{!}swedish_town_recruits", 0, 0, fac_commoners, 0, [(trp_swedish_alvsborg_recruit,1,10),(trp_swedish_jonkoping_recruit,1,5),(trp_swedish_pikeman_recruit,1,15),(trp_swedish_mellins_estlandska_recruit,1,5)] ),
("swedish_town_recruits_2", "{!}swedish_town_recruits", 0, 0, fac_commoners, 0, [(trp_swedish_dal_recruit,1,5),(trp_swedish_narke_varmlands_recruit,1,5),(trp_swedish_sodermanlands_recruit,1,5),(trp_swedish_drummer,1,1),(trp_swedish_corporal,1,1)] ),
("swedish_town_recruits_3", "{!}swedish_town_recruits", 0, 0, fac_commoners, 0, [(trp_swedish_uppland_recruit,1,5),(trp_swedish_nv_tremannigar_recruit,1,5),(trp_swedish_grenadier_recruit,1,5),(trp_swedish_standard_bearer,1,1)] ),
("prussian_town_recruits_1", "{!}prussian_town_recruits", 0, 0, fac_commoners, 0, [(trp_prussia_markgraf_recruit,1,10),(trp_prussia_anhalt_dessau_recruit,1,5),(trp_prussia_anhalt_zerbst_recruit,1,5)] ),
("prussian_town_recruits_2", "{!}prussian_town_recruits", 0, 0, fac_commoners, 0, [(trp_prussia_grenadier_garde_recruit,1,5),(trp_prussia_potsdam_giant_recruit,1,5),(trp_prussia_leibregiment_recruit,1,5)] ),
("prussian_town_recruits_3", "{!}prussian_town_recruits", 0, 0, fac_commoners, 0, [(trp_prussia_drummer,1,1),(trp_prussia_standard_bearer,1,1),(trp_prussia_corporal,1,5)] ),
("habsburg_town_recruits_1", "{!}habsburg_town_recruits", 0, 0, fac_commoners, 0, [(trp_habsburg_guerilla_recuit,1,15),(trp_habsburg_muntaya_recruit,1,5),(trp_habsburg_diputacio_recruit,1,5),(trp_habsburg_nostra_del_roser_recruit,1,5),(trp_habsburg_standard_bearer,1,1)] ),
("habsburg_town_recruits_2", "{!}habsburg_town_recruits", 0, 0, fac_commoners, 0, [(trp_habsburg_barcelona_recruit,1,5),(trp_habsburg_immaculado_recruit,1,5),(trp_habsburg_eulalia_recruit,1,5),(trp_habsburg_mallorca_recruit,1,5)] ),
("habsburg_town_recruits_3", "{!}habsburg_town_recruits", 0, 0, fac_commoners, 0, [(trp_habsburg_nostra_senyora_recruit,1,5),(trp_habsburg_grenadier_recruit,1,5),(trp_habsburg_san_narciso_recruit,1,5),(trp_habsburg_drummer,1,1),(trp_habsburg_corporal,1,5)] ),
("polish_town_recruits_1", "{!}polish_town_recruits", 0, 0, fac_commoners, 0, [(trp_polish_thielau_recruit,1,10),(trp_polish_musketeer_recruit,1,10),(trp_polish_fusilier_recruit,1,5),(trp_polish_saxon_drummer,1,1),(trp_polish_saxon_sergeant,1,5)] ),
("polish_town_recruits_2", "{!}polish_town_recruits", 0, 0, fac_commoners, 0, [(trp_polish_grenadier_recruit,1,5),(trp_polish_steinau_recruit,1,5),(trp_polish_pistoris_recruit,1,5),(trp_polish_drummer,1,1),(trp_polish_corporal,1,5)] ),
("polish_town_recruits_3", "{!}polish_town_recruits", 0, 0, fac_commoners, 0, [(trp_polish_kuprinz_recruit,1,5),(trp_polish_polinishce_garde_recruit,1,5),(trp_polish_sachische_garde_recruit,1,5),(trp_polish_saxon_standard_bearer,1,1)] ),
("russian_town_recruits_1", "{!}russian_town_recruits", 0, 0, fac_commoners, 0, [(trp_russia_strelets_recruit,1,20),(trp_russia_st_petersburg_recruit,1,5),(trp_russia_cossacks_recruit,1,10),(trp_russia_preobrazhenksy_grenadier_recruit,1,5)] ),
("russian_town_recruits_2", "{!}russian_town_recruits", 0, 0, fac_commoners, 0, [(trp_russia_butyrsky_recruit,1,5),(trp_russia_narvsky_recruit,1,5),(trp_russia_semenovksy_recruit,1,5),(trp_russia_artillery_recruit,1,5),(trp_russia_standard_bearer,1,1)] ),
("russian_town_recruits_3", "{!}russian_town_recruits", 0, 0, fac_commoners, 0, [(trp_russia_kampenhausen_recruit,1,5),(trp_russia_nizhnynovgorodsky_recruit,1,5),(trp_russia_preobrazhenksy_recruit,1,5),(trp_russia_drummer,1,1),(trp_russia_corporal,1,5)] ),
("ottoman_town_recruits_1", "{!}ottoman_town_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_bashi_bazouk_recruit,1,20),(trp_ottoman_palestinian_recruit,1,10),(trp_ottoman_albanian_levy_recruit,1,5),(trp_ottoman_janissary_recruit,1,10)] ),
("ottoman_town_recruits_2", "{!}ottoman_town_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_solak_recruit,1,5),(trp_ottoman_leventi_recruit,1,5),(trp_ottoman_bulgarian_recruit,1,5),(trp_ottoman_artillery_recruit,1,5),(trp_ottoman_standard_bearer,1,1)] ),
("ottoman_town_recruits_3", "{!}ottoman_town_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_wallachian_recruit,1,5),(trp_ottoman_azap_recruit,1,5),(trp_ottoman_bimbasha_recruit,1,5),(trp_ottoman_drummer,1,2),(trp_ottoman_corporal,1,6)] ),

#Castle recruits
("french_castle_recruits_1", "{!}french_castle_recruits", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,1,3),(trp_french_royal_carabinier_recruit,1,2),(trp_french_cavalry_officer,0,1),(trp_mercenary_horseman,1,5)] ),
("french_castle_recruits_2", "{!}french_castle_recruits", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,1,2),(trp_french_royal_carabinier_recruit,1,3),(trp_french_cavalry_officer,0,1)] ),
("french_castle_recruits_3", "{!}french_castle_recruits", 0, 0, fac_commoners, 0, [(trp_french_mousquetaires_de_la_garde_recruit,1,4),(trp_french_royal_carabinier_recruit,1,4),(trp_french_cavalry_officer,0,1)] ),
("british_castle_recruits_1", "{!}british_castle_recruits", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,1,5),(trp_british_duke_of_schomberg_regiment_recruit,1,5),(trp_british_cavalry_officer,1,3),(trp_mercenary_horseman,1,5)] ),
("british_castle_recruits_2", "{!}british_castle_recruits", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,1,5),(trp_british_duke_of_schomberg_regiment_recruit,1,5),(trp_british_cavalry_officer,1,3)] ),
("british_castle_recruits_3", "{!}british_castle_recruits", 0, 0, fac_commoners, 0, [(trp_british_dragoon_recruit,1,5),(trp_british_duke_of_schomberg_regiment_recruit,1,5),(trp_british_cavalry_officer,1,3)] ),
("hre_castle_recruits_1", "{!}hre_castle_recruits", 0, 0, fac_commoners, 0, [(trp_austrian_hussar_recruit,1,10),(trp_austrian_cuirassier_recruit,1,5),(trp_wurttenberg_prince_cavalry_recruit,1,5)] ),
("hre_castle_recruits_2", "{!}hre_castle_recruits", 0, 0, fac_commoners, 0, [(trp_hessen_light_horse_recruit,1,5),(trp_savoy_dragoon_recruit,1,5),(trp_savoy_cavalry_officer,1,5),(trp_austrian_hussar_recruit,1,5)] ),
("hre_castle_recruits_3", "{!}hre_castle_recruits", 0, 0, fac_commoners, 0, [(trp_savoy_dragoon_recruit,1,5),(trp_savoy_house_guard_recruit,1,5),(trp_austrian_cavalry_officer,1,5)] ),
("bavarian_castle_recruits_1", "{!}bavarian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,1,10),(trp_bavaria_grenadier_guard_recruit,1,5),(trp_bavaria_prince_phillipe_recruit,1,5),(trp_bavaria_cavalry_officer,1,2)] ),
("bavarian_castle_recruits_2", "{!}bavarian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,1,10),(trp_bavaria_grenadier_guard_recruit,1,5),(trp_bavaria_prince_phillipe_recruit,1,5),(trp_bavaria_cavalry_officer,1,2)] ),
("bavarian_castle_recruits_3", "{!}bavarian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_bavaria_dragoon_recruit,1,10),(trp_bavaria_grenadier_guard_recruit,1,5),(trp_bavaria_prince_phillipe_recruit,1,5),(trp_bavaria_cavalry_officer,1,2)] ),
("dutch_castle_recruits_1", "{!}dutch_castle_recruits", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,1,10),(trp_dutch_cuirassier_recruit,1,10),(trp_dutch_cavalry_officer,1,5),(trp_mercenary_horseman,1,5)] ),
("dutch_castle_recruits_2", "{!}dutch_castle_recruits", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,1,10),(trp_dutch_cuirassier_recruit,1,10),(trp_dutch_cavalry_officer,1,5),(trp_mercenary_horseman,1,5)] ),
("dutch_castle_recruits_3", "{!}dutch_castle_recruits", 0, 0, fac_commoners, 0, [(trp_dutch_van_massou_recruit,1,10),(trp_dutch_cuirassier_recruit,1,10),(trp_dutch_cavalry_officer,1,5),(trp_mercenary_horseman,1,5)] ),
("bourbon_castle_recruits_1", "{!}bourbon_castle_recruits", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,1,10),(trp_bourbon_royal_guards_recruit,1,10),(trp_bourbon_cavalry_officer,1,3),(trp_mercenary_horseman,1,5)] ),
("bourbon_castle_recruits_2", "{!}bourbon_castle_recruits", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,1,10),(trp_bourbon_royal_guards_recruit,1,10),(trp_bourbon_cavalry_officer,1,3),(trp_mercenary_horseman,1,5)] ),
("bourbon_castle_recruits_3", "{!}bourbon_castle_recruits", 0, 0, fac_commoners, 0, [(trp_bourbon_mosquetero_guardia_recruit,1,10),(trp_bourbon_royal_guards_recruit,1,10),(trp_bourbon_cavalry_officer,1,3),(trp_mercenary_horseman,1,5)] ),
("danish_castle_recruits_1", "{!}danish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,1,10),(trp_danish_ungerska_drongera_recruit,1,5),(trp_danish_livegardet_till_hast_recruit,1,5)] ),
("danish_castle_recruits_2", "{!}danish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_danish_cavalry_officer,1,5),(trp_mercenary_horseman,1,5)] ),
("danish_castle_recruits_3", "{!}danish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_danish_life_dragoon_recruit,1,10),(trp_danish_ungerska_drongera_recruit,1,5),(trp_danish_livegardet_till_hast_recruit,1,5)] ),
("swedish_castle_recruits_1", "{!}swedish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_swedish_pommerska_recruit,1,10),(trp_swedish_skanska_recruit,1,5)] ),
("swedish_castle_recruits_2", "{!}swedish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_swedish_nyland_recruit,1,5),(trp_swedish_drabant_garde_recruit,1,5)] ),
("swedish_castle_recruits_3", "{!}swedish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_swedish_karelska_recruit,1,5),(trp_swedish_cavalry_officer,1,5)] ),
("prussian_castle_recruits_1", "{!}prussian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,1,10),(trp_prussia_wartensleben_recruit,1,5),(trp_prussia_leibregiment_cavalry_recruit,1,5)] ),
("prussian_castle_recruits_2", "{!}prussian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_prussia_cuirassier_recruit,1,5),(trp_prussia_cavalry_officer,1,3),(trp_mercenary_horseman,1,5)] ),
("prussian_castle_recruits_3", "{!}prussian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_prussia_portail_cavalry_recruit,1,10),(trp_prussia_wartensleben_recruit,1,5),(trp_prussia_leibregiment_cavalry_recruit,1,5)] ),
("habsburg_castle_recruits_1", "{!}habsburg_castle_recruits", 0, 0, fac_commoners, 0, [(trp_habsburg_nebot_dragoon_recruit,1,10),(trp_habsburg_de_la_fe_dragoon_recruit,1,10),(trp_habsburg_san_miguel_recruit,1,5)] ),
("habsburg_castle_recruits_2", "{!}habsburg_castle_recruits", 0, 0, fac_commoners, 0, [(trp_habsburg_cavalry_officer,1,2),(trp_habsburg_nebot_dragoon_recruit,1,10),(trp_habsburg_de_la_fe_dragoon_recruit,1,10),(trp_habsburg_san_miguel_recruit,1,5)] ),
("habsburg_castle_recruits_3", "{!}habsburg_castle_recruits", 0, 0, fac_commoners, 0, [(trp_habsburg_cavalry_officer,1,2),(trp_habsburg_nebot_dragoon_recruit,1,10),(trp_habsburg_de_la_fe_dragoon_recruit,1,10),(trp_habsburg_san_miguel_recruit,1,5)] ),
("polish_castle_recruits_1", "{!}polish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_polish_dragoon_recruit,1,5),(trp_polish_goltz_dragoon_recruit,1,10),(trp_polish_cavalry_officer,1,2)] ),
("polish_castle_recruits_2", "{!}polish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_polish_guard_dragoon_recruit,1,5),(trp_polish_arquebusier_cavalry_recruit,1,5),(trp_polish_cuirassier_recruit,1,5)] ),
("polish_castle_recruits_3", "{!}polish_castle_recruits", 0, 0, fac_commoners, 0, [(trp_polish_hussar_recruit,1,5),(trp_polish_saxon_cuirassier_recruit,1,5),(trp_polish_saxon_cavalry_officer,1,2)] ),
("russian_castle_recruits_1", "{!}russian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_russia_moskovsky_recruit,1,10),(trp_russia_ingermanlandski_recruit,1,5),(trp_russia_cossack_cavalry_recruit,1,15)] ),
("russian_castle_recruits_2", "{!}russian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_russia_kroptov_recruit,1,5),(trp_russia_cavalry_officer,1,5)] ),
("russian_castle_recruits_3", "{!}russian_castle_recruits", 0, 0, fac_commoners, 0, [(trp_russia_moskovsky_recruit,1,10),(trp_russia_ingermanlandski_recruit,1,5),(trp_russia_cossack_cavalry_recruit,1,15)] ),
("ottoman_castle_recruits_1", "{!}ottoman_castle_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_ackinci_recruit,1,5),(trp_ottoman_mameluke_recruit,1,5),(trp_ottoman_cebelu_recruit,1,5)] ),
("ottoman_castle_recruits_2", "{!}ottoman_castle_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_aleppo_recruit,1,5),(trp_ottoman_sipahi_recruit,1,5),(trp_ottoman_kapikulu_recruit,1,5)] ),
("ottoman_castle_recruits_3", "{!}ottoman_castle_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_ackinci_recruit,1,5),(trp_ottoman_mameluke_recruit,1,5),(trp_ottoman_cebelu_recruit,1,5),(trp_ottoman_cavalry_officer,1,2)] ),

#Village recruits
("european_village_recruits_1", "{!}european_village_recruits", 0, 0, fac_commoners, 0, [(trp_watchman,1,6),(trp_mercenary_swordsman,1,5),(trp_mercenary_crossbowman,1,2)] ),
("european_village_recruits_2", "{!}european_village_recruits", 0, 0, fac_commoners, 0, [(trp_watchman,1,10),] ),
("ottoman_village_recruits_1", "{!}ottoman_village_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_militia_1,1,6),(trp_ottoman_militia_2,1,4)] ),
("ottoman_village_recruits_2", "{!}ottoman_village_recruits", 0, 0, fac_commoners, 0, [(trp_ottoman_militia_1,1,6)] ),

("forest_bandit_lair" ,"Highwaymen's Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
("taiga_bandit_lair","Rebel Uskoci Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
("steppe_bandit_lair" ,"Illegal Trade Smugglers' Area",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
("sea_raider_lair","Monarchist Agitator Gathering Spot",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
("mountain_bandit_lair", "Jacobite Rebel Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mountain_bandit,15,58),(trp_scottish_rebel_leader,1,3)] ),
("desert_bandit_lair" ,"Slavic Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
("regiment","regiment", 0, 0,fac_commoners,merchant_personality,[]),
]
