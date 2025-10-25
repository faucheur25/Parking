# --- IMPORTS PYTHON ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# --- PARAMÈTRES DE CONNEXION ---
USERNAME = "0686267142"    # ⬅️ Mets ton identifiant PayByPhone
PASSWORD = ".k/rua7N7AJD6zi"   # ⬅️ Mets ton mot de passe PayByPhone

# --- CONFIGURATION CHROME HEADLESS (sans interface graphique) ---
chrome_options = Options()
#chrome_options.add_argument("--headless")

# --- LANCEMENT DU NAVIGATEUR ---
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://m2.paybyphone.fr/login")

wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

# --- CONNEXION ---
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Se connecter']]"))).click()

# --- STATIONNEMENT ---
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='park-button']"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "locationNumber"))).send_keys("75011", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.ID, "duration"))).send_keys("7", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='notNow-button']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='pay-button']"))).click()

time.sleep(120)
driver.quit()
