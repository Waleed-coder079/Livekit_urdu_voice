# LiveKit Urdu Voice Agent

A real-time conversational voice assistant in Urdu using LiveKit, RunPod serverless endpoints, and open-source models.

## Features

- **Speech-to-Text (STT)**: Urdu speech recognition via RunPod
- **Large Language Model (LLM)**: Urdu text generation via RunPod  
- **Text-to-Speech (TTS)**: Urdu speech synthesis via RunPod
- **Voice Activity Detection (VAD)**: Silero VAD for automatic speech detection
- **Real-time Processing**: LiveKit agents framework for live conversations

## Project Structure

```
livekit-agent/
├── livekit_basic_agent.py      # Main LiveKit agent entry point
├── runpod_client.py             # RunPod API client with polling
├── runpod_stt.py               # Speech-to-Text adapter
├── runpod_llm.py               # Language Model adapter
├── runpod_tts.py               # Text-to-Speech adapter
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
├── start-agent.ps1             # PowerShell startup script
├── stop-agent.ps1              # PowerShell shutdown script
└── README.md                    # This file
```

## Prerequisites

- Python 3.9+
- RunPod account with deployed endpoints for:
  - STT (Speech-to-Text)
  - LLM (Language Model)
  - TTS (Text-to-Speech)
- CUDA-capable GPU (for local processing)

## Installation

1. **Clone/Setup the project**
   ```powershell
   cd d:\Waleed Ali\Desktop\livekit-agent
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create/update `.env` file:
   ```env
   RUNPOD_API_KEY=your_runpod_api_key
   RUNPOD_ENDPOINT_ID=your_endpoint_id
   ```

## Configuration

### Environment Variables

- `RUNPOD_API_KEY`: Your RunPod API key for authentication
- `RUNPOD_ENDPOINT_ID`: Your RunPod endpoint ID (default: v4zb6mwe5sdx7g)

### Timeout Settings

The default STT timeout is set to **300 seconds (5 minutes)** in `runpod_stt.py`. Adjust if needed:

```python
# In runpod_stt.py
result = call_runpod_sync(payload, timeout=300)  # Increase/decrease as needed
```

## Usage

### Start the Agent

```powershell
./start-agent.ps1
```

The agent will:
1. Initialize LiveKit components (STT, LLM, TTS, VAD)
2. Start listening for audio input
3. Greet the user in Urdu
4. Wait for user input and respond conversationally

### Stop the Agent

```powershell
./stop-agent.ps1
```

Or press `Ctrl+C` in the terminal.

## How It Works

### Speech Pipeline

1. **Audio Input**: Captured via microphone (Conexant ISST Audio or system audio)
2. **VAD**: Silero detects speech boundaries (10-second timeout)
3. **STT**: Audio sent to RunPod Urdu Whisper model
4. **LLM**: Transcribed text sent to RunPod for Urdu response generation
5. **TTS**: Generated text sent to RunPod for Urdu speech synthesis
6. **Audio Output**: Synthesized audio played back to user

### Key Components

#### `runpod_client.py`
- Handles async/sync API calls to RunPod
- Implements job polling with configurable timeout
- Cleans payloads to remove None/NotGiven values

#### `runpod_stt.py`
- Converts LiveKit audio frames to WAV format
- Encodes audio as base64 for transmission
- Handles STT results and returns SpeechEvent

#### `runpod_llm.py`
- Sends transcribed text to LLM endpoint
- Returns generated Urdu response text

#### `runpod_tts.py`
- Sends response text to TTS endpoint
- Decodes base64 audio response
- Returns raw audio bytes for playback

#### `livekit_basic_agent.py`
- Main orchestrator using LiveKit AgentSession
- Initializes STT, LLM, TTS, and VAD
- Handles greeting and continuous conversation loop

## Testing

### Test Individual Components

```powershell
# Test RunPod connection
python test.py

# Test STT locally
python -c "from runpod_stt import RunPodSTT; print('STT loaded')"

# Test LLM locally
python -c "from runpod_llm import RunPodLLM; print('LLM loaded')"

# Test TTS locally
python -c "from runpod_tts import RunPodTTS; print('TTS loaded')"
```

## Troubleshooting

### "Timeout" Errors
- Increase timeout in `runpod_client.py` (currently 300 seconds)
- Check RunPod endpoint status
- Verify API key and endpoint ID

### "No audio returned"
- Ensure RunPod handlers return audio in base64 format
- Check response format in handler.py

### "Whisper not installed"
- Run: `pip install openai-whisper`

### Audio Quality Issues
- Check microphone input levels
- Verify VAD settings in `livekit_basic_agent.py`
- Ensure audio sample rate is 16kHz

## API Response Format

### STT Response
```json
{
  "text": "سلام علیکم"
}
```

### LLM Response
```json
{
  "response": "وعلیکم السلام، میں آپ کی کیسے مدد کر سکتا ہوں؟"
}
```

### TTS Response
```json
{
  "audio_b64": "UklGRiYAAABXQVZFZm10..."
}
```

## Performance Notes

- **STT Processing**: 3-10 seconds (depends on audio length)
- **LLM Generation**: 2-5 seconds
- **TTS Synthesis**: 1-3 seconds
- **Total Round Trip**: ~10-20 seconds

## Deployment

To deploy on RunPod:

1. Push code to GitHub
2. Create Docker image with `Dockerfile`
3. Deploy handler.py as RunPod serverless endpoint
4. Update endpoint IDs in `.env`

## License

Open source

## Support

For issues or questions about:
- **LiveKit**: https://docs.livekit.io
- **RunPod**: https://docs.runpod.io
- **Whisper**: https://github.com/openai/whisper
