# Huai-Yuan (Hamilton) Chang

New Taipei, Taiwan · +886 934 027 001 · hamiltonchangwork@gmail.com  
[LinkedIn](https://www.linkedin.com/in/huai-yuan-chang-63074517a/)

**AI R&D Lead | Computer Vision · Edge AI · ML Product Delivery**

## Professional Summary

Hands-on AI R&D lead managing approximately **6–7 engineers**, with experience spanning CV model training, evaluation, inference optimization, edge deployment, and API/SDK integration. Led LumeFace edge optimization, reducing tablet pipeline call latency from **500–600 ms to 30–40 ms**, and on-schedule delivery of **protective clothing and fall detection for AIONXIS v1.2**. Diagnoses failures across models, tracking, and rules; balances recognition quality, hardware constraints, and product requirements, and drives delivery through technical guidance, delegation, and cross-functional coordination.

## Experience

### ioNetworks | New Taipei, Taiwan

**Assistant Technical Manager (AI R&D Department Lead) | Oct. 2025 – Present**

- Lead approximately **6–7 engineers**, owning technical planning, resource allocation, and personnel decisions while contributing to architecture and core development. Assign project leads, typically senior engineers, and use **1-on-1s and technical guidance** to align assignments with development interests.
- Led **LumeFace AI SDK CPU-to-NPU optimization on MTK Genio 700**: reduced face detection / embedding model inference from **133 / 228 ms to 9 / 19 ms**, respectively, and tablet pipeline call latency from **500–600 to 30–40 ms** after integration. Evaluated conversion and mixed-precision trade-offs against recognition quality, target use cases, and hardware constraints; passed internal acceptance testing on the target hardware.
- Conducted internal matching tests with a **10,000-entry face database**, passing internal quality acceptance testing with the original threshold unchanged. Also completed **Qualcomm RB3** porting and internal acceptance testing, extending hardware support for the same SDK.
- Led refactoring, official releases, and ongoing optimization of **AIONXIS's DSE AI engine (DeepStream) and LumeFace AI services (Triton, RESTful API, and AI SDK)**; LumeFace API is also offered as a standalone product. Led on-schedule delivery of **2 capabilities—protective clothing and fall detection—for AIONXIS v1.2**.
- Addressed **DSE line-crossing detection failures** by proposing circle–ROI overlap to resolve missed triggers near frame boundaries and guiding implementation. Prioritized deduplication and geometric triggering fixes within the release schedule, deferring model classification improvements based on functional impact, data availability, and development time. Delivered the rule fixes on schedule and passed **SQA testing of rule behavior**.
- Prioritize fixes by impact and technical component, guide developers, and align estimates and **delivery timelines with PM**. Coordinate cross-functional work for model optimization and backend/middleware interface changes. For critical issues that delay delivery, communicate the full solution and timeline alongside **1–2 short-term alternatives**.
- Owned planning and task allocation, leading **4 developers to complete Phase 1 of Local Engineering Agent in approximately 2–3 months** for internal multi-user use, with personal memory, MCP/RAG access controls, and department GitLab integration.

**Senior AI Algorithm Engineer | Oct. 2022 – Oct. 2025**

- Contributed to the **MediaTek person Re-ID project**, covering model development, internal training/evaluation tools, and edge deployment; demonstrated at **ISC 2024**.
- Developed a bus-stop mask detection model for **steep camera angles and long-distance views**, using General Focal Loss, attention mechanisms, and Bag of Freebies. Evaluated scene suitability on a validation set including **camera tilt angles of up to 70°** and long-distance imagery.
- Developed a **YOLOv10 training framework combining knowledge distillation and learning from unlabeled data**, providing teammates with tools for detection model development in commercial video analytics.
- Integrated inference and deployment using **TensorRT, CUDA/PyCUDA, and shared memory**; developed **GPU-based NMS** on NVIDIA Jetson and contributed to DeepStream video analytics development.

### Infortrend Technology | New Taipei, Taiwan

**AI Research and Development Engineer | May 2021 – July 2022**

- Led development of an **AI Service API platform** for face detection and recognition inference. Used **shared memory** to share face embedding databases across processes and **TensorRT/CUDA** to optimize NVIDIA Jetson inference.
- Developed an **Auto Tiering model** for storage systems. To meet a **24-hour prediction requirement** beyond the initial short-term access forecast, added features including file type, revised time intervals, and reframed access classification as a file-hotness regression problem for storage workload optimization.

### Earlier Experience

- **Patere Technologies | Computer Vision Engineer | Nov. 2020 – Jan. 2021:** Developed remote interview attention analysis and speech-feature analysis capabilities.
- **Lenovo Research | Computer Vision & AI Algorithm Intern | Aug. 2019 – Nov. 2019:** Developed commodity detection models for unmanned retail, including data collection and training optimization.
- **Zero Zero Robotics | Computer Vision & AI Algorithm Intern | Nov. 2018 – Aug. 2019:** Contributed to long-term object tracking development and optimization for Hover 2, integrating correlation-filter tracking and Re-ID strategies.

## Skills

- **Computer Vision & ML:** Object detection, person Re-ID, tracking, face recognition, model evaluation, scene-specific error analysis; Python, C++, PyTorch, TensorFlow, OpenCV, knowledge distillation.
- **Edge AI & Inference:** NVIDIA Jetson, MediaTek Genio 700, Qualcomm RB3, TensorRT, ONNX, CUDA/PyCUDA, DeepStream, TFLite.
- **ML Systems & Engineering Tools:** Triton, RESTful APIs/SDKs, FastAPI, Docker, Kubernetes, Linux, GitLab CI, shared memory; internal document/code RAG, hybrid retrieval, knowledge base integration.
- **Leadership & Delivery:** Technical planning, resource allocation, project ownership, technical guidance, 1-on-1s, mentoring, personnel decisions, release prioritization, cross-functional coordination.

## Education

- **Peking University | M.E. in Software Engineering | Sept. 2017 – Aug. 2020**
- **Chung Yuan Christian University | B.S. in Computer Science and Information Engineering | Sept. 2013 – June 2017**

<!-- v0.8 | 2026-11-11 | Berry AI ML Team Lead. Based on v0.7, historical resumes, and user-confirmed DSE/LumeFace case discussions. Model inference, tablet pipeline latency, and database quality tests have distinct measurement scopes; pipeline timing boundaries remain subject to the v0.6 verification notes. DSE rule fixes are not assigned to v1.2 and do not imply resolution of model classification issues. See Resume_BerryAI_審視與案例補充.md and the v0.6 data verification notes. -->
