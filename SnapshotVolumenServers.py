#===================================================
#07102015 by Roberto Carlos Reyes Fernandez @rctaptap
#====================================================

import boto.ec2
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
							if "/var/lib/mysql" in vol.tags['Name']:
								print "%s (%s) [%s] [%s] [%s]" % (inst.tags['Use'], inst.id, vol.id, vol.tags['Name'], inst.region)
								#print "%s (%s) [%s] [%s]" % (inst.tags['Use'], inst.id, vol.id, inst.region)
								description = inst.tags['Name'] + " " + vol.id  + " " + vol.tags['Name']
								print description
							#snapshot = conn.create_snapshot()
							#snapshot.add_tags({'Name': vol.tags['Name'], 'Server': inst.tags['Name']})
