#===================================================
#07102015 by Roberto Carlos Reyes Fernandez @rctaptap
#====================================================

import boto.ec2
import codecs
regiones = ["us-east-1","us-west-1","us-west-2","ap-northeast-1","ap-southeast-1","ap-southeast-2","eu-central-1","eu-west-1","sa-east-1"]
for region in regiones:
	conn=boto.ec2.connect_to_region(region)	
	reservations = conn.get_all_instances()
	for res in reservations:		
		for inst in res.instances:
			if 'Use' in inst.tags:     
				if str(inst.tags['Use']) == 'bd':					
					volumes = conn.get_all_volumes(filters={'attachment.instance-id': inst.id})
					for vol in volumes:
						if 'Name' in vol.tags:
							if 'Name' in inst.tags:
								if "/var/lib/mysql" in vol.tags['Name']:
									descrip = inst.tags['Name']  + " " + vol.id + " " + vol.tags['Name'] + " "  + vol.attach_data.device
									descripcode = descrip.encode('ascii', 'ignore')
									volname = vol.tags['Name']
									volnamecode = volname.encode('ascii', 'ignore')
									instname = inst.tags['Name']
									instnamecode = instname.encode('ascii', 'ignore')
									snapshot = conn.create_snapshot(vol.id, descripcode)
									snapshot.add_tags({'Name': volnamecode, 'Server': instnamecode})
									print "%s (%s) [%s]" % (descripcode, snapshot.id , inst.region)
								if "/var/lib/mongo" in vol.tags['Name']:
									descrip = inst.tags['Name']  + " " + vol.id + " " + vol.tags['Name'] + " "  + vol.attach_data.device
									descripcode = descrip.encode('ascii', 'ignore')
									volname = vol.tags['Name']
									volnamecode = volname.encode('ascii', 'ignore')
									instname = inst.tags['Name']
									instnamecode = instname.encode('ascii', 'ignore')
									snapshot = conn.create_snapshot(vol.id, descripcode)
									snapshot.add_tags({'Name': volnamecode, 'Server': instnamecode})
									print "%s (%s) [%s]" % (descripcode, snapshot.id , inst.region)
