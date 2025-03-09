from pyexpat import model
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

#หน้าที่3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error
import streamlit as st
import numpy as np
import datetime
#หน้าที่4
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error




# หน้าที่ 1: อธิบายการเตรียมข้อมูลและทฤษฎีของอัลกอริธึม
def data_preparation_and_algorithm_theory():
    st.title("การเตรียมข้อมูลและทฤษฎีของอัลกอริธึม")
    st.write("""
        ในขั้นตอนนี้ เราเริ่มจากการเตรียมข้อมูล โดยการเลือกฟีเจอร์ที่เกี่ยวข้องและการลบข้อมูลที่ขาดหายไป 
        รวมถึงการปรับขนาดข้อมูลเพื่อให้เหมาะสมกับโมเดลที่ใช้
        ทฤษฎีอัลกอริธึมที่ใช้ในโมเดล Machine Learning เช่น Linear Regression, Random Forest, XGBoost, 
        และ Support Vector Machine (SVM) และการทำงานของโมเดล Neural Networks
    """)
    st.title("Demo การทำงานของโมเดล Machine Learning")
    st.write("ระบุที่มาของ Dataset ", "[Food-101 Nutritional Information](https://www.kaggle.com/datasets/sanadalali/food-101-nutritional-information)")
    st.write("รายละเอียด Features ของ Dataset:")
    st.write("""
    1. **Food Name** (ชื่ออาหาร)
    - ชื่อของอาหารในชุดข้อมูลนี้
    - เป็นข้อมูลที่แสดงถึงประเภทหรือชนิดของอาหารที่ถูกเก็บข้อมูล

    2. **Calories** (แคลอรี่)
    - จำนวนแคลอรี่ในหนึ่งหน่วยของอาหาร
    - เป็นตัวชี้วัดที่สำคัญในการประเมินพลังงานที่ได้รับจากการทานอาหาร

    3. **Protein** (โปรตีน)
    - ปริมาณโปรตีนที่มีในอาหารต่อหนึ่งหน่วย
    - โปรตีนเป็นสารอาหารที่จำเป็นต่อการเจริญเติบโตและการซ่อมแซมเนื้อเยื่อในร่างกาย

    4. **Carbohydrates** (คาร์โบไฮเดรต)
    - ปริมาณคาร์โบไฮเดรตที่มีในอาหารต่อหนึ่งหน่วย
    - คาร์โบไฮเดรตเป็นแหล่งพลังงานหลักของร่างกายและมีบทบาทสำคัญในการทำงานของสมองและระบบประสาท

    5. **Fats** (ไขมัน)
    - ปริมาณไขมันในอาหารต่อหนึ่งหน่วย
    - ไขมันเป็นสารอาหารที่ให้พลังงานสูงและสำคัญสำหรับการทำงานของเซลล์และการดูดซึมวิตามิน

    6. **Fiber** (ไฟเบอร์)
    - ปริมาณใยอาหารในอาหารต่อหนึ่งหน่วย
    - ใยอาหารช่วยในการย่อยอาหารและการขับถ่าย รวมถึงช่วยควบคุมระดับน้ำตาลในเลือด

    7. **Sugar** (น้ำตาล)
    - ปริมาณน้ำตาลในอาหารต่อหนึ่งหน่วย
    - น้ำตาลสามารถเพิ่มระดับน้ำตาลในเลือดได้อย่างรวดเร็ว ซึ่งอาจมีผลกระทบต่อการควบคุมระดับน้ำตาลในเลือด

    8. **Sodium** (โซเดียม)
    - ปริมาณโซเดียมในอาหารต่อหนึ่งหน่วย
    - โซเดียมมีบทบาทในการควบคุมการทำงานของระบบไตและความดันโลหิต แต่การบริโภคในปริมาณมากอาจเป็นอันตราย

    9. **Potassium** (โพแทสเซียม)
    - ปริมาณโพแทสเซียมในอาหารต่อหนึ่งหน่วย
    - โพแทสเซียมมีบทบาทสำคัญในการทำงานของกล้ามเนื้อและระบบประสาท

    10. **Cholesterol** (คอเลสเตอรอล)
        - ปริมาณคอเลสเตอรอลในอาหารต่อหนึ่งหน่วย
        - คอเลสเตอรอลมีผลต่อสุขภาพหัวใจและหลอดเลือด หากบริโภคมากเกินไปอาจเพิ่มความเสี่ยงในการเกิดโรคหัวใจ
    """)
    st.title("Demo การทำงานของโมเดล Neural Networks")
    st.write("ระบุที่มาของ Dataset ", "[Kaggle Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)")
    st.write("รายละเอียด Features ของ Dataset:")
    st.write("""
    1. **Pregnancies** (จำนวนการตั้งครรภ์)
    - จำนวนการตั้งครรภ์ที่ผู้หญิงคนหนึ่งเคยมี
    - ลักษณะของฟีเจอร์นี้สามารถบ่งชี้ถึงสุขภาพทางสรีรวิทยาของผู้หญิงในช่วงเวลาต่างๆ

    2. **Glucose** (ระดับน้ำตาลในเลือด)
    - ค่าน้ำตาลในเลือดที่ตรวจวัดหลังจากที่ไม่ได้ทานอาหาร (Fasting Blood Sugar)
    - เป็นตัวชี้วัดสำคัญของโรคเบาหวาน เนื่องจากระดับน้ำตาลในเลือดที่สูงเป็นสัญญาณของการเป็นโรคเบาหวาน

    3. **BloodPressure** (ความดันโลหิต)
    - ความดันโลหิตของผู้ป่วย (ค่าระดับความดันโลหิตขณะพัก)
    - ความดันโลหิตสูงอาจเป็นสัญญาณของโรคที่เกี่ยวข้องกับหัวใจและหลอดเลือด รวมทั้งโรคเบาหวาน

    4. **SkinThickness** (ความหนาของผิวหนัง)
    - วัดความหนาของผิวหนังที่บริเวณท้อง (Triceps skinfold thickness)
    - ความหนาของผิวหนังสามารถเป็นสัญญาณของภาวะที่เกี่ยวข้องกับโรคเบาหวาน เช่น ภาวะดื้อต่ออินซูลิน

    5. **Insulin** (ระดับอินซูลิน)
    - ระดับของฮอร์โมนอินซูลินในเลือด
    - อินซูลินมีบทบาทสำคัญในการควบคุมระดับน้ำตาลในเลือด การผลิตอินซูลินที่ไม่เพียงพออาจเป็นสัญญาณของโรคเบาหวาน

    6. **BMI** (ดัชนีมวลกาย)
    - คำนวณจากน้ำหนักตัวและส่วนสูง (Body Mass Index)
    - BMI ที่สูงอาจเป็นสัญญาณของโรคเบาหวาน โดยเฉพาะเมื่อเกี่ยวข้องกับภาวะดื้อต่ออินซูลิน

    7. **DiabetesPedigreeFunction** (ฟังก์ชันประวัติการเป็นเบาหวาน)
    - เป็นค่าที่ใช้บ่งชี้ความเสี่ยงของโรคเบาหวานตามประวัติทางพันธุกรรม
    - ค่านี้สามารถใช้ในการประเมินโอกาสที่ผู้ป่วยจะเป็นโรคเบาหวานตามประวัติของครอบครัว

    8. **Age** (อายุ)
    - อายุของผู้ป่วย
    - อายุที่มากขึ้นสามารถเพิ่มความเสี่ยงในการเป็นโรคเบาหวาน

    9. **Outcome** (ผลลัพธ์)
    - ตัวแปรเป้าหมายที่บ่งชี้ว่า ผู้ป่วยเป็นโรคเบาหวานหรือไม่
    - 0 = ไม่เป็นโรคเบาหวาน
    - 1 = เป็นโรคเบาหวาน
    """)

# หน้าที่ 2: อธิบายการพัฒนาโมเดล Machine Learning และ Neural Networks
def model_development():
    st.title("การพัฒนาโมเดลทั้งสองประเภท (Machine Learning และ Neural Network) ")
    st.write("ในการพัฒนาโมเดลทั้งสองประเภท (Machine Learning และ Neural Network) โดยใช้ข้อมูลจากชุดข้อมูล PIMA Indians Diabetes Database และ Food-101 Nutritional Information เราสามารถแบ่งขั้นตอนการพัฒนาได้ตามนี้:")


    st.write("""
    ## 1. PIMA Indians Diabetes Database
    ชุดข้อมูลนี้ถูกใช้ในการทำนายว่า ผู้ป่วยจะเป็นโรคเบาหวานหรือไม่ โดยมีฟีเจอร์หลัก ๆ เช่น ระดับน้ำตาลในเลือด, ความดันโลหิต, น้ำหนักตัว และอายุ ซึ่งเหมาะกับการทำ Classification (การจำแนกประเภท) เพื่อทำนายผลลัพธ์ "โรคเบาหวาน" (เป็นหรือไม่เป็น)

    ### ขั้นตอนการพัฒนาโมเดล Machine Learning (ML)
    #### ข้อมูลเบื้องต้น
    - ฟีเจอร์: มีทั้งหมด 8 ฟีเจอร์ที่เกี่ยวข้องกับสุขภาพ เช่น จำนวนการตั้งครรภ์, น้ำตาลในเลือด, ความดันโลหิต, และอื่น ๆ
    - ตัวแปรเป้าหมาย (Target): Outcome ซึ่งแสดงผลลัพธ์ว่าเป็นโรคเบาหวานหรือไม่ (0 = ไม่เป็น, 1 = เป็น)

    #### การเตรียมข้อมูล
    - การทำความสะอาดข้อมูล: ตรวจสอบค่าที่หายไปหรือค่าผิดปกติ
    - การแปลงข้อมูล: ฟีเจอร์ที่เป็นตัวเลขอาจต้องทำการสเกล (Normalization/Standardization) เช่น การปรับค่าให้อยู่ในช่วงที่เหมาะสม
    - การแบ่งชุดข้อมูล: แบ่งข้อมูลเป็นชุดฝึกสอน (Training) และชุดทดสอบ (Testing) โดยปกติจะใช้การแบ่งเป็น 80/20 หรือ 70/30

    #### การเลือกอัลกอริธึม Machine Learning
    - Decision Tree: เป็นอัลกอริธึมที่เข้าใจง่ายและสามารถจัดการข้อมูลประเภทนี้ได้ดี
    - Logistic Regression: เป็นอัลกอริธึมที่เหมาะสำหรับการจำแนกประเภทที่มีค่าเป็น 2 ชนิด
    - Random Forest: ใช้การสร้างหลายๆ ต้นไม้การตัดสินใจ (Decision Trees) เพื่อเพิ่มความแม่นยำ
    - SVM (Support Vector Machine): ใช้ในการแยกข้อมูลที่มีลักษณะไม่เป็นเชิงเส้น

    #### การฝึกสอนและทดสอบ
    - ใช้ชุดข้อมูลฝึกสอนเพื่อฝึกโมเดล
    - ทดสอบโมเดลกับชุดข้อมูลทดสอบเพื่อประเมินประสิทธิภาพ

    #### การประเมินผล
    - ประเมินผลการทำงานของโมเดลด้วย Accuracy, Precision, Recall, F1-Score หรือ ROC-AUC เพื่อเลือกโมเดลที่ดีที่สุด

    ### ขั้นตอนการพัฒนา Neural Network (NN)
    #### ข้อมูลเบื้องต้น
    - ฟีเจอร์และตัวแปรเป้าหมายเช่นเดียวกับใน Machine Learning แต่จะใช้โมเดลที่มีหลายชั้นในการเรียนรู้จากข้อมูล

    #### การเตรียมข้อมูล
    - การทำความสะอาดและการแปลงข้อมูลยังคงเป็นขั้นตอนสำคัญเช่นเดียวกับใน ML

    #### การออกแบบ Neural Network
    - Input Layer: ฟีเจอร์ 8 ตัวจากชุดข้อมูล
    - Hidden Layers: ใช้หลายๆ ชั้นในการเรียนรู้จากข้อมูล โดยสามารถใช้ 1-2 ชั้นแรกที่มีจำนวนโหนดมาก และลดจำนวนโหนดในชั้นถัดไป
    - Output Layer: เลือกใช้ 1 โหนดที่แสดงผลเป็น 0 หรือ 1 (เป็นหรือไม่เป็นโรคเบาหวาน)

    #### การเลือก Activation Functions
    - ReLU (Rectified Linear Unit) สำหรับ Hidden Layers
    - Sigmoid สำหรับ Output Layer เนื่องจากเป็นปัญหาการจำแนกประเภทแบบ Binary

    #### การฝึกสอน
    - ใช้ Backpropagation เพื่อปรับน้ำหนักของโมเดล
    - ใช้ Optimizer เช่น Adam เพื่อปรับการเรียนรู้
    - กำหนดจำนวน Epochs ที่เหมาะสม

    #### การประเมินผล
    - ประเมินประสิทธิภาพของโมเดลด้วย Accuracy, Precision, Recall หรือ AUC-ROC
    """)

    st.write("""
    ## 2. Food-101 Nutritional Information
    ชุดข้อมูลนี้ประกอบไปด้วยข้อมูลทางโภชนาการของอาหาร 101 ชนิด ซึ่งใช้ในการทำนายหรือการแนะนำข้อมูลอาหารให้เหมาะสมกับผู้ใช้ เช่น การจัดการแคลอรี่หรือโปรตีนที่ควรบริโภค

    ### ขั้นตอนการพัฒนาโมเดล Machine Learning (ML)
    #### ข้อมูลเบื้องต้น
    - ฟีเจอร์: ชื่ออาหาร, จำนวนแคลอรี่, โปรตีน, คาร์โบไฮเดรต, ไขมัน, ใยอาหาร, โซเดียม เป็นต้น
    - ตัวแปรเป้าหมาย: อาจเป็นการคำนวณแคลอรี่รวมจากอาหารต่าง ๆ หรือสามารถทำการจำแนกประเภทของอาหาร (เช่น ประเภทอาหาร)

    #### การเตรียมข้อมูล
    - การทำความสะอาดข้อมูล และการแปลงค่าต่าง ๆ (เช่น การสเกลข้อมูล)
    - การแบ่งชุดข้อมูลเป็นชุดฝึกสอนและทดสอบ

    #### การเลือกอัลกอริธึม Machine Learning
    - K-Nearest Neighbors (KNN): ใช้ในการทำนายประเภทหรือแนะนำอาหาร
    - Random Forest: ใช้ในการทำนายปริมาณสารอาหารต่าง ๆ
    - Decision Trees: ช่วยในการจัดหมวดหมู่อาหารตามฟีเจอร์ที่มี

    #### การฝึกสอนและทดสอบ
    - ใช้ชุดฝึกสอนในการฝึกโมเดล
    - ทดสอบกับชุดทดสอบเพื่อประเมินประสิทธิภาพ

    #### การประเมินผล
    - ใช้ Accuracy, Precision, Recall, F1-Score เพื่อประเมินผล

    ### ขั้นตอนการพัฒนา Neural Network (NN)
    #### ข้อมูลเบื้องต้น
    - ฟีเจอร์เช่นเดียวกับใน ML แต่การพัฒนา Neural Network จะมีการเรียนรู้จากข้อมูลที่มีหลายมิติ

    #### การเตรียมข้อมูล
    - การทำความสะอาดและการแปลงข้อมูลยังคงเป็นขั้นตอนสำคัญ

    #### การออกแบบ Neural Network
    - Input Layer: ฟีเจอร์ต่าง ๆ เช่น แคลอรี่, โปรตีน, คาร์โบไฮเดรต
    - Hidden Layers: เลือกจำนวนชั้นที่เหมาะสม โดยอาจใช้ ReLU เป็น Activation Function
    - Output Layer: ใช้ Softmax หรือ Sigmoid ขึ้นอยู่กับว่าต้องการทำนายแบบ Class หรือ Regression

    #### การฝึกสอน
    - ใช้ Backpropagation ในการฝึกโมเดล
    - ใช้ Optimizer เช่น Adam และกำหนดจำนวน Epochs ที่เหมาะสม

    #### การประเมินผล
    - ใช้ Accuracy, Precision, Recall, และ AUC-ROC ในการประเมินผลการทำงาน
    """)


# หน้าที่ 3: Demo การทำงานของโมเดล Machine Learning
# โหลดข้อมูลสำหรับการพยากรณ์โรคเบาหวาน
diabetes_df = pd.read_csv("diabetes.csv")
features_diabetes = ["Glucose", "BloodPressure", "BMI", "Age"]
X_diabetes = diabetes_df[features_diabetes]
y_diabetes = diabetes_df["Outcome"]
X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_diabetes, y_diabetes, test_size=0.2, random_state=42)
scaler_d = StandardScaler()
X_train_d = scaler_d.fit_transform(X_train_d)
X_test_d = scaler_d.transform(X_test_d)
model_d = LogisticRegression()
model_d.fit(X_train_d, y_train_d)


# โหลดข้อมูลโภชนาการ
nutrition_df = pd.read_csv("nutrition.csv")
features_nutrition = ["calories", "protein", "carbohydrates", "fats", "fiber", "sodium"]
X_nutrition = nutrition_df[features_nutrition]
y_nutrition = nutrition_df["calories"]
X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_nutrition, y_nutrition, test_size=0.2, random_state=42)
scaler_n = StandardScaler()
X_train_n = scaler_n.fit_transform(X_train_n)
X_test_n = scaler_n.transform(X_test_n)
model_n = LogisticRegression()
model_n.fit(X_train_n, y_train_n)


# UI Streamlit
st.sidebar.title("เลือกฟังก์ชันการทำนาย")
page = st.sidebar.radio("ไปยังหน้า:", ["การเตรียมข้อมูลและทฤษฎี", "การพัฒนาโมเดล", "ทำนายโรคเบาหวาน", "แนะนำโภชนาการ"])

if page == "การเตรียมข้อมูลและทฤษฎี":
    data_preparation_and_algorithm_theory()

elif page == "การพัฒนาโมเดล":
    model_development()

elif page == "ทำนายโรคเบาหวาน":
    
        st.title("🔍 ระบบทำนายความเสี่ยงโรคเบาหวาน")
        # แบบฟอร์มรับข้อมูล
        glucose = st.number_input("ระดับน้ำตาลในเลือด:", min_value=0, max_value=300, value=100)
        blood_pressure = st.number_input("ความดันโลหิต:", min_value=0, max_value=200, value=80)
        bmi = st.number_input("ดัชนีมวลกาย (BMI):", min_value=0.0, max_value=50.0, value=25.0)
        age = st.number_input("อายุ:", min_value=1, max_value=120, value=30)
        
        if st.button("ทำนาย"):
            input_data = scaler_d.transform([[glucose, blood_pressure, bmi, age]])
            prediction = model_d.predict(input_data)
            result = "เป็นโรคเบาหวาน" if prediction[0] == 1 else "ไม่เป็นโรคเบาหวาน"
            st.write(f"ผลลัพธ์: {result}")

elif page == "แนะนำโภชนาการ":
    st.title("แบบฟอร์มแนะนำโภชนาการ")

    # ข้อมูลผู้ใช้
    weight = st.number_input("น้ำหนัก (กก.)", min_value=30.0, max_value=200.0, value=70.0)
    height = st.number_input("ส่วนสูง (ซม.)", min_value=100.0, max_value=250.0, value=170.0)
    age = st.number_input("อายุ (ปี)", min_value=10, max_value=100, value=30)
    gender = st.radio("เพศ", ["ชาย", "หญิง"])
    
    # ระดับกิจกรรม
    activity_level = st.selectbox("ระดับกิจกรรม", [
        "นั่งทำงาน (ไม่ออกกำลังกาย)",
        "ออกกำลังกายเบาๆ (1-2 ครั้งต่อสัปดาห์)",
        "ออกกำลังกายปานกลาง (3-5 ครั้งต่อสัปดาห์)",
        "ออกกำลังกายหนัก (6-7 ครั้งต่อสัปดาห์)"
    ])
    
    # เป้าหมายโภชนาการ
    goal = st.selectbox("เป้าหมายของคุณ", ["ลดน้ำหนัก", "เพิ่มน้ำหนัก", "รักษาน้ำหนัก", "สร้างกล้ามเนื้อ"])

    # คำนวณ BMR (Basal Metabolic Rate)
    if gender == "ชาย":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    # คำนวณ TDEE ตามระดับกิจกรรม
    activity_factors = {
        "นั่งทำงาน (ไม่ออกกำลังกาย)": 1.2,
        "ออกกำลังกายเบาๆ (1-2 ครั้งต่อสัปดาห์)": 1.375,
        "ออกกำลังกายปานกลาง (3-5 ครั้งต่อสัปดาห์)": 1.55,
        "ออกกำลังกายหนัก (6-7 ครั้งต่อสัปดาห์)": 1.725
    }
    tdee = bmr * activity_factors[activity_level]

    # ปรับ TDEE ตามเป้าหมาย
    if goal == "ลดน้ำหนัก":
        target_calories = tdee - 500
    elif goal == "เพิ่มน้ำหนัก":
        target_calories = tdee + 500
    elif goal == "สร้างกล้ามเนื้อ":
        target_calories = tdee + 300
    else:
        target_calories = tdee

    # แนะนำสัดส่วนสารอาหาร
    protein = (target_calories * 0.3) / 4
    carbs = (target_calories * 0.4) / 4
    fats = (target_calories * 0.3) / 9

    # แสดงผลลัพธ์
    st.subheader("คำแนะนำโภชนาการของคุณ:")
    st.write(f"🔥 แคลอรี่ที่ควรบริโภคต่อวัน: **{target_calories:.0f} kcal**")
    st.write(f"🍗 โปรตีน: **{protein:.0f} กรัม**")
    st.write(f"🍞 คาร์โบไฮเดรต: **{carbs:.0f} กรัม**")
    st.write(f"🥑 ไขมัน: **{fats:.0f} กรัม**")

    st.write("💡 **คำแนะนำเพิ่มเติม**")
    if goal == "ลดน้ำหนัก":
        st.write("- ควบคุมปริมาณน้ำตาล และไขมันอิ่มตัว")
        st.write("- เน้นการกินโปรตีนสูงและผัก")
    elif goal == "เพิ่มน้ำหนัก":
        st.write("- เพิ่มปริมาณโปรตีน และคาร์โบไฮเดรตที่ดี เช่น ข้าวกล้อง มันฝรั่ง")
        st.write("- กินอาหารที่ให้พลังงานสูงแต่มีประโยชน์")
    elif goal == "สร้างกล้ามเนื้อ":
        st.write("- โปรตีนเป็นสิ่งสำคัญ ควรเน้นอาหารประเภทไก่, ปลา, ไข่")
        st.write("- ควรทานอาหารหลังออกกำลังกายภายใน 30 นาที")
