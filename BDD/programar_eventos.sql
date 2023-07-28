-- Enciende el programador de eventos
SET GLOBAL event_scheduler="ON";

-- Se crea la tarea que cambia el estado del prestamo de activo (1) a retrasado (3) una vez el estudiante excede el periodo de prestamo
CREATE
DEFINER=`root`@`localhost`
EVENT `Cambiar_Estado_Prestamo` ON
SCHEDULE EVERY 1 HOUR
STARTS '2023-07-24 00:00:00'
ENDS '2037-01-19 03:14:07'
ON COMPLETION PRESERVE ENABLE
COMMENT 'Cambia el estado de activo a retrasado'
DO
    UPDATE `gestion_prestamos_prestamo`
    SET `estado_prestamo`=3,
        `updated`=NOW()
WHERE ((`estado_prestamo`=1) AND (`fecha_devolucion` < CURRENT_DATE()));

-- Se crea la tarea que cambia el estado de la sancion de activa (1) a inactiva (0) una vez esta se vence
CREATE
DEFINER=`root`@`localhost`
EVENT `INACT_SANCION` ON
SCHEDULE EVERY 1 HOUR
STARTS '2023-07-24 00:02:00'
ENDS '2037-01-19 03:14:07'
ON COMPLETION PRESERVE ENABLE
COMMENT 'Inactiva la sancion vencida'
DO
    UPDATE `gestion_prestamos_sancion`
    SET `estado`=0,
        `updated`=NOW()
WHERE (`fecha_culminacion` <= CURRENT_DATE());

-- Se crea la tarea que cambia el estado del estudiante de inactivo(0) a activo(1) si la sancion se vencio
CREATE
DEFINER=`root`@`localhost`
EVENT `ACT_ESTUDIANTE_POST_SANCION` ON
SCHEDULE EVERY 1 HOUR
STARTS '2023-07-24 00:04:00'
ENDS '2037-01-19 03:14:07'
ON COMPLETION PRESERVE ENABLE
COMMENT 'Activa estudiante una vez se vence sancion'
DO
    UPDATE `gestion_usuarios_persona`
    SET `estado`=1,
	`updated`=NOW()
WHERE `id` IN (
    SELECT `id_est` FROM `gestion_prestamos_prestamo`
    WHERE `id` IN (
        SELECT `id_prestamo` FROM `gestion_prestamos_sancion`
        WHERE `estado`=0
    )
);

-- PARA ELIMINAR LOS EVENTOS DE SER NECESARIO
-- DROP EVENT IF EXISTS `Cambiar_Estado_Prestamo`;
-- DROP EVENT IF EXISTS `INACT_SANCION`;
-- DROP EVENT IF EXISTS `ACT_ESTUDIANTE_POST_SANCION`;