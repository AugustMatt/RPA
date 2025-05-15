from selenium.webdriver.common.by import By
from utils import wait_download_ends
import time

# Função para obter o link da fatura aberta
def get_open_invoice_link(driver):

    table = driver.find_element(By.ID, "DataTables_Table_0")
    rows = table.find_elements(By.TAG_NAME, "tr")

    invoice_link = None

    for row in reversed(rows[1:]):  # Ignora o cabeçalho
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) < 4:
            continue
        invoice_status = columns[2].text.strip().lower()
        if invoice_status == "aberto":
            link_element = columns[3].find_element(By.TAG_NAME, "a")
            invoice_link = link_element.get_attribute("href")
            break

    if not invoice_link:
        raise Exception("Nenhuma fatura em aberto encontrada.")

    return invoice_link

# Função para salvar a fatura como PDF
def save_invoice_pdf(driver, link_pdf, download_path):
    # Abre o link da fatura em uma nova aba
    driver.execute_script(f"window.open('{link_pdf}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # Aguarda carregar (ajuste conforme necessário)
    time.sleep(5)

    # Comando para imprimir como PDF
    driver.execute_script("window.print();")

    # Espera um tempo para garantir que o PDF foi salvo
    print("Esperando download do PDF...")
    file_name = wait_download_ends(download_path)
    print(f"Download concluído: {file_name}")

    # Fecha a aba da fatura
    driver.switch_to.window(driver.window_handles[0])
