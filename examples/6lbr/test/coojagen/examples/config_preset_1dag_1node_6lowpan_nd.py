"""
Load a preset topology: preset-2dags-20nodes, which is 2 totally disjoint DODAGs with 10 nodes in each.
The first 2 nodes in the generated array are the ones meant to be use as slip-radio, so we assign them as such
"""

outputfolder = 'coojagen/output'
template = 'coojagen/templates/cooja-template-udgm-darko.csc'
radio_model = 'udgm'
tx_range = 45
tx_interference = 45
topology = 'preset'
#preset_data_path = 'coojagen/templates/preset_1dag_1router_2nodes'
preset_data_path = 'coojagen/templates/preset_1dag_2routers_2nodes'
mote_types=[]
multi_br=0

assignment = {'all':'node', '0':'slipradio', '1':'router', '2':'router'}

mote_type_slipradio = {	'shortname':'slipradio', 
			'fw_folder':'[CONTIKI_DIR]/examples/ipv6/slip-radio/', 
			'maketarget':'slip-radio', 
			'makeargs':'', 
			'description':"6LBR Slip Radio",
			'serial':'socket',
			'mote_type':'sky'  }

mote_type_6lowpan_nd_router = {	'shortname':'router', 
			'fw_folder':'/opt/contiki/contiki-darko/examples/6lowpan-nd-rpl', 
			'maketarget':'6lowpan-nd-router', 
			'makeargs':'', 
			'description':"6lowpan-nd router",
			'serial':'pty',
			'mote_type':'z1' }

mote_type_6lowpan_nd_node = {	'shortname':'node', 
			'fw_folder':'/opt/contiki/contiki-darko/examples/6lowpan-nd-rpl', 
			'maketarget':'6lowpan-nd-host', 
			'makeargs':'', 
			'description':"6lowpan-nd nodes",
			'serial':'pty',
			'mote_type':'z1' }

mote_types.append(mote_type_slipradio)
mote_types.append(mote_type_6lowpan_nd_node)
mote_types.append(mote_type_6lowpan_nd_router)