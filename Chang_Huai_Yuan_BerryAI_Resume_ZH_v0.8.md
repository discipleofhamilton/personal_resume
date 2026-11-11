# 張懷元 Huai-Yuan (Hamilton) Chang

新北市，台灣 · +886 934 027 001 · hamiltonchangwork@gmail.com  
[LinkedIn](https://www.linkedin.com/in/huai-yuan-chang-63074517a/)

**AI 研發主管｜電腦視覺 · Edge AI · ML 產品交付**

## 專業摘要

帶領約 **6–7 人 AI 研發團隊**，持續參與架構與核心開發，經驗涵蓋電腦視覺模型訓練、評估、推論優化、邊緣部署與 API／SDK 整合。主導 LumeFace Edge 優化，將平板 pipeline 調用時間由 **500–600 ms 降至 30–40 ms**；帶領團隊如期交付 **AIONXIS v1.2 防塵服與跌倒偵測功能**。擅長從場景錯誤拆解模型、追蹤與規則問題，結合品質、硬體限制與產品需求做出技術取捨，透過開發指導、分工授權與跨部門協調推進交付。

## 工作經歷

### ioNetworks｜台灣，新北市

**Assistant Technical Manager（AI 演算法研發部門主管）｜2025.10 – 至今**

- 帶領約 **6–7 人**團隊，負責技術規劃、資源配置與人事決策，持續參與架構及核心開發；為多人專案指定主導人，通常由資深工程師帶領，並透過 **1-on-1 與開發指導**，結合成員發展方向安排任務。
- 主導 **LumeFace AI SDK 的 MTK Genio 700 CPU→NPU 優化**：人臉偵測／特徵抽取模型推論分別由 **133／228 ms 降至 9／19 ms**；整合至平板後，pipeline 調用時間由 **500–600 降至 30–40 ms**。結合辨識品質評估、目標場景與硬體限制，評估模型轉換及混合精度的效能／品質取捨，通過目標硬體內部驗收。
- 以 **10,000 筆人臉資料庫**進行內部比對測試，在維持原 threshold 下通過內部品質驗收；另完成 **Qualcomm RB3** 移植並通過內部驗收，擴充同一 SDK 的硬體支援。
- 主導 **AIONXIS 的 DSE AI 引擎（DeepStream）與 LumeFace AI 服務（Triton、RESTful API、AI SDK）**重構、正式發佈與持續優化；LumeFace API 亦作為獨立產品提供服務。帶領團隊如期交付 **AIONXIS v1.2 防塵服與跌倒偵測 2 項功能**。
- 針對 **DSE 越線偵測異常**，提出圓形範圍與 ROI 重疊判定方案，指導開發人員實作，改善畫面邊緣漏觸發；依功能影響及資料、工期限制，優先安排去重與幾何觸發規則修復，將模型分類優化列入長期計畫。規則修復如期交付，並通過 **SQA 規則功能測試**。
- 依問題影響與技術環節安排修復、提供開發指導，確認預估工期並向 **PM 同步交付時程**；涉及模型優化或 backend／middleware 介面變更時，協調跨部門工作。對嚴重延期問題，同步完整解法與時程，並提出 **1–2 項短期方案**。
- 負責規劃與分工，帶領 **4 位開發人員於約 2–3 個月完成 Local Engineering Agent 第一階段**並供內部多人使用，交付具個人記憶、MCP／RAG 存取權限與部門 GitLab 整合的工程知識工具。

**Senior AI Algorithm Engineer（資深 AI 演算法工程師）｜2022.10 – 2025.10**

- 參與 **MediaTek 平台行人 Re-ID** 專案，涵蓋模型開發、內部訓練／評估工具與邊緣部署，專案於 **ISC 2024** 展示。
- 針對公車站**大俯角與遠距離**影像開發口罩偵測模型，採用 General Focal Loss、注意力機制與 Bag of Freebies；以包含**攝影機俯角達 70°**及遠距離影像的驗證集評估場景適用性。
- 開發結合**知識蒸餾與未標註資料學習的 YOLOv10 訓練框架**，提供組員開發偵測模型的工具，支援商用影像分析系統研發。
- 使用 **TensorRT、CUDA／PyCUDA、共享記憶體**進行推論與部署整合；開發 NVIDIA Jetson 的 **GPU NMS** 處理，並參與 DeepStream 影像分析開發。

### Infortrend Technology｜台灣，新北市

**AI Research and Development Engineer（AI 研發工程師）｜2021.05 – 2022.07**

- 主導 **AI Service API 平台**開發，建置人臉偵測與辨識推論服務；以**共享記憶體**處理多行程共用人臉特徵資料庫，並使用 **TensorRT／CUDA** 優化 NVIDIA Jetson 推論。
- 開發儲存系統 **Auto Tiering 模型**：面對由短期存取預測延伸至 **24 小時預測**的需求，增加檔案類型等特徵、調整時間區間，並由存取分類改為熱度回歸預測，支援儲存工作負載優化。

### 早期經歷

- **Patere Technologies｜Computer Vision Engineer｜2020.11 – 2021.01**：開發遠端面試注意力與語音特徵分析功能。
- **Lenovo Research｜Computer Vision & AI Algorithm Intern｜2019.08 – 2019.11**：開發無人零售場景商品偵測模型，參與資料蒐集與訓練優化。
- **Zero Zero Robotics｜Computer Vision & AI Algorithm Intern｜2018.11 – 2019.08**：參與 Hover 2 無人機長期物件追蹤開發與優化，整合相關濾波追蹤與 Re-ID 策略。

## 技術專長

- **電腦視覺與模型開發：** 物件偵測、行人 Re-ID、追蹤、人臉辨識、模型評估與場景錯誤分析；Python、C++、PyTorch、TensorFlow、OpenCV、知識蒸餾。
- **Edge AI 與推論：** NVIDIA Jetson、MediaTek Genio 700、Qualcomm RB3、TensorRT、ONNX、CUDA／PyCUDA、DeepStream、TFLite。
- **ML 系統與工程工具：** Triton、RESTful API／SDK、FastAPI、Docker、Kubernetes、Linux、GitLab CI、共享記憶體；內部文件／程式碼 RAG、混合檢索與知識庫整合。
- **團隊與交付管理：** 技術規劃、資源配置、專案責任分工、開發指導、1-on-1、人才培育、人事決策、版本優先順序與跨部門協調。

## 學歷

- **北京大學｜軟體工程碩士｜2017.09 – 2020.08**
- **中原大學｜資訊工程學士｜2013.09 – 2017.06**

<!-- v0.8 | 2026-11-11 | Berry AI ML Team Lead. 以 v0.7 為底，整合歷史履歷與本人確認的 DSE／LumeFace 案例。模型推論、平板 pipeline 與資料庫品質測試為不同量測範圍；pipeline 計時邊界仍沿用 v0.6 查核限制。DSE 規則修復未指定為 v1.2，亦不代表模型分類問題已解決。詳見 Resume_BerryAI_審視與案例補充.md 及 v0.6 數據查核。 -->
