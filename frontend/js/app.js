const audioState = {
  originalUrl: "./../data/samples/sample_audio.wav",
  generatedUrl: "./../data/samples/generated_demo.wav"
};

async function loadDemo() {
  const editor = document.getElementById("promptEditor");
  const promptTags = editor.value
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);

  let data;
  try {
    data = await loadFromApi(promptTags);
  } catch (error) {
    data = await loadFromMock();
    data.runtime = {
      source: "mock",
      reason: error.message
    };
  }

  renderAnalysisCards(data.analysis);
  renderSpectrum("spectrumCanvas", data.analysis.spectrum_bins);
  renderFeatureBoard(data.analysis);
  renderRuntimeInfo(data);
  renderNarrative(data);
  renderAudioPlayers(data);

  const visualPrompt = document.getElementById("visualPrompt");
  visualPrompt.textContent = data.visualization.visual_prompt;

  const resultJson = document.getElementById("resultJson");
  resultJson.textContent = JSON.stringify(data, null, 2);

  const runtimeBadge = document.getElementById("runtimeBadge");
  const source = data.runtime?.source === "api" ? "后端接口模式" : "本地 Mock 模式";
  runtimeBadge.textContent = source;
}

async function loadFromApi(promptTags) {
  const response = await fetch("http://localhost:8080/api/demo-flow", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      audio_name: "sample_audio.wav",
      classroom_context: "高中音乐鉴赏课",
      prompt_tags: promptTags,
      preserve_melody: true
    })
  });

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }

  const data = await response.json();
  data.runtime = {
    source: "api"
  };
  return data;
}

async function loadFromMock() {
  const response = await fetch("./mock/sample_result.json");
  return response.json();
}

function renderRuntimeInfo(data) {
  const runtimeInfo = document.getElementById("runtimeInfo");
  const items = [
    {
      title: "数据来源",
      content: data.runtime?.source === "api" ? "当前结果来自本地后端 API。" : "当前结果来自本地 mock 数据。"
    },
    {
      title: "生成音频",
      content: data.generation.output_audio
    },
    {
      title: "模型状态",
      content: `${data.analysis.status} / ${data.generation.status} / ${data.visualization.status}`
    }
  ];

  runtimeInfo.innerHTML = items
    .map(
      (item) => `
        <article class="status-item">
          <strong>${item.title}</strong>
          <p>${item.content}</p>
        </article>
      `
    )
    .join("");
}

function renderNarrative(data) {
  const element = document.getElementById("demoNarrative");
  const styleTags = data.analysis.style_tags.join("、");
  const moodTags = data.analysis.mood_tags.join("、");
  element.textContent =
    `这段样例音频首先经过 CLAP 风格的分析模块，提取出 ${styleTags} 等风格特征，以及 ${moodTags} 等情绪标签。` +
    `随后学生可以直接修改提示词，由 MuseLoom 对原始旋律进行风格重构，最后再由 SeedDance 风格的视觉模块生成可供鉴赏的画面描述。`;
}

function renderAudioPlayers(data) {
  const originalAudio = document.getElementById("originalAudio");
  const generatedAudio = document.getElementById("generatedAudio");
  const audioFileName = document.getElementById("audioFileName");

  originalAudio.src = audioState.originalUrl;
  generatedAudio.src = data.generation.output_audio || audioState.generatedUrl;
  audioFileName.textContent = data.analysis.audio_name || "sample_audio.wav";
}

const audioInput = document.getElementById("audioInput");
audioInput.addEventListener("change", () => {
  const file = audioInput.files && audioInput.files[0];
  if (!file) {
    return;
  }

  const objectUrl = URL.createObjectURL(file);
  audioState.originalUrl = objectUrl;
  document.getElementById("originalAudio").src = objectUrl;
  document.getElementById("audioFileName").textContent = file.name;
});

function renderAnalysisCards(analysis) {
  const cards = [
    { label: "风格", value: analysis.style_tags.join(", ") },
    { label: "情绪", value: analysis.mood_tags.join(", ") },
    { label: "速度", value: `${analysis.tempo_bpm} BPM` },
    { label: "教学用途", value: analysis.teaching_hint }
  ];

  const container = document.getElementById("analysisCards");
  container.innerHTML = "";

  cards.forEach((item) => {
    const card = document.createElement("article");
    card.className = "metric-card";
    card.innerHTML = `
      <div class="metric-label">${item.label}</div>
      <div class="metric-value">${item.value}</div>
    `;
    container.appendChild(card);
  });
}

document.getElementById("runDemoButton").addEventListener("click", () => {
  loadDemo().catch((error) => {
    const resultJson = document.getElementById("resultJson");
    resultJson.textContent = `Demo load failed: ${error.message}`;
  });
});

loadDemo().catch(() => {});
