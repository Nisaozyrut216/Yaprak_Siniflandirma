import streamlit as st
import tensorflow as tf
import numpy as np

#Tensorflow Modeli Tahmini
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #tek görüntüyü topluya dönüştür
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #max elemanının dönüş indeksi

# Genel sayfa stilleri
st.markdown(
    """
    <style>
        body {
            background-color: #800080; /* Arka plan rengi */
            color: #333333; /* Metin rengi */
            font-family: Arial, sans-serif; /* Yazı tipi */
        }
        .st-bw {
            background-color: #ffffff; /* Sidebar arka plan rengi */
        }
        .st-bq {
            font-size: 20px; /* Blockquote yazı boyutu */
            color: #555555; /* Blockquote metin rengi */
        }
    </style>
    """,
    unsafe_allow_html=True
)

#Sidebar
st.sidebar.title("Gösterge Paneli")
app_mode = st.sidebar.selectbox("Sayfa Seçiniz",["Anasayfa","Hakkında","Yaprak Tanıma"])

# Ana Sayfa
if app_mode == "Anasayfa":
    st.header("Yaprak Türü  Tanıma Sistemi")
    image_path = "resim.png"
    st.image(image_path, use_column_width=True)
    st.markdown(
        """
        Yaprak Tanıma Sistemine Hoş Geldiniz! 🌿🔍

        Bir bitki resmi yükleyin ve sistemimiz  bitki türünü tespit etmek için analiz etsin. 
        Hadi gelin birlikte yaprak türlerinden meyve veya sebzeyi tanıyalım.

        """
    )

# Hakkında Sayfası
elif app_mode == "Hakkında":
    st.header("Hakkında")
    st.markdown(
        """
        #### Veri Kümesi Hakkında
       Bu veri kümesi bir kısmı kaggle sitesinden bir kısmı ise elle oluşturulmuştur bir veri setidir. Bu veri seti 26 sınıftan 
       oluşmaktadır.
        #### İçerik
        1. eğitim 
        2. Test
        3. doğrulama 
        
        """
    )

# Yaprak Tanıma Sayfası
elif app_mode == "Yaprak Tanıma":
    st.header("Yaprak Türü Tahmini")
    test_image = st.file_uploader("Lütfen Tahmin Edilecek Resmi Seçin:")
    if st.button("Görüntüyü Göster"):
        st.image(test_image, width=4, use_column_width=True)
    # Tahmin butonu
    if st.button("Tahmin Et"):
        st.balloons()
        st.write("Yaprak Tahminimiz")
        result_index = model_prediction(test_image)
        # Etiketleri oku
        class_name = ['Anhui Barberry','apple','AriveDantu', 'basale', 'betel','carrot',
                      'cherry','Icrape jasmine','curry', 'drumstick','fenugreek', 'goldenrain tree','guava','hibiscus',
                      'indian beech', 'indian mustard','jackfruit','jamaika cherry','jamun','jasmine','karanda','lemon',
                        'tomato', 'true indigo','tulsi','wintersweet']
                    
        st.success("Modelin Tahmin Ettiği Yaprak {}".format(class_name[result_index]))

        