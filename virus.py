import keyboard # Ações do teclado;
import pyautogui # Mover mouse;
from pywinauto import Application # Alternar janelas;
from pynput.mouse import Button, Controller # Ações do mouse;
import time, subprocess # Tempo, delays e CMD;

mouse = Controller()

def esperar(tempo):
  try:
    time.sleep(tempo)
  except TypeError: pass

def click(numClicks, esquerdoOuDireito):
  try:
    for x in range(0, numClicks):
      match esquerdoOuDireito:
        case 1: # Click Esquerdo;
          mouse.press(Button.left)
          mouse.release(Button.left)
        case 2: # Click Direito;
          mouse.press(Button.right)
          mouse.release(Button.right)
  except TypeError: pass

def mover(x, y, duração):
  try:
    pyautogui.moveTo(x, y, duration=duração)
  except TypeError: pass

def escrever(texto):
  try:
    keyboard.write(texto)
  except TypeError: pass

def botaoTeclado(botão):
  try:
    keyboard.press_and_release(botão)
  except TypeError: pass

# TODO: Adaptar para funcionar com hotkeys de 3 teclas ou mais;
def hotkey(tecla1, tecla2):
  try:
    pyautogui.hotkey(tecla1, tecla2)
  except TypeError: pass

# TODO: Precisa funcionar com aplicativos com sub processos;
def alternarJanela(nomeJanela):
  try:
    app = Application().connect(title_re=nomeJanela)
    app.top_window().set_focus()
  except TypeError: pass

# TODO: Encontrar jeito de deixar stealth ou de limpar histórico do Windows + R;
def winR(action):
  try:
    hotkey("win", "r")
    escrever(action)
    botaoTeclado("enter")
  except TypeError: pass

def interceptar(mensagem):
  try:
    #winR(f"cmd /c PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}')")
    subprocess.run(f"PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}')")
  except TypeError: pass

def runCMD(fecharPosExecucao, comandoCMD):
  try:
    if fecharPosExecucao: # Fechar pós execução (True);
      winR(f"cmd /c {comandoCMD}")
    else: # Manter aberto (False);
      winR(f"cmd /k {comandoCMD}")
  except TypeError: pass