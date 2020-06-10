#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_behaviors.part_choice_sm import PartchoiceSM
from ariac_flexbe_behaviors.parts_to_agv_sm import partstoAGVSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 03 2020
@author: Bas Jochems, Geert van der Meijden
'''
class OrderverwerkingSM(Behavior):
	'''
	verwerkt de binnenkomende orders
	'''


	def __init__(self):
		super(OrderverwerkingSM, self).__init__()
		self.name = 'Orderverwerking'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(PartchoiceSM, 'Part choice')
		self.add_behavior(partstoAGVSM, 'parts to AGV')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1789 y:363, x:970 y:749
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type1', 'part_type2', 'pose_on_agv1', 'agv_id', 'pose_on_agv2'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.offset1 = ''
		_state_machine.userdata.offset2 = ''
		_state_machine.userdata.part_type1 = ''
		_state_machine.userdata.part_type2 = ''
		_state_machine.userdata.pose_on_agv1 = []
		_state_machine.userdata.pose_on_agv2 = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:489 y:290
			OperatableStateMachine.add('Part choice',
										self.use_behavior(PartchoiceSM, 'Part choice'),
										transitions={'finished': 'parts to AGV', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type1': 'part_type1', 'part_type2': 'part_type2', 'offset1': 'offset1', 'offset2': 'offset2'})

			# x:916 y:289
			OperatableStateMachine.add('parts to AGV',
										self.use_behavior(partstoAGVSM, 'parts to AGV'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'agv_id': 'agv_id', 'offset2': 'offset2', 'offset1': 'offset1', 'pose_on_agv1': 'pose_on_agv1', 'pose_on_agv2': 'pose_on_agv2'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
