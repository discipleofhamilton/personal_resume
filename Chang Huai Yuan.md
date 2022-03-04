<font size=5 face="Times New Roman">**Chang Huai-Yuan**</font>

<font face="Times New Roman">Chaiyi, Taiwan  -  (+886) 0934027001  -  hamiltonchangwork@gmail.com / hamiltonchang@pku.edu.cn</font>

<font face="Times New Roman">**Applied Position: Computer Vision and C++ Engineer**</font>

## <font face="Times New Roman">Education</font>

* <font size=4 face=Times New Roman>**Peking University**, Beijing, China</font><img src=".\assets\pku.png" align='right' height="10%" width="10%"/>

  <font face="Times New Roman">**M.E. in Software Engineering**, Sept. 2017 - Aug. 2020</font>

  * <font face="Times New Roman">Graduate thesis: Design and Implement of Real-time Long-term Single-person Tracking System</font>

* <font size=4 face="Time New Roman">**Chung Yuan Christian
  University**, Chungli, Taiwan</font><img src=".\assets\CYCU.png" align='right' height="10%" width="10%"/>

  <font face="Times New Roman">**B.S. in Computer Science and Information Engineering**, Sept. 2013 - June 2017</font>

  - <font face="Times New Roman">Graduate thesis: Face Recognition Access Control System Based on Raspberry Pi</font>

## <font face="Times New Roman">Experience</font>

- <font size=4 face="Times New Roman">**Infortrend Technology**, Taiwan, New-Taipei</font><img src="./assets/infortrend.png" align='right' height="15%" width="15%"/>

  <font face="Times New Roman">**AI Research and Develop Engineer**, May.2021-now</font>

  - <font face="Times New Roman">Analized the reason why the board system which contains AI models on NVIDIA Xavier is slow with Nsight System and NVTX, and improved about 10% performance with changing the way of using TensorRT models.</font>
  - <font face="Times New Roman">Ported the CMS from NVIDIA Nano to x86 server, packed it into a docker image with a dockerfile, and used a CI/CD script to automatically build and deploy it to the Infortrend devices.</font>
  - <font face="Times New Roman">Led project AI Service API and project Resource Space</font>
    - <font face="Times New Roman">Surveyed Triton Inference Server and regarded Trition Inference Server as AI model server, picking ONNX, TensorRT, and Python backend.</font>
    - <font face="Times New Roman">Developed Face Recognition API:</font>
      1. <font face="Times New Roman">Surveyed Face Detection models, such as MTCNN, CenterFace, RetinaFace, etc., and picked the MTCNN model as the basic model.</font>
      2. <font face="Times New Roman">Surveyed Face Recognition, such as FaceNet, CosFace, ArcFace, etc., selecting FaceNet and ArcFace to provide to users.</font>
      3. <font face="Times New Roman">Utilized shared memory and KD-Tree for face embeddings database to resolve the multi-processes communication issue and accelerate the performance about 3 times.</font>
      4. <font face="Times New Roman">Utilized pruning, uatization and specific hardware acceleration framework(TensorRT) to improve model performance on GPUs.</font>
    - <font face="Times New Roman">Utilized dockerfiles and the technologies like Multi-Stage, delete redundant dependencies, etc. to pack the project and get the minimized docker image size.</font>
    - <font face="Times New Roman">Accelerated the model inference on general CPU platforms, using framework Tensorflow Lite with plugin library XNNPack.</font>
  - <font face="Times New Roman">Developed Auto Tiering AI model for the Infortrend storage systems and accelerated at least 60% IO performance.</font>
    - <font face="Times New Roman">Utilized machine learning model (XGBoost) rather than deep learning model because of the consideration of the storage system performance.</font>
    - <font face="Times New Roman">Implemented the method from the paper to predict whether the files are accessed in the future period because the specification of predicting a day is too long to get the result good enough.</font>
    - <font face="Times New Roman">Implemented a regression model to predict the temperature of the files and improve at least 60% IO performance of the storage system.</font>

- <font size=4 face="Times New Roman">**Patere Technologies, Inc.**, Taipei, Taiwan</font><img src=".\assets\patere.png" align='right' height="15%" width="15%"/>

  <font face="Times New Roman">**Computer Vision Engineer**, Nov. 2020 - Jan. 2021</font>

  - <font face="Times New Roman">Confidence and speech fluency detection</font>
    - <font face="Times New Roman">Surveyed how to detect the speech fluency and confidence of the candidate with speech detection. </font>
    - <font face="Times New Roman">Designed and implemented the rule-based project with basic speech features. Researched more complex and useful features which served for ML/DL, such as MFCC, FBank features.</font>
  - <font face="Times New Roman">Focus detection</font>
    - <font face="Times New Roman">Designed and Implemented the algorithm to check the candidate is focusing or not.</font>
    - <font face="Times New Roman">Accuracy, precision, and recall are all about 80% on the self-record dataset and the fewer testing dataset which acquired from YouTube.</font>

- <font size=4 face="Times New Roman">**Lenovo Group Ltd, Lenovo Research**, Beijing, China</font><img src=".\assets\lenovo-logo.png" align='right' height="15%" width="15%"/>

  <font face="Times New Roman">**Computer Vision and AI Algorithm Intern**, Aug. 2019 - Nov. 2019</font>

  - <font face="Times New Roman">Developed automatic training system for commodity detection based on RetinaNet for unmanned stores, and found the reason resulted in low detect success rate by analyzing the testing result</font>
  - <font face="Times New Roman">Increased the success rate of commodity detection about 20% through collecting and generating the more complicated and suitable data to train the model</font>

- <font size=4 face="Times New Roman">**Zero Zero Robotics**, Beijing, China</font><img src=".\assets\zerozero-logo.png" align='right' height="16%" width="16%"/>

  <font face="Times New Roman">**Computer Vision and AI Algorithm Intern**, Nov. 2018 - Aug. 2019</font>

  - <font face="Times New Roman">Involved in Hover 2 drone development</font>
    - <font face="Times New Roman">Researched and tested object tracking and Template Matching Algorithms, and analyzed their advantages and shortcomings</font>
    - <font face="Times New Roman">Implemented, maintained and optimized long-term object tracking function</font>
    - <font face="Times New Roman">Increased the success rate of object tracking function by 15%, and CPU utility decreased by 5% through adding constraints and modifying object re-identification strategy</font>
  - <font face="Times New Roman">Designed and researched binocular face recognition access control system</font>
    - <font face="Times New Roman">Studied the algorithms of face detection and recognition (MTCNN, FaceNet, and FaceBoxes) </font>
    - <font face="Times New Roman">Tried to achieve face anti-spoofing with binocular</font>

## <font face="Times New Roman">Competition</font>

* <font size=4 face="Times New Roman">**IBM Watson Build Competition: Clothes Master**</font>

  <font face="Times New Roman">**Team Leader**, May 2018 - June 2018</font>

  - <font face="Times New Roman">**2nd place in China**</font>
  - <font face="Times New Roman">Implemented a personal dress recommendation web which based on IBM Watson chatbot</font>
  - <font face="Times New Roman">Achieved  front-end(Javascript) and back-end(Node.js)</font>
  - <font face="Times New Roman">Designed software architecture and main functions, and Implemented them</font>

## <font face="Times New Roman">Project</font>

- <font size=4 face="Times New Roman">**Design and Implementation of Real-time Long-term Single Person Tracking System**</font>

  <font face="Times New Roman">**Individual Work**, Nov. 2019 - April. 2020</font>

  - <font face="Times New Roman">Utilized two trackers to reach the goal, one is the tracker based on pose estimation, and the other is object tracking</font>
  - <font face="Times New Roman">Divided the tracker into three states: target selection, track and retrieval, to facilitate the design and implementation</font>
  - <font face="Times New Roman">Designed and Developed several methods to achieve the goal of real-time and stable long-term person tracking</font>
  - <font face="Times New Roman">Regarded self-collection and self-record drone dataset as test dataset</font>
  - <font face="Times New Roman">Tracking successful rate is 79.02%. Recall is 77.54%. FPS on computer CPU is 12.87</font>

- <font size=4 face="Times New Roman">**2D Anime Charactors Recognition Based on CNN**</font>

  <font face="Times New Roman">**Team Leader**, May 2018 - June 2018</font>

  - <font face="Times New Roman">Tried to recognize the anime character successfully by the same character but different styles</font>
  - <font face="Times New Roman">Utilized the LBPcascade trained by other developers to detected anime faces</font>
  - <font face="Times New Roman">Utilized Inception v3 of TensorFlow official version to recognize anime figures, and only trained the classifier layer by transfer learning</font>
  - <font face="Times New Roman">**TOP1 result is 73.25%**</font>

- <font size=4 face="Times New Roman">**Scheme Interpreter Implemented in C++**</font>

   <font face="Times New Roman">**Individual Work**, Mar. 2017 - May 2017</font>

     - <font face="Times New Roman">Designed Scanner and Parser, and Binding and Error Message by analyzing Scheme code structure</font>
     - <font face="Times New Roman">Transformed Scheme code into designed logical tree structure</font>

- <font size=4 face="Times New Roman">**Face Recognition Access Control System Based on Raspberry Pi**</font>

   <font face="Times New Roman">**Team Leader**,  Feb. 2016 - Nov. 2016</font>

   - <font face="Times New Roman">Learned and utilized the technologies of face recognition and pre-processing, and balanced the security and praticality during the development</font>
   - <font face="Times New Roman">There are establishment of face key and face recognition two partition of software system, and the systme had ported to Raspberry Pi and send signal to relay to control the electromagnetic induction door lock</font>

## <font face="Times New Roman">Skills</font>

- <font face="Times New Roman">Programming Language: C, C++, Java, R, Python </font>
- <font face="Times New Roman">Other: Git, GDB, Docker, pdb</font>

