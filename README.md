🎵 多智能体驱动的“听、创、赏”一体化音乐教学平台 🤖
💡 项目初衷：解决传统音乐教学中知识符号与情感体验的断层，跨越传统经典与现代数字思维的认知鸿沟，让学生从“被动听众”转变为“主动创作者”。本项目通过极低的使用门槛和简易的部署流程，致力于在教育领域普及 AI 音乐创作。

👤 项目作者：杜羽禾
🏫 所属单位：深圳中学科技高中

✨ 核心特性 (Key Features)
本项目主打 轻量级部署 与 零门槛使用，完全符合开源精神，极具教育推广价值：

🎧 听（数字化解析）：基于开源的 CLAP 模型，一键自动识别音频的旋律走势、节拍与 50+ 种情绪标签，将抽象听觉转化为具象数据。

🎹 创（低门槛生成）：核心采用自训练的 MuseLoom 模型。无需专业乐理，学生仅需修改提示词（如将“赛博朋克”改为“印象派”），即可瞬间完成音乐风格的跨维度重组。

🖼️ 赏（跨模态感知）：集成 SeedDance 2.0（字节跳动），根据生成的音乐流派自动渲染深度契合的视觉图景，打破“不可见”的审美屏障。

🚀 开箱即用：前端提供基于 Canvas 2D 的实时动态声谱图交互，后端核心语义理解由 DeepSeek V4 API 驱动，大幅降低本地算力要求。

🏗️ 架构与技术栈 (Tech Stack)
本项目采用模块化多智能体协同架构，高度解耦，便于二次开发与复现：

🧠 语义逻辑中心：DeepSeek V4 (深度求索)

🎼 定制音乐基座：MuseLoom (基于 Musicgen 的深度微调模型)

📊 跨模态分析：CLAP (Contrastive Language-Audio Pretraining)

🤖 智能体编排：Dify / 扣子 (Coze) 智能体流

🎨 视觉与前端：Canvas 2D (动态声谱图), Echarts (交互式看板), SeedDance 2.0 (视觉图景生成)

📁 目录结构 (File Structure)
Plaintext
music-teaching-platform/
├── 📂 frontend/                 # 前端展示模块
│   ├── index.html               # 交互式主界面
│   ├── js/
│   │   ├── spectrum_render.js   # 基于 Canvas 2D 的能量密度实时映射代码
│   │   └── echarts_board.js     # 基于 Echarts 的音频特征看板代码
├── 📂 backend/                  # 后端与智能体流
│   ├── agent_workflows/         # Dify/Coze 导出的智能体流配置文件 (JSON/YAML)
│   └── api_server.py            # 连接前后端与各个 AI 节点的网关服务
├── 📂 models/                   # 核心模型文件与微调脚本
│   ├── clap_analysis/           # CLAP 语义特征提取模块 (梅尔频谱处理)
│   ├── museloom_finetune/       # MuseLoom 自训练与微调脚本
│   │   ├── dataset/             # 高中音乐全风格乐库 (示例与数据结构)
│   │   └── train_musicgen.py    # 基于 Musicgen 架构的深度微调(Fine-tuning)代码
│   └── seeddance_integration/   # 跨模态视觉生成 API 调用封装
├── 📄 requirements.txt          # Python 依赖清单
└── 📄 README.md                 # 项目说明文档
🛠️ 安装与部署 (Installation)
本项目坚持“安装容易”的原则，推荐使用虚拟环境进行隔离部署。

1. 基础环境准备
Bash
git clone https://github.com/your-username/music-teaching-platform.git
cd music-teaching-platform
python -m venv venv
source venv/bin/activate  # Windows 用户请使用 venv\Scripts\activate
pip install -r requirements.txt
2. 配置环境变量
复制 .env.example 文件并重命名为 .env，填入必需的 API Keys：

代码段
DEEPSEEK_API_KEY="your_deepseek_v4_api_key"  # 必需，用于语义逻辑中心
COZE_API_TOKEN="your_coze_token"             # 必需，用于调用编排好的工作流
3. 下载自训练 MuseLoom 权重
为降低复现门槛，我们将基于“高中音乐全风格乐库”微调好的 MuseLoom 权重开源。

Bash
# 在 models/museloom_finetune 目录下执行
wget https://huggingface.co/your-repo/MuseLoom/resolve/main/model.safetensors
4. 启动服务
Bash
python backend/api_server.py
访问 http://localhost:8080 即可开启音乐探索之旅！

🎛️ MuseLoom 微调指南 (Fine-tuning Guide)
对于希望自行扩充曲库的教育工作者，我们提供了极其简单的微调接口。MuseLoom 模型针对乐器特性与流派脉络进行了深度优化。

数据准备
准备你的音频数据（.wav 或 .mp3），并按照以下结构放置在 models/museloom_finetune/dataset/ 下，系统会自动提取对应的语义描述。

执行微调 (Fine-tuning)
Bash
cd models/museloom_finetune
python train_musicgen.py \
  --dataset_path ./dataset \
  --epochs 50 \
  --batch_size 4 \
  --output_dir ./checkpoints
提示：由于本项目采用高效微调策略，消费级单卡（如 RTX 3060/4060）即可在数小时内完成教学级微调。

💡 使用指南 (Usage)
平台的操作流程极其直观，符合“听、创、赏”的教学认知路径：

🎧 智能聆听与解析

上传一段原版音频文件。

观察前端 Canvas 2D 实时渲染的动态声谱图。

系统后台调用 CLAP 模型，自动提取出包含力度、情绪、速度等信息的提示词（如：“风格:文艺复兴 + 情绪:激昂”）。

🎹 逆向提示词与重组生成

DeepSeek V4 与 Dify 智能体会将上一步提取的结构化数据转化为可编辑的创作“配方”。

低门槛操作：学生直接在界面上微调提示词（例如，将风格标签从 赛博朋克 替换为 印象派）。

点击生成，MuseLoom 模型将结合原始旋律骨架，瞬间产出个性化的音乐曲目。

🖼️ 跨维度多维鉴赏

等待几秒钟，SeedDance 2.0 会根据新生成的音乐特征（如“宏大”或“哀婉”）自动输出深度契合的视觉画卷。

系统会将“原曲视觉”与“重构视觉”进行并置对比，辅助学生建立立体的审美判别力。

🤝 贡献指南 (Contributing)
我们非常欢迎来自开源社区与教育界的 Pull Requests！

如果您是 AI 开发者，欢迎优化提示词逆向工程的 Agent 逻辑。

如果您是一线教师，欢迎提供更多不同风格的教学乐库来增强 MuseLoom 的表现力。

请确保提交的代码符合项目的“低门槛、易部署”核心思想。

🌟 如果这个项目对你的教学或学习有帮助，请给它点个 Star 吧！
