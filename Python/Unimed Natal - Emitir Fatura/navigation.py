from utils import wait_element_be_visible
from selenium.webdriver.common.by import By
from config import PAGE_WAIT_TIME
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def access_login_page(driver):
    """Acessa a pagina inicial do sistema, que tambem é a pagina de login"""
    url = "https://beneficiario.unimednatal.com.br/usuarios/login"
    driver.get(url)
    wait_element_be_visible(driver, By.ID, "UsuarioUsername", PAGE_WAIT_TIME)
    print("Acesso a pagina de login realizado com sucesso!")

def verify_credentials_on_login(driver, timeout=5):
    """Verifica se as credenciais informadas são validas"""
    try:
        gritter = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gritter-item"))
        )
        mensagem = gritter.find_element(By.TAG_NAME, "p").text.strip().lower()
        if "login ou senha inválidos" in mensagem or "usuário ou senha inválido" in mensagem:
            print("Notificação de erro de login detectada!")
            return False
        return True
    except Exception as e:
        return True

def perform_login(driver, login, senha):
    """Insere credenciais e realiza a verificação de login"""
    for char in login:
        driver.find_element(By.ID, "UsuarioUsername").send_keys(char)
        time.sleep(0.3)

    for char in senha:
        driver.find_element(By.ID, "UsuarioPassword").send_keys(char)
        time.sleep(0.3)

    botao_login = driver.find_element(By.XPATH, "/html/body/section/div[1]/div[1]/form/div[4]/div[2]/button")
    botao_login.click()

    if verify_credentials_on_login(driver):
        wait_element_be_visible(driver, By.LINK_TEXT, "Financeiro", PAGE_WAIT_TIME)
        print("Login realizado com sucesso!")
        return True
    else:
        return "invalid-credentials"

def navigate_to_invoice_page(driver):
    """Realiza a navegação da pagina pós login até a pagina de faturas"""
    try:
        driver.find_element(By.LINK_TEXT, "Financeiro").click()
        wait_element_be_visible(driver, By.LINK_TEXT, "Faturas", PAGE_WAIT_TIME)
        driver.find_element(By.LINK_TEXT, "Faturas").click()

        try:
            wait_element_be_visible(driver, By.ID, "DataTables_Table_0", timeout=PAGE_WAIT_TIME)
            return "has-invoice"
        except:
            wait_element_be_visible(driver, By.XPATH, "//h4[text()='Nenhum registro foi encontrado.']", timeout=PAGE_WAIT_TIME)
            return "no-invoice"
    except Exception as e:
        raise Exception(f"Erro durante navegação para página de faturas: {e}")

def perform_logout(driver):
    try:
        botao_usuario = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/button")
        botao_usuario.click()
        time.sleep(0.5)  # pequena pausa para abrir o menu

        menu = driver.find_element(By.CSS_SELECTOR, "ul.dropdown-menu.pull-right")
        sair = menu.find_element(By.TAG_NAME, "a")
        sair.click()

        wait_element_be_visible(driver, By.ID, "UsuarioUsername", timeout=PAGE_WAIT_TIME)
        return True
    except Exception as e:
        print(f"Erro ao tentar realizar logoff: {e}")
        return False

