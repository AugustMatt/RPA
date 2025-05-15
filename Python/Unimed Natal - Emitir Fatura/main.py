from config import LOGIN, PASSWORD, DOWNLOAD_PATH
from utils import recreate_download_folder
from driver import start_driver
from navigation import access_login_page, perform_login, navigate_to_invoice_page, perform_logout
from invoice import get_open_invoice_link, save_invoice_pdf
import os
from send_email import send_mail, send_error_mail
import time

# === Função principal ===
def main():

    # Variaveis para controlar o fluxo de re-tentativas do bot
    max_retries = 3
    wait_time_between_retries = 60  # segundos
    actual_try = 0
    success = False
    last_exception = None
    invalid_credentials = False

    while actual_try < max_retries and not success:

        actual_try += 1
        print(f"Tentativa {actual_try} de {max_retries}...")

        invoice_generated = False
        invoice_path = None

        # Limpa a pasta de downloads antes de começar
        recreate_download_folder(DOWNLOAD_PATH)

        # Inicializa o WebDriver
        driver = start_driver(DOWNLOAD_PATH)

        try:
            # Acessa o site
            access_login_page(driver)

            # Realiza o login
            if(perform_login(driver, LOGIN, PASSWORD)=='invalid-credentials'):
                invalid_credentials = True
                break
            else:
        
                # Navega até a página de faturas
                result = navigate_to_invoice_page(driver)

                if result=="has-invoice":
                    try:
                        link_pdf = get_open_invoice_link(driver)
                        save_invoice_pdf(driver, link_pdf, DOWNLOAD_PATH)
                        invoice_generated = True
                        files = os.listdir(DOWNLOAD_PATH)
                        invoice_path = os.path.join(DOWNLOAD_PATH, files[0]) if files else None
                    except Exception as e:
                        print(f"Erro ao obter ou baixar fatura: {e}")
                        invoice_generated = False
                        invoice_path = None
                elif result=="no-invoice":
                    print("Sem faturas para serem emitidas")
                    invoice_generated = False
                    invoice_path = None

                perform_logout(driver)
                send_mail(invoice_generated, invoice_path)
                success = True # finaliza loop de tentar novamente
                
        except Exception as e:
            last_exception = e
            print(f"Ocorreu um erro: {e}")
            driver.quit()
            if actual_try < max_retries:
                print(f"Aguardando {wait_time_between_retries} segundos antes de tentar novamente...")
                time.sleep(wait_time_between_retries)
        finally:
            # Finaliza o WebDriver (fecha o navegador)
            try:
                driver.quit()
            except:
                pass
    

    if invalid_credentials:
        send_error_mail('A automação falhou. Erro: Credenciais de Login Invalidas')
    elif not success and last_exception:
        send_error_mail('A automação falhou após 3 tentativas. Erro: ' + str(last_exception))

if __name__ == "__main__":
    main()
