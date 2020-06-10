#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_first_part_camera_ariac_state import DetectFirstPartCameraAriacState
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.robotselector_sm import RobotSelectorSM
from ariac_flexbe_states.compute_drop_bin import ComputeDropBin
from ariac_flexbe_behaviors.binplace_sm import BinPlaceSM
from ariac_flexbe_behaviors.offsetcounter_sm import OffsetCounterSM
from ariac_support_flexbe_states.replace_state import ReplaceState
from flexbe_states.wait_state import WaitState
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
		# x:24 y:122, x:399 y:289
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
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.tool_linkR = 'right_ee_link'
		_state_machine.userdata.armidl = 'left'
		_state_machine.userdata.armidr = 'right'
		_state_machine.userdata.tool_linkL = 'left_ee_link'
		_state_machine.userdata.offset = 0
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.config_name = ''
		_state_machine.userdata.arm = ''
		_state_machine.userdata.armklaar = 'klaar'
		_state_machine.userdata.config_nameA = ''
		_state_machine.userdata.config_name_bin = ''
		_state_machine.userdata.offsety = 0
		_state_machine.userdata.offsetz = 0
		_state_machine.userdata.offsetx = 0
		_state_machine.userdata.configGH = 'Gantry_Home'
		_state_machine.userdata.partarmlinks = ''
		_state_machine.userdata.partarmrechts = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:121 y:45
			OperatableStateMachine.add('DetectPart',
										DetectFirstPartCameraAriacState(part_list=['gasket_part_blue', 'piston_rod_part_red'], time_out=0.5),
										transitions={'continue': 'RobotSelector', 'failed': 'Retry', 'not_found': 'Retry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:673 y:39
			OperatableStateMachine.add('StopConveyor',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'MoveToPrePick', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'NoPower'})

			# x:951 y:38
			OperatableStateMachine.add('MoveToPrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'WelkeArm', 'planning_failed': 'failed', 'control_failed': 'WelkeArm', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1052 y:186
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

			# x:982 y:310
			OperatableStateMachine.add('GripperAan',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'ArmHomePick', 'failed': 'WelkeArm', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:58 y:251
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

			# x:1338 y:170
			OperatableStateMachine.add('ComputePickLinks',
										ComputeGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_linkL', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1192 y:8
			OperatableStateMachine.add('WelkeArm',
										EqualState(),
										transitions={'true': 'PartArmRechts', 'false': 'PartArmLinks'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'armidr'})

			# x:394 y:45
			OperatableStateMachine.add('RobotSelector',
										self.use_behavior(RobotSelectorSM, 'RobotSelector'),
										transitions={'finished': 'StopConveyor', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part', 'offset': 'offset', 'move_group': 'move_group', 'config_name': 'config_name', 'arm_id': 'arm_id', 'arm': 'arm', 'config_nameA': 'config_nameA'})

			# x:1151 y:493
			OperatableStateMachine.add('KlaarPick?',
										EqualState(),
										transitions={'true': 'GantryHome', 'false': 'StartBelt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm', 'value_b': 'armklaar'})

			# x:1329 y:633
			OperatableStateMachine.add('GantryHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'BinPlace', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'configGH', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1070 y:768
			OperatableStateMachine.add('MoveToBin',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'WelkeArm2', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:670 y:637
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

			# x:51 y:762
			OperatableStateMachine.add('ArmHomePlace',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'KlaarPlaatsen?', 'planning_failed': 'failed', 'control_failed': 'KlaarPlaatsen?', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_nameA', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1262 y:742
			OperatableStateMachine.add('BinPlace',
										self.use_behavior(BinPlaceSM, 'BinPlace'),
										transitions={'finished': 'MoveToBin', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm': 'arm', 'partarmlinks': 'partarmlinks', 'partarmrechts': 'partarmrechts', 'arm_id': 'arm_id', 'move_group': 'move_group', 'config_nameA': 'config_nameA', 'binpose': 'binpose', 'config_name_bin': 'config_name_bin'})

			# x:46 y:671
			OperatableStateMachine.add('KlaarPlaatsen?',
										EqualState(),
										transitions={'true': 'OffsetCounter', 'false': 'BinPlace'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm', 'value_b': 'armklaar'})

			# x:57 y:509
			OperatableStateMachine.add('OffsetCounter',
										self.use_behavior(OffsetCounterSM, 'OffsetCounter'),
										transitions={'finished': 'GantryHome_2', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'offsetx': 'offsetx', 'offsety': 'offsety'})

			# x:253 y:755
			OperatableStateMachine.add('GripperUit',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'ArmHomePlace', 'failed': 'WelkeArm2', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:76 y:376
			OperatableStateMachine.add('GantryHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'StartBelt', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'configGH', 'move_group': 'move_groupG', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1102 y:96
			OperatableStateMachine.add('PartArmRechts',
										ReplaceState(),
										transitions={'done': 'ComputePickRechts'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part', 'result': 'partarmrechts'})

			# x:1334 y:70
			OperatableStateMachine.add('PartArmLinks',
										ReplaceState(),
										transitions={'done': 'ComputePickLinks'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part', 'result': 'partarmlinks'})

			# x:236 y:127
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=0),
										transitions={'done': 'DetectPart'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
