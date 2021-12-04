
2016/03/28

;***********************************************************************************
;■ Archivo de configuración de HUD hud / ***. Txt
;***********************************************************************************

; ★ Importante ★
; HUD se puede recargar mientras Minecraft se está ejecutando.
; [Conducir el avión → Tecla R para suministrar pantalla → Opción MOD → Desarrollo → Volver a cargar todo el HUD]
; La recarga de texturas utiliza las funciones predeterminadas de Minecraft, no de modificaciones de helicópteros.
; [Tecla Esc: menú Juego → Configuración → Paquete de recursos → Listo]


;************************************************************************************************************
; Solo el archivo de configuración de HUD afecta el orden.
; El procesamiento se ejecuta en el orden descrito en el archivo de configuración y se convierte en el orden de dibujo.

;************************************************************************************************************
; Sobre la fórmula
; ■DrawString y DrawCenteredString. Las fórmulas se pueden configurar para valores numéricos que no sean la parte de datos de DrawString y DrawCenteredString.
;   Ejemplo: Color = 123 + 456
; ■Hexadecimal se puede establece7r en la fórmula. Prefijo # o 0x antes del número.
;   Ejemplo: Color = # 123 + 0x456 + 789
; ■"Variable" se puede establecer en la fórmula.
;   Ejemplo: Color = hp_rto * 100
;      hp_rto ingresa el valor de resistencia de la aeronave de 0.0 a 1.0. Por lo tanto, se convierte en 0.0 a 100.0 en * 100.
; ■ Las condiciones se pueden establecer en la fórmula.
;   Formato: condición? Valor cuando se cumple la condición: Valor cuando no se cumple la condición
;   Ejemplo: Color = hp_rto> 0.2? 0xFFFFFFFF: 0x00000000
;      Si hp_rto excede 0.2, 0xFFFFFFFF se establece en Color, y si hp_rto es 0.2 o menos, 0x00000000 se establece en Color
;
; "Lista de variables"
; center_x    : Coordenada central X
; center_y    : Coordinar Y en el centro de la pantalla
; width       : Ancho de pantalla
; height      : Altura de la pantalla
; yaw         : Desviación de la aeronave [rotación lateral] (-180.0-180.0)
; pitch       : Paso de la aeronave [rotación vertical] (-90.0 a 90.0)
; roll        : Rollo de aeronave (-180.0-180.0)
; plyr_yaw    : Guiñada del jugador [rotación lateral] (-180.0-180.0)
; plyr_pitch  : Lanzamiento del jugador [rotación vertical] (-90.0 a 90.0)
; altitude    : Altitud del avión (0-) Distancia del avión al bloque de abajo (no negativo)
; sea_alt     : Altitud de la aeronave (0-) sobre el nivel del mar. Distancia desde el nivel del mar de referencia (no negativo)
; hp          : Valor de durabilidad restante de la aeronave (0 ~)
; max_hp      : Máxima durabilidad de la aeronave (0-)
; hp_rto      : Relación de HP restante de la aeronave (0.0 a 1.0)
; throttle    : Acelerador actual de la aeronave (0.0-1.0)
; pos_x       : Coordenadas de la aeronave X
; pos_y       : Coordenadas de la aeronave y
; pos_z       : Coordenadas de la aeronave z
; motion_x    : Aceleración de aeronaves X
; motion_y    : Aceleración de aeronaves y
; motion_z    : Aceleración de aeronaves z
; fuel        : Porcentaje de combustible restante en la aeronave (0.0 a 1.0)
; low_fuel    : Pantalla de advertencia de combustible bajo. 0 y 1 se repiten en el momento de la disminución porque parpadea (0 = con combustible, 1 = combustible bajo)
; stick_x     : Dirección X cantidad de palanca de control (-1.0 a 1.0)
; stick_y     : Cantidad de palanca de control en dirección Y (-1.0 a 1.0)
; reloading   : Estado de recarga del arma (0 = no recarga, 1 = recarga)
; reload_time : El tiempo restante de recarga del arma (0.0 a 1.0) 0.0 indica que la recarga se completó
; wpn_heat    : Calorías de arma (0.0-1.0)
; is_heat_wpn : Si el arma es un arma de calorías (0 = no calorías, 1 = calorías)
; dsp_mt_dist : Si se muestra la distancia de impacto (0 = sin visualización, 1 = visualización)
; mt_dist     : Distancia de aterrizaje (si es menor a 0.0, el cálculo no es posible)
; have_radar  : Si un radar está equipado (0 = sin radar, 1 = con radar)
; radar_rot   : Ángulo de rotación del radar. Después de una vuelta, la posición de la entidad se actualiza.
; vtol_stat   : Solo aviones de ala fija. 0 = Normal, 1 = Conmutación VTOL, 2 = VTOL
; free_look   : 0 = Normal, 1 = MIRADA LIBRE
; cam_mode    : 0 = Normal, 1 = VISIÓN NOCTURNA, 2 = VISIÓN TÉRMICA
; cam_zoom    : Ampliación de cámara. 1.0 ~ 10.0
; auto_pilot  : 0 = Normal, 1 = Durante el piloto automático
; have_flare  : Si está instalado o no un dispositivo de inyección de antorcha (0 = No, 1 = Sí)
; can_flare   : Si se pueden usar bengalas (0 = habilitado, 1 = no listo, deshabilitado)
; sight_type  : Tipo de objetivo (0 = ninguno, 1 = MoveSight, 2 = MissileSight)
; lock        : Estado de bloqueo del misil (0.0 a 1.0)
; color       : Configuración de color actual (0x00000000 ~ 0xFFFFFFFF)
; inventory   : Número de ranuras en inventario (0 a 54)
; hovering    : Estado de desplazamiento (0 = sin desplazamiento, 1 = desplazamiento)
; is_uav      : Si UAV (0 = no UAV, 1 = UAV)
; uav_fs      : Fuerza de señal de UAV. Cuanto más grande, más cerca de la estación de UAV (0.0-1.0)
; gunner_mode : Ya sea en modo Artillero (0 = modo Normal, 1 = modo Artillero)
; time        : Micra tiempo 24,000 recuentos por día (0-24000), 0 = 6:00 am, 6000 = mediodía
; test_mode   : Modo de prueba (0 = modo normal, 1 = modo de prueba)


;************************************************************************************************************
; Llame a otro archivo de dibujo de HUD
; Si especifica el nombre del archivo de texto del HUD, puede ejecutar el proceso de dibujo de ese archivo de configuración.
;
; Call = common_pilot, common_pilot.txt se ejecuta
; Se puede leer otro archivo en el archivo de configuración llamado, pero el mismo archivo no se puede leer dos veces.
; Por ejemplo, si Call = heli en heli.txt, heli.txt se ignora porque ya se está ejecutando.
; Si escribe Call = plane en heli.txt y Call = heli en plane.txt,
; Como heli.txt se está ejecutando, tampoco se ejecuta en este caso.
call = common_pilot


;************************************************************************************************************
; Terminar de dibujar el archivo HUD actual
;
; Call  Si se llama, regrese a la persona que llama
; heli.txt Llame a uav_fs.txt desde y use Exit en uav_fs.txt, el dibujo de uav_fs termina,
; heli.txt El procesamiento continúa desde la línea que sigue a la llamada a uav_fs.txt.
;
Exit


;************************************************************************************************************
; Rama condicional
; Ejecute el procesamiento solo cuando se cumpla la condición especificada
;
; Si la condición no es 0, procesando 1 procesando 2 procesando 3 se ejecuta
; Si la condición es 0, el procesamiento 1 el procesamiento 2 el procesamiento 3 no se ejecuta
; If = Condición
; 	Procesamiento 1
; 	Procesamiento 2
; 	Procesamiento 3
; EndIf
; * No se admite el anidamiento (no se puede insertar If entre If y EndIf)
;
; En el siguiente ejemplo, si is_heat_wpn es 1, se ejecutan Color y DrawRect.
If = is_heat_wpn==1
	Color = 0xFF28d448
	DrawRect = -145, 57, 43, 10
EndIf


;************************************************************************************************************
; Configuraciones de color
; Después de configurar el color, los colores de texto y línea posteriores se dibujarán con este color de configuración
;
; Hay dos métodos de configuración.
; Un parámetro y cuatro parámetros.
; Cuando se configura con uno: Opacidad, rojo, verde, azul desde arriba
;                  :Un ejemplo) 0xAABBCCDD , Opacidad = AA, rojo = BB, verde = CC, azul = DD
; Cuando se configura con cuatro: opacidad, rojo, verde, azul desde el frente
;                  :Un ejemplo) 12, 34, 56, 78  , Opacidad = 12, rojo = 34, verde = 56, azul = 78
; Especifique en hexadecimal o especifique 4 en decimal
; Ejemplo: las siguientes son todas las configuraciones válidas
Color = 0xFFFFFFFF
Color = #FFFFFFFF
Color = 0xFF,  40, 212,  72


;************************************************************************************************************
; Dibujar una cuerda
;  DrawString         : Dibujar a la derecha desde las coordenadas especificadas
;  DrawCenteredString : Dibuje de modo que las coordenadas especificadas estén en el centro
;
; Parámetro 1 = coordenada X desde el centro de la pantalla
; Parámetro 2 = coordenada Y desde el centro de la pantalla
; Parámetro 3 = Formato de visualización (printf o String.format format ,, no se puede usar)
;               El número de% y el número de datos después del parámetro 4 deben coincidir
; Parámetro 4 o posterior = ★ Datos (se pueden omitir; sin límite superior)
;
; Ejemplo (altitud)：DrawString = -20,  20, "Hello"
;           Hello Se muestra en la pantalla.
;
; Ejemplo (altitud)：DrawString =  0,  40, "[ %3d ]", ALTITUDE
;           ALTITUDE(Altitud) Mostrar como un entero de tres dígitos → [ 123 ]
;
; Ejemplo (fecha)：DrawString =  0, -30, "%tY/%tm/%td", DATE, DATE, DATE
;           DATE(Fecha) A / Separado por → 2014/10/11
;
; ★ Datos (mayúsculas y minúsculas)
; Las fórmulas no se pueden usar para datos
;
; Como se muestra a continuación,% s,% d, y% f se determinan para cada dato. Sin embargo, es posible insertar un valor numérico que represente el número de dígitos entre% y caracteres alfabéticos.
; Por ejemplo,% f no especifica el número de decimales, por lo que no sabe cuántos dígitos se muestran。 → 123.45678 Etc.
; %.2f significa que el punto decimal siempre es un dígito. %.0f → 123    %.1f → 123.4    %.2f → 123.45
; Esto también es posible con% d. Busque printf para más detalles.
;
;  NAME        : %s : Nombre de la aeronave (igual que el nombre del artículo)
;  ALTITUDE    : %d : Muestra la altitud como un entero.
;  DATE        : %tY %tm %td %td %tH %tM %tS ...
;              :Representa la fecha y hora actuales. % tY = año,% tm = mes,% td = día,% tH = hora,% tM = minuto,% tS = segundo
;  MC_THOR     : %d : Representa la hora en Minecraft. 0-23. Tenga en cuenta que el tiempo en Minecraft es 72 veces real
;  MC_TMIN     : %d : Representa minutos de tiempo en Minecraft. 0-59. Tenga en cuenta que el tiempo en Minecraft es 72 veces real
;  MC_TSEC     : %d : Representa los segundos de tiempo en Minecraft. 0-59. Tenga en cuenta que el tiempo en Minecraft es 72 veces real
;  MAX_HP      : %d : El valor de durabilidad máxima se indica mediante un número entero.
;  HP          : %d : El valor de durabilidad restante se indica mediante un número entero.
;  HP_PER      : %f : La relación restante se muestra como un decimal (100.0 a 0.0). % .1f significa mostrar un lugar decimal.
;  THROTTLE    : %f : El acelerador se indica por decimal (100.0-0.0). % .1f significa mostrar un lugar decimal.
;  POS_X       : %f : Muestra la coordenada X de la aeronave como un decimal.
;  POS_Y       : %f : Muestra la coordenada Y de la aeronave como un decimal.
;  POS_Z       : %f : Muestra la coordenada Z de la aeronave como un decimal.
;  MOTION_X    : %f : Muestra la aceleración de la aeronave en la dirección X como un número decimal.
;  MOTION_Y    : %f : Muestra la aceleración de la aeronave en la dirección y como un número decimal.
;  MOTION_Z    : %f : Muestra la aceleración de la aeronave en la dirección z como un número decimal.
;  YAW         : %f : Muestra el ángulo horizontal de la aeronave como un número decimal.
;  PITCH       : %f : Muestra el ángulo vertical de la aeronave como un número decimal. ★ Tenga en cuenta que el ángulo de cabeceo real es opuesto al signo. (La parte superior es positiva, la parte inferior es negativa)
;  ROLL        : %f : Muestra el ángulo de giro del avión como un número decimal.
;  PLYR_YAW    : %f : Muestra el ángulo horizontal del jugador como un número decimal.
;  PLYR_PITCH  : %f : Muestra el ángulo vertical del jugador como un número decimal. ★ Tenga en cuenta que el ángulo de cabeceo real es opuesto al signo. (La parte superior es positiva, la parte inferior es negativa)
;  INVENTORY   : %d : Muestra el número de inventario de la aeronave.
;  WPN_NAME    : %s : Muestra el nombre del arma seleccionada actualmente.
;  WPN_AMMO    : %s : Muestra el número de balas del arma seleccionada actualmente.
;  WPN_RM_AMMO : %s : Muestra la munición restante para el arma seleccionada actualmente.
;  RELOAD_PER  : %f : Indica el estado de recarga como un decimal (100.0 a 0.0). La recarga se completó en 100.0. % .1f significa mostrar un lugar decimal.
;  RELOAD_SEC  : %f : El número de segundos de recarga restantes se indica mediante un decimal (de 0.0). Recarga completa con 0.0. % .1f significa mostrar un lugar decimal.
;  MORTAR_DIST : %f : Distancia de aterrizaje (si es menor a 0.0, el cálculo no es posible)
;  MC_VER      : %s : Versión de Minecraft.
;  MOD_VER     : %s : Versión MOD.
;  MOD_NAME    : %s : El nombre del MOD. Siempre "MC Helicopter MOD".
;  TVM_POS_X   : %f : Coordenada X del misil de TV
;  TVM_POS_Y   : %f : Coordenada y del misil de TV
;  TVM_POS_Z   : %f : Coordenada z del misil de TV
;  TVM_DIFF    : %f : Distancia entre misiles de TV y aviones
;  CAM_ZOOM    : %f : Aumento de la cámara
;  UAV_DIST    : %f : Distancia desde la estación de UAV (0.0 ~)
;  KEY_GUI     : %s : Nombre de clave de GUI (R para la configuración de clave predeterminada)
;
DrawCenteredString = 0,  40, "[ %3d ]", ALTITUDE
→ Si ALTITUDE es 12, la pantalla mostrará [12]. Aunque se especifican 3 dígitos, 12 son 2 dígitos, por lo que el lugar de los 100 es un espacio.
DrawString         = 0,  30, "%tY %tm %td  [ %02d:%02d:%02d ]", DATE, DATE, DATE, MC_THOR, MC_TMIN, MC_TSEC
→ Si la hora en Micra el 24/10/2014 es 12:34:56, la pantalla mostrará 2014 10 24 [12:34:56].
DrawString         = 0,  20, "%3d/%3d  = %.1f%%", HP, MAX_HP, HP_PER
→ Si el HP actual es 50 y el HP máximo es 100, la pantalla mostrará 50/100 = 50%. %% representa el carácter%.
DrawString         = 0,  10, "[ %s ]", name
→ Si el avión es AH-64, la pantalla mostrará AH-64D Apache Longbow.
DrawCenteredString = 0, -10, "HUD Test"
→ Como no hay parte de datos, la prueba de HUD siempre se muestra en la pantalla.


;************************************************************************************************************
; Dibujar textura
; La textura recomendada es 256x256. Todos los enteros o decimales se pueden especificar después del parámetro 2.
; Parámetro 1  : Nombre del archivo de textura (sin extensión; archivos en activos \ mcheli \ textures \ gui)
; Parámetro 2  : Coordenada X desde el centro de la pantalla
; Parámetro 3  : Coordenada Y desde el centro de la pantalla
; Parámetro 4  : Ancho en pantalla
; Parámetro 5  : Altura en pantalla
; Parámetro 6  : Coordenada X de textura para leer
; Parámetro 7  : Coordenada Y de textura para leer
; Parámetro 8  : Ancho de textura para leer
; Parámetro 9  : Altura de textura a leer
; Parámetro 10 : Ángulo de rotación en pantalla (opcional)
DrawTexture = heli_hud, -100.0, 20,  50,20,  0,0, 64,64,  90.0


;************************************************************************************************************
; Dibuja un rectángulo
; Parámetro 1: coordenada X desde el centro de la pantalla
; Parámetro 2: coordenada Y desde el centro de la pantalla
; Parámetro 3: ancho de pantalla
; Parámetro 4: Altura en pantalla
DrawRect = -20, -30, 40*throttle, -20


;************************************************************************************************************
; Dibuja una línea
; Si especifica el parámetro 5 o posterior, puede dibujar líneas continuamente.
; 1,2 → 3,4 → 5,6 → 7,8 ... 
; Se requiere hasta el parámetro 4 y se usa si es necesario después de 5
;
; Parámetro 1: coordenada X desde el centro de la pantalla
; Parámetro 2: coordenada Y desde el centro de la pantalla
; Parámetro 3: coordenada X desde el centro de la pantalla
; Parámetro 4: coordenada Y desde el centro de la pantalla
; Parámetro 5: después del parámetro 5, coordenada X, coordenada Y, coordenada X, coordenada Y ...
DrawLine = -40,  30,   40, 30
DrawLine = -20, -30,  -20+40*throttle, -30,  -20+40*throttle, -20,  -20, -20,  -20, -30


;************************************************************************************************************
; Dibuja una línea discontinua
; Si especifica el parámetro 7 o posterior, puede dibujar líneas continuamente.
; 3,4 → 5,6 → 7,8 ... 
; Se requiere hasta el parámetro 6 y se usa si es necesario después de 7
; El parámetro 1 es el factor de glLineStipple, y el parámetro 2 es el patrón de glLineStipple.
;
; Parámetro 1: el patrón de línea discontinua está representado por hexadecimal 0 o 1 (si no está seguro, configure 0xCCCC o 0xAAAA)
; Parámetro 2: aumento de línea discontinua (entero)
; Parámetro 3: coordenada X desde el centro de la pantalla
; Parámetro 4: coordenada Y desde el centro de la pantalla
; Parámetro 5: coordenada X desde el centro de la pantalla
; Parámetro 6: coordenada Y desde el centro de la pantalla
; Parámetro 7: después del parámetro 7, coordenada X, coordenada Y, coordenada X, coordenada Y ...
DrawLineStipple = 0xF0F0, 1,   -40,  30,   40, 30
DrawLineStipple = 0xFF00, 1,   -20, -30,  -20+40*throttle, -30,  -20


;************************************************************************************************************
; Dibuja marcas que representan ángulos
; 
; DrawGraduationYaw    El ángulo de rotación horizontal se muestra en una escala. En la configuración de ejemplo, se muestra en la parte superior de la pantalla
; DrawGraduationPitch1 El ángulo de rotación vertical se muestra en una escala. En la configuración de ejemplo, se muestra a la izquierda y a la derecha de la pantalla
; DrawGraduationPitch2 Muestra la dirección vertical y el ángulo de balanceo. En la configuración de ejemplo, se muestra en el centro de la pantalla
; Parámetro 1: ángulo de rotación
; Parámetro 2: ángulo de rotación del rollo
; Parámetro 3: coordenada X desde el centro de la pantalla
; Parámetro 4: coordenada Y desde el centro de la pantalla
; DrawGraduationYaw Se recomienda utilizar los siguientes valores para parámetros distintos del parámetro 3.
DrawGraduationYaw    = plyr_yaw,    0,     0, -100
DrawGraduationPitch1 = plyr_pitch,  0,     0, 0
DrawGraduationPitch2 = plyr_pitch, -roll,  0, 0


;************************************************************************************************************
; Dibuja la diferencia de ángulo entre el jugador y el avión
; 
Un pequeño cuadrado indica dónde está el jugador frente a la aeronave.
; Parámetro 1: coordenada X desde el centro de la pantalla
; Parámetro 2: coordenada Y desde el centro de la pantalla
DrawCameraRot = 0, 60
