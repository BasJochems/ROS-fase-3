#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.message_state import MessageState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.detect_first_part_camera_ariac_state import DetectFirstPartCameraAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.robotselector_sm import RobotSelectorSM
from ariac_flexbe_states.compute_drop_bin import ComputeDropBin
from ariac_flexbe_behaviors.binplace_sm import BinPlaceSM
from ariac_flexbe_behaviors.offsetcounter_sm import OffsetCounterSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Bas en Geert
'''
class belt_to_binSM(Behavior):
	'''
	belt_to_bin
	'''


	def __init__(self):
		super(belt_to_binSM, self).__init__()
		self.name = 'belt_to_bin'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(RobotSelectorSM, 'RobotSelector')
		self.add_behavior(BinPlaceSM, 'BinPlace')
		self.add_behavior(OffsetCounterSM, 'OffsetCounter')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:646, x:399 y:289
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.Power = 100
		_state_machine.userdata.NoPower = 0
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_band'
		_state_machine.userdata.camera_frame = 'logical_camera_band_frame'
		_state_machine.userdata.part = ''
		_state_machine.userdata.pose = []
		_state_machine.userdata.move_groupG = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.move_groupL = 'Left_Arm'
		_state_machine.userdata.move_groupR = 'Right_Arm'
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.tool_linkR = 'right_ee_link'
		_state_machine.userdata.config_namePBR = 'Right_Pre_Band'
		_state_machine.userdata.armidl = 'left'
		_state_machine.userdata.armidr = 'right'
		_state_machine.userdata.config_namePBL = 'Left_Pre_Band'
		_state_machine.userdata.tool_linkL = 'left_ee_link'
		_state_machine.userdata.offset = 0
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.config_name = ''
		_state_machine.userdata.arm = ''
		_state_machine.userdata.armklaar = 'klaar'
		_state_machine.userdata.config_nameA = ''
		_state_machine.userdata.config_name_bin = 'Gantry_R-pistonR_L-gasketB'
		_state_machine.userdata.offsety = 0
		_state_machine.userdata.offsetz = 0
		_state_machine.userdata.offsetx = 0
		_state_machine.userdata.configGH = 'Gantry_Home'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:54 y:551
			OperatableStateMachine.add('StopConveyor_2',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'LH', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'NoPower'})

			# x:119 y:11
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=0),
										transitions={'done': 'DetectPart'},
										autonomy={'done': Autonomy.Off})

			# x:673 y:39
			OperatableStateMachine.add('StopConveyor',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'MoveToPrePick', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'NoPower'})

			# x:322 y:5
			OperatableStateMachine.add('MsgPart',
										MessageState(),
										transitions={'continue': 'MsgPose'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part'})

			# x:500 y:7
			OperatableStateMachine.add('MsgPose',
										MessageState(),
										transitions={'continue': 'RobotSelector'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose'})

			# x:951 y:38
			OperatableStateMachine.add('MoveToPrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'WelkeArm', 'planning_failed': 'failed', 'control_failed': 'WelkeArm', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1074 y:121
			OperatableStateMachine.add('ComputePickRechts',
										ComputeGraspAriacState(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'Pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_linkR', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1222 y:258
			OperatableStateMachine.add('Pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperAan', 'planning_failed': 'failed', 'control_failed': 'GripperAan'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:94 y:314
			OperatableStateMachine.add('RH',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperUitR', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_namePBR', 'move_group': 'move_groupR', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:136 y:128
			OperatableStateMachine.add('DetectPart',
										DetectFirstPartCameraAriacState(part_list=['gasket_part_blue', 'piston_rod_part_red'], time_out=0.5),
										transitions={'continue': 'MsgPart', 'failed': 'Retry', 'not_found': 'Retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:982 y:310
			OperatableStateMachine.add('GripperAan',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'ArmHomePick', 'failed': 'WelkeArm', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:962 y:401
			OperatableStateMachine.add('StartBelt',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'DetectPart', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'Power'})

			# x:1238 y:358
			OperatableStateMachine.add('ArmHomePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'KlaarPick?', 'planning_failed': 'failed', 'control_failed': 'KlaarPick?', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_nameA', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1303 y:109
			OperatableStateMachine.add('ComputePickLinks',
										ComputeGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_linkL', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1192 y:8
			OperatableStateMachine.add('WelkeArm',
										EqualState(),
										transitions={'true': 'ComputePickRechts', 'false': 'ComputePickLinks'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'armidr'})

			# x:83 y:394
			OperatableStateMachine.add('GripperUitL',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'RH', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'armidl'})

			# x:113 y:212
			OperatableStateMachine.add('GripperUitR',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'StartBelt', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'armidr'})

			# x:345 y:80
			OperatableStateMachine.add('RobotSelector',
										self.use_behavior(RobotSelectorSM, 'RobotSelector'),
										transitions={'finished': 'StopConveyor', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part', 'offset': 'offset', 'move_group': 'move_group', 'config_name': 'config_name', 'arm_id': 'arm_id', 'arm': 'arm', 'config_nameA': 'config_nameA'})

			# x:1221 y:490
			OperatableStateMachine.add('KlaarPick?',
										EqualState(),
										transitions={'true': 'GantryHome', 'false': 'StartBelt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm', 'value_b': 'armklaar'})

			# x:1329 y:633
			OperatableStateMachine.add('GantryHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveToBin', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'configGH', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1328 y:738
			OperatableStateMachine.add('MoveToBin',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'BinPlace', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:705 y:639
			OperatableStateMachine.add('ComputeDropL',
										ComputeDropBin(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Place', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_linkL', 'pose': 'binpose', 'offsetx': 'offsetx', 'offsety': 'offsety', 'offsetz': 'offsetz', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:682 y:772
			OperatableStateMachine.add('ComputeDropR',
										ComputeDropBin(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'Place', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_linkR', 'pose': 'binpose', 'offsetx': 'offsetx', 'offsety': 'offsety', 'offsetz': 'offsetz', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:841 y:756
			OperatableStateMachine.add('WelkeArm2',
										EqualState(),
										transitions={'true': 'ComputeDropR', 'false': 'ComputeDropL'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'armidr'})

			# x:436 y:712
			OperatableStateMachine.add('Place',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperUit', 'planning_failed': 'failed', 'control_failed': 'GripperUit'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:260 y:733
			OperatableStateMachine.add('ArmHomePlace',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'KlaarPlaatsen?', 'planning_failed': 'failed', 'control_failed': 'KlaarPlaatsen?', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_nameA', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1075 y:741
			OperatableStateMachine.add('BinPlace',
										self.use_behavior(BinPlaceSM, 'BinPlace'),
										transitions={'finished': 'WelkeArm2', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm': 'arm', 'arm_id': 'arm_id', 'move_group': 'move_group', 'config_nameA': 'config_nameA', 'binpose': 'binpose'})

			# x:74 y:737
			OperatableStateMachine.add('KlaarPlaatsen?',
										EqualState(),
										transitions={'true': 'OffsetCounter', 'false': 'BinPlace'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm', 'value_b': 'armklaar'})

			# x:82 y:633
			OperatableStateMachine.add('OffsetCounter',
										self.use_behavior(OffsetCounterSM, 'OffsetCounter'),
										transitions={'finished': 'GantryHome_2', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'offsetx': 'offsetx', 'offsety': 'offsety'})

			# x:321 y:596
			OperatableStateMachine.add('GripperUit',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'ArmHomePlace', 'failed': 'WelkeArm2', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:223 y:518
			OperatableStateMachine.add('GantryHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'StartBelt', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'configGH', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:80 y:492
			OperatableStateMachine.add('LH',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperUitL', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_namePBL', 'move_group': 'move_groupL', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
