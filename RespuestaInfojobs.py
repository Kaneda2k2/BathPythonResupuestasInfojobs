#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hochi
#
# Created:     30/07/2021
# Copyright:   (c) hochi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!Programa responder Cuestionario infojobs, cuentanos sobre tu experiencia
import  sys,pyperclip


TEXT = "Si, Solucionar incidencias con equipos informaticos, \
 ,instalar aplicaciones ,pruebas de seguridad , credenciales windows, \
  generador de scrips bat y bash, privilegios de usuarios, \
   monitorizacion de red,memoria,disco duro , Samba, ftp, \
    facilitar tareas de los trabajadores desarrollando programas de automatizacion, \
     BBDD , mariadb, workbench ,OTP, servicios , gestionar IP, DCHP, SSH, PK, \
      Entre otros. Actualmente sigo formandome en wireshark,kali linux, \
      ciber seguridad y python como lenguaje favorito."

pyperclip.copy(TEXT)

print("Texto copiado perfectamente")