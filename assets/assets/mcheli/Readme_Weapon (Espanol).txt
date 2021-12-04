
2016/04/17

;***********************************************************************************
;■Archivos de configuración de armas armas /***.Txt, sonido/***_snd.ogg
;***********************************************************************************

;★Importante★
; Los archivos de configuración de armas se pueden volver a cargar incluso cuando Minecraft se está ejecutando.
; Sube al avión → Pantalla de suministro con la tecla R → MOD Option → Development → Reload All Weapons
; Esto recargará todas las armas, incluidas las armas móviles.

;Los siguientes 2 archivos son necesarios para aumentar las armas (todos deben estar en minúsculas)
; ・ Aumente el archivo de configuración de armas (txt) en la carpeta de armas
; ・ En la carpeta de sonido, aumente el sonido de uso (ogg) del mismo nombre que el archivo de configuración del arma + _snd
; Por ejemplo, armas / abc.txt y sound / abc_snd.ogg son necesarios para el arma abc.
; *Desde 0.9.4, los archivos de audio ya no son necesarios.

;Algunos parámetros numéricos tienen límites superior e inferior.

DisplayName = M134 Minigun
;Nombre mostrado *No utilice caracteres de ancho completo, solo caracteres alfanuméricos de medio ancho y símbolos

Type = MachineGun1
;Tipo de arma Puedes configurar una de las siguientes
;	MachineGun1	Ametralladora con orientación fija ... M134 etc.
;	MachineGun2	Una ametralladora orientada al punto de vista del jugador ... M230
;	Torpedo		Un torpedo que se dirige al objetivo bajo el agua cuando se cae al agua ... Mk46
;	CAS		Proporcionar apoyo aéreo cercano al punto objetivo ... A-10
;	Rocket		Cohete no guiado de dirección fija ... Hydra70 y SNEB68mm
;	ASMissile	Misiles volando a un punto objetivo en el suelo ... AGM119
;	AAMissile	Misiles que rastrean mobs en el aire ... AIM92
;	TVMissile	El misil permite al jugador controlar la orientación después del lanzamiento. ... AGM114[TV]
;	ATMissile	Misiles que rastrean mobs en el suelo ... AGM114
;	Bomb		Una bomba que cae abajo ... CBU-100
;	MkRocket	Un cohete que dispara en el punto de impacto. ... Hydra 70mm M264RP
;	Dummy		Arma inutilizable. Se usa para mostrar personajes en el campo de armas.
;	Smoke		Generar estelas ... Smoke white
;	Dispenser	Usa objetos en los puntos de impacto ... Water Dispenser(Till)
;	TargetingPod    Marcar mobs, puntos de jugador y bloques ... targeting_pod_block

Power = 8
;Daño

DamageFactor = tank, 2.0
;Multiplicador de daños
; Establezca uno de los siguientes en el primer parámetro
;  player : Jugador
;  heli または helicopter : Helicóptero
;  plane : Avión de ala fija
;  tank : Tanque o carro
;  vehicle : Armas de tierra
; El segundo parámetro establece el multiplicador de daño [0 ~]. Si 3.4 y Poder es 10, se hace 34 daños
; Esta configuración se refleja cuando se escriben varias líneas

Acceleration = 4.0
;Velocidad de bala (hasta 4.0 con algunas excepciones)
; Solo MachineGun1, MachineGun2, Rocket hasta 100.0

AccelerationInWater = 4.0
;Velocidad del torpedo bajo el agua (hasta 4.0)

VelocityInWater = 0.5
;Aceleración en el agua
; Bajo el agua, este valor se multiplica por la velocidad de cada tic.

Explosion = 0
;Poder de explosión al aterrizar (0 = sin explosión, 1 = poder de munición de ráfaga, 2 ~)
ExplosionInWater = 0
;Poder de explosión al aterrizar en el agua
ExplosionBlock = 0
;Bloquea el poder destructivo de la explosión al aterrizar. Si es 0, el bloque no se destruye.
ExplosionAltitude = 10
; Altura de explosión sobre el suelo
;Cuando se establece en 10, explota cuando está a menos de 10 m del suelo

DelayFuse = 30
;Espoleta retrasada: cuenta desde el impacto hasta la desaparición
; Explosion / ExplosionInWater explota cuando se extingue, si no 0

Bound = 0.4
;Fuerza de rebote en el impacto
; Cuando se usa Bound, si DelayFuse no está configurado, explotará inmediatamente después del impacto, por lo que no tiene sentido.

TimeFuse = 30
;Espoleta cronometrada: cuenta desde disparar hasta la bala desaparecida
; Si Explosion / ExplosionInWater no es 0, explotará cuando desaparezca

Flaming = false
;Si disparar o no la llama al aterrizar (falso = deshabilitar, verdadero = habilitar)
; * Válido solo cuando Explosión> 0

Sight = MoveSight or None or MissileSight
;Objetivos mostrados en la pantalla
;	MoveSight		Objetivo que se mueve de acuerdo con la dirección de la aeronave.
;	MissileSight	Tipo de objetivo que bloquea las turbas (requerido para AAMissile / ATMissile)

Zoom = 4.2, 9.2
; Configuración solo para armas móviles
; Ampliación sin alcance. Si establece múltiples separándolos con, y, puede cambiar con la tecla Z.

Group = MainGun
; Establecer un grupo de armas
; Usar cualquier grupo de la misma arma recargará todo
; Específicamente, divida las armas del arma principal del tanque por tipo de bala de la siguiente manera,
; Cuando Group = MainGun está configurado para tres de rehinmetall_apfsds.txt, rehinmetall_he.txt, canistershell.txt
; Usar uno recargará los otros dos. Las balas no disminuyen
;  Primero: rehinmetall_apfsds
;  Segundo: rehinmetall_he
;  Tercero: canistershell
; Esta es una configuración para evitar la acción de cambiar a la segunda arma inmediatamente después de usar la primera arma

Delay = 5
;Tiempo de espera hasta el próximo uso (en unidades de aproximadamente 1/20 segundos), cuanto más pequeño, más rápido

ReloadTime = 80
; Tiempo de espera para completar la recarga (unidad de 1/20 segundos), más pequeño es más rápido
; * Al establecer el tiempo de recarga en 0, establezca el número de disparos en un valor que no sea 0.

Round = 100
;Número de viñetas Establecer 0 cuando no se usa, o no enumera este parámetro en sí

SoundVolume = 3
;Volumen cuando se usa arma
; Establecer a 1.0 o superior en las especificaciones de Micra para un volumen máximo
; (Si desea bajar el volumen, hágalo menos de 1,0)
; Si excede 1.0, puede escuchar el sonido desde la distancia.

SoundPitch = 1.0
;tono del sonido (0.0 y 1.0)

SoundPitchRandom = 0.1
;Rango de cambio de tono al azar (0.0 a 1.0)
; En el ejemplo a continuación, el tono del sonido finalmente reproducido es de 0.6 a 0.8.
; SoundPitch = 0.8
: SoundPitchRandom = 0.2

SoundDelay = 1
; Tiempo de espera hasta que se emita el siguiente sonido al repetir la voz
Si no tiene esta configuración, M134 etc. repetirá demasiados sonidos y otros sonidos desaparecerán.

Sound = rocket_snd
;Especificar archivo de audio. No se requiere extensión
;Si no se especifica ningún archivo de audio con esta configuración, se usará el nombre del arma _snd.ogg.

LockTime = 20
;Es hora de bloquear misiles. Cuanto más grande se tarda, más se tarda en bloquearる。

RidableOnly = true
; Configuración para bloquear el reproductor solo mientras está a bordo

ProximityFuseDist = 1.0
;Distancia de funcionamiento de la espoleta de proximidad del misil de bloqueo
;Si especifica 1, explota dentro de 1 m

RigidityTime = 0
; Contando desde disparar misiles hasta comenzar a rastrear
;Si no se especifica, 7 se establece como el valor predeterminado

Accuracy = 1
; Error de bala o cohete no guiado. Cuanto mayor sea el valor, mayor será el error.

Bomblet = 25
;Después del uso, el número de submuniciones desplegadas. Utilizado para bombas de racimo, etc.
BombletSTime = 5
;Hora de desplegar sub-viñetas
BombletDiff = 0.7
;Tasa de propagación de submuniciones

ModeNum = 2
; Número de modos de arma que se pueden cambiar con la tecla X
; Solo se puede configurar con los siguientes tipos de armas
; Type = MachineGun2 → Cambie a bala HE (bala explosiva). Inválido si la explosión es 0.
; Type = TVMissile   → Cambiar a misil guiado normal (misil guiado no está en vista de misil)
; Type = ATMissile   → Cambia al modo TA (Top Attack) (después de subir frente al enemigo y luego hundirte)
; Type = Rocket      → Cambie a bala HEIAP (esparza múltiples sub-balas en el aire)
; Actualmente solo se pueden configurar 1 o 2。
; Si se omite, 1

Piercing = 2
; Número de penetraciones de bloque

HeatCount = 20
;La cantidad de calor que puede aumentarse con un solo uso de un arma de calorías tipo barril
MaxHeatCount = 150
;Límite superior de calor

FAE = true
;ENCENDIDO / APAGADO de la bomba de vaporización de combustible
;Se convierte en una bomba de vaporización de combustible con verdadero
;Las bombas de vapor de combustible no destruyen bloques

ModelBullet = bullet
ModelBomblet = cbc
; Especificación de archivo de modelo de bala
; En el caso anterior, se utilizan modelos / bullets / bullet.obj y textures / bullets / bullet.png.
; Los modelos / bullets / cbc.obj y textures / bullets / cbc.png se utilizan para las submuniciones de la bomba de racimo.

Destruct = true
El avión se autodestruye cuando se usa
Solo disponible cuando Tipo = Bomba.
Solo es efectivo si el avión es un helicóptero UAV.

Gravity = -0.04
GravityInWater = 0.0
; Velocidad de caída de la ojiva
; Cuanto mayor es el valor absoluto, más rápido cae
; GravityInWater es la velocidad de caída en el agua

GuidedTorpedo = true
;Configuración para cambiar el torpedo / torpedo no inducido
; Si se establece en verdadero, será un torpedo y una cabeza para el bloque especificado.
; Si se establece en falso, será un torpedo no guiado y procederá directamente desde donde cayó.

TrajectoryParticle = flame
; Especifique el efecto de "trayectoria" cuando use un arma específica (como partículas cuando un misil está rastreando)
; none          ...Sin efecto
; explode       ...Efecto de humo
; flame         ...Efecto de llama
; hugeexplosion ...Efecto de humo
; largeexplode  ...Efecto de humo
; largesmoke    ...Efecto de humo
; smoke         ...Efecto de humo
;
; Explicación detallada: dado que es una cadena que se establecerá en spawnParticle, se pueden especificar otras cadenas.
; Particle Se suprime de 1.0.0. Utilice AddMuzzleFlash o AddMuzzleFlashSmoke en su lugar.

TrajectoryParticleStartTick = 10
; Contar para el efecto de TrajectoryParticle comienza


DisableSmoke = true
; Desactiva el efecto de humo en ciertas armas
; (Efecto del humo producido al moverse, no efecto del disparo)


AddMuzzleFlash  =  0.5,             0.20,   1,        150,254,219,184
;AddMuzzleFlash = Distancia desde la fuente, tamaño, tiempo de visualización,  A,  R,  G,  B
; ★ ¡Precaución!: No use armas, ya que pueden no mostrarse correctamente si se usan alrededor de 5 veces.

AddMuzzleFlashSmoke  =  2.2,             1,       5.0,    2.0,  15,      180,250,245,240
;AddMuzzleFlashSmoke = Distancia desde la fuente, número de vistas, tamaño, rango, duración,  A,  R,  G,  B
; ★ ¡Precaución!: No use armas, ya que pueden no mostrarse correctamente si se usan alrededor de 5 veces.


SetCartridge = cartridge, 0.0, 0, 0, 2.00, -0.04, 0.40
; Configuración para soltar la carcasa vacía cuando se usa un arma
; SetCartridge = model_name, Acceleration, Yaw, Pitch, ModelScale, Gravity, Bound
; model_name   : Nombre del modelo Minúscula, mitad de tamaño
; Acceleration : Si la fuerza para volar es 0, cae directamente debajo
; Yaw          : Ángulo para volar lateralmente desde el arma (yaw) Valor positivo: izquierda, valor negativo: derecha
; Pitch        : Paso vertical visto desde el arma (Pitch) Valor positivo: Inferior, Valor negativo: Superior
; ModelScale   : Aumento de pantalla
; Gravity      : Fuerza de la gravedad
; Bound        : Fuerza de rebote al golpear un bloque


MaxAmmo = 40
; Número máximo de balas que puede contener el avión.
SuppliedNum = 10
; Número de municiones agregadas por un suministro de munición
Item =  3, iron_ingot
Item =  4, gunpowder
Item =  2, redstone
; Artículos y pilas necesarios para reponer (solo se pueden especificar lingotes de hierro, pólvora y piedra roja)

; MaxAmmo = 40
; SuppliedNum = 10
; Item =  3, iron_ingot
; Item =  4, gunpowder
; Item =  2, redstone
; En este ejemplo, una recarga consume 3 lingotes de hierro, 4 pólvora y 2 piedras rojas.
; Puedes reponer 10 disparos. Como puede reponer hasta 40 disparos,
; Consume 12 lingotes de hierro, 16 pólvora, 8 piedras rojas


BulletColor        = 255, 255, 255, 255
BulletColorInWater = 255,  25,  25,  75
; Configuración de color de viñeta (0 a 255). Alfa, rojo, verde, azul en orden desde el frente
; BulletColorInWater especifica el color bajo el agua.

SmokeColor  = 230, 200, 20, 80
; Configuración de color de humo (0 a 255). Alfa, rojo, verde, azul en orden desde el frente
SmokeSize   = 2.0
; El tamaño del humo
SmokeMaxAge = 500
; Tiempo de visualización de humo


DisplayMortarDistance = true
; Visualización de la distancia de aterrizaje

FixCameraPitch = true
; Fijar la cámara vertical a 0

CameraRotationSpeedPitch = 0.3
; Aumento de la velocidad de rotación de la cámara (cuanto más pequeño pueda ajustar finamente el punto de aterrizaje)



DispenseItem = flint_and_steel
; Use el artículo especificado al aterrizar
; Hay elementos que son efectivos y elementos que no lo son.
; No sé a menos que lo intente.
; Al establecer ↑, use piedras de pedernal en el punto de impacto
; La excepción no es colocar el agua en un cubo de agua
; Tiene el efecto de extinguir el fuego y el magma cerca del punto de impacto.

DispenseRange = 4
; Rango de uso del elemento especificado en DispenseItem (unidad: bloque)


Recoil = 1.1
; Fuerza de la sacudida de la aeronave cuando se usan armas


RecoilBufCount = 40, 5
; RecoilBufCount = Conteo de jubilación, multiplicador de conteo durante el retiro
;  Aumentar el recuento de residentes aumentará el tiempo total del residente
;  El aumento de la tasa de conteo durante la retirada solo acelerará la retirada.


Target = monsters/others
; Especifique el tipo de entidad para detectar o si marcar el bloque
; Puede especificar varias configuraciones de las siguientes. Al especificar más de uno, sepárelos con /
; La excepción es el bloque, y la especificación del bloque invalida otras especificaciones.
;
;  planes		Heli mod aviones de ala fija
;  helicopters		Helicóptero Mod Helicóptero
;  vehicles		Heli mod armas terrestres
;  players		Otros jugadores
;  monsters		Monstruo
;  others		Otras turbas
;  block		Se convierte en una función para marcar bloques. Ya no es una función puntual.

Length = 100
; Especifique la distancia para detectar
; La unidad es un bloque, y si es 15, está a una distancia de 15 bloques de una línea recta.

Radius = 45
; Especifique el tamaño del área de punto posible por ángulo
; Si 45, entonces el radio es de 45 grados

MarkTime = 10
; Especifique el tiempo de visualización del punto en segundos
; Si 10 entonces 10 segundos
