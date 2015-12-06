from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "folies_of_spain.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),

  ("ambushed_by_neutral", "ambushed_neutral_cavalry_march.wav", mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("ambushed_by_khergit", "ambushed_by_hre_panini.wav", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_nord",    "ambushed_nord_french_guard.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_rhodok",  "dutch_battle_march.wav", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_module_track|mtf_culture_all),
  ("ambushed_by_swadian", "ambushed_by_swadian.ogg", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_vaegir",  "fight_as_british_grenadiers.ogg", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_sarranid", "ambushed_spain_elbolero.wav", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  
  ("arena_1", "arena_1.ogg", mtf_sit_arena, 0),
#  ("arena_2", "arena_2.ogg", mtf_looping|mtf_sit_arena, 0),
  ("armorer", "armorer_bustijn.wav", mtf_sit_travel|mtf_module_track, 0),
  ("bandit_fight", "fight_seyffertitz_march.wav", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

  ("calm_night_1", "calm_night_pacabel.ogg", mtf_sit_night|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "defeat_by_neutral_froberger.ogg",mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("defeated_by_neutral_3", "defeat_bodeckker.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape_fairy_queen.ogg", mtf_persist_until_finished|mtf_module_track, 0),

  ("fight_1", "fight_1_imperiale.wav", mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, 0),
  ("fight_2", "combat_hre_fight.wav", mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, 0),
  ("fight_3", "fight_over_the_hills_and_far_away.ogg", mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, 0),
  ("fight_as_khergit", "hre_battle_eroica_sinfonia.wav", mtf_culture_3|mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("fight_4", "fight_4_russian_osp.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),  
  ("fight_as_nord", "fight_as_nord.ogg", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_rhodok", "fight_dutch.ogg", mtf_culture_5|mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_swadian", "french_battle_les_dragons_de_noailles.ogg", mtf_culture_1|mtf_sit_fight|mtf_module_track, mtf_culture_all),
  ("fight_as_vaegir", "fight_as_british_lilliburlero_march.ogg", mtf_culture_2|mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, mtf_culture_all),
  ("fight_while_mounted_1", "fight_seyffertitz_march.wav", mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, 0),
  ("fight_while_mounted_2", "fight_mounted_2_boismortier.wav", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_while_mounted_3", "fight_2_dutch.wav", mtf_sit_fight|mtf_module_track|mtf_sit_ambushed, 0),
  
  ("infiltration_khergit", "infiltration_hre.wav", mtf_culture_3|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_all),

  ("killed_by_khergit", "killed_by_khergit_lully_versailles.ogg", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed|mtf_module_track, 0),
  ("killed_by_neutral", "killed_by_neutral_tin_whistles.ogg", mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed|mtf_module_track, 0),
  ("killed_by_nord", "killed_by_nord_dutch_inspection.ogg", mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed|mtf_module_track, 0),
  ("killed_by_rhodok", "french_defeat_la_pompe_funebre.ogg", mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed, mtf_module_track,0),
  ("killed_by_swadian", "killed_by_swadian.ogg", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
  ("killed_by_vaegir", "defeat_by_british_funeral_march.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed|mtf_module_track, 0),
  
  ("lords_hall_khergit", "lords_hall_hre_bach_suite_3.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("lords_hall_nord", "lords_hall_nord_lully_deum.ogg", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_swadian", "french_town_marche_triumph.wav", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_rhodok", "lords_hall_dutch.ogg", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_vaegir", "lords_hall_british_purcell.wav", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("mounted_snow_terrain_calm", "mounted_snow_terrain_calm.ogg", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),
  ("outdoor_beautiful_land", "outdoor_beautiful_land.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("seige_neutral", "seige_neutal_marche_combattants.ogg", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("enter_the_juggernaut", "enter_the_juggernaut.ogg", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("siege_attempt", "seige_marche_royale.ogg", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("crazy_battle_music", "crazy_battle_music.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  
  ("tavern_1", "tavern_marc_antoine.wav", mtf_sit_tavern|mtf_sit_feast|mtf_module_track, 0),
  ("tavern_2", "tavern_2_gentleman_soldier.ogg", mtf_sit_tavern|mtf_sit_feast|mtf_module_track, 0),

  ("town_neutral", "travel_neutral_clares_dragoons.wav", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
  ("town_khergit", "town_hre_landsknecht_kommen.wav", mtf_culture_3|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_nord", "town_nord_pavel.wav", mtf_culture_4|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_rhodok", "town_dutch.wav", mtf_culture_5|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian", "french_tavern_piemontaise.wav", mtf_culture_1|mtf_sit_town|mtf_module_track|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir", "town_british_purcell.wav", mtf_culture_2|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_khergit", "travel_hre_fasch.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_neutral", "travel_neutral_turenne_regiment.ogg", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_nord",    "travel_bavarian_unico.ogg",    mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok",  "travel_dutch_fesch.ogg",  mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_swadian", "french_airs_de_trompettes.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_vaegir",  "travel_as_british_pipers_maggot.ogg",  mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_sarranid",  "travel_spain_unico.wav",  mtf_culture_6|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("uncertain_homestead", "uncertain_homstead_british_handel.ogg", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("hearth_and_brotherhood", "hearth_and_brotherhood.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("tragic_village", "tragic_village.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  ("victorious_neutral_1", "victorious_neutral_handel.ogg", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("victorious_neutral_2", "victorious_neutral_pogues.ogg", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("victorious_neutral_3", "fight_1_imperiale.wav", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track	, 0),

  ("victorious_swadian", "french_victory_ballet_de_la_nuit.wav", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious|mtf_module_track, 0),
  ("victorious_vaegir", "victorious_vaegir_lully_trompettes.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious|mtf_module_track, 0),
  ("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("wedding", "wedding_greensleeves.ogg", mtf_persist_until_finished|mtf_module_track, 0),

  ("coronation", "french_tavern_marche_pour_le_combat_de_la_barriere.ogg", mtf_persist_until_finished|mtf_module_track, 0),

  

  
]
