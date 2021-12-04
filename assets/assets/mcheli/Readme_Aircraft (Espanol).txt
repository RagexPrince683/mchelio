
2017/08/17

Traducido el 14/01/2020 (Con google traductor)


; ★ Importante ★
; Los archivos y modelos de configuración se pueden volver a cargar mientras se ejecuta Minecraft.
; [Conducir el avión → Tecla R para suministrar pantalla → Opción MOD → Desarrollo → Recargar configuración de avión]
; Recargar texturas y sonidos usando las funciones predeterminadas de Minecraft, no desde mods de helicóptero.
; [Tecla Esc: menú Juego → Configuración → Paquete de recursos → Listo]

; *******************************************************************************************************************
■ Configuración común de archivo de configuración de helicóptero / caza / arma terrestre / vehículo
; *******************************************************************************************************************

DisplayName = AH-6 Killer Egg
; Nombre mostrado * No utilice caracteres de doble byte, solo caracteres y símbolos alfanuméricos de byte único

AddDisplayName = ja_JP, AH-6 Killer egg
; Nombre mostrado al sostener el artículo
; * Cuando utilice caracteres japoneses de ancho completo, establezca el código de caracteres del archivo en UTF-8.

ItemID = 28801
; ID del artículo (utilizado como +256 en Minecraft)
; * ItemID no se usa después de 1.7.2, pero debe establecerse si corresponde a 1.6.4 o anterior

                    __________ A A A __________

AddSeat = -0.45,  0.80, 1.20
AddSeat =  0.45, -0.50, 1.20
AddSeat = -0.90, -0.50, 0.20
AddSeat =  0.90, -0.50, 0.20, verdadero
; Agregar un asiento * Debe haber al menos un asiento excepto UAV
El primero es el asiento del piloto.
; El parámetro es la posición (X, Y, Z)
El cuarto parámetro es si cambiar la posición del asiento de acuerdo con la orientación del piloto (principalmente la torreta del tanque)

AddTexture = sh60-us-1
AddTexture = sh60-jp-1
AddTexture = sh60-jp-2
; Textura (s) adicional (es)
; Por defecto, png con el mismo nombre que el nombre del archivo de configuración,
; Agregue otras texturas adicionales (no se necesita extensión).

AddTexture = sh60-us-1
AddTexture = sh60-jp-1
AddTexture = sh60-jp-2
; Textura (s) adicional (es)
; Por defecto, png con el mismo nombre que el nombre del archivo de configuración,
; Agregue otras texturas adicionales (no se necesita extensión)

AddGunnerSeat = -0.45, 0.80, 1.20, 0.0, 2.00, -1.01, verdadero
AddGunnerSeat = -0.45, 0.80, 1.20, 0.0, 2.00, -1.01, verdadero, -60, 78, verdadero
; AddGunnerSeat = Asiento X, Asiento Y, Asiento Z, Cámara X, Cámara Y, Cámara Z, punto de vista conmutable, Límite superior de la cámara (-90-0), Límite inferior de la cámara (0-90), Cambiar la posición del asiento para que coincida con la torreta
; Agregar un asiento
; Para los jugadores en los asientos agregados por AddGunnerSeat, el punto de vista se convierte en el punto de vista de la cámara
; (Si se establece en el asiento del piloto, no será el punto de vista de la cámara)
; Los parámetros son la posición del asiento (X, Y, Z) y la posición de la cámara
; La posición de la cámara se puede omitir. Si se omite, se utilizará la posición de CameraPosition.
; Omita el cambio de punto de vista o ajuste a falso solo el punto de vista de la cámara, ajuste a verdadero para cambiar al punto de vista del jugador con la tecla H
; El décimo parámetro es si cambiar la posición del asiento de acuerdo con la orientación del piloto (principalmente la torreta del tanque)

AddFixRotSeat = -0.45, 0.80, 1.20, 0.0,2.00, -1.01, verdadero, -50, 40
; AddGunnerSeat = Asiento X, Asiento Y, Asiento Z, Cámara X, Cámara Y, Cámara Z, punto de vista conmutable, ángulo fijo de cámara (horizontal), ángulo fijo de cámara (vertical)
; Agregar un asiento
Similar a AddGunnerSeat, excepto que la cámara está fija.
; Cuando se establece el ángulo fijo de la cámara, la posición de la cámara no se puede cambiar con el mouse. Puede cambiar a FreeLook con la tecla Ctrl.

; ★★★★★
; La función de carga de la aeronave
; ・ Especifique la aeronave a ser montada por el piloto (AddRack)
; ・ Especifique el número de bastidor de la aeronave en la que viaja el conductor (RideRack)
Habilitado si cualquiera está configurado.

AddRack = contenedor,                   0.0, 1.4, -4.7,  0.0, 1.0, -16.1
AddRack = contenedor / ah-64,           0.0, 1.4, -4.7,  0.0, 1.0, -16.1,  5.0, 20
AddRack = helicóptero / vehículo / t-4, 0.0, 1.4, -4.7,  0.0, 1.0, -16.1,  5.0, 100000, 0.0, 0.0
; ■ Esta es la configuración para el viaje
; AddRack =
; Param1: Nombre de la entidad a poner
; Param2 ~ 4: Coordenadas del bastidor X, Y, Z Especificar dónde colocar en el cuerpo
; Param5 ~ 7: Entrada del bastidor X, Y, Z Se puede cargar cuando la entidad que se va a cargar está cerca de esta coordenada. Desde aquí cuando lo dejes caer.
;: ↑ Por ejemplo, para AC-130 Especifique las coordenadas del bastidor dentro de la máquina y especifique la entrada del bastidor cerca de la escotilla trasera
; Param8: se puede omitir el rango (radio) desde la entrada Param8 y posterior
; Param9: altitud de apertura del paracaídas Si el valor es muy grande como en el ejemplo, el paracaídas no se abrirá
; Param10: ángulo horizontal de la entidad cargada
; Param11: ángulo vertical de la entidad cargada
; Agregue un estante que pueda transportar contenedores, helicópteros, etc. en la aeronave como mobs
El nombre de la entidad es una combinación de un contenedor, helicóptero, avión de ala fija, arma terrestre o nombre de avión. Separado por /
; contenedor contenedor
; helicóptero todos los helicópteros
; avión Todos los aviones de ala fija
; vehículo Todas las armas terrestres
; Especifique el nombre del avión directamente como ah-64, t-4, s-75

AddWeapon = m230,    0.00, 0.90, 2.54,  0.0, 0.0, verdadero, 2
AddWeapon = hydra70, 0.00, 0.90, 2.54,  0.0, 0.0, verdadero, 1, 0, -60,60, 0,25
AddWeapon = m134,    1.48, 0.40, 1.54,  1.0, 0.0
AddWeapon = m134,   -1.48, 0.40, 1.54, -1.0, 0.0
AddTurretWeapon = hydra70, 0.00, 0.90, 2.54, 0.0, 0.0, verdadero, 1, 0, -60,60, 0,25
; Agregar arma (Hacer coincidir el nombre del archivo sin la extensión de la carpeta de armas)
; Si registra la misma arma continuamente como m134,
; Tratar como un arma usada en orden desde dos lugares
; Parámetros en orden desde el nombre del archivo de configuración del Arma frontal, posición (X, Y, Z), ángulo de rotación (horizontal, vertical), disponibilidad del piloto, asiento, DefaultYaw, MinYaw, MaxYaw, MinPitch, MaxPitch
;
Los asientos son primero, primero, segundo, segundo, tercero y cuarto.
; Suplemento sobre la combinación "Disponibilidad de piloto, asiento"
; verdadero, 2 → Disponible para el 2º jugador. El piloto se puede usar cuando no hay un jugador en el segundo asiento.
; falso, 2 → Disponible para el 2º jugador. Piloto no disponible.
; falso, 1 → Solo se pueden usar pilotos (no recomendado)
; verdadero, 1 → piloto solo disponible
; Verdadero, 1 si se omite.
;
; DefaultYaw es la orientación predeterminada del arma y se ajusta al modelo
; MinYaw es un ángulo que permite que la aeronave se mueva en sentido antihorario desde DefaultYaw cuando se ve desde arriba.
; MaxYaw es el ángulo que puede moverse en sentido horario desde DefaultYaw cuando el avión se ve desde arriba.
; MinPitch es el ángulo que se puede mover hacia arriba
; MaxPitch es el ángulo que se puede mover hacia abajo
;
; AddTurretWeapon difiere de AddWeapon solo en que la posición de disparo cambia según la dirección de la torreta

AddSearchLight         =  0.71, -0.02, 0.02, 0x50FFFFFF, 0x10FFFFC0, 60.0, 20.0, 0, 0
AddFixedSearchLight    =  0.71, -0.02, 0.02, 0x50FFFFFF, 0x10FFFFC0, 60.0, 20.0, 0, 0
AddSteeringSearchLight = -0.52,  0.90, 1.76, 0x50FFFFFF, 0x00FFFFC0, 27.0, 15.0, 5, 0, 45
; AddSearchLight       = cordX, cordY,cordZ, color del punto inicial, color del punto final, distancia, radio final, guiñada, inclinación, ángulo de dirección
; AddSearchLight: una luz móvil que siempre ajusta su ángulo en la dirección que enfrenta el pasajero.
; AddFixedSearchLight: luz fija siempre orientada en la misma dirección
; AddSteeringSearchLight: una luz fija que siempre apunta en la misma dirección que la llanta. El ángulo de dirección debe ajustarse al ángulo de dirección del neumático.
; Yaw y Pitch son ángulo de luz de búsqueda, la luz fija y la luz móvil son efectivas

AddPartLightHatch = 0.32, 0.23, 1.83, -1,0, -0.024, 90
; AddPartLightHatch = coordenada X, coordenada Y, coordenada Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación -1800 a 1800
; Agregue una parte que se abra solo mientras el reflector esté ENCENDIDO.
Importante: se requiere AddSearchLight o AddFixedSearchLight

AddRecipe = "Y", "YXY", "YD", X, iron_block, Y, iron_ingot, D, tinte, 2
AddRecipe = "YXY", X, mcheli: ah-6, Y, redstone
AddShapelessRecipe = iron_block, iron_ingot, tinte, 2
; Agregue una receta (si se escriben más de 2 líneas de AddRecipe, aumentará el número de recetas)
; Los tres caracteres en "" indican una fila en el banco de trabajo.
; (Mismo formato que Forge's GameRegistry.addRecipe)
; Detalles del ejemplo anterior
; X = nombre del bloque de hierro
; Y = Nombre del artículo de lingote de hierro
; D = Nombre del elemento de tinte verde, si cambia por especificación de daño como tinte o poción, el daño será después del nombre del elemento
; El nombre del elemento solo debe especificar el nombre del siguiente sitio tal como está.
http://minecraft.gamepedia.com/Data_values
; Ejemplo: minecraft: iron_block.
; Para artículos / bloques de vainilla, minecraft: se puede omitir
; Al especificar un elemento MOD, se debe especificar el nombre MOD, como mcheli: ah-6
; Especificar con AddShapelessRecipe dará como resultado una receta irregular

ArmorDamageFactor = 0.5
; Coeficiente de daños a la aeronave
; 1.0 se reduce al 100%, 0.5 se reduce al 50%

ArmorMinDamage = 5
; Valor mínimo para tratar como daño
; No se tomarán daños menores a este valor

ArmorMaxDamage = 500
; Daño máximo
; El daño mayor que este se redondeará al valor especificado
Por ejemplo, si especifica 100 e intenta hacer 300 daños, el avión solo recibirá 100 daños

AddPartHatch = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180
; Agregue una compuerta que se pueda abrir y cerrar con la tecla Z.
; Nombre de archivo del modelo Nombre de unidad nombre_hatch.
;? Es un número secuencial a partir de 0
; El primer AddPartHatch es machine name_hatch0.obj
; El segundo AddPartHatch es machine name_hatch1.obj
; Si no se encuentra ningún modelo con este nombre de archivo, no se mostrará (si no se requiere visualización, no se requiere ningún modelo)

AddPartSlideHatch = Mover X, Mover Y, Mover Z
; Agregue una escotilla que se abra deslizándose
; Nombre del archivo del modelo (común para rotación / deslizamiento) Nombre del avión_hatch? .Obj (Consulte AddPartHatch para conocer las reglas de denominación)

AddPartCamera = Coordenadas X, Y, Z, Yaw vinculado, Pitch vinculado
; Agrega partes que siempre estén de cara al jugador.
Si hay mobs en el segundo asiento, recurra a los mobs en el segundo asiento.
; Nombre del archivo del modelo Nombre_cámara de la aeronave? .Obj (Consulte AddPartHatch para conocer las reglas de nomenclatura)

AddPartRotation = 0.00, 9.00, -31.17, 0, -1,0, 1.3, falso
; AddPartRotation = posición X, Y, eje de rotación Z X, Y, velocidad de rotación Z, si rotar siempre
; Agregue partes que giran a intervalos regulares

AddPartWeapon        = m230,       falso, verdadero, verdadero, -2.51, 1.29, -1.51
AddPartWeapon        = m102_105mm, falso, verdadero, verdadero, -2.51, 1.29, -1.51, 1.00
AddPartWeapon        = rehinmetall_apfsds / rehinmetall_he, false, true, false, 0.00, 2.10, 0.00, 0
AddPartTurretWeapon  = mg7_62mm,   falso, verdadero, verdadero, -0.83, 3.39, -0.57, 0
AddPartRotWeapon     = m134_r50,   falso, verdadero, verdadero, -1.825, 1.475, -0.25, 1,0,0
AddPartWeaponChild   = falso, verdadero, 0.00, 0.5, 3.00
AddPartWeaponMissile = aim120,     falso, falso, falso, -2.51, 1.29, -1.51
; Ajuste de piezas de armas para helicópteros y cazas
; AddPartWeapon = Nombre del arma vinculado (ninguno si ninguno), oculto cuando artillero? , Enlace de guiñada, enlace de paso, coordenadas de rotación X, Y, Z, distancia de estacionamiento
; AddPartRotWeapon = Nombre del arma vinculada (ninguna si no hay ninguna), oculta cuando artillero? , Enlace de guiñada, enlace de paso, coordenadas de rotación X, Y, Z, ejes de rotación X, Y, Z
; AddPartWeaponChild = Enlace de guiñada, enlace de tono, coordenadas de rotación X, Y, Z
; El ángulo cambia según el arma agregada por AddWeapon. Puede configurar varios nombres de armas separados por /
El rango de ángulo del arma también sigue al arma agregada con AddWeapon.
; La distancia de retirada es la distancia a la que se retira el arma
; AddPartRotWeapon es para recoger y rotar cuando se usa un arma
; Nombre del archivo del modelo Nombre del avión nombre_ama? .Obj (Consulte AddPartHatch para conocer las reglas de nomenclatura)
;
; AddPartWeaponChild se puede agregar como una pequeña parte de AddPartWeapon.
; Escriba en la línea que sigue a AddPartWeapon.
; Puedes agregar múltiples partes como las pequeñas partes de las armas terrestres.
; Nombre del archivo del modelo nombre_maquina_arma? _0.obj (? Es el número de pieza principal)
; El nombre del arma vinculada y la no exhibición del artillero serán los mismos que los de la parte principal.
;
; AddPartWeaponMissile está oculto después del uso del arma hasta que pueda usarse.
Utilizado para misiles y bombas, por ejemplo.
;
; La posición de visualización de AddPartTurretWeapon cambia a medida que gira la torreta. De lo contrario, lo mismo que AddPartWeapon

AddPartWeaponBay = Nombre del arma, posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180
; Se agregó un compartimento para armas que gira y se abre
AddPartSlideWeaponBay = Nombre del arma, Movimiento X, Movimiento Y, Movimiento Z
; Bahía de arma agregada que se abre deslizando
; Nombre del archivo del modelo (común para rotación / deslizamiento) Nombre del avión_wb? .Obj
; Nombre del archivo del modelo Nombre de la unidad_wb? .Obj (Consulte la escotilla para la convención de nomenclatura)

AddPartCanopy = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180
; Toldo agregado que gira y se abre
AddPartSlideCanopy = Mover X, Mover Y, Mover Z
; Toldo de apertura deslizante agregado
; Nombre del archivo del modelo (común para rotación / deslizamiento) Nombre del avión nombre_capía? .Obj
; Canopy se puede agregar varias veces
; Nombre del archivo del modelo nombre_equipo_capina? .Obj (consulte la sección de sombreado para la convención de nomenclatura)
; Si la parte numérica se omite solo para el dosel por compatibilidad, se tratará como el nombre del avión _canopy0.obj.

AddPartThrottle = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación (0 a 180), cantidad de movimiento X, cantidad de movimiento Y, cantidad de movimiento Z
; Agregue partes que giran / se mueven junto con el acelerador
; Requerido hasta el ángulo de rotación

AddPartLG = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180 [, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180]
AddPartLGRev = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180 [, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180]
AddPartSlideRotLG = Cantidad de movimiento X, Cantidad de movimiento Y, Cantidad de movimiento Z, Posición X, Posición Y, Posición Z, Eje de rotación X, Eje de rotación Y, Eje de rotación Z, Ángulo de rotación de 0 a 180
AddPartLGHatch = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180 [, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180]
; Agregar tren de aterrizaje
; Implementar / almacenar automáticamente en el despegue
; Nombre del archivo del modelo Nombre de la unidad_lg? .Obj (consulte la escotilla para la convención de nomenclatura)
; La operación de AddPartLGRev es opuesta a la de AddPartLG.
; AddPartLGHatch se abre solo cuando el equipo está plegado o desplegado.
;
; AddPartLG ... engranaje plegado 0 → 90
; AddPartLGRev ... cuando el equipo está plegado 90 → 0
; AddPartSlideRotLG ... Cuando el engranaje está plegado 0 → 90
; AddPartLGHatch ... cuando el equipo está plegado 0 → 90 → 0

AddTrackRoller = -1.72, 0.77, 5.04
; Agregue una rueda. El ajuste son solo las coordenadas. Si el eje X es un valor negativo, estará en el lado derecho, si es un valor positivo, estará en el lado izquierdo
; Se mueve de la misma manera que el rastreador, pero se puede configurar sin rastreador

AddCrawlerTrack = falso, 0.37, -2.09, 1.03 / -3.41, 0.72 / -3.57, 0.37 / -3.42, -0.15 / -2.55, -0.25 / -2.16, -0.25 / 3.88, -0.13 / 4.21, 0.52 / 5.29, 0.78 / 5.39, 1.03 / 5.28, 1.10 / 5.04, 1.15 / -3.12
; AddCrawlerTrack = Retroceso de pista, espaciado de pista, posición X de pista, punto de rotación de pista Y / Z, punto de rotación de pista Y / Z, punto de rotación de pista Y / Z, ...
Si la pista se da vuelta o la pista se mueve de manera extraña, se puede arreglar estableciendo "Track reverse" en verdadero o falso.
Nota: Falso cuando el punto de rotación de la pista se establece en el sentido de las agujas del reloj como se ve desde el lado izquierdo del tanque, y verdadero cuando lo contrario es cierto.
Funciona sin ruedas.
; Cuando ingresas al modo de prueba en el juego, la posición especificada se muestra como un punto rojo a un punto azul.

AddPartWheel = -1.05, 0.157, 1.965, 30
; Agregue la coordenada X del neumático, la coordenada Y, la coordenada Z, el ángulo de dirección
AddPartWheel = 0.68, 0.19, 1.20, 30, 0.0, 1.0, 0.2, 0.68, 0.19, 0.70
; Agregue la coordenada X del neumático, la coordenada Y, la coordenada Z, el ángulo de dirección, el eje de rotación X, Y, Z, la posición de rotación X, Y, Z
; El ángulo del timón es el ángulo máximo del eje Y del neumático al girar
; Omitiendo usos del eje de rotación (0,1,0)

AddPartSteeringWheel = -0.54, 0.88, 0.48, 0.0, 1.0, -1.7, 130
; Agregue el controlador de coordenadas X, coordenadas Y, coordenadas Z, eje de rotación X, eje Y, eje Z, ángulo de rotación máximo

AmmoSupplyRange = 35
; Configuraciones para reabastecer municiones a otras aeronaves
Reabastecer municiones a todos los aviones en esta área. 35m en el ejemplo anterior
; Reponer otras aeronaves no reduce su munición
; Sin embargo, no se puede suministrar a la propia aeronave

AutoPilotRot = -0.4
; Ángulo durante el giro automático. Cuanto mayor sea el valor, mayor será la cantidad de rotación.
; Si se establece en 0, siga recto.
Un valor negativo gira a la izquierda; un valor positivo gira a la derecha.


                    __________ B B B __________


BoundingBox = centro de juicio de colisión X, centro de juicio de colisión Y, centro de juicio de colisión Z, ancho de juicio, altura de juicio, aumento de daños
; Añadir detección de colisión
; Golpea solo ametralladoras y misiles MOD
; No golpea bloques o entidades
; Aparece al activar TestMode desde Config o la Opción MOD en el juego
; El multiplicador de daño es 1.0 si no especifica el multiplicador de daño
; Ejemplo de multiplicador de daño: 0.5 recibirá la mitad del daño, 3.0 recibirá el daño triple


                    __________ C C C __________


Categoría = W.A
; Establecer categoría de aeronave.
; Se usa solo para ordenar pestañas creativas.

CanMoveOnGround = falso
CanRotOnGround  = falso
; Si es falso, prohibir el movimiento y la rotación en el suelo
; CanMoveOnGround prohíbe el movimiento en el suelo
; CanRotOnGround prohíbe la rotación en el suelo

CreativeOnly = true
; Solo el jugador creativo puede instalar y detallar.

CameraZoom = 3
; Zoom máximo de la cámara

CameraPosition = 0.0, 1.1, 3.7
CameraPosition = 0.0, 1.1, 3.7, falso
CameraPosition = 0.0, 1.1, 3.7, verdadero, 30, 45
; Coordenadas de la cámara
; Si configura múltiples, puede cambiar el punto de vista con la tecla H
; Coordenadas 1,2,3
; Si el cuarto ajuste es verdadero, siempre será el punto de vista de la cámara
; Quinto ángulo horizontal
; Sexto ángulo vertical

CanRide = falso
; Configuraciones para evitar subir al avión
; verdadero = andar en avión (predeterminado)
; falso = no puede viajar en el avión

ConcurrentGunnerMode = true
; Puedes ingresar al modo Artillero incluso si tienes un jugador en el segundo asiento.


                    __________ D D D __________


DamageFactor = 0.2
; Factor de daño cuando el jugador recibe daño
; Si se especifica 0.2, el daño se reduce al 20% del daño original
Independientemente de esta configuración, el daño recibido por el jugador también es recibido por el avión.


                    __________ E E E __________


EnableGunnerMode = true
; Si cambiar el modo artillero (verdadero = Sí, No falso)

EnableNightVision = true
; Si cambiar la visión nocturna (verdadero = sí, no falso)

EnableEntityRadar = false
; Presencia de radar (verdadero = sí, no falso)

ExclusionSeat = 15, 17
; El parámetro se puede configurar hasta dos o más
; Establecer exclusión entre asientos o bastidores especificados
; Esto también funciona para bastidores, de modo que si un contenedor está en un bastidor determinado, es posible realizar ajustes como no cargar el avión.
;
; Por ejemplo, ExclusionSeat = 3, 4, 5
; Si la mafia está en el tercer asiento, la mafia no puede estar en el cuarto y quinto asiento
;Además, si hay mobs en el 4to asiento, los mobs no pueden estar en el 3er y 5to asiento
:Del mismo modo, si hay mobs en el quinto asiento, los mobs no pueden estar en el tercer y cuarto asientos.
;
; Los números de asientos / estantes se asignan en el orden de todos los asientos y luego los estantes restantes
; Ejemplo: Número cuando el asiento o estante se configura en el archivo de configuración de la siguiente manera
; AddSeat ← 1
; AddRack ← 4
; AddGunnerSeat ← 2
; AddRack ← 5
; AddSeat ← 3
; AddRack ← 6
Como puede ver en este ejemplo, los números son más fáciles de entender si coloca el estante después de cada asiento

EntityWidth = 0.9
EntityHeight = 0.9
; Establezca el tamaño de dibujo (ancho y alto) de los mobs en los que está montando
; Rango es -100.0 a 0.0 a 100.0
; 0.5 reducirá el tamaño a la mitad

EntityPitch = 45
EntityRoll = 20
; Establecer el ángulo (-360 a 360) al dibujar las turbas a bordo

EnableParachuting = true
; Establecer en verdadero para permitir el descenso en paracaídas.
; Solo puedes dejar la mafia después del 3er asiento. Los jugadores después del 3er pueden usar la tecla espacio para soltar


                    __________ F F F __________


FuelConsumption = 0,5
; Combustible consumido por segundo
; Tiempo de vuelo [seg] = capacidad de combustible / combustible consumido por segundo
; 1200 segundos = 600 / 0.5

FlareType = 1
; Presencia de llamarada
; 0 = ninguno
; 1 = Sí
; 2 = Bengala para aviones grandes
; 3 = extendido horizontalmente
; 4 = extendido al frente
; 5 = extendido hacia abajo
; 10 = descargador de humo para tanques

Flotador = verdadero
; Flotando en el agua

FloatOffset = -1.0
; Desplazamiento de altura cuando flota en el agua (valores negativos permitidos)

FuelSupplyRange = 25
; Configuraciones para repostar otras aeronaves
; Repostar todos los aviones en esta área. 25m en el ejemplo anterior
; El reabastecimiento de combustible de otros aviones no reduce su propio combustible
; Sin embargo, no se puede suministrar a la propia aeronave


                    __________ G G G __________


Gravedad = -0.04
; Establecer la gravedad aplicada a la aeronave
; Caer con valor negativo

GravityInWater = -0.04
; Establecer la gravedad aplicada a la aeronave en el agua
; Caer con valor negativo


                    __________ H H H __________


HUD = heli, heli_gnr, none, gunner
; Nombre de archivo de configuración de HUD utilizado para cada asiento
; En el ejemplo, el piloto es heli.txt, el segundo heli_gnr.txt, el tercero no tiene HUD y el cuarto es gunner.txt.
; Además, si el número de asientos se establece más pequeño que el número de asientos, los asientos omitidos tendrán la siguiente configuración predeterminada.
; Si no se proporciona esta configuración, las siguientes configuraciones se utilizan de forma predeterminada.
; Helicóptero       : HUD = heli,    heli_gnr, gunner, gunner, gunner, gunner ...
; Avión de ala fija : HUD = plane,   plane,    gunner, gunner, gunner, gunner ...
; Arma terrestre    : HUD = solo vehículo
;
; * Asiento piloto solamente, use la configuración HUD del segundo asiento en modo Artillero
; Incluso para aeronaves de un solo asiento, las aeronaves con el Modo Artillero habilitado deben tener un segundo asiento.
; HUD = heli, heli_gnr

HideEntity = false
; Establecer si ocultar al jugador que monta
; verdadero = ocultar
; falso = mostrar


                    __________ I I I __________


Invulnerable = true
El avión se vuelve invencible.
Úselo para armas de defensa multijugador.

InventorySize = 18
; Tamaño del inventario de la aeronave (debe ser un múltiplo de 9)


                    __________ M M M __________


MaxHP = 100
; Resistencia

MaxFuel = 600
; Capacidad de combustible

MotionFactor = 0.96
Un valor de desaceleración de la velocidad de desplazamiento de la aeronave. El rango es de 0.0 a 1.0, cuanto menor es la velocidad, menor es la velocidad y menor es la velocidad.
El valor predeterminado es 0.96, y un ligero cambio en el valor es efectivo.

MobilityYaw
MobilityYawOnGround
; Cuanto mayor sea la rotación lateral de la aeronave, mejor será la movilidad
; MobilityYawOnGround solo afecta el suelo. No tiene efecto sobre el agua.
MobilityRoll
; La cantidad de rotación del rollo del fuselaje, cuanto más grande, más rápido es el rollo
MobilityPitch
; Cuanto mayor sea la rotación vertical de la aeronave, mayor será la movilidad, mayor será el ángulo de elevación del arma terrestre
MinRotationPitch
MaxRotationPitch
; Rango MinRotationPitch -80 a 0
; Rango MaxRotationPitch   0 a 80
; Límite de rotación vertical de la aeronave (mínimo / máximo)
; * Helicópteros y cazas tienen restricciones de desplazamiento cuando esta configuración está habilitada

MinRotationRoll
MaxRotationRoll
; Límite de rotación de la aeronave (mínimo / máximo)
; Rango MinRotationRoll -80 a 0
; Rango MaxRotationRoll   0 a 80
; * Helicópteros y cazas tienen rotación vertical limitada cuando esta configuración está habilitada

MobDropOption = 0.0, 0.0, -11.5, 10
; MobDropOption = posición de descenso X, posición de descenso Y, posición de descenso Z, intervalo de descenso (1/20 segundo)
; Opciones adicionales al soltar mobs


                    __________ O O O __________


OnGroundPitch = ángulo de rotación
; Especifique el ángulo de elevación cuando esté en el suelo.
; Aviones como Zero Fighter están ligeramente arriba cuando están en tierra


                    __________ P P P __________


PartWheelRot = 40
; Velocidad de rotación del neumático, más grande, más rápido

ParticlesScale = 0.1
; Cambiar el tamaño del efecto como el humo de arena 0.1
; Cuanto mayor sea el tamaño, mayor será el tamaño.


                    __________ R R R __________


RideRack = c5, 1
; ■ Esta es la configuración para el piloto
; RideRack = Nombre del piloto, número de rack (1 ~)
; Establecer al conducir otro avión

Regeneration = true
; Mob después del segundo asiento se recupera automáticamente

RotorSpeed = 50.0
; La velocidad de rotación de la cuchilla; Cuanto más grande, más rápido.
; Los valores negativos dan como resultado una rotación inversa, pero no se recomienda el uso de valores negativos.


                    __________ S S S __________


Speed = 0.6
; Cuanto mayor sea la velocidad de la aeronave, más rápido

StepHeight = 2.5
; Especifique la altura del bloque que se puede superar

SubmergedDamageHeight = 2
; Sin daños al tocar agua hasta la altura especificada
; Si 2 entonces no hay daño hasta 2 bloques

Sonido = heli
; Especifique el nombre del archivo de audio cuando se acelere
; En este ejemplo, se carga sonidos / heli.ogg

Stealth = 0.5
; Configuración de sigilo (0.0 a 1.0).
; Predeterminado = 0.0
; Más grande para bloquear misiles
Un tiempo de bloqueo más largo y una distancia de bloqueo más corta.

SmoothShading = false
; Activar / desactivar sombreado suave
; Si se establece en falso, el sombreado plano no se completará para las esquinas
; Si es verdadero, habilite el sombreado suave para mostrar las esquinas suavemente
; Si SmoothShading de mcheli.cfg es falso, todos los aviones tendrán un sombreado plano


                    __________ T T T __________


ThirdPersonDist = 12
; Especifique la distancia predeterminada para la vista en tercera persona.
; En Helicopter MOD, se recomienda un múltiplo de 4 para cambiar la distancia en 4 bloques con PageUp / Down

TrackRollerRot = 30
; Velocidad de rotación de la rueda rodante: si se establece en un valor inferior a 0, debe producirse una rotación inversa

ThrottleUpDown = 1.0
ThrottleUpDownOnEntity = 2.0
; Acelerador arriba / abajo coeficiente
; Cuanto más pequeño es, más difícil es subir el acelerador y más tiempo tarda en despegar
;
; ThrottleUpDownOnEntity es el factor acelerador arriba / abajo cuando el avión está en otra entidad (predeterminado 2.0)
El siguiente cálculo cuando el avión está en otra entidad
; ThrottleUpDown * Velocidad de la entidad a bordo * ThrottleUpDownOnEntity-> Facilidad de aceleración
; Ejemplo: ThrottleUpDownOnEntity = 2.0 y poner en el carro principal, la velocidad máxima es de aproximadamente 1.7,
; 1.7 * 2.0 = 3.4, es decir, puede despegar a una distancia de aproximadamente 1/3

TargetDrone = verdadero
Válido solo para luchadores. Si se establece en verdadero, el avión se convertirá en un avión objetivo no tripulado y no podrá subirse al asiento del piloto.
; La generación desde otra estación que no sea UAV está desactivada.
; Vuela automáticamente a la altitud más baja cuando se genera y sigue girando

TurretPosition = 0.0, 0.0, 0.25
; Posición central de rotación de la torreta
; Se desaconseja el uso de esta configuración. Si es posible, es deseable que las coordenadas X y Z de la posición de rotación de la torreta sean cero.


                    __________ U U U __________


UAV = true
SmallUAV = true
; Si se establece en verdadero, el avión no estará tripulado y no podrá entrar en los asientos de piloto.
; La creación y operación desde otra estación que no sea UAV no será posible.
; Cuando UAV = true: se trata como un UAV grande y no se puede controlar desde un terminal de control de UAV móvil.
; Cuando SmallUAV = true: se trata como un UAV pequeño y se puede controlar desde un terminal de control de UAV portátil.
Nota: Las estaciones UAV pueden controlar todos los UAV, independientemente de su tamaño.
Los terminales de control de UAV móviles solo pueden controlar UAV pequeños.

UnmountPosition = 3.0, 1.0, -2.0
; Coordina al bajar del avión



;**************************************************************************************************************************************************************
■ Archivo de configuración del helicóptero helicopters / abc.txt, models / helicopters / abc.obj, textures / helicopters / abc.png, textures / items / abc.png
;**************************************************************************************************************************************************************

; Los siguientes 4 archivos son necesarios para aumentar las armas terrestres (todo en minúsculas)
; ・vehicles           Archivo de configuración de arma terrestre en carpeta
; ・models/vehicles    Modelo de arma de tierra en carpeta
; ・textures/vehicles  Archivo de textura de arma de tierra en carpeta
; ・textures/items     Archivos de textura para elementos en carpetas

AddPart = Param1, Param2, Param3, Param4, Posición X, Posición Y, Posición Z                 Display: Palabra en inglés que puede significar "monitor" o "mostrar"
; Agrega partes que giran con el jugador
; Param1 = Si se oculta en la vista en primera persona true = display, false = no display
; Param2 = rotar horizontalmente de acuerdo con el jugador verdadero = rotar, falso = no rotar
; Param3 = rotar verticalmente según el jugador o no verdadero = rotar, falso = no rotar
; Param4 = Tipo de pieza, 0 = Normal (sin función), 1 = Girar cuando se usa un arma, 2 = Emboscada cuando se usa un arma
; Nombre de archivo del modelo Nombre de unidad nombre_parte.
AddChildPart = Param1, Param2, Param3, Param4, Posición X, Posición Y, Posición Z
; Partes para agregar a AddPart
; Debe agregarse después de AddPart. Los parámetros son los mismos que para AddPart.
; Esta parte tiene una convención de nomenclatura especial.
; Nombre del archivo del modelo Nombre de la unidad parte_ _ #. Obj
; Es necesario agregar _ # al modelo agregado por AddPart (# es un número secuencial que comienza desde 0)
; Ejemplo
; AddPart = verdadero, verdadero, falso, 0, 0.00, 0.00, 0.00 → Nombre del avión_parte0.obj
; AddChildPart = falso, falso, verdadero, 0, -1.00, 0.00, 2.00 → Nombre del avión_parte_0.0j
; AddChildPart = falso, falso, verdadero, 0, 1.00, 0.00, 2.00 → Nombre del avión_parte0_1.obj

; No utilice RotationPitchMax y RotationPitchMin porque son configuraciones antiguas.



; ************************************************************************************************************************************************
■ Archivo de configuración de luchador planes / abc.txt, modelos / planos / abc.obj, texturas / planos / abc.png, texturas / elementos / abc.png
; ************************************************************************************************************************************************

; Los siguientes cuatro archivos son necesarios para aumentar el número de luchadores (todos deben estar en minúsculas)
; ・planes          Archivo de configuración del luchador en la carpeta
; ・models/planes   Modelo de luchador en carpeta
; ・textures/planes Archivo de textura de luchador en carpeta
; ・textures/items  Archivos de textura para elementos en carpetas

AddPartRotor = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación (-180 a 180)
; Agregar rotor
; No hay rotación cuando se acelera el acelerador. Gira durante VTOL.
; Nombre de archivo del modelo nombre_máquina_toror? .Obj (consulte la escotilla para la convención de nomenclatura)
; (No es necesario preparar un modelo para un avión que no sea Osprey)

AddBlade = número de cuchillas dibujadas, ángulo entre cuchillas, posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z
; Debe agregarse después de AddPartRotor.
; Cada pala del rotor
; Nombre del archivo del modelo Nombre_avión_blade? .Obj (Consulte la escotilla para la convención de nomenclatura)

AddPartWing = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180
; Añadir ala plegable
; Nombre del archivo del modelo Nombre de la aeronave nombre_ala? .Obj (Consulte la escotilla para la convención de nomenclatura)

AddPartPylon = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180
; Pilón de ala plegable agregado
; Nombre del archivo del modelo Nombre de la aeronave _wing? _Pylon? .Obj (vea la escotilla para la convención de nomenclatura)
; Debe haber AddPartWing antes de AddPartPylon.
; Ejemplo
; AddPartWing  = 1.50, 2.50, -4.57, 0,  1,0, 35 Nombre del modelo en este caso: Nombre del avión_wing0.obj
; AddPartPylon = 6.69, 2.50, -7.18, 0, -1,0, 35 Nombre del modelo en este caso: Nombre del avión_wing0_pylon0.obj
; AddPartPylon = 3.92, 2.50, -6.34, 0, -1,0, 35 Nombre del modelo en este caso: Nombre del avión_wing0_pylon1.obj

PivotTurnThrottle = 0.0
; La cantidad de movimiento al girar en el suelo
; Establecer en 0 para rotar en el lugar, establecer en un valor mayor que 0 para moverse durante la rotación
; Si es un tanque, configure de la siguiente manera.
; En el caso de super pivot, = 0
; Para giro de pivote = Establecer un valor mayor que 0

EnableBack = true
; Retráctil

VariableSweepWing = true
SweepWingSpeed ​​= 1.2
; Configuración de ala variable
; Válido solo cuando se agrega un ala que se puede plegar con AddPartWing
; VariableSweepWing = true Las alas se pueden plegar en el aire
; SweepWingSpeed ​​= 1.2 Velocidad cuando el ala principal está plegada

AddPartNozzle = posición X, posición Y, posición Z, eje de rotación X, eje de rotación Y, eje de rotación Z, ángulo de rotación de 0 a 180
; Añadir boquilla de avión de combate
; Efecto de humo cuando se aumenta el acelerador
; Rotar en VTOL
; Nombre de archivo del modelo Nombre de unidad nombre_nozzle? .Obj (Consulte la escotilla para la convención de nomenclatura)
; El efecto de humo de la boquilla se puede cambiar de tamaño con ParticlesScale

EnableVtol = true
; Función VTOL (falso = sin función VTOl, verdadero = VTOl disponible)
DefaultVtol = true
; Estado VTOL predeterminado con función VTOL
; Cuando se establece en verdadero, ingresa automáticamente al estado VTOL cuando está en el suelo
VtolYaw = 0.3
; Cantidad de rotación horizontal en estado VTOL
VtolPitch = 0.3
; Rotación del ángulo de elevación en estado VTOL

EnableEjectionSeat = true
; Asiento existente
; Si se establece en verdadero, se agregará un asiento de expulsión a la GUI.
Un asiento para un asiento y dos asientos para dos asientos.

AddParticleSplash = 1.0, 0.97, 13.19, 3, 9.0, 1.1, 20, 0.30, -0.03
; AddParticleSplash = coordenadas X, Y, Z, número de pantalla, tamaño, velocidad, tiempo de pantalla, ascenso, gravedad
; Salpica cuando se mueve sobre el agua
; No está relacionado con EnableSeaSurfaceParticle. Las partículas se generan incluso si es falso.

EnableSeaSurfaceParticle = true
; Ya sea para generar salpicaduras al volar "en el mar"
Está relacionado con ParticlesScale, y cuanto mayor sea el tamaño, mayor será el rango y el tamaño. (Se recomienda aproximadamente 0.7)
; Tenga en cuenta que no tiene nada que ver con AddParticleSplash



; ****************************************************************************************************************************************
■ Archivo de configuración del vehículo tanks / abc.txt, models / tanks / abc.obj, textures / tanks / abc.png, textures / items / abc.png
; ****************************************************************************************************************************************

; Los siguientes cuatro archivos son necesarios para aumentar el número de vehículos (todos deben estar en minúsculas)
; ・tanks          Archivo de configuración del vehículo en la carpeta
; ・models/tanks   Modelo de vehículo en carpeta
; ・textures/tanks Archivo de textura del vehículo en la carpeta
; ・textures/items Archivos de textura para elementos en carpetas

DefaultFreelook = true
; Establecer si hacer una mirada libre inmediatamente después de subir al avión
; Utilizado principalmente para tanques

OnGroundPitchFactor = 2.0
OnGroundRollFactor = 1.3
; Velocidad de inclinación según el terreno
; Cuanto mayor sea el valor, más rápido se ajusta al terreno
; Los vehículos más rápidos deberían ser más grandes y los vehículos más lentos deberían ser más pequeños
; La pantalla tiembla violentamente si es demasiado grande
; Si es demasiado pequeño, no seguirá la pendiente del terreno y se hundirá en el bloque

CameraRotationSpeed ​​= 25
; Velocidad de rotación de la cámara
Un tanque que puede usarse para limitar la velocidad de rotación de la torreta.

WeightType = Tank
; Tanque o Auto o Desconocido
; Tipo de peso de la aeronave
Tanque: no te dañas a ti mismo cuando golpeas mobs, muchos bloques para destruir
; Coche: si golpeas mobs, recibirás daño, menos bloques para destruir
; Comportamiento indefinido si ni Tank ni Car
; Los bloques a destruir se pueden configurar en mcheli.cfg

WeightedCenterZ = 0.0
; Configuración de coordenadas del centro de gravedad Z
; Coordenada Z del centro de gravedad cuando la aeronave se inclina según el terreno
; * No funciona muy bien, por lo que es mejor no usarlo si se siente incómodo

SetWheelPos = 1.75, -0.24, 4.85, 3.02, 1.44, -1.54, -2.91
; SetWheelPos = coordenada X, coordenada Y, coordenada Z 1, coordenada Z 2, coordenada Z 3 ...
; Especifique la posición de contacto con el suelo. El avión se inclina hacia este punto de instalación.
; No hay necesidad de coordenadas X negativas
; ★ Se recomienda encarecidamente que la coordenada Y se establezca en -0.24 independientemente del modelo.



