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
from ariac_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Bas en Geert
'''
class RobotSelectorSM(Behavior):
	'''
	Selects the right robotarm
	'''


	def __init__(self):
		super(RobotSelectorSM, self).__init__()
		self.name = 'RobotSelector'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1430 y:296, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part'], output_keys=['offset', 'move_group', 'config_name', 'arm_id', 'arm', 'config_nameA'])
		_state_machine.userdata.part = ''
		_state_machine.userdata.partG = 'gasket_part_blue'
		_state_machine.userdata.partPR = 'piston_rod_part_red'
		_state_machine.userdata.offset = 0
		_state_machine.userdata.offsetG = 0.04
		_state_machine.userdata.offsetPR = 0.02
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.config_name = ''
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.armidl = 'left'
		_state_machine.userdata.armidr = 'right'
		_state_machine.userdata.move_groupL = 'Left_Arm'
		_state_machine.userdata.move_groupR = 'Right_Arm'
		_state_machine.userdata.config_nameL = 'Gantry_Transportband_Links'
		_state_machine.userdata.config_nameR = 'Gantry_Transportband_Rechts'
		_state_machine.userdata.arm = ''
		_state_machine.userdata.armlinks = 'links'
		_state_machine.userdata.armklaar = 'klaar'
		_state_machine.userdata.move_groupG = 'Gantry'
		_state_machine.userdata.config_namePLA = 'Left_Pre_Band'
		_state_machine.userdata.config_namePRA = 'Right_Pre_Band'
		_state_machine.userdata.config_nameA = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Part?',
										EqualState(),
										transitions={'true': 'OffsetPR', 'false': 'OffsetG'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part', 'value_b': 'partPR'})

			# x:1047 y:60
			OperatableStateMachine.add('ConfigRechts',
										ReplaceState(),
										transitions={'done': 'ArmNaarLinks'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_nameR', 'result': 'config_name'})

			# x:853 y:450
			OperatableStateMachine.add('MoveGroupLinks',
										ReplaceState(),
										transitions={'done': 'ConfigLinks'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_groupL', 'result': 'move_group'})

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
										transitions={'done': 'ConfigRechts'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_groupR', 'result': 'move_group'})

			# x:499 y:219
			OperatableStateMachine.add('Arm?',
										EqualState(),
										transitions={'true': 'ArmIDLinks', 'false': 'ArmIDRechts'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm', 'value_b': 'armlinks'})

			# x:1241 y:63
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

			# x:412 y:55
			OperatableStateMachine.add('offset',
										MessageState(),
										transitions={'continue': 'Arm?'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'offset'})

			# x:233 y:121
			OperatableStateMachine.add('OffsetPR',
										ReplaceState(),
										transitions={'done': 'offset'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsetPR', 'result': 'offset'})

			# x:231 y:235
			OperatableStateMachine.add('OffsetG',
										ReplaceState(),
										transitions={'done': 'offset'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsetG', 'result': 'offset'})

			# x:1043 y:461
			OperatableStateMachine.add('ConfigLinks',
										ReplaceState(),
										transitions={'done': 'ArmNaarKlaar'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_nameL', 'result': 'config_name'})

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


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
