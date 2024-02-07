import whisper
import string
import keyboard
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import keyboard
import numpy as np

def clean_command(command: str) -> str:
    """
    Nettoie la commande vocale reçue.

    :param command: Commande vocale sous forme de chaîne de caractères.
    :return: Commande nettoyée.
    """
    return command.lower().translate(str.maketrans('', '', string.punctuation)).strip()

def map_command_to_action(command: str) -> str:
    """
    Traduit la commande vocale en action spécifique pour le robot.

    :param command: Commande vocale nettoyée.
    :return: Action spécifique pour le robot.
    """
    records = {
        "stand up": "standUp",
        "up": "standUp",
        "sit down": "standDown",
        "down": "standDown",
        "sit": "standDown",
        "stand down": "standDown",
        "dance": "dance1",
        "dance one": "dance1",
        "dance two": "dance2",
        "left": "turnLeft",
        "jump": "jumpYaw",
    }
    print(command)

    return records.get(command, "Command not found.")

def transcribe_audio_with_whisper(audio_path: str) -> str:
    """
    Utilise Whisper pour transcrire l'audio en texte.

    :param audio_path: Chemin vers le fichier audio à transcrire.
    :return: Texte transcrit.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

def process_voice_command(audio_path: str) -> str:
    """
    Traite une commande vocale en utilisant Whisper pour la transcription,
    nettoie la transcription, et la mappe à une action de robot.

    :param audio_path: Chemin vers le fichier audio contenant la commande vocale.
    :return: Commande spécifique pour le robot.
    """
    transcription = transcribe_audio_with_whisper(audio_path)
    clean_cmd = clean_command(transcription)
    robot_command = map_command_to_action(clean_cmd)
    print(f"Mapped command: {robot_command}")  # Pour débogage
    return robot_command

def record_audio():
    # Paramètres de configuration
    sample_rate = 44100  # Fréquence d'échantillonnage
    channels = 1  # Stéréo
    filename = "recording.wav"  # Nom du fichier pour l'enregistrement
    print("Appuyez sur espace pour commencer l'enregistrement...")
    keyboard.wait("space")
    print("Enregistrement... Appuyez sur espace pour arrêter.")

    recordings = []

    def callback(indata, frames, time, status):
        recordings.append(indata.copy())

    with sd.InputStream(samplerate=sample_rate, channels=channels, callback=callback):
        keyboard.wait("space")
        print("Enregistrement terminé.")

    recording = np.concatenate(recordings, axis=0)
    write(
        filename, sample_rate, recording
    )  # Enregistre l'audio dans le fichier spécifié
    return filename
