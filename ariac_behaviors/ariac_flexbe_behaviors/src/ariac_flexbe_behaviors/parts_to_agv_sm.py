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
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.ComputeDropPartOffsetGraspAriacState import ComputeDropPartOffsetGraspAriacState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 03 2020
@author: Bas Jochems, Geert van der Meijden
'''
class partstoAGVSM(Behavior):
	'''
	Bezorgd de onderdelen naar de juiste agv
	'''


	def __init__(self):
		super(partstoAGVSM, self).__init__()
		self.name = 'parts to AGV'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:737 y:206, x:797 y:409
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['agv_id', 'offset2', 'offset1', 'pose_on_agv1', 'pose_on_agv2', 'part_type2'])
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.move_group_G = 'Gantry'
		_state_machine.userdata.move_group_L = 'Left_Arm'
		_state_machine.userdata.move_group_R = 'Right_Arm'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.offset1 = ''
		_state_machine.userdata.offset2 = ''
		_state_machine.userdata.config_name_GantryL_AGVL = 'Gantry_AGV_Links_L'
		_state_machine.userdata.config_name_GantryL_AGVR = 'Gantry_AGV_Links_R'
		_state_machine.userdata.config_name_GantryR_AGVL = 'Gantry_AGV_Rechts_L'
		_state_machine.userdata.config_name_GantryR_AGVR = 'Gantry_AGV_Rechts_R'
		_state_machine.userdata.config_name_GantryAGVL = ''
		_state_machine.userdata.config_name_GantryAGVR = ''
		_state_machine.userdata.agv1 = 'agv1'
		_state_machine.userdata.agv2 = 'agv2'
		_state_machine.userdata.config_name_PlaceAGVL = 'Links_PreDrop_AGV'
		_state_machine.userdata.tool_link_R = 'right_ee_link'
		_state_machine.userdata.tool_link_L = 'left_ee_link'
		_state_machine.userdata.agv_pose = []
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.pose_on_agv1 = []
		_state_machine.userdata.arm_idL = 'left'
		_state_machine.userdata.config_name_PlaceAGVR = 'Rechts_PreDrop_AGV'
		_state_machine.userdata.arm_idR = 'right'
		_state_machine.userdata.pose_on_agv2 = []
		_state_machine.userdata.config_name_homeL = 'Left_Home'
		_state_machine.userdata.config_name_homeR = 'Right_Home'
		_state_machine.userdata.config_name_Gantry_home = 'Gantry_Transportband_Home'
		_state_machine.userdata.part_type2 = ''
		_state_machine.userdata.empty = 'empty'
		_state_machine.userdata.kit_tray = 'kit_tray_1'
		_state_machine.userdata.KT1 = 'kit_tray_1'
		_state_machine.userdata.KT2 = 'kit_tray_2'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:98 y:59
			OperatableStateMachine.add('AGV choice',
										EqualState(),
										transitions={'true': 'SetPosL1', 'false': 'SetPosL2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv2'})

			# x:340 y:29
			OperatableStateMachine.add('SetPosL1',
										ReplaceState(),
										transitions={'done': 'SetPosR1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_GantryR_AGVL', 'result': 'config_name_GantryAGVL'})

			# x:534 y:29
			OperatableStateMachine.add('SetPosR1',
										ReplaceState(),
										transitions={'done': 'MoveL to AGV'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_GantryR_AGVR', 'result': 'config_name_GantryAGVR'})

			# x:340 y:91
			OperatableStateMachine.add('SetPosL2',
										ReplaceState(),
										transitions={'done': 'SetPosR2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_GantryL_AGVL', 'result': 'config_name_GantryAGVL'})

			# x:535 y:91
			OperatableStateMachine.add('SetPosR2',
										ReplaceState(),
										transitions={'done': 'MoveL to AGV'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_GantryL_AGVR', 'result': 'config_name_GantryAGVR'})

			# x:1187 y:33
			OperatableStateMachine.add('Move to PrePlace',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'AGV choice_3', 'planning_failed': 'failed', 'control_failed': 'AGV choice_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PlaceAGVL', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:833 y:56
			OperatableStateMachine.add('MoveL to AGV',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move to PrePlace', 'planning_failed': 'failed', 'control_failed': 'Move to PrePlace', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_GantryAGVL', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1472 y:127
			OperatableStateMachine.add('GetAGV1pose',
										GetObjectPoseState(object_frame='kit_tray_1', ref_frame='world'),
										transitions={'continue': 'pose_on_AGV', 'failed': 'retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose'})

			# x:1604 y:295
			OperatableStateMachine.add('pose_on_AGV',
										ComputeDropPartOffsetGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'MoveToDrop1', 'failed': 'retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_L', 'part_pose': 'pose_on_agv1', 'pose': 'agv_pose', 'offset': 'offset1', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1219 y:277
			OperatableStateMachine.add('retry',
										WaitState(wait_time=0.5),
										transitions={'done': 'Move to PrePlace'},
										autonomy={'done': Autonomy.Off})

			# x:1650 y:386
			OperatableStateMachine.add('MoveToDrop1',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'DisableGripper', 'planning_failed': 'failed', 'control_failed': 'DisableGripper'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_L', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1658 y:491
			OperatableStateMachine.add('DisableGripper',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'Move to PrePlace_2', 'failed': 'Move to PrePlace_2', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_idL'})

			# x:1678 y:599
			OperatableStateMachine.add('Move to PrePlace_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move L to home ', 'planning_failed': 'failed', 'control_failed': 'Move L to home ', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PlaceAGVL', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1294 y:690
			OperatableStateMachine.add('MoveR to AGV',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move to PrePlace_3', 'planning_failed': 'failed', 'control_failed': 'Move to PrePlace_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_GantryAGVR', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1066 y:683
			OperatableStateMachine.add('Move to PrePlace_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'pose_on_AGV_2', 'planning_failed': 'failed', 'control_failed': 'pose_on_AGV_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PlaceAGVR', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:491 y:669
			OperatableStateMachine.add('GetAGV1pose_2',
										GetObjectPoseState(object_frame='kit_tray_1', ref_frame='world'),
										transitions={'continue': 'pose_on_AGV_2', 'failed': 'retry_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose2'})

			# x:14 y:717
			OperatableStateMachine.add('pose_on_AGV_2',
										ComputeDropPartOffsetGraspAriacState(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'MoveToDrop2', 'failed': 'retry_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_R', 'part_pose': 'pose_on_agv2', 'pose': 'agv_pose', 'offset': 'offset2', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:586 y:481
			OperatableStateMachine.add('retry_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'Move to PrePlace_3'},
										autonomy={'done': Autonomy.Off})

			# x:43 y:604
			OperatableStateMachine.add('MoveToDrop2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'DisableGripper_2', 'planning_failed': 'failed', 'control_failed': 'DisableGripper_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_R', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:48 y:494
			OperatableStateMachine.add('DisableGripper_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'Move to PrePlace_2_2', 'failed': 'Move to PrePlace_2_2', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_idR'})

			# x:61 y:378
			OperatableStateMachine.add('Move to PrePlace_2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move R to home ', 'planning_failed': 'failed', 'control_failed': 'Move R to home ', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PlaceAGVR', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1684 y:711
			OperatableStateMachine.add('Move L to home ',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'CheckSecondPart', 'planning_failed': 'failed', 'control_failed': 'CheckSecondPart', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_homeL', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:65 y:279
			OperatableStateMachine.add('Move R to home ',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GantryHome', 'planning_failed': 'failed', 'control_failed': 'GantryHome', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_homeR', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:335 y:205
			OperatableStateMachine.add('GantryHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_home', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1479 y:750
			OperatableStateMachine.add('CheckSecondPart',
										EqualState(),
										transitions={'true': 'GantryHome', 'false': 'MoveR to AGV'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'empty'})

			# x:668 y:546
			OperatableStateMachine.add('GetAGV2pose_2',
										GetObjectPoseState(object_frame='kit_tray_2', ref_frame='world'),
										transitions={'continue': 'pose_on_AGV_2', 'failed': 'retry_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose2'})

			# x:749 y:650
			OperatableStateMachine.add('AGV choice_2',
										EqualState(),
										transitions={'true': 'GetAGV2pose_2', 'false': 'GetAGV1pose_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv2'})

			# x:1462 y:28
			OperatableStateMachine.add('AGV choice_3',
										EqualState(),
										transitions={'true': 'GetAGV2pose', 'false': 'GetAGV1pose'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv2'})

			# x:1666 y:199
			OperatableStateMachine.add('GetAGV2pose',
										GetObjectPoseState(object_frame='kit_tray_2', ref_frame='world'),
										transitions={'continue': 'pose_on_AGV', 'failed': 'retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
