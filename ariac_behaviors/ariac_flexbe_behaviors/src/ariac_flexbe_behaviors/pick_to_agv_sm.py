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
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Bas Jochems, Geert van der Meijden
'''
class PicktoAGVSM(Behavior):
	'''
	verplaatst onderdelen van opslag naar AGV
	'''


	def __init__(self):
		super(PicktoAGVSM, self).__init__()
		self.name = 'Pick to AGV'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:944 y:732, x:764 y:355
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.part_type = 'gear_part_red'
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.offset = 0.025
		_state_machine.userdata.move_group_G = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_bins1'
		_state_machine.userdata.camera_frame = 'logical_camera_bins1_frame'
		_state_machine.userdata.tool_link_R = 'right_ee_link'
		_state_machine.userdata.arm_id = 'Left_Arm'
		_state_machine.userdata.config_name_Gantry_pick = 'Gantry_Bins_LinksBovenRechts'
		_state_machine.userdata.null = 0
		_state_machine.userdata.config_name_Gantry_Transportband = 'Gantry_Transportband'
		_state_machine.userdata.config_name_Gantry_AGV = 'Gantry_AGV_Rechts_L'
		_state_machine.userdata.config_name_Left_home = 'Left_Home'
		_state_machine.userdata.config_name_Right_home = 'Right_Home'
		_state_machine.userdata.move_group_L = 'Left_Arm'
		_state_machine.userdata.move_group_R = 'Right_Arm'
		_state_machine.userdata.config_name_L = 'Links_PreDrop_Stelling'
		_state_machine.userdata.config_name_R = 'Rechts_PreDrop_Stelling'
		_state_machine.userdata.tool_link_L = 'left_ee_link'
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.camera_ref_frame = 'world'
		_state_machine.userdata.config_name_PrePick = 'Links_PreGrasp_Bins'
		_state_machine.userdata.config_name_PreDrop = 'Links_PreDrop_AGV'
		_state_machine.userdata.pose = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:73 y:57
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'stop belt'},
										autonomy={'continue': Autonomy.Off})

			# x:1574 y:26
			OperatableStateMachine.add('Pregrasp_G',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'PrePick', 'planning_failed': 'failed', 'control_failed': 'PrePick', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_pick', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:261 y:30
			OperatableStateMachine.add('stop belt',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'PreLeftHome', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'null'})

			# x:988 y:18
			OperatableStateMachine.add('LeftHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'RightHome', 'planning_failed': 'failed', 'control_failed': 'RightHome', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Left_home', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1259 y:20
			OperatableStateMachine.add('RightHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Right_home', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:522 y:12
			OperatableStateMachine.add('PreLeftHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'PreRightHome', 'planning_failed': 'failed', 'control_failed': 'PreRightHome', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_L', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:759 y:14
			OperatableStateMachine.add('PreRightHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'LeftHome', 'planning_failed': 'failed', 'control_failed': 'LeftHome', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1566 y:263
			OperatableStateMachine.add('CheckPartPoseBin',
										DetectPartCameraAriacState(time_out=2),
										transitions={'continue': 'ComputePick', 'failed': 'failed', 'not_found': 'Retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:1579 y:349
			OperatableStateMachine.add('ComputePick',
										ComputeGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Pick', 'failed': 'Retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_L', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1326 y:337
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=0.2),
										transitions={'done': 'PrePick'},
										autonomy={'done': Autonomy.Off})

			# x:1579 y:157
			OperatableStateMachine.add('PrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'CheckPartPoseBin', 'planning_failed': 'CheckPartPoseBin', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PrePick', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1329 y:732
			OperatableStateMachine.add('LeftHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Left_home', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1602 y:444
			OperatableStateMachine.add('Pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperEnable', 'planning_failed': 'failed', 'control_failed': 'GripperEnable'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_L', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1597 y:703
			OperatableStateMachine.add('PrePick_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'LeftHome_2', 'planning_failed': 'failed', 'control_failed': 'LeftHome_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PrePick', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1582 y:575
			OperatableStateMachine.add('GripperEnable',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'PrePick_2', 'failed': 'Retry', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
