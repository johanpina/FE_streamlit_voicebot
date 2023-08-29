import os 

# The Root Directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_CONFIG = os.path.join(ROOT_DIR, 'logging.yml')
OUT_DIR = os.path.join(ROOT_DIR, 'output/')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DATA_DIR_AUDIO = os.path.join(DATA_DIR, 'audio')
RECORDING_DIR = os.path.join(OUT_DIR, 'recording')
WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")
# Audio configurations
INPUT_DEVICE = 0
MAX_INPUT_CHANNELS = 1  # Max input channels
DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
DURATION = 3   # 3 seconds
CHUNK_SIZE = 1024