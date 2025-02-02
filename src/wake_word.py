import pvporcupine
import pyaudio
import struct

class WakeWordDetector:
    def __init__(self, keyword_paths):
        self.keyword_paths = keyword_paths
        self.porcupine = pvporcupine.create(keyword_paths=keyword_paths)
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def run(self):
        print("Listening for wake word...")
        while True:
            pcm = self.audio_stream.read(self.porcupine.frame_length)
            pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

            keyword_index = self.porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                # Chame a função para iniciar o assistente aqui
                self.start_assistant()

    def start_assistant(self):
        print("Iniciando o assistente...")
        # Implemente a lógica para iniciar o assistente aqui

    def close(self):
        self.audio_stream.close()
        self.pa.terminate()
        self.porcupine.delete()

if __name__ == "__main__":
    keyword_paths = ["path/to/your/keyword/file.ppn"]
    detector = WakeWordDetector(keyword_paths)
    try:
        detector.run()
    except KeyboardInterrupt:
        detector.close()
