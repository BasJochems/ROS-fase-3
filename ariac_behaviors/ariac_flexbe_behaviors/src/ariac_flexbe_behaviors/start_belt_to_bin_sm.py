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
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
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
		# x:1274 y:459, x:654 y:517
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.move_groupL = 'Left_Arm'
		_state_machine.userdata.move_groupR = 'Right_Arm'
		_state_machine.userdata.armidl = 'left'
		_state_machine.userdata.armidr = 'right'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.config_namePBL = 'Left_Pre_Band'
		_state_machine.userdata.config_namePBR = 'Right_Pre_Band'
		_state_machine.userdata.Power = 100
		_state_machine.userdata.NoPower = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:51 y:37
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'BeltOff'},
										autonomy={'continue': Autonomy.Off})

			# x:1464 y:55
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:1219 y:45
			OperatableStateMachine.add('belt_to_bin',
										self.use_behavior(belt_to_binSM, 'belt_to_bin'),
										transitions={'finished': 'EndAssignment', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:616 y:39
			OperatableStateMachine.add('RH',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperUitR', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_namePBR', 'move_group': 'move_groupR', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:428 y:38
			OperatableStateMachine.add('GripperUitL',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'RH', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'armidl'})

			# x:791 y:39
			OperatableStateMachine.add('GripperUitR',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'BeltOn', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'armidr'})

			# x:225 y:36
			OperatableStateMachine.add('LH',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperUitL', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_namePBL', 'move_group': 'move_groupL', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:112 y:134
			OperatableStateMachine.add('BeltOff',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'LH', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'NoPower'})

			# x:1011 y:39
			OperatableStateMachine.add('BeltOn',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'belt_to_bin', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'Power'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
