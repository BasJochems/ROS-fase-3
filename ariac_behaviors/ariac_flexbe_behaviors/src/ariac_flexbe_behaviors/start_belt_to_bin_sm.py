#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_behaviors.belt_to_bin_sm import belt_to_binSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Bas en Geert
'''
class start_belt_to_binSM(Behavior):
	'''
	start_belt_to_bin
	'''


	def __init__(self):
		super(start_belt_to_binSM, self).__init__()
		self.name = 'start_belt_to_bin'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(belt_to_binSM, 'belt_to_bin')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:714 y:77, x:440 y:495
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:90 y:51
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'belt_to_bin'},
										autonomy={'continue': Autonomy.Off})

			# x:418 y:49
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:229 y:38
			OperatableStateMachine.add('belt_to_bin',
										self.use_behavior(belt_to_binSM, 'belt_to_bin'),
										transitions={'finished': 'EndAssignment', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
