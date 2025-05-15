from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import time

def wait_element_be_visible(driver, by, valor, timeout):
    """Aguarda um elemento ficar visivel na pagina"""
    print(f"Aguardando elemento {by} -> {valor} aparecer...")
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, valor)))
    except:
        raise Exception(f"Timeout ao esperar por elemento: {valor}")

def recreate_download_folder(download_path):
    """Remove e recria a pasta de downloads do bot."""
    if os.path.exists(download_path):
        shutil.rmtree(download_path)
    os.makedirs(download_path)

def wait_download_ends(folder_path, timeout=30):
    """Verifica periodicamente um novo arquivo em uma pasta"""
    initial_time = time.time()
    while time.time() - initial_time < timeout:
        files = os.listdir(folder_path)
        non_temp_files = [
            f for f in files 
            if not f.endswith('.crdownload') and not f.endswith('.tmp')
        ]
        if non_temp_files:
            return non_temp_files[0]  # Retorna o nome do arquivo
        time.sleep(1)
    raise Exception("Download não foi concluído dentro do tempo esperado.")
