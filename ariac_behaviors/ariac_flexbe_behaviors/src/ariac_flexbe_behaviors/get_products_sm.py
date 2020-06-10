#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from ariac_flexbe_behaviors.orderverwerking_sm import OrderverwerkingSM
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_states.message_state import MessageState
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Jun 04 2020
@author: Bas Jochems, Geert van der Meijden
'''
class Get_ProductsSM(Behavior):
	'''
	Assign products to arms
	'''


	def __init__(self):
		super(Get_ProductsSM, self).__init__()
		self.name = 'Get_Products'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(OrderverwerkingSM, 'Orderverwerking')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:587 y:648, x:611 y:249
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['Products', 'NumberOfProducts', 'agv_id'])
		_state_machine.userdata.ProductIterator = 0
		_state_machine.userdata.OneValue = 1
		_state_machine.userdata.ProductType = ''
		_state_machine.userdata.ProductPose = []
		_state_machine.userdata.Products = []
		_state_machine.userdata.NumberOfProducts = 0
		_state_machine.userdata.MaterialsLocationList = []
		_state_machine.userdata.MaterialLocation = ''
		_state_machine.userdata.MaterialLocationIndex = 0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.part_type1 = 'empty'
		_state_machine.userdata.part_type2 = 'empty'
		_state_machine.userdata.empty = 'empty'
		_state_machine.userdata.done = 'false'
		_state_machine.userdata.true = 'true'
		_state_machine.userdata.false = 'false'
		_state_machine.userdata.pose_on_agv1 = []
		_state_machine.userdata.pose_on_agv2 = []
		_state_machine.userdata.Zero = 0
		_state_machine.userdata.Minus = -1

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:84 y:253
			OperatableStateMachine.add('SetCountlimit',
										AddNumericState(),
										transitions={'done': 'GetProduct'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'NumberOfProducts', 'value_b': 'Minus', 'result': 'NumberOfProducts'})

			# x:892 y:34
			OperatableStateMachine.add('GetMaterialLocation',
										GetItemFromListState(),
										transitions={'done': 'product iterator_2', 'invalid_index': 'failed'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'MaterialsLocationList', 'index': 'MaterialLocationIndex', 'item': 'MaterialLocation'})

			# x:1161 y:108
			OperatableStateMachine.add('Orderverwerking',
										self.use_behavior(OrderverwerkingSM, 'Orderverwerking'),
										transitions={'finished': 'ResetPart1', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type1': 'part_type1', 'part_type2': 'part_type2', 'pose_on_agv1': 'pose_on_agv1', 'agv_id': 'agv_id', 'pose_on_agv2': 'pose_on_agv2'})

			# x:399 y:673
			OperatableStateMachine.add('ProductITerator',
										AddNumericState(),
										transitions={'done': 'GetProduct'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'ProductIterator', 'value_b': 'OneValue', 'result': 'ProductIterator'})

			# x:672 y:673
			OperatableStateMachine.add('CompareIterator',
										EqualState(),
										transitions={'true': 'check arm', 'false': 'ProductITerator'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'NumberOfProducts', 'value_b': 'ProductIterator'})

			# x:585 y:37
			OperatableStateMachine.add('GetMaterialsLocation',
										GetMaterialLocationsState(),
										transitions={'continue': 'GetMaterialLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'ProductType', 'material_locations': 'MaterialsLocationList'})

			# x:1391 y:708
			OperatableStateMachine.add('SetPart1',
										ReplaceState(),
										transitions={'done': 'CompareIterator'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'ProductType', 'result': 'part_type1'})

			# x:1327 y:31
			OperatableStateMachine.add('set arm1',
										EqualState(),
										transitions={'true': 'SetPose1', 'false': 'set arm2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'empty'})

			# x:671 y:461
			OperatableStateMachine.add('SetPart2',
										ReplaceState(),
										transitions={'done': 'GetProduct'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'ProductType', 'result': 'part_type2'})

			# x:1289 y:268
			OperatableStateMachine.add('set arm2',
										EqualState(),
										transitions={'true': 'SetPose2', 'false': 'Orderverwerking'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type2', 'value_b': 'empty'})

			# x:1012 y:262
			OperatableStateMachine.add('ResetPart1',
										ReplaceState(),
										transitions={'done': 'ResetPart2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'empty', 'result': 'part_type1'})

			# x:1010 y:360
			OperatableStateMachine.add('ResetPart2',
										ReplaceState(),
										transitions={'done': 'ResetPose1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'empty', 'result': 'part_type2'})

			# x:715 y:573
			OperatableStateMachine.add('check arm',
										EqualState(),
										transitions={'true': 'ResetIterator', 'false': 'done'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type1', 'value_b': 'empty'})

			# x:509 y:361
			OperatableStateMachine.add('done?',
										EqualState(),
										transitions={'true': 'ResetIterator', 'false': 'ProductITerator'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'done', 'value_b': 'true'})

			# x:1155 y:596
			OperatableStateMachine.add('done',
										ReplaceState(),
										transitions={'done': 'Orderverwerking'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'true', 'result': 'done'})

			# x:979 y:471
			OperatableStateMachine.add('SetPose2',
										ReplaceState(),
										transitions={'done': 'SetPart2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'pose_on_agv', 'result': 'pose_on_agv2'})

			# x:1454 y:327
			OperatableStateMachine.add('SetPose1',
										ReplaceState(),
										transitions={'done': 'SetPart1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'pose_on_agv', 'result': 'pose_on_agv1'})

			# x:748 y:373
			OperatableStateMachine.add('ResetPose1',
										ReplaceState(),
										transitions={'done': 'ResetPose2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'Zero', 'result': 'pose_on_agv1'})

			# x:754 y:269
			OperatableStateMachine.add('ResetPose2',
										ReplaceState(),
										transitions={'done': 'done?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'Zero', 'result': 'pose_on_agv2'})

			# x:283 y:59
			OperatableStateMachine.add('product iterator',
										MessageState(),
										transitions={'continue': 'GetMaterialsLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'ProductIterator'})

			# x:1134 y:23
			OperatableStateMachine.add('product iterator_2',
										MessageState(),
										transitions={'continue': 'set arm1'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'ProductIterator'})

			# x:138 y:480
			OperatableStateMachine.add('GetProduct',
										GetPartFromProductsState(),
										transitions={'continue': 'product iterator', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'Products', 'index': 'ProductIterator', 'type': 'ProductType', 'pose': 'pose_on_agv'})

			# x:502 y:551
			OperatableStateMachine.add('ResetIterator',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'Zero', 'result': 'ProductIterator'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
