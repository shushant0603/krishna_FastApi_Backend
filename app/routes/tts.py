from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import edge_tts
import io

router = APIRouter()


class TTSRequest(BaseModel):
    text: str


@router.post("/tts")
async def tts(request: TTSRequest):

    communicate = edge_tts.Communicate(
        text=request.text,
#   voice="hi-IN-SwaraNeural" # Indian female voice
   voice="hi-IN-MadhurNeural",
      rate="-2%",
    pitch="-2Hz",
    volume="+0%",
#   voice="hi-IN-MadhurNeural" # Indian male voice


# voice="en-US-AndrewMultilingualNeural"
    )

    audio_buffer = io.BytesIO()

    async for chunk in communicate.stream():

        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])

    audio_buffer.seek(0)

    return StreamingResponse(
        audio_buffer,
        media_type="audio/mpeg"
    )