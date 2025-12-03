import re

input_file = "index.html"
output_file = "index_clean.html"

print(f"--- Limpiando {input_file} ---")

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. SEGURIDAD: Verificar que leímos el archivo bien
    if len(content) == 0:
        raise Exception("El archivo está vacío.")

    # 2. ELIMINAR SOLO EL ANUNCIO (WIX_ADS)
    # Busca exactamente el div que tiene el id="WIX_ADS"
    patron_anuncio = r'<div id="WIX_ADS".*?</div>'
    
    # Comprobamos si existe antes de borrar
    if re.search(patron_anuncio, content, re.DOTALL):
        content = re.sub(patron_anuncio, '', content, flags=re.DOTALL)
        print("✅ [EXITO] Publicidad de Wix eliminada.")
    else:
        print("⚠️ [INFO] No se encontró el banner de publicidad (¿ya lo borraste?).")

    # 3. AJUSTAR EL MARGEN SUPERIOR (Quitar el hueco blanco)
    # Cambiamos las variables de 50px a 0px
    cambios = 0
    if '--wix-ads-height:50px' in content:
        content = content.replace('--wix-ads-height:50px', '--wix-ads-height:0px')
        cambios += 1
    if '--wix-ads-top-height:50px' in content:
        content = content.replace('--wix-ads-top-height:50px', '--wix-ads-top-height:0px')
        cambios += 1
        
    print(f"✅ [EXITO] Ajustados {cambios} parámetros de altura (espacios en blanco).")

    # 4. LIMPIAR TITULO
    content = content.replace(' | Wix.com', '')

    # 5. FORMATEAR (Hacerlo legible) - Opcional pero recomendado
    # Separa las etiquetas principales para que no sea una sola línea eterna
    content = content.replace('><div', '>\n<div')
    content = content.replace('><script', '>\n<script')
    content = content.replace('><style', '>\n<style')
    content = content.replace('</head>', '\n</head>\n')
    content = content.replace('</body>', '\n</body>\n')

    # Guardar
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✨ LISTO: Abre '{output_file}' en tu navegador para probarlo.")

except Exception as e:
    print(f"❌ ERROR: {e}")
