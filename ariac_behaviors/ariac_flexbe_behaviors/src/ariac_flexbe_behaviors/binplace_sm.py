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
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 03 2020
@author: Bas en Geert
'''
class BinPlaceSM(Behavior):
	'''
	Behavior that controls the placing of the parts
	'''


	def __init__(self):
		super(BinPlaceSM, self).__init__()
		self.name = 'BinPlace'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1424 y:263, x:653 y:236
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm'], output_keys=['arm', 'arm_id', 'move_group', 'config_nameA', 'binpose'])
		_state_machine.userdata.binpose = []
		_state_machine.userdata.arm = ''
		_state_machine.userdata.armlinks = 'links'
		_state_machine.userdata.armklaar = 'klaar'
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.move_groupL = 'Left_Arm'
		_state_machine.userdata.move_groupR = 'Right_Arm'
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.armidl = 'left'
		_state_machine.userdata.armidr = 'right'
		_state_machine.userdata.config_nameA = ''
		_state_machine.userdata.config_namePLA = 'Left_Pre_Band'
		_state_machine.userdata.config_namePRA = 'Right_Pre_Band'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:219 y:239
			OperatableStateMachine.add('Arm?',
										EqualState(),
										transitions={'true': 'GetPoseBin7', 'false': 'GetPoseBin2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm', 'value_b': 'armlinks'})

			# x:651 y:447
			OperatableStateMachine.add('ArmIDLinks',
										ReplaceState(),
										transitions={'done': 'MoveGroupLinks'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'armidl', 'result': 'arm_id'})

			# x:663 y:58
			OperatableStateMachine.add('ArmIDRechts',
										ReplaceState(),
										transitions={'done': 'MoveGroupRechts'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'armidr', 'result': 'arm_id'})

			# x:845 y:59
			OperatableStateMachine.add('MoveGroupRechts',
										ReplaceState(),
										transitions={'done': 'ArmNaarLinks'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_groupR', 'result': 'move_group'})

			# x:1105 y:53
			OperatableStateMachine.add('ArmNaarLinks',
										ReplaceState(),
										transitions={'done': 'ConfigRechtsHome'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'armlinks', 'result': 'arm'})

			# x:1249 y:458
			OperatableStateMachine.add('ArmNaarKlaar',
										ReplaceState(),
										transitions={'done': 'ConfigLinksHome'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'armklaar', 'result': 'arm'})

			# x:1207 y:161
			OperatableStateMachine.add('ConfigRechtsHome',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_namePRA', 'result': 'config_nameA'})

			# x:1227 y:359
			OperatableStateMachine.add('ConfigLinksHome',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_namePLA', 'result': 'config_nameA'})

			# x:452 y:82
			OperatableStateMachine.add('GetPoseBin2',
										GetObjectPoseState(object_frame='bin2_frame', ref_frame='world'),
										transitions={'continue': 'ArmIDRechts', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'binpose'})

			# x:444 y:347
			OperatableStateMachine.add('GetPoseBin7',
										GetObjectPoseState(object_frame='bin7_frame', ref_frame='world'),
										transitions={'continue': 'ArmIDLinks', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'binpose'})

			# x:853 y:450
			OperatableStateMachine.add('MoveGroupLinks',
										ReplaceState(),
										transitions={'done': 'ArmNaarKlaar'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_groupL', 'result': 'move_group'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
