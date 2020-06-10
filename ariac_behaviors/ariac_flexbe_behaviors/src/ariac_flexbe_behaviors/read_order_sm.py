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
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_behaviors.getshipments_sm import GetShipmentsSM
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Jun 04 2020
@author: Bas Jochems, Geert van der Meijden
'''
class ReadorderSM(Behavior):
	'''
	Order gets read
	'''


	def __init__(self):
		super(ReadorderSM, self).__init__()
		self.name = 'Read order'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(GetShipmentsSM, 'GetShipments')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1751 y:131, x:910 y:358
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.shipments = []
		_state_machine.userdata.material_locations = []
		_state_machine.userdata.NumberOfShipments = 0
		_state_machine.userdata.OrderId = ''
		_state_machine.userdata.Products = []
		_state_machine.userdata.NumberOfProducts = 0
		_state_machine.userdata.power = 0
		_state_machine.userdata.config_name_PreHomeR = 'Rechts_PreDrop_AGV'
		_state_machine.userdata.config_name_PreHomeL = 'Links_PreDrop_AGV'
		_state_machine.userdata.move_group_R = 'Right_Arm'
		_state_machine.userdata.move_group_L = 'Left_Arm'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.Old_Id = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:62 y:57
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'TurnOffBelt'},
										autonomy={'continue': Autonomy.Off})

			# x:958 y:51
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'Id_Check'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'OrderId', 'shipments': 'Shipments', 'number_of_shipments': 'NumberOfShipments'})

			# x:1552 y:126
			OperatableStateMachine.add('EndAssigment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:1317 y:273
			OperatableStateMachine.add('GetShipments',
										self.use_behavior(GetShipmentsSM, 'GetShipments'),
										transitions={'finished': 'GetOrder', 'failed': 'EndAssigment'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'Shipments': 'Shipments', 'NumberOfShipments': 'NumberOfShipments'})

			# x:249 y:56
			OperatableStateMachine.add('TurnOffBelt',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'PreHomeL', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'power'})

			# x:514 y:36
			OperatableStateMachine.add('PreHomeL',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'PreHomeR', 'planning_failed': 'failed', 'control_failed': 'PreHomeR', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PreHomeL', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:739 y:53
			OperatableStateMachine.add('PreHomeR',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GetOrder', 'planning_failed': 'failed', 'control_failed': 'GetOrder', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PreHomeR', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1318 y:161
			OperatableStateMachine.add('Old_Id',
										ReplaceState(),
										transitions={'done': 'GetShipments'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'OrderId', 'result': 'Old_Id'})

			# x:1314 y:38
			OperatableStateMachine.add('Id_Check',
										EqualState(),
										transitions={'true': 'EndAssigment', 'false': 'Old_Id'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'OrderId', 'value_b': 'Old_Id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
