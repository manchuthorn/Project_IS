import streamlit as st
from sklearn.linear_model import LogisticRegression
import pandas

#หน้าที่3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import streamlit as st
import numpy as np

#หน้าที่4
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd





# หน้าที่ 1: อธิบายการเตรียมข้อมูลและทฤษฎีของอัลกอริธึม
def data_preparation_and_algorithm_theory():
    st.title("Machine Learning")
    st.write("ที่มาของ Dataset : ", "[Food-101 Nutritional Information](https://www.kaggle.com/datasets/sanadalali/food-101-nutritional-information)")
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
    #ทฤษฎีของอัลกอริทึมที่พัฒนา
    st.write("**ทฤษฎีของอัลกอริทึม Support Vector Machine (SVM)**")
    st.write("""
    Support Vector Machine (SVM) เป็นอัลกอริทึมที่ใช้สำหรับ Classification (การจำแนกประเภท) และ Regression (การพยากรณ์ค่า) โดยอาศัยแนวคิดของ Hyperplane เพื่อแบ่งข้อมูลออกเป็นกลุ่มที่แตกต่างกัน
             
    **หลักการทำงานของ SVM**
    - SVM สร้างเส้นแบ่งหรือ Hyperplane ที่แยกกลุ่มข้อมูลให้ห่างจากกันมากที่สุด
    - จุดข้อมูลที่อยู่ใกล้ Hyperplane มากที่สุด เรียกว่า Support Vectors
    - ใช้ Kernel Trick สำหรับข้อมูลที่ไม่สามารถแยกกันได้ด้วยเส้นตรง

    **💡 จุดเด่นของ SVM**
    - ✅ ใช้งานได้ดีแม้ข้อมูลมีขนาดเล็ก
    - ✅ ป้องกัน Overfitting ได้ดี
    - ✅ ใช้ Kernel Trick ช่วยให้ทำงานกับข้อมูลที่ซับซ้อนได้
    
    - ❌ ใช้เวลาประมวลผลนานเมื่อมีข้อมูลเยอะ
    - ❌ ต้องปรับพารามิเตอร์ (C, gamma) ให้เหมาะสม
    """)
#ขั้นตอน ML
    st.write("**ขั้นตอนการพัฒนาของโมเดล**")
    st.write("""
    1. **นำเข้าไลบรารีที่จำเป็น**
    - **pandas** และ **numpy** ใช้จัดการข้อมูลในรูปแบบ DataFrame และ Array
    - **train_test_split** ใช้แบ่งข้อมูลเป็นชุดฝึก (Training set) และชุดทดสอบ (Test set)
    - **StandardScaler** ใช้ปรับค่าข้อมูลให้มีสเกลมาตรฐาน
    - **SVC ใช้สร้างโมเดล** Support Vector Machine (SVM)
    - **classification_report** และ **accuracy_score** ใช้ประเมินผลโมเดล
    """)
    code = '''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score'''
    st.code(code, language="python")
    st.write("""
    2. **โหลดชุดข้อมูล**
    - โหลดข้อมูลจากไฟล์ **nutrition.csv**
    """)
    code = '''nutrition_df = pd.read_csv("nutrition.csv")'''
    st.code(code, language="python")
    st.write("""
    3. **เลือก Features และ Target**
    - features_nutrition: เลือกคอลัมน์ที่ใช้เป็นตัวแปรอิสระ (Features) ได้แก่ โปรตีน, คาร์โบไฮเดรต, ไขมัน ฯลฯ
    - X_nutrition: เก็บเฉพาะค่าของ Features
    - y_nutrition: กำหนดให้ตัวแปรตาม (Target) เป็น "calories"
    """)
    code = '''
    features_nutrition = ["calories", "protein", "carbohydrates", "fats", "fiber", "sodium"]
X_nutrition = nutrition_df[features_nutrition]
y_nutrition = nutrition_df["calories"]'''
    st.code(code, language="python")
    st.write("""
    4. **แบ่งชุดข้อมูลเป็นชุดฝึก (Train) และทดสอบ (Test)**
    - ใช้ train_test_split() เพื่อแบ่งข้อมูลออกเป็น 80% สำหรับการฝึก และ 20% สำหรับการทดสอบ
    """)
    code = '''X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_nutrition, y_nutrition, test_size=0.2, random_state=42)'''
    st.code(code, language="python")
    st.write("""
    5. **ปรับมาตรฐานข้อมูล (Feature Scaling)**
    - ใช้ StandardScaler เพื่อปรับค่าคุณลักษณะ (Features) ให้มีค่าเฉลี่ย = 0 และค่าความแปรปรวน = 1
    - ช่วยให้โมเดลทำงานได้ดีขึ้น
    - ใช้ X_test เพื่อให้โมเดลพยากรณ์ค่า y
    """)
    code = '''
    scaler_n = StandardScaler()
X_train_n = scaler_n.fit_transform(X_train_n)
X_test_n = scaler_n.transform(X_test_n)'''
    st.code(code, language="python")
    st.write("""
    6. **สร้างและฝึกโมเดล SVM**
    - ใช้ Support Vector Classifier (SVC)
    - kernel='linear' → ใช้เส้นแบ่งแบบ Linear
    - C=1 → ควบคุมความเข้มงวดของขอบเขตการจำแนก
    - fit(X_train, y_train) → ฝึกโมเดลด้วย Training Data
    """)
    code = '''model_n = LogisticRegression()
model_n.fit(X_train_n, y_train_n)'''
    st.code(code, language="python")
    st.write("""
    7. **ประเมินผล**
    - Accuracy Score → คำนวณความแม่นยำของโมเดล
    - Classification Report → แสดงค่าต่าง ๆ เช่น Precision, Recall, F1-score
    """)
    code = '''y_pred = svm_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))'''
    st.code(code, language="python")
    st.image("PhotoML/accuracy.png", use_container_width=True)

# หน้าที่ 2: อธิบายการพัฒนาโมเดล Machine Learning และ Neural Networks
def model_development():
    st.title("Neural Networks")
    st.write("ที่มาของ Dataset : ", "[Kaggle Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)")
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
    #ทฤษฎีของอัลกอริทึมที่พัฒนา
    st.write("**ทฤษฎีของอัลกอริทึม MLP (Multilayer Perceptron)**")
    st.write("""
    Multilayer Perceptron (MLP) เป็นประเภทของ Artificial Neural Network (ANN) ที่ประกอบด้วย หลายชั้น (Layers) ของนิวรอน (Neurons) ซึ่งสามารถเรียนรู้และจำแนกข้อมูลที่ซับซ้อนขึ้นกว่าระบบ Perceptron แบบธรรมดา
             
    Multilayer Perceptron (MLP) เป็นโมเดลที่ใช้โครงข่ายประสาทเทียม (Artificial Neural Network) โดยมีโครงสร้างดังนี้:

    - Input Layer (ชั้นนำเข้า) → รับค่าตัวแปร (Features) เช่น Glucose, Blood Pressure, BMI, Age ฯลฯ
    - Hidden Layers (ชั้นซ่อน) → ประมวลผลข้อมูลผ่าน Activation Function (เช่น ReLU, Sigmoid)
    - Output Layer (ชั้นส่งออก) → แสดงผลลัพธ์เป็น 0 = ไม่เป็นเบาหวาน หรือ 1 = เป็นเบาหวาน
             
    📌 เป้าหมายของโมเดล คือเรียนรู้จากข้อมูลสุขภาพของผู้ป่วยและคาดการณ์ว่าพวกเขาจะเป็นเบาหวานหรือไม่

    **💡 จุดเด่นของ MLP**
    - ✅ รองรับการเรียนรู้แบบไม่เป็นเส้นตรง (Non-linearity)
    - ✅ เรียนรู้ความซับซ้อนของข้อมูลได้ดี
    - ✅ ใช้ Backpropagation ในการปรับปรุงโมเดล
    - ✅ ใช้ได้ทั้ง Classification และ Regression
    
    MLP เหมาะกับการนำไปใช้วิเคราะห์ข้อมูลสุขภาพ เช่น Pima Indians Diabetes Dataset เพื่อช่วยคัดกรองผู้ป่วยเบาหวานได้อย่างมีประสิทธิภาพ 
    """)
    #ขั้นตอน NN
    st.write("**ขั้นตอนการพัฒนาของโมเดล**")
    st.write("""
    1. **นำเข้าไลบรารีที่จำเป็น**
    - **numpy** และ **pandas** ใช้สำหรับการจัดการข้อมูล
    - **tensorflow** และ **keras** ใช้สำหรับสร้างโมเดลปัญญาประดิษฐ์
    - **train_test_split** ใช้แบ่งชุดข้อมูลออกเป็น ชุดฝึก (train) และ ชุดทดสอบ (test)
    - **StandardScaler** ใช้ปรับขนาดข้อมูลให้อยู่ในช่วงที่เหมาะสมสำหรับการฝึกโมเดล
    """)
    code = '''
    import numpy as np  
import pandas as pd  
import tensorflow as tf  
from tensorflow import keras  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  '''
    st.code(code, language="python")
    st.write("""
    2. **โหลดและเตรียมข้อมูล**
    - โหลดไฟล์ diabetes.csv 
    - กำหนดชื่อคอลัมน์ของ DataFrame (df)
    - df.head() ใช้แสดงข้อมูล 5 แถวแรกเพื่อดูโครงสร้างข้อมูล
    """)
    code = '''
    from google.colab import files'''
    st.code(code, language="python")

    code = '''
    uploaded = files.upload()
file_path = "diabetes.csv"
df = pd.read_csv(file_path)

columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]  
df.columns = columns
df.head()'''
    st.code(code, language="python")
    st.image("PhotoNN/filehead.png", use_container_width=True)
    st.write("""
    3. **โหลดและเตรียมข้อมูลแยกข้อมูลออกเป็นคุณลักษณะ (Features) และผลลัพธ์ (Labels)**
    - X คือข้อมูลที่ใช้ในการทำนาย (เช่น Glucose, BMI, Age)
    - y คือผลลัพธ์ที่ต้องการทำนาย (0 = ไม่มีเบาหวาน, 1 = เป็นเบาหวาน)
    """)
    code = '''
    X = df.drop(columns=["Outcome"])
y = df["Outcome"]'''
    st.code(code, language="python")
    st.write("""
    4. **แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ**
    - แบ่งข้อมูลออกเป็น 80% ชุดฝึก และ 20% ชุดทดสอบ
    - random_state=42 กำหนดค่าให้สุ่มเหมือนเดิมทุกครั้งที่รัน
    """)
    code = '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)'''
    st.code(code, language="python")
    st.write("""
    5. **ปรับขนาดข้อมูลให้เหมาะสม**
    - ใช้ StandardScaler() ปรับขนาดข้อมูลให้อยู่ในช่วงที่เหมาะสมสำหรับโมเดล Neural Network (มีค่าเฉลี่ยเป็น 0 และค่าเบี่ยงเบนมาตรฐานเป็น 1)
    """)
    code = '''
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)'''
    st.code(code, language="python")
    st.write("""
    6. **สร้างโมเดล Neural Network**
    - ใช้โครงสร้างของ Neural Network 3 ชั้น:
        - ชั้นแรก (Hidden Layer 1): 16 นิวรอน + relu activation
        - ชั้นที่สอง (Hidden Layer 2): 8 นิวรอน + relu activation
        - ชั้นเอาต์พุต (Output Layer): 1 นิวรอน + sigmoid activation (เพราะเป็นปัญหาจำแนกประเภท)
    """)
    code = '''model = keras.Sequential([
    keras.layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)), 
    keras.layers.Dense(8, activation='relu'), 
    keras.layers.Dense(1, activation='sigmoid')  
])'''
    st.code(code, language="python")
    st.write("""
    7. **คอมไพล์โมเดล**
    - ใช้ adam optimizer เพื่อปรับค่าพารามิเตอร์ของโมเดล
    - ใช้ binary_crossentropy เป็น loss function (เหมาะสำหรับปัญหาจำแนกประเภทแบบ 2 class)
    - ใช้ accuracy เป็นตัววัดผล
    """)
    code = '''model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])'''
    st.code(code, language="python")
    st.write("""
    8. **คอมไพล์โมเดล**
    - ฝึกโมเดลเป็นเวลา 50 รอบ (epochs)
    - ใช้ขนาดชุดข้อมูลย่อย (batch size) เท่ากับ 10
    - ใช้ validation_data=(X_test, y_test) เพื่อตรวจสอบความแม่นยำระหว่างการฝึก
    """)
    code = '''history = model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_test, y_test))'''
    st.code(code, language="python")
    st.image("PhotoNN/8.1.png", use_container_width=True)
    st.image("PhotoNN/8.2.png", use_container_width=True)
    st.write("""
    9. **ประเมินโมเดล**
    - ใช้ model.evaluate() ประเมินผลลัพธ์กับชุดข้อมูลทดสอบ
    - แสดงค่าความแม่นยำของโมเดล
    """)
    code = '''loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")'''
    st.code(code, language="python")
    st.image("PhotoNN/9.1.png", use_container_width=True)
    


# หน้าที่ 4
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

# หน้าที่ 3
# โหลดข้อมูลโภชนาการ
nutrition_df = pd.read_csv("nutrition.csv")
features_nutrition = ["calories", "protein", "carbohydrates", "fats", "fiber", "sodium"]
X_nutrition = nutrition_df[features_nutrition]
y_nutrition = nutrition_df["calories"]
X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_nutrition, y_nutrition, test_size=0.2, random_state=42)
X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_nutrition, y_nutrition, test_size=0.2, random_state=42)
scaler_n = StandardScaler()
X_train_n = scaler_n.fit_transform(X_train_n)
X_test_n = scaler_n.transform(X_test_n)
model_n = LogisticRegression()
model_n.fit(X_train_n, y_train_n)


# UI Streamlit
st.sidebar.title("Project Intelligent System")
page = st.sidebar.selectbox("ไปยังหน้า:", ["Machine Learning", "Neural Network", "Demo Machine Learning", "Demo Neural Network"])

if page == "Machine Learning":
    data_preparation_and_algorithm_theory()

elif page == "Neural Network":
    model_development()

elif page == "Demo Machine Learning":
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
elif page == "Demo Neural Network":
    
        st.title("🔍 ระบบทำนายความเสี่ยงโรคเบาหวาน")
        # แบบฟอร์มรับข้อมูล
        glucose = st.number_input("ระดับน้ำตาลในเลือด:", min_value=0, max_value=500, value=100)
        blood_pressure = st.number_input("ความดันโลหิต:", min_value=0, max_value=200, value=80)
        bmi = st.number_input("ดัชนีมวลกาย (BMI):", min_value=0.0, max_value=50.0, value=25.0)
        age = st.number_input("อายุ:", min_value=1, max_value=120, value=30)
        
        if st.button("ทำนาย"):
            input_data = scaler_d.transform([[glucose, blood_pressure, bmi, age]])
            prediction = model_d.predict(input_data)
            result = "เป็นโรคเบาหวาน" if prediction[0] == 1 else "ไม่เป็นโรคเบาหวาน"
            st.write(f"ผลลัพธ์: {result}")