#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_behaviors.pick_two_parts_v3_sm import PicktwopartsV3SM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Jun 02 2020
@author: Bas Jochems
'''
class PartchoiceSM(Behavior):
	'''
	part 1 en 2 worden bepaald en geconfigureerd
	'''


	def __init__(self):
		super(PartchoiceSM, self).__init__()
		self.name = 'Part choice'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(PicktwopartsV3SM, 'Pick two parts V3')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1797 y:531, x:804 y:795
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type1', 'part_type2'], output_keys=['offset1', 'offset2'])
		_state_machine.userdata.part_type1 = ''
		_state_machine.userdata.part_type2 = ''
		_state_machine.userdata.offset1 = ''
		_state_machine.userdata.offset2 = ''
		_state_machine.userdata.camera_topic1 = ''
		_state_machine.userdata.camera_topic2 = ''
		_state_machine.userdata.camera_frame1 = ''
		_state_machine.userdata.camera_frame2 = ''
		_state_machine.userdata.config_name_Gantry_pick1 = ''
		_state_machine.userdata.config_name_Gantry_pick2 = ''
		_state_machine.userdata.config_name_PrePick1 = 'Links_PreGrasp_Bins'
		_state_machine.userdata.config_name_PrePick2 = 'Rechts_PreGrasp_Bins'
		_state_machine.userdata.offset_GR = 0.027
		_state_machine.userdata.offset_PL = 0.084
		_state_machine.userdata.offset_PR = 0.02
		_state_machine.userdata.offset_GK = 0.034
		_state_machine.userdata.PLR = 'pulley_part_red'
		_state_machine.userdata.PLB = 'pulley_part_blue'
		_state_machine.userdata.GRR = 'gear_part_red'
		_state_machine.userdata.GRB = 'gear_part_blue'
		_state_machine.userdata.PRR = 'piston_rod_part_red'
		_state_machine.userdata.PRB = 'piston_rod_part_blue'
		_state_machine.userdata.GKR = 'gasket_part_red'
		_state_machine.userdata.GKB = 'gasket_part_blue'
		_state_machine.userdata.topic0 = '/ariac/logical_camera_bins0'
		_state_machine.userdata.topic1 = '/ariac/logical_camera_bins1'
		_state_machine.userdata.topic2 = '/ariac/logical_camera_shelve1'
		_state_machine.userdata.topic3 = '/ariac/logical_camera_shelve2'
		_state_machine.userdata.frame0 = 'logical_camera_bins0_frame'
		_state_machine.userdata.frame1 = 'logical_camera_bins1_frame'
		_state_machine.userdata.frame2 = 'logical_camera_shelve1_frame'
		_state_machine.userdata.frame3 = 'logical_camera_shelve2_frame'
		_state_machine.userdata.LgearR = 'Gantry_R-nx_L-gearR'
		_state_machine.userdata.LpulleyR = 'Gantry_R-nx_L-pulleyR'
		_state_machine.userdata.LpistonR_RgasketB = 'Gantry_R-gasketB_L-pistonR'
		_state_machine.userdata.LgasketB_RpistonR = 'Gantry_R-pistonR_L-gasketB'
		_state_machine.userdata.LgasketR_RgearB = 'Gantry_R-gearB_L-gasketR'
		_state_machine.userdata.LgearB_RgasketR = 'Gantry_R-gasketR_L-gearB'
		_state_machine.userdata.RgearR = 'Gantry_R-gearR_L-nx'
		_state_machine.userdata.RpulleyR = 'Gantry_R-pulleyR_L-nx'
		_state_machine.userdata.config_name_L = 'Links_PreGrasp_Bins'
		_state_machine.userdata.config_name_R = 'Rechts_PreGrasp_Bins'
		_state_machine.userdata.config_name_R = 'Rechts_PreGrasp_Bins'
		_state_machine.userdata.PrePickstelling_L = 'Links_PreDrop_Stelling'
		_state_machine.userdata.PrePickstelling_R = 'Rechts_PreDrop_Stelling'
		_state_machine.userdata.empty = 'empty'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:0 y:63
			OperatableStateMachine.add('pulley_R',
										EqualState(),
										transitions={'true': 'gantrypos_1', 'false': 'gear_R'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'PLR'})

			# x:0 y:200
			OperatableStateMachine.add('gear_R',
										EqualState(),
										transitions={'true': 'gantrypos_3', 'false': 'gear_B'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'GRR'})

			# x:0 y:319
			OperatableStateMachine.add('gear_B',
										EqualState(),
										transitions={'true': 'gantrypos_4', 'false': 'gasket_R'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'GRB'})

			# x:0 y:454
			OperatableStateMachine.add('gasket_R',
										EqualState(),
										transitions={'true': 'gantrypos_5', 'false': 'gasket_B'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'GKR'})

			# x:0 y:593
			OperatableStateMachine.add('gasket_B',
										EqualState(),
										transitions={'true': 'gantrypos_6', 'false': 'piston_R'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'GKB'})

			# x:0 y:721
			OperatableStateMachine.add('piston_R',
										EqualState(),
										transitions={'true': 'gantrypos_7', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'PRR'})

			# x:454 y:68
			OperatableStateMachine.add('offset_pulley',
										ReplaceState(),
										transitions={'done': 'pulley_R_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_PL', 'result': 'offset1'})

			# x:449 y:206
			OperatableStateMachine.add('offset_gear',
										ReplaceState(),
										transitions={'done': 'pulley_R_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_GR', 'result': 'offset1'})

			# x:452 y:461
			OperatableStateMachine.add('offset_gasket',
										ReplaceState(),
										transitions={'done': 'pulley_R_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_GK', 'result': 'offset1'})

			# x:449 y:722
			OperatableStateMachine.add('offset_piston',
										ReplaceState(),
										transitions={'done': 'pulley_R_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_PR', 'result': 'offset1'})

			# x:1678 y:369
			OperatableStateMachine.add('Pick two parts V3',
										self.use_behavior(PicktwopartsV3SM, 'Pick two parts V3'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type1': 'part_type1', 'part_type2': 'part_type2', 'offset1': 'offset1', 'offset2': 'offset2', 'camera_topic1': 'camera_topic1', 'camera_topic2': 'camera_topic2', 'camera_frame1': 'camera_frame1', 'camera_frame2': 'camera_frame2', 'config_name_Gantry_pick1': 'config_name_Gantry_pick1', 'config_name_Gantry_pick2': 'config_name_Gantry_pick2', 'config_name_PrePick1': 'config_name_PrePick1', 'config_name_PrePick2': 'config_name_PrePick2'})

			# x:118 y:0
			OperatableStateMachine.add('gantrypos_1',
										ReplaceState(),
										transitions={'done': 'camera frame_1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LpulleyR', 'result': 'config_name_Gantry_pick1'})

			# x:113 y:142
			OperatableStateMachine.add('gantrypos_3',
										ReplaceState(),
										transitions={'done': 'camera frame_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgearR', 'result': 'config_name_Gantry_pick1'})

			# x:112 y:259
			OperatableStateMachine.add('gantrypos_4',
										ReplaceState(),
										transitions={'done': 'camera frame_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgearB_RgasketR', 'result': 'config_name_Gantry_pick1'})

			# x:110 y:387
			OperatableStateMachine.add('gantrypos_5',
										ReplaceState(),
										transitions={'done': 'camera frame_4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgasketR_RgearB', 'result': 'config_name_Gantry_pick1'})

			# x:108 y:525
			OperatableStateMachine.add('gantrypos_6',
										ReplaceState(),
										transitions={'done': 'camera frame_5'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgasketB_RpistonR', 'result': 'config_name_Gantry_pick1'})

			# x:104 y:661
			OperatableStateMachine.add('gantrypos_7',
										ReplaceState(),
										transitions={'done': 'camera frame_6'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LpistonR_RgasketB', 'result': 'config_name_Gantry_pick1'})

			# x:231 y:62
			OperatableStateMachine.add('camera frame_1',
										ReplaceState(),
										transitions={'done': 'camera topic_1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame0', 'result': 'camera_frame1'})

			# x:223 y:200
			OperatableStateMachine.add('camera frame_2',
										ReplaceState(),
										transitions={'done': 'camera topic_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame1', 'result': 'camera_frame1'})

			# x:222 y:325
			OperatableStateMachine.add('camera frame_3',
										ReplaceState(),
										transitions={'done': 'camera topic_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame2', 'result': 'camera_frame1'})

			# x:221 y:455
			OperatableStateMachine.add('camera frame_4',
										ReplaceState(),
										transitions={'done': 'camera topic_4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame3', 'result': 'camera_frame1'})

			# x:213 y:590
			OperatableStateMachine.add('camera frame_5',
										ReplaceState(),
										transitions={'done': 'camera topic_5'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame0', 'result': 'camera_frame1'})

			# x:213 y:724
			OperatableStateMachine.add('camera frame_6',
										ReplaceState(),
										transitions={'done': 'camera topic_6'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame0', 'result': 'camera_frame1'})

			# x:342 y:0
			OperatableStateMachine.add('camera topic_1',
										ReplaceState(),
										transitions={'done': 'offset_pulley'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic0', 'result': 'camera_topic1'})

			# x:341 y:145
			OperatableStateMachine.add('camera topic_2',
										ReplaceState(),
										transitions={'done': 'offset_gear'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic1', 'result': 'camera_topic1'})

			# x:340 y:262
			OperatableStateMachine.add('camera topic_3',
										ReplaceState(),
										transitions={'done': 'shelvePickL'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic2', 'result': 'camera_topic1'})

			# x:307 y:392
			OperatableStateMachine.add('camera topic_4',
										ReplaceState(),
										transitions={'done': 'shelvePickL_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic3', 'result': 'camera_topic1'})

			# x:334 y:532
			OperatableStateMachine.add('camera topic_5',
										ReplaceState(),
										transitions={'done': 'offset_gasket'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic0', 'result': 'camera_topic1'})

			# x:333 y:661
			OperatableStateMachine.add('camera topic_6',
										ReplaceState(),
										transitions={'done': 'offset_piston'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic0', 'result': 'camera_topic1'})

			# x:712 y:0
			OperatableStateMachine.add('pulley_R_2',
										EqualState(),
										transitions={'true': 'gantrypos_1_2', 'false': 'gear_R_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'PLR'})

			# x:714 y:131
			OperatableStateMachine.add('gear_R_2',
										EqualState(),
										transitions={'true': 'gantrypos_3_2', 'false': 'gear_B_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'GRR'})

			# x:716 y:264
			OperatableStateMachine.add('gear_B_2',
										EqualState(),
										transitions={'true': 'gantrypos_4_2', 'false': 'gasket_R_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'GRB'})

			# x:720 y:407
			OperatableStateMachine.add('gasket_R_2',
										EqualState(),
										transitions={'true': 'gantrypos_5_2', 'false': 'gasket_B_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'GKR'})

			# x:718 y:546
			OperatableStateMachine.add('gasket_B_2',
										EqualState(),
										transitions={'true': 'gantrypos_6_2', 'false': 'piston_R_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'GKB'})

			# x:719 y:682
			OperatableStateMachine.add('piston_R_2',
										EqualState(),
										transitions={'true': 'gantrypos_7_2', 'false': 'empty'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'PRR'})

			# x:896 y:0
			OperatableStateMachine.add('gantrypos_1_2',
										ReplaceState(),
										transitions={'done': 'camera frame_1_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'RpulleyR', 'result': 'config_name_Gantry_pick2'})

			# x:897 y:128
			OperatableStateMachine.add('gantrypos_3_2',
										ReplaceState(),
										transitions={'done': 'camera frame_2_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'RgearR', 'result': 'config_name_Gantry_pick2'})

			# x:899 y:260
			OperatableStateMachine.add('gantrypos_4_2',
										ReplaceState(),
										transitions={'done': 'camera frame_3_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgasketR_RgearB', 'result': 'config_name_Gantry_pick2'})

			# x:898 y:407
			OperatableStateMachine.add('gantrypos_5_2',
										ReplaceState(),
										transitions={'done': 'camera frame_4_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgearB_RgasketR', 'result': 'config_name_Gantry_pick2'})

			# x:897 y:546
			OperatableStateMachine.add('gantrypos_6_2',
										ReplaceState(),
										transitions={'done': 'camera frame_5_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LpistonR_RgasketB', 'result': 'config_name_Gantry_pick2'})

			# x:899 y:681
			OperatableStateMachine.add('gantrypos_7_2',
										ReplaceState(),
										transitions={'done': 'camera frame_6_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'LgasketB_RpistonR', 'result': 'config_name_Gantry_pick2'})

			# x:1077 y:0
			OperatableStateMachine.add('camera frame_1_2',
										ReplaceState(),
										transitions={'done': 'camera topic_1_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame0', 'result': 'camera_frame2'})

			# x:1077 y:129
			OperatableStateMachine.add('camera frame_2_2',
										ReplaceState(),
										transitions={'done': 'camera topic_2_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame1', 'result': 'camera_frame2'})

			# x:1075 y:259
			OperatableStateMachine.add('camera frame_3_2',
										ReplaceState(),
										transitions={'done': 'camera topic_3_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame2', 'result': 'camera_frame2'})

			# x:1072 y:406
			OperatableStateMachine.add('camera frame_4_2',
										ReplaceState(),
										transitions={'done': 'camera topic_4_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame3', 'result': 'camera_frame2'})

			# x:1073 y:543
			OperatableStateMachine.add('camera frame_5_2',
										ReplaceState(),
										transitions={'done': 'camera topic_5_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame0', 'result': 'camera_frame2'})

			# x:1078 y:679
			OperatableStateMachine.add('camera frame_6_2',
										ReplaceState(),
										transitions={'done': 'camera topic_6_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'frame0', 'result': 'camera_frame2'})

			# x:1259 y:0
			OperatableStateMachine.add('camera topic_1_2',
										ReplaceState(),
										transitions={'done': 'offset_pulley_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic0', 'result': 'camera_topic2'})

			# x:1259 y:132
			OperatableStateMachine.add('camera topic_2_2',
										ReplaceState(),
										transitions={'done': 'offset_gear_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic1', 'result': 'camera_topic2'})

			# x:1260 y:258
			OperatableStateMachine.add('camera topic_3_2',
										ReplaceState(),
										transitions={'done': 'shelvePickR'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic2', 'result': 'camera_topic2'})

			# x:1261 y:405
			OperatableStateMachine.add('camera topic_4_2',
										ReplaceState(),
										transitions={'done': 'shelvePickR_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic3', 'result': 'camera_topic2'})

			# x:1260 y:543
			OperatableStateMachine.add('camera topic_5_2',
										ReplaceState(),
										transitions={'done': 'offset_gasket_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic0', 'result': 'camera_topic2'})

			# x:1261 y:680
			OperatableStateMachine.add('camera topic_6_2',
										ReplaceState(),
										transitions={'done': 'offset_piston_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'topic0', 'result': 'camera_topic2'})

			# x:1452 y:0
			OperatableStateMachine.add('offset_pulley_2',
										ReplaceState(),
										transitions={'done': 'Pick two parts V3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_PL', 'result': 'offset2'})

			# x:1452 y:188
			OperatableStateMachine.add('offset_gear_2',
										ReplaceState(),
										transitions={'done': 'Pick two parts V3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_GR', 'result': 'offset2'})

			# x:1452 y:472
			OperatableStateMachine.add('offset_gasket_2',
										ReplaceState(),
										transitions={'done': 'Pick two parts V3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_GK', 'result': 'offset2'})

			# x:1461 y:675
			OperatableStateMachine.add('offset_piston_2',
										ReplaceState(),
										transitions={'done': 'Pick two parts V3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_PR', 'result': 'offset2'})

			# x:453 y:318
			OperatableStateMachine.add('shelvePickL',
										ReplaceState(),
										transitions={'done': 'offset_gear'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PrePickstelling_L', 'result': 'config_name_PrePick1'})

			# x:484 y:384
			OperatableStateMachine.add('shelvePickL_2',
										ReplaceState(),
										transitions={'done': 'offset_gasket'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PrePickstelling_L', 'result': 'config_name_PrePick1'})

			# x:1455 y:285
			OperatableStateMachine.add('shelvePickR',
										ReplaceState(),
										transitions={'done': 'offset_gear_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PrePickstelling_R', 'result': 'config_name_PrePick2'})

			# x:1452 y:357
			OperatableStateMachine.add('shelvePickR_2',
										ReplaceState(),
										transitions={'done': 'offset_gasket_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PrePickstelling_R', 'result': 'config_name_PrePick2'})

			# x:1048 y:766
			OperatableStateMachine.add('empty',
										EqualState(),
										transitions={'true': 'Pick two parts V3', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'empty'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
