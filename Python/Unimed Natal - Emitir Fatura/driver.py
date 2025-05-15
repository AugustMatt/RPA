from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def start_driver(download_path):
    """Inicializa o WebDriver com as configurações desejadas."""
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # Opção para criar uma pasta de downloads no diretorio do script
    options.add_experimental_option("prefs", {
        "printing.print_preview_sticky_settings.appState": """
            {
              "recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
              "selectedDestinationId": "Save as PDF",
              "version": 2
            }
        """,
        "savefile.default_directory": download_path,
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    })

    # Opção para permitir o "salvar como PDF" em um arquivo aberto no navegador
    options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    return driver
