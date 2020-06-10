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
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Bas Jochems, Geert van der Meijden
'''
class PositiontestSM(Behavior):
	'''
	test alle posities in omgeving
	'''


	def __init__(self):
		super(PositiontestSM, self).__init__()
		self.name = 'Position test'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:32 y:406, x:900 y:385
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.offset = ''
		_state_machine.userdata.move_group = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.ref_frame = 'torso_base_main_joint'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_bins1'
		_state_machine.userdata.camera_frame = 'logical_camera_bins1_frame'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.arm_id = 'links'
		_state_machine.userdata.config_name_Gantry_Bins_RechtsBovenRechts = 'Gantry_Bins_RechtsBovenRechts'
		_state_machine.userdata.config_name_Gantry_Bins_RechtsBovenLinks = 'Gantry_Bins_RechtsBovenLinks'
		_state_machine.userdata.config_name_Gantry_Bins_LinksBovenRechts = 'Gantry_Bins_LinksBovenRechts'
		_state_machine.userdata.config_name_Gantry_Bins_LinksBovenLinks = 'Gantry_Bins_LinksBovenLinks'
		_state_machine.userdata.null = 0
		_state_machine.userdata.config_name_Gantry_Transportband = 'Gantry_Transportband'
		_state_machine.userdata.config_name_Gantry_AGV_Rechts_L = 'Gantry_AGV_Rechts_L'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:73 y:57
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'stop belt'},
										autonomy={'continue': Autonomy.Off})

			# x:582 y:39
			OperatableStateMachine.add('Pregrasp_G',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G_2', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_Bins_RechtsBovenLinks', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:261 y:30
			OperatableStateMachine.add('stop belt',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Pregrasp_G', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'null'})

			# x:819 y:34
			OperatableStateMachine.add('Pregrasp_G_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G_3', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_Bins_RechtsBovenRechts', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1030 y:31
			OperatableStateMachine.add('Pregrasp_G_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G_4', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_Bins_LinksBovenRechts', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1253 y:26
			OperatableStateMachine.add('Pregrasp_G_4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G_5', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G_5', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_Bins_LinksBovenLinks', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1264 y:264
			OperatableStateMachine.add('Pregrasp_G_5',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G_6', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G_6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_Transportband', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1288 y:401
			OperatableStateMachine.add('Pregrasp_G_6',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'finished', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_AGV_Rechts_L', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
