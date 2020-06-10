#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_flexbe_behaviors.get_products_sm import Get_ProductsSM
from ariac_flexbe_states.notify_shipment_ready_state import NotifyShipmentReadyState
from flexbe_states.wait_state import WaitState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_states.message_state import MessageState
from ariac_flexbe_states.get_agv_status_state import GetAgvStatusState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Jun 04 2020
@author: Bas Jochems, Geert van der Meijden
'''
class GetShipmentsSM(Behavior):
	'''
	Regelt shipments
	'''


	def __init__(self):
		super(GetShipmentsSM, self).__init__()
		self.name = 'GetShipments'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Get_ProductsSM, 'Get_Products')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:291 y:423, x:814 y:225
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['Shipments', 'NumberOfShipments'])
		_state_machine.userdata.Shipments = []
		_state_machine.userdata.NumberOfShipments = 0
		_state_machine.userdata.Products = []
		_state_machine.userdata.NumberOfProducts = 0
		_state_machine.userdata.AgvId = ''
		_state_machine.userdata.ShipmentIndex = 0
		_state_machine.userdata.ShipmentType = ''
		_state_machine.userdata.ShipmentIterator = 0
		_state_machine.userdata.OneValue = 1
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.agv_ready_state = "ready_to_deliver"
		_state_machine.userdata.agv_state = ''
		_state_machine.userdata.Zero = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:55 y:39
			OperatableStateMachine.add('GetProducts',
										GetProductsFromShipmentState(),
										transitions={'continue': 'number of products', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'Shipments', 'index': 'ShipmentIterator', 'shipment_type': 'ShipmentType', 'agv_id': 'agv_id', 'products': 'Products', 'number_of_products': 'NumberOfProducts'})

			# x:600 y:38
			OperatableStateMachine.add('Get_Products',
										self.use_behavior(Get_ProductsSM, 'Get_Products'),
										transitions={'finished': 'NotifyShipmentReady', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'Products': 'Products', 'NumberOfProducts': 'NumberOfProducts', 'agv_id': 'agv_id'})

			# x:870 y:36
			OperatableStateMachine.add('NotifyShipmentReady',
										NotifyShipmentReadyState(),
										transitions={'continue': 'agv_busy', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'shipment_type': 'ShipmentType', 'success': 'success', 'message': 'message'})

			# x:1131 y:38
			OperatableStateMachine.add('agv_busy',
										WaitState(wait_time=8),
										transitions={'done': 'Shipment nr.'},
										autonomy={'done': Autonomy.Off})

			# x:1145 y:384
			OperatableStateMachine.add('ShipmentIterator',
										AddNumericState(),
										transitions={'done': 'Shipment nr._2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'ShipmentIterator', 'value_b': 'OneValue', 'result': 'ShipmentIterator'})

			# x:680 y:378
			OperatableStateMachine.add('CompareIterator',
										EqualState(),
										transitions={'true': 'ResetIterator', 'false': 'GetProducts'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'NumberOfShipments', 'value_b': 'ShipmentIterator'})

			# x:399 y:24
			OperatableStateMachine.add('number of products',
										MessageState(),
										transitions={'continue': 'Get_Products'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'NumberOfProducts'})

			# x:1171 y:283
			OperatableStateMachine.add('Shipment nr.',
										MessageState(),
										transitions={'continue': 'ShipmentIterator'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'ShipmentIterator'})

			# x:915 y:383
			OperatableStateMachine.add('Shipment nr._2',
										MessageState(),
										transitions={'continue': 'CompareIterator'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'ShipmentIterator'})

			# x:1346 y:166
			OperatableStateMachine.add('AGVstatus',
										EqualState(),
										transitions={'true': 'Shipment nr.', 'false': 'agv_busy'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_state', 'value_b': 'agv_ready_state'})

			# x:1378 y:49
			OperatableStateMachine.add('getAGVstatus',
										GetAgvStatusState(),
										transitions={'continue': 'AGVstatus', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'agv_state': 'agv_state'})

			# x:436 y:410
			OperatableStateMachine.add('ResetIterator',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'Zero', 'result': 'ShipmentIterator'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
