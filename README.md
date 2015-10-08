# SnapshotVolumenServersAWS
Genera un snapshot del volumen de todos los servidores de Base de datos como contingencia ante incidentes. 
## Instalación y requisitos
Se debe tener instalado el [SDK Boto AWS](https://aws.amazon.com/sdk-for-python/)

Los detalles de su configuración se pueden encontrar en [github](https://github.com/boto/boto3)

## Uso
Backup de volumenes de servidores de base de datos en Amazon Cloud Computing
## Detalles
Lista todas las regiones

 `regiones = ["us-east-1","us-west-1","us-west-2","ap-northeast-1","ap-southeast-1","ap-southeast-2","eu-central-1","eu-west-1","sa-east-1"]`

Se conecta a AWS

```
 for region in regiones: 
	conn=boto.ec2.connect_to_region(region)
```

Obtiene todas los servidores en base al ID Reservado

 `reservations = conn.get_all_instances()`
	
Para cada uno de ellos listaremos en base al ID de la instancia	

 ```
 for res in reservations:
 	for inst in res.instances:
```

Es posible obtener el valor del atributo Termination Protection

 `atri = conn.get_instance_attribute(inst.id,'disableApiTermination')`

Evaluamos si es falso

 `if str(atri) == "{u'disableApiTermination': False}":`	

Esta comparación solamente es para mostrar el resultado de forma ordenada

 ```
 if 'Name' in inst.tags: 
 	print "%s (%s) [%s] [%s]" % (inst.tags['Name'], inst.id, atri, inst.region)
else:
   	print "%s [%s] [%s]" % (inst.id, inst.state, atri, inst.region)
```

La modificación del valor de protección se realiza con este comando

 `inst.modify_attribute('disableApiTermination', True)	`
## Creditos
Roberto Carlos Reyes Fernández




