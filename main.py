from mqtt_manager import MQTTManager
from voice_commands import *


def main() -> None:
    # Remplacer 'broker_address' par l'adresse réelle de votre broker MQTT
    mqtt_manager = MQTTManager()

    try:
        while True:
            # Enregistrement de l'audio et sauvegarde dans un fichier temporaire
            audio_path = record_audio()

            # Transcription de l'audio et obtention de la commande pour le robot
            robot_command = process_voice_command(audio_path)

            # Envoie la commande au robot via MQTT
            mqtt_manager.client.publish("controller/action", robot_command)
            print(f"Sent command: {robot_command}")

            print("Appuyez sur 'c' pour continuer ou sur 'q' pour quitter.")
            key = keyboard.read_key()
            if key.lower() == "q":
                print("Arrêt du programme.")
                break

    except KeyboardInterrupt:
        print("\nProgram interrupted by the user. Exiting...")


if __name__ == "__main__":
    main()
