from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    audio_name: str | None = None
    audio_path: str | None = None
    classroom_context: str | None = None


class AnalyzeResponse(BaseModel):
    audio_name: str
    tempo_bpm: int
    style_tags: list[str]
    mood_tags: list[str]
    teaching_hint: str
    feature_profile: list[int]
    spectrum_bins: list[float]
    status: str


class GenerateRequest(BaseModel):
    prompt_tags: list[str] = Field(default_factory=list)
    source_audio: str | None = None
    preserve_melody: bool = True


class GenerateResponse(BaseModel):
    status: str
    revised_prompt: str
    output_audio: str
    note: str


class VisualizeRequest(BaseModel):
    style_tags: list[str] = Field(default_factory=list)
    mood_tags: list[str] = Field(default_factory=list)
    visual_focus: str | None = None


class VisualizeResponse(BaseModel):
    status: str
    visual_prompt: str
    provider: str
    image_url: str | None = None
    image_path: str | None = None
    task_id: str | None = None


class PromptRevisionRequest(BaseModel):
    style_tags: list[str] = Field(default_factory=list)
    mood_tags: list[str] = Field(default_factory=list)
    teaching_hint: str = ""
    classroom_context: str = ""
    user_prompt_overrides: list[str] = Field(default_factory=list)


class PromptRevisionResponse(BaseModel):
    status: str
    revised_prompt: str
    prompt_tags: list[str]
    provider: str


class DemoFlowRequest(BaseModel):
    audio_name: str | None = None
    audio_path: str | None = None
    classroom_context: str | None = "高中音乐鉴赏课"
    prompt_tags: list[str] = Field(default_factory=list)
    preserve_melody: bool = True


class DemoFlowResponse(BaseModel):
    analysis: AnalyzeResponse
    generation: GenerateResponse
    visualization: VisualizeResponse
