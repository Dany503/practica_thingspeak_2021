# -*- coding: utf-8 -*-
import paho.mqtt.publish as publish
import random
channelID = "xxxxxxx" # canal
apiKey = "xxxxxxxxxxxxxx" # key para escribir

useUnsecuredTCP = True # conexión predeterminada
useUnsecuredWebsockets = False # socket por el puerto 80 

mqttHost = "mqtt.thingspeak.com"
# Parámetros para las conexiones
if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None
if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

# crear cadena de topic
topic = "channels/" + channelID + "/publish/" + apiKey

dato = random.randint(20, 30)
# campo de datos
tPayload = "field1=" + str(dato) 
# publicación de los datos
try:
    publish.single(topic, payload=tPayload, 
                   hostname=mqttHost, port=tPort, tls=tTLS, 
                   transport=tTransport)
    print("Dato publicado: ", dato)
except:
    print("Fallo al publicar los datos")
    
