#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Bas Jochems, Geert van der Meijden
'''
class PicktwopartsV3SM(Behavior):
	'''
	pakt twee onderdelen
	'''


	def __init__(self):
		super(PicktwopartsV3SM, self).__init__()
		self.name = 'Pick two parts V3'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:692 y:77, x:764 y:355
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type1', 'part_type2', 'offset1', 'offset2', 'camera_topic1', 'camera_topic2', 'camera_frame1', 'camera_frame2', 'config_name_Gantry_pick1', 'config_name_Gantry_pick2', 'config_name_PrePick1', 'config_name_PrePick2'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.part_type1 = ''
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.offset1 = ''
		_state_machine.userdata.move_group_G = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.camera_topic1 = ''
		_state_machine.userdata.camera_frame1 = ''
		_state_machine.userdata.tool_link_R = 'right_ee_link'
		_state_machine.userdata.arm_id1 = 'left'
		_state_machine.userdata.config_name_Gantry_pick1 = ''
		_state_machine.userdata.null = 0
		_state_machine.userdata.config_name_Left_home = 'Left_Home'
		_state_machine.userdata.config_name_Right_home = 'Right_Home'
		_state_machine.userdata.move_group_L = 'Left_Arm'
		_state_machine.userdata.move_group_R = 'Right_Arm'
		_state_machine.userdata.config_name_L = 'Links_PreDrop_Stelling'
		_state_machine.userdata.config_name_R = 'Rechts_PreDrop_Stelling'
		_state_machine.userdata.tool_link_L = 'left_ee_link'
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.camera_ref_frame = 'world'
		_state_machine.userdata.config_name_PrePick1 = ''
		_state_machine.userdata.config_name_PreDrop = 'Links_PreDrop_AGV'
		_state_machine.userdata.pose = []
		_state_machine.userdata.config_name_Gantry_pick2 = ''
		_state_machine.userdata.part_type2 = ''
		_state_machine.userdata.camera_frame2 = ''
		_state_machine.userdata.camera_topic2 = ''
		_state_machine.userdata.offset2 = ''
		_state_machine.userdata.arm_id2 = 'right'
		_state_machine.userdata.config_name_PrePick2 = ''
		_state_machine.userdata.config_name_GantrySafe = 'Gantry_Transportband_Home'
		_state_machine.userdata.AtShelve = 0
		_state_machine.userdata.true = 1
		_state_machine.userdata.false = 0
		_state_machine.userdata.Lshelve = 'Links_PreDrop_Stelling'
		_state_machine.userdata.Rshelve = 'Rechts_PreDrop_Stelling'
		_state_machine.userdata.empty = 'empty'
		_state_machine.userdata.config_name_Gantry_AtShelve = 'Gantry_Stelling'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:939 y:13
			OperatableStateMachine.add('LeftHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'RightHome', 'planning_failed': 'failed', 'control_failed': 'RightHome', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Left_home', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1150 y:13
			OperatableStateMachine.add('RightHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperDisable_2', 'planning_failed': 'failed', 'control_failed': 'GripperDisable_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Right_home', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1650 y:396
			OperatableStateMachine.add('CheckPartPoseBin',
										DetectPartCameraAriacState(time_out=2),
										transitions={'continue': 'ComputePick', 'failed': 'failed', 'not_found': 'Retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic1', 'camera_frame': 'camera_frame1', 'part': 'part_type1', 'pose': 'pose'})

			# x:1660 y:495
			OperatableStateMachine.add('ComputePick',
										ComputeGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Pick', 'failed': 'Retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_L', 'pose': 'pose', 'offset': 'offset1', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1430 y:397
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=0.2),
										transitions={'done': 'PrePick'},
										autonomy={'done': Autonomy.Off})

			# x:1673 y:283
			OperatableStateMachine.add('PrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'CheckPartPoseBin', 'planning_failed': 'failed', 'control_failed': 'CheckPartPoseBin', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PrePick1', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1451 y:763
			OperatableStateMachine.add('LeftHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'empty?', 'planning_failed': 'failed', 'control_failed': 'empty?', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Left_home', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1348 y:541
			OperatableStateMachine.add('Pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperEnable', 'planning_failed': 'failed', 'control_failed': 'GripperEnable'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_L', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1679 y:758
			OperatableStateMachine.add('PrePick_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'LeftHome_2', 'planning_failed': 'failed', 'control_failed': 'LeftHome_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PrePick1', 'move_group': 'move_group_L', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1657 y:659
			OperatableStateMachine.add('GripperEnable',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'PrePick_2', 'failed': 'ComputePick', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id1'})

			# x:475 y:757
			OperatableStateMachine.add('Pregrasp_G_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'PrePick_3', 'planning_failed': 'failed', 'control_failed': 'PrePick_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_pick2', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:15 y:701
			OperatableStateMachine.add('CheckPartPoseBin_2',
										DetectPartCameraAriacState(time_out=2),
										transitions={'continue': 'ComputePick_2', 'failed': 'Retry_2', 'not_found': 'Retry_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic2', 'camera_frame': 'camera_frame2', 'part': 'part_type2', 'pose': 'pose2'})

			# x:13 y:536
			OperatableStateMachine.add('ComputePick_2',
										ComputeGraspAriacState(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'Pick_2', 'failed': 'Retry_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_R', 'pose': 'pose2', 'offset': 'offset2', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:271 y:602
			OperatableStateMachine.add('Retry_2',
										WaitState(wait_time=0.2),
										transitions={'done': 'PrePick_3'},
										autonomy={'done': Autonomy.Off})

			# x:255 y:742
			OperatableStateMachine.add('PrePick_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'CheckPartPoseBin_2', 'planning_failed': 'failed', 'control_failed': 'CheckPartPoseBin_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PrePick2', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:285 y:456
			OperatableStateMachine.add('Pick_2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperEnable_2', 'planning_failed': 'failed', 'control_failed': 'GripperEnable_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_R', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:28 y:367
			OperatableStateMachine.add('GripperEnable_2',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'PrePick_2_2', 'failed': 'ComputePick_2', 'invalid_arm_id': 'PrePick_2_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id2'})

			# x:39 y:257
			OperatableStateMachine.add('PrePick_2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'RightHome_2', 'planning_failed': 'failed', 'control_failed': 'RightHome_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PrePick2', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1568 y:9
			OperatableStateMachine.add('GripperDisable',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'ShelveCheck1', 'failed': 'ShelveCheck1', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id1'})

			# x:1359 y:10
			OperatableStateMachine.add('GripperDisable_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'GripperDisable', 'failed': 'GripperDisable', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id2'})

			# x:37 y:150
			OperatableStateMachine.add('RightHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'SavePosShelve2_2', 'planning_failed': 'failed', 'control_failed': 'SavePosShelve2_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Right_home', 'move_group': 'move_group_R', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1657 y:92
			OperatableStateMachine.add('ShelveCheck1',
										EqualState(),
										transitions={'true': 'SetShelve1', 'false': 'Pregrasp_G'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'config_name_PrePick1', 'value_b': 'Lshelve'})

			# x:1441 y:206
			OperatableStateMachine.add('SavePosShelve1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_GantrySafe', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1433 y:102
			OperatableStateMachine.add('SetShelve1',
										ReplaceState(),
										transitions={'done': 'SavePosShelve1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'true', 'result': 'AtShelve'})

			# x:1044 y:755
			OperatableStateMachine.add('AtShelve?',
										EqualState(),
										transitions={'true': 'ShelveCheck3', 'false': 'ShelveCheck2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'AtShelve', 'value_b': 'true'})

			# x:770 y:765
			OperatableStateMachine.add('ShelveCheck3',
										EqualState(),
										transitions={'true': 'Pregrasp_G_2', 'false': 'SavePosShelve2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'config_name_PrePick2', 'value_b': 'Rshelve'})

			# x:692 y:623
			OperatableStateMachine.add('SavePosShelve2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pregrasp_G_2', 'planning_failed': 'failed', 'control_failed': 'Pregrasp_G_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_GantrySafe', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:354 y:107
			OperatableStateMachine.add('SavePosShelve2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_GantrySafe', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1237 y:753
			OperatableStateMachine.add('empty?',
										EqualState(),
										transitions={'true': 'SavePosShelve2_2', 'false': 'AtShelve?'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'empty'})

			# x:1671 y:179
			OperatableStateMachine.add('Pregrasp_G',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'PrePick', 'planning_failed': 'failed', 'control_failed': 'PrePick', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_Gantry_pick1', 'move_group': 'move_group_G', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:870 y:686
			OperatableStateMachine.add('ShelveCheck2',
										EqualState(),
										transitions={'true': 'SavePosShelve2', 'false': 'Pregrasp_G_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'config_name_PrePick2', 'value_b': 'Rshelve'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
