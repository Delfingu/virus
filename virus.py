import keyboard # Ações do teclado;
import pyautogui # Mover mouse;
from pywinauto import Application # Alternar janelas;
from pynput.mouse import Button, Controller # Ações do mouse;
import time, subprocess # Tempo, delays e CMD;

mouse = Controller()

def esperar(tempo):
  time.sleep(tempo)

def click(numClicks, esquerdoOuDireito):
  for x in range(0, numClicks):
    match esquerdoOuDireito:
      case 1: # Click Esquerdo;
        mouse.press(Button.left)
        mouse.release(Button.left)
      case 2: # Click Direito;
        mouse.press(Button.right)
        mouse.release(Button.right)

def mover(x, y, duração):
  pyautogui.moveTo(x, y, duration=duração)

def escrever(texto):
  keyboard.write(texto)

def botaoTeclado(botão):
  keyboard.press_and_release(botão)

# TODO: Adaptar para funcionar com hotkeys de 3 teclas ou mais;
def hotkey(tecla1, tecla2):
  pyautogui.hotkey(tecla1, tecla2)

# TODO: Precisa funcionar com aplicativos com sub processos;
def alternarJanela(nomeJanela):
  app = Application().connect(title_re=nomeJanela)
  app.top_window().set_focus()

# TODO: Encontrar jeito de deixar stealth ou de limpar histórico do Windows + R;
def winR(action):
  hotkey("win", "r")
  escrever(action)
  botaoTeclado("enter")

def interceptar(mensagem):
  winR(f"cmd /c PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}')")

def runCMD(fecharPosExecucao, comandoCMD):
  if fecharPosExecucao: # Fechar pós execução (True);
    winR(f"cmd /c {comandoCMD}")
  else: # Manter aberto (False);
    winR(f"cmd /k {comandoCMD}")