"""
ARGPARSE AVANZADO - Script Educativo
=====================================
Este script demuestra el uso avanzado de argparse para crear programas
de línea de comandos profesionales con múltiples tipos de argumentos.

¿QUÉ ES ARGPARSE?
argparse es una librería de Python que permite crear interfaces de línea
de comandos (CLI) profesionales, similares a comandos como 'ls', 'grep', etc.

¿QUÉ APRENDERÁS?
- Argumentos posicionales (obligatorios)
- Argumentos opcionales (con --)
- Valores por defecto
- Validación de opciones (choices)
- Validación de tipos de datos
- Banderas booleanas (flags)
- Generación automática de ayuda

EJEMPLO DE USO:
    python argparse_usage_advanced.py entrada.txt salida.txt --user Juan --format csv --threshold 10 --verbose

PARA VER LA AYUDA:
    python argparse_usage_advanced.py --help
"""

# Importamos la librería argparse
# Esta librería viene incluida con Python, no necesitas instalarla
import argparse


def main():
    """
    Función principal que configura y procesa los argumentos de línea de comandos.
    """
    
    # PASO 1: CREAR EL PARSER
    # ------------------------
    # El parser es el objeto que se encarga de analizar los argumentos
    parser = argparse.ArgumentParser(
        description="Un script para procesar archivos con múltiples opciones configurables.",
        epilog="Ejemplo: python argparse_usage_advanced.py entrada.txt salida.txt --user Juan"
    )

    # PASO 2: DEFINIR ARGUMENTOS POSICIONALES (OBLIGATORIOS)
    # -------------------------------------------------------
    # Los argumentos posicionales NO llevan -- delante
    # Son obligatorios y deben ir en el orden especificado
    
    parser.add_argument(
        "archivo_entrada",
        help="Ruta al archivo de entrada que se procesará"
    )
    
    parser.add_argument(
        "archivo_salida",
        help="Ruta al archivo de salida donde se guardarán los resultados"
    )

    # PASO 3: ARGUMENTOS OPCIONALES CON OPCIONES LIMITADAS
    # -----------------------------------------------------
    # Este argumento solo acepta ciertos valores específicos
    
    parser.add_argument(
        "--formato",
        choices=["json", "csv", "txt"],  # Solo acepta estos valores
        default="json",  # Valor por defecto si no se especifica
        help="Formato del archivo de salida (opciones: json, csv, txt). Por defecto: json"
    )

    # PASO 4: ARGUMENTO OPCIONAL PERO REQUERIDO
    # ------------------------------------------
    # Aunque lleva --, es obligatorio especificarlo
    
    parser.add_argument(
        "--usuario",
        required=True,  # Este argumento es obligatorio
        help="Nombre del usuario que ejecuta el procesamiento (obligatorio)"
    )

    # PASO 5: ARGUMENTO CON VALIDACIÓN DE TIPO
    # -----------------------------------------
    # Este argumento valida que el valor sea un entero
    
    parser.add_argument(
        "--umbral",
        type=int,  # Solo acepta números enteros
        help="Valor umbral (número entero) para el procesamiento. Ejemplo: --umbral 100"
    )

    # PASO 6: BANDERA BOOLEANA (FLAG)
    # --------------------------------
    # Las banderas son argumentos que no necesitan un valor
    # Si se incluyen = True, si no = False
    
    parser.add_argument(
        "--verbose",
        action="store_true",  # store_true = si está presente, vale True
        help="Activar modo detallado (muestra más información durante la ejecución)"
    )

    # PASO 7: PROCESAR LOS ARGUMENTOS
    # --------------------------------
    # parse_args() lee sys.argv y convierte los argumentos en un objeto
    args = parser.parse_args()

    # PASO 8: USAR LOS ARGUMENTOS
    # ----------------------------
    # Ahora podemos acceder a los valores con args.nombre_argumento
    
    print("=" * 70)
    print("CONFIGURACIÓN DEL SCRIPT")
    print("=" * 70)
    print()
    
    # Argumentos posicionales
    print("Archivos:")
    print(f"  - Archivo de entrada:  {args.archivo_entrada}")
    print(f"  - Archivo de salida:   {args.archivo_salida}")
    print()
    
    # Argumentos opcionales
    print("Configuración:")
    print(f"  - Formato de salida:   {args.formato}")
    print(f"  - Usuario:             {args.usuario}")
    
    # Argumento opcional que puede ser None
    if args.umbral is not None:
        print(f"  - Umbral:              {args.umbral}")
    else:
        print(f"  - Umbral:              No especificado")
    
    # Bandera booleana
    if args.verbose:
        print(f"  - Modo verbose:        Activado ✓")
        print()
        print("INFORMACIÓN DETALLADA (modo verbose):")
        print(f"  - Tipo de formato: {type(args.formato)}")
        print(f"  - Tipo de umbral: {type(args.umbral)}")
        print(f"  - Argumentos completos: {args}")
    else:
        print(f"  - Modo verbose:        Desactivado")
    
    print()
    print("=" * 70)
    print("PROCESAMIENTO INICIADO")
    print("=" * 70)
    print()
    
    # Aquí iría la lógica real del script
    # Por ejemplo: leer archivo_entrada, procesarlo, guardar en archivo_salida
    print(f"[Simulación] Leyendo archivo: {args.archivo_entrada}")
    print(f"[Simulación] Procesando datos con usuario: {args.usuario}")
    print(f"[Simulación] Guardando resultado en: {args.archivo_salida}")
    print(f"[Simulación] Formato de salida: {args.formato}")
    
    if args.umbral is not None:
        print(f"[Simulación] Aplicando umbral: {args.umbral}")
    
    print()
    print("✓ Procesamiento completado exitosamente")
    print()


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo si el script se ejecuta directamente
    """
    main()
