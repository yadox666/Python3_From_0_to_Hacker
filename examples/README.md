<div align="center">

# 📂 Ejemplos del curso

**Ordenados de más sencillo a más avanzado, en el mismo orden que el [temario](../Readme.md)**

</div>

## ⚙️ Preparación

```bash
cd examples
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Leyenda:** 🟢 básico · 🟡 intermedio · 🔴 avanzado · 🔒 requiere `sudo` · 🌐 requiere Internet

## 1️⃣ Argumentos de línea de comandos

| Nivel | Script | Qué aprendes | Ejecutar |
|:---:|---|---|---|
| 🟢 | [`argv_usage.py`](argv_usage.py) | Leer argumentos con `sys.argv` | `python3 argv_usage.py uno dos` |
| 🟢 | [`argparse_usage.py`](argparse_usage.py) | Opciones con nombre usando `argparse` | `python3 argparse_usage.py --nombre Ana --edad 30` |
| 🟡 | [`argparse_usage_advanced.py`](argparse_usage_advanced.py) | Opciones avanzadas de `argparse` | `python3 argparse_usage_advanced.py -h` |

## 2️⃣ Clases y objetos

| Nivel | Script | Qué aprendes | Ejecutar |
|:---:|---|---|---|
| 🟡 | [`classFirewallRule.py`](classFirewallRule.py) | Una clase que modela reglas de firewall | `python3 classFirewallRule.py` |

## 3️⃣ Archivos, CSV y JSON

| Nivel | Script | Qué aprendes | Ejecutar |
|:---:|---|---|---|
| 🟢 | [`csv_process.py`](csv_process.py) | Leer un CSV línea a línea con `with` | `python3 csv_process.py` |
| 🟢 | [`json_from_dict.py`](json_from_dict.py) | Guardar un diccionario como JSON | `python3 json_from_dict.py` |
| 🟢 | [`json_file_to_dict.py`](json_file_to_dict.py) | Leer ese JSON de vuelta *(ejecuta antes el anterior)* | `python3 json_file_to_dict.py` |
| 🟡 | [`get_oui_txt.py`](get_oui_txt.py) 🌐 | Descargar y convertir la lista de fabricantes MAC a `oui_list.json` | `python3 get_oui_txt.py` |

## 4️⃣ Redes y sockets

| Nivel | Script | Qué aprendes | Ejecutar |
|:---:|---|---|---|
| 🟡 | [`socket_scanner.py`](socket_scanner.py) | Escáner de puertos TCP con `socket` | `python3 socket_scanner.py` |
| 🟡 | [`socket_scanner_multithreaded.py`](socket_scanner_multithreaded.py) | El mismo escáner, con hilos (mucho más rápido) | `python3 socket_scanner_multithreaded.py` |
| 🟡 | [`nmap_scanner.py`](nmap_scanner.py) | Controlar Nmap desde Python y guardar en JSON | `python3 nmap_scanner.py` |
| 🔴 | [`scapy_get_aps_around.py`](scapy_get_aps_around.py) 🔒 | Detectar redes Wi-Fi cercanas *(tarjeta en modo monitor)* | `sudo python3 scapy_get_aps_around.py` |

## 5️⃣ Web y APIs

| Nivel | Script | Qué aprendes | Ejecutar |
|:---:|---|---|---|
| 🟢 | [`check-url.py`](check-url.py) 🌐 | Comprobar el código de estado HTTP de una URL | `python3 check-url.py --url example.com` |
| 🟡 | [`scrap.py`](scrap.py) 🌐 | Extraer datos de una web con expresiones regulares | `python3 scrap.py https://example.com` |
| 🟡 | [`crawler_spider.py`](crawler_spider.py) 🌐 | Araña que sigue enlaces con BeautifulSoup | `python3 crawler_spider.py` |
| 🟡 | [`api_users.py`](api_users.py) | Tu propia API REST con Flask | `python3 api_users.py` → abre `http://127.0.0.1:8000/users` |
| 🔴 | [`api_users_443.py`](api_users_443.py) 🔒 | La misma API con HTTPS | `sudo python3 api_users_443.py` |
| 🔴 | [`api_honeypot.py`](api_honeypot.py) 🔒 | Honeypot que registra cada petición | `sudo python3 api_honeypot.py` |
| 🔴 | [`api_honeypot_with_geolocation_data.py`](api_honeypot_with_geolocation_data.py) 🔒🌐 | Honeypot que además geolocaliza la IP | `sudo python3 api_honeypot_with_geolocation_data.py` |
| 🔴 | [`api_fuzzer.py`](api_fuzzer.py) | Descubrir rutas ocultas de una API con `endpoints.txt` | `python3 api_fuzzer.py` |

> [!TIP]
> **Práctica completa de laboratorio:** arranca `api_honeypot.py` en una terminal y lanza `api_fuzzer.py` en otra. Después abre `registro_honeypot.json` y mira todo lo que el honeypot ha registrado sobre el "atacante".

> [!NOTE]
> Los ejemplos HTTPS necesitan un certificado autofirmado. Genéralo una vez en esta carpeta:
> ```bash
> openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
> ```
> Los archivos `*.pem` están en `.gitignore` para que la clave privada nunca se suba al repositorio.

## 📦 Archivos de datos

| Archivo | Lo usa |
|---|---|
| [`ejemplo.csv`](ejemplo.csv) | `csv_process.py` |
| [`endpoints.txt`](endpoints.txt) | `api_fuzzer.py` (diccionario de rutas) |
| [`oui_list.json`](oui_list.json) | `scapy_get_aps_around.py` (se regenera con `get_oui_txt.py`) |
| [`scan_results.json`](scan_results.json) | Ejemplo de salida de un escaneo |
| [`requirements.txt`](requirements.txt) | `pip install -r requirements.txt` |

---

<div align="center">

[⬅️ Volver al temario](../Readme.md)

</div>
