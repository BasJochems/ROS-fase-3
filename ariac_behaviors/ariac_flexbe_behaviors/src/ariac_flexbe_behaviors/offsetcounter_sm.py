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
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Jun 04 2020
@author: Bas en Geert
'''
class OffsetCounterSM(Behavior):
	'''
	Changes offset for placing parts
	'''


	def __init__(self):
		super(OffsetCounterSM, self).__init__()
		self.name = 'OffsetCounter'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:346 y:592, x:899 y:56
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['offsetx', 'offsety'], output_keys=['offsetx', 'offsety'])
		_state_machine.userdata.offsetx = 0
		_state_machine.userdata.offsety = 0
		_state_machine.userdata.opschuifx = 0.2
		_state_machine.userdata.opschuify = 0.2
		_state_machine.userdata.een = 1
		_state_machine.userdata.nul = 0
		_state_machine.userdata.tellerx = 0
		_state_machine.userdata.tellery = 0
		_state_machine.userdata.twee = 2
		_state_machine.userdata.message = 'BinisVol!'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:121 y:40
			OperatableStateMachine.add('CheckY',
										EqualState(),
										transitions={'true': 'ResetY', 'false': 'AddY'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'tellery', 'value_b': 'twee'})

			# x:103 y:280
			OperatableStateMachine.add('AddTellerY',
										AddNumericState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'tellery', 'value_b': 'een', 'result': 'tellery'})

			# x:339 y:34
			OperatableStateMachine.add('ResetY',
										ReplaceState(),
										transitions={'done': 'CheckX'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'tellery', 'result': 'nul'})

			# x:369 y:276
			OperatableStateMachine.add('AddX',
										AddNumericState(),
										transitions={'done': 'AddTellerX'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'offsetx', 'value_b': 'opschuifx', 'result': 'offsetx'})

			# x:383 y:409
			OperatableStateMachine.add('AddTellerX',
										AddNumericState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'tellerx', 'value_b': 'een', 'result': 'tellerx'})

			# x:340 y:138
			OperatableStateMachine.add('CheckX',
										EqualState(),
										transitions={'true': 'ResetX', 'false': 'AddX'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'tellerx', 'value_b': 'twee'})

			# x:576 y:131
			OperatableStateMachine.add('ResetX',
										ReplaceState(),
										transitions={'done': 'ResetX'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'tellerx', 'result': 'nul'})

			# x:776 y:130
			OperatableStateMachine.add('BinisVol',
										MessageState(),
										transitions={'continue': 'failed'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'message'})

			# x:114 y:170
			OperatableStateMachine.add('AddY',
										AddNumericState(),
										transitions={'done': 'AddTellerY'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'offsety', 'value_b': 'opschuify', 'result': 'offsety'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
