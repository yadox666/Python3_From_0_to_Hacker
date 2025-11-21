# Hoja de Referencia de Wireshark

![Wireshark Logo](https://www.wireshark.org/assets/theme-2015/images/wireshark_logo.png)

## ¿Qué es Wireshark?

Wireshark, cuyo nombre antiguo es Ethereal, es un programa que puede ejecutarse en muchos sistemas operativos como Windows, Linux, MacOS o Solaris y puede analizar todo el tráfico que va a las tarjetas de red conectadas al ordenador. Analiza más de 750 protocolos, puede capturar paquetes y guardarlos en un archivo.

## Operadores Lógicos

Los operadores lógicos están disponibles para todos los filtros.

**Ejemplo:** `http & ip.src == 192.168.0.1`

## Tipos de Tramas

- **Trama de Gestión (Management Frame):** La trama para la conexión entre el dispositivo de red y el cliente.

- **Trama de Control (Control Frame):** Controla la integridad del tráfico de datos entre el dispositivo de red y el cliente.

- **Trama de Datos (Data Frame):** La trama sobre la cual se transfieren los datos originales.

## Filtros de Wireshark

### Tramas de Gestión (Management Frames)

Mostrar solo los paquetes salientes de la trama de gestión.
 
```
wlan.fc.type==0
```

Mostrar paquetes entrantes y salientes a través de la trama de control.

```
wlan.fc.type==1
```

Mostrar paquetes transferidos sobre la trama de datos.

```
wlan.fc.type==2
```

### Subtipos de Tramas

Lista las peticiones de asociación.

```
wlan.fc.type_subtype==0
```

Lista las respuestas de asociación.

```
wlan.fc.type_subtype==1
```

Lista las peticiones de sondeo (probe requests).

```
wlan.fc.type_subtype==4
```

Lista las respuestas de sondeo (probe responses).

```
wlan.fc.type_subtype==5
```

Lista las señales/ondas Beacon.

```
wlan.fc.type_subtype==8
```

Lista las peticiones de autenticación.

```
wlan.fc.type_subtype==11
```

Lista las peticiones de desautenticación.

```
wlan.fc.type_subtype==12
```

### Filtros TCP

Lista los paquetes TCP salientes hacia el puerto xx.

```
tcp.port == xx
```

Lista los paquetes TCP con puerto de origen xx.

```
tcp.srcport == xx
```

Lista los paquetes TCP con puerto de destino xx.

```
tcp.dstport == xx
```

### Filtros UDP

Lista los paquetes UDP salientes hacia el puerto xx.

```
udp.port == xx
```

Lista los paquetes UDP con puerto de origen xx.

```
udp.srcport == xx
```

Lista los paquetes UDP con puerto de destino xx.

```
udp.dstport == xx
```

### Filtros HTTP

Lista las peticiones HTTP Get.

```
http.request
```

### Filtros por Dirección MAC

Lista los paquetes con dirección MAC de origen o destino.

```
wlan.addr == MAC-Address
```

Lista los paquetes que tienen una dirección MAC de origen específica.

```
wlan.sa == MAC-Address
```

Lista los paquetes que tienen una dirección MAC de destino específica.

```
wlan.da == MAC-Address
```

---

## Créditos

Este documento está basado en la hoja de referencia original de [ismailtasdelen/wireshark-cheatsheet](https://github.com/ismailtasdelen/wireshark-cheatsheet)

**Clonar el Repositorio Original (HTTPS):**
```bash
git clone https://github.com/ismailtasdelen/wireshark-cheatsheet.git
```

**Clonar el Repositorio Original (SSH):**
```bash
git clone git@github.com:ismailtasdelen/wireshark-cheatsheet.git
```
