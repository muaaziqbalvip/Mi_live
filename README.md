# 🚀 MiTV Network - 24/7 Multi-Stream Engine

<p align="center">
  <img src="https://i.ibb.co/XxYZrrBf/IMG-20260311-124411.png" alt="MiTV-Live-Streaming-Banner" width="800">
</p>

---

## 🌟 Introduction
Yeh **MUSLIM ISLAM** ka aik advanced cloud-based streaming project hai. Is engine ke zarye aap GitHub Actions ka istemal karte hue kisi bhi video ko **YouTube**, **Facebook**, ya **Custom RTMP** platforms par **24/7 non-stop** live chala sakte hain.

---

## 🛠️ Powerful Features
* 📺 **Multi-Streaming:** Aik hi waqt mein 3 mukhtalif channels par live broadcast.
* 🔄 **Infinite Looping:** Video kabhi nahi rukay gi (Smooth transition technology).
* 🤖 **Fully Automated:** Har 5 hours 55 minutes baad auto-restart (24/7 continuity).
* 📄 **Playlist Support:** `playlist.m3u` file se video links uthane ki sahulat.
* ☁️ **Zero Server Cost:** Poora setup GitHub ke cloud servers par chalta hai.

---

## 🚀 Istemal Karne Ka Tariqa (How to Use)

Is system ko chalane ke liye niche diye gaye steps follow karein:

### 1️⃣ Playlist Setup
Apni repository mein maujood `playlist.m3u` file ko open karein aur usmein apni video ka direct link (Dropbox, Drive, ya Server link) paste kar dein.

### 2️⃣ Stream Keys Configuration
`mitv_final.yml` file ko edit karein aur jahan RTMP URLs hain, wahan apni **YouTube Stream Key** ya kisi bhi platform ki key paste kar dein:
`rtmp://a.rtmp.youtube.com/live2/APNI-KEY-YAHAN-LIKHEIN`

### 3️⃣ Start Streaming
1. Repository ke **Actions** tab par jayein.
2. **MiTV_YouTube_24-7_Multi_Stream** workflow select karein.
3. **Run workflow** par click karein. Yeh workflow baghair kisi sawal ke `main` branch par streaming shuru kar dega.

---

## 🛠️ Editing & Customization
Agar aap is system mein tabdeeli karna chahte hain:

* **Video Change:** Sirf `playlist.m3u` mein link badlein, engine khud hi naya link pick kar lega.
* **Auto-Restart:** Yeh engine **5 hours 55 mins** ke gap se chalta hai taake stream kabhi offline na ho.
* **Smoothness:** Is mein `-stream_loop -1` aur `until` loop ka logic lagaya gaya hai jo video atekne nahi deta.

---

## 👤 Developer & Founder
**Maaz Iqbal** *Founder & CEO of MiTV Network* *Project of **MUSLIM ISLAM***

---

## ⚠️ Disclaimer
Yeh project educational purposes aur media management ke liye hai. Istemal karte waqt platform ki terms and conditions ka khayal rakhein.
