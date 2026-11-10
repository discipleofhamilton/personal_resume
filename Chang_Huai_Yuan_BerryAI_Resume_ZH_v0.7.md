# 張懷元 Huai-Yuan (Hamilton) Chang

新北市，台灣 · +886 934 027 001 · hamiltonchangwork@gmail.com  
[LinkedIn](https://www.linkedin.com/in/huai-yuan-chang-63074517a/)

**AI 研發主管｜電腦視覺 · Edge AI · ML 產品交付**

## 專業摘要

帶領約 **6–7 人 AI 研發團隊**，持續參與架構與核心開發，經驗涵蓋電腦視覺模型訓練、評估、推論優化、邊緣部署與 API／SDK 整合。主導 LumeFace Edge 優化，將平板完整 pipeline 調用時間由 **500–600 ms 降至 30–40 ms**；帶領團隊如期交付 AIONXIS v1.2 的 **2 項偵測功能**。優勢在於結合模型品質、硬體效能與產品需求做出技術取捨，並透過分工、授權與驗收推進交付。

## 工作經歷

### ioNetworks｜台灣，新北市

**Assistant Technical Manager（AI 演算法研發部門主管）｜2025.10 – 至今**

- 帶領約 **6–7 人**團隊，持續參與架構及核心開發；在多人專案中指定主導人，通常由資深工程師帶領，並透過 1-on-1 了解成員發展方向、安排分工。負責人事決策，向 CTO／COO 提出技術策略與預算需求，由高階主管核決。
- 主導 **LumeFace AI SDK 的 MTK Genio 700 CPU→NPU 優化**：人臉偵測模型推論由 **133→9 ms（約 14.8 倍加速）**、特徵抽取由 **228→19 ms（12 倍加速）**；整合至 LumeFace 平板後，完整 pipeline 調用時間由 **500–600→30–40 ms**，縮短裝置端辨識流程的等待時間，並完成目標硬體的內部驗收。
- 以 **10,000 筆人臉資料庫**進行內部比對測試，在維持原 threshold 下通過內部品質驗收，作為效能與辨識品質取捨的依據。
- 完成 **Qualcomm RB3** 平台移植，人臉偵測／特徵抽取模型推論分別為 **31／13.5 ms**，通過內部驗收，擴充同一 SDK 的硬體支援。
- 主導 **AIONXIS AI 模組（DeepStream）與 LumeFace AI 服務（Triton、RESTful API、AI SDK）**重構、正式發佈及持續優化；LumeFace API 同時作為獨立產品提供服務。帶領團隊於 **AIONXIS v1.2 如期交付防塵服與跌倒偵測 2 項功能**。
- 負責規劃與分工，帶領 **4 位開發人員於約 2–3 個月完成 Local Engineering Agent 第一階段**並供內部多人使用，交付具個人記憶、MCP／RAG 權限與部門 GitLab 整合的工程知識工具。

**Senior AI Algorithm Engineer（資深 AI 演算法工程師）｜2022.10 – 2025.10**

- 參與 **MediaTek 平台行人 Re-ID** 專案，完成模型開發、內部訓練／評估工具與邊緣部署相關工作，專案於 **ISC 2024** 展示，累積模型、硬體限制與實際場景整合經驗。
- 針對公車站**大俯角與遠距離**影像開發口罩偵測模型，採用 General Focal Loss、注意力機制與 Bag of Freebies 訓練方法；以包含**攝影機俯角達 70°**及遠距離影像的驗證集評估場景適用性。
- 開發結合**知識蒸餾與未標註資料學習的 YOLOv10 訓練框架**，以及物件偵測、人臉辨識與追蹤能力，支援商用影像分析系統開發。
- 使用 **TensorRT、CUDA／PyCUDA、共享記憶體**進行推論與部署整合；開發 NVIDIA Jetson 的 GPU NMS 處理，並參與 DeepStream 影像分析開發。

### Infortrend Technology｜台灣，新北市

**AI Research and Development Engineer（AI 研發工程師）｜2021.05 – 2022.07**

- 主導 **AI Service API 平台**開發，建置人臉偵測與辨識推論服務，提供應用系統整合介面。
- 使用 **TensorRT／CUDA** 優化 NVIDIA Jetson 推論，開發以機器學習進行儲存工作負載優化的 **Auto Tiering 模型**。

### 早期經歷

- **Patere Technologies｜Computer Vision Engineer｜2020.11 – 2021.01**：開發遠端面試注意力與語音特徵分析功能。
- **Lenovo Research｜Computer Vision & AI Algorithm Intern｜2019.08 – 2019.11**：開發無人零售場景商品偵測模型，參與資料蒐集與訓練優化。
- **Zero Zero Robotics｜Computer Vision & AI Algorithm Intern｜2018.11 – 2019.08**：參與 Hover 2 無人機長期物件追蹤開發、維護與優化。

## 技術專長

- **電腦視覺與模型開發：** 物件偵測、行人 Re-ID、追蹤、人臉辨識、模型評估；Python、C++、PyTorch、TensorFlow、OpenCV、知識蒸餾。
- **Edge AI 與推論：** NVIDIA Jetson、MediaTek Genio 700、Qualcomm RB3、TensorRT、ONNX、CUDA／PyCUDA、DeepStream、TFLite。
- **ML 系統與工程知識平台：** Triton、RESTful API／SDK、FastAPI、Docker、Kubernetes、Linux、GitLab CI、共享記憶體；內部文件／程式碼 RAG、dense／sparse／graph 混合檢索、Neo4j／SQLite 異質知識庫與動態路由。
- **團隊與交付管理：** 技術規劃、資源配置、專案責任分工、1-on-1、人才培育、人事決策與跨部門協作。

## 學歷

- **北京大學｜軟體工程碩士｜2017.09 – 2020.08**
- **中原大學｜資訊工程學士｜2013.09 – 2017.06**

<!-- v0.7 | 2026-11-09 | Berry AI ML Team Lead. 模型推論、平板 pipeline 與資料庫品質測試為不同量測範圍；查核事項另見 v0.6 數據查核及 v0.7 編修說明。 -->
