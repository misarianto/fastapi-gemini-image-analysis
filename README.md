### FASTAPI GEMINI IMAGE ANALYSIS

Create API KEY [disini]("https://aistudio.google.com/apikey")

Anda dapat menjalankan perintah ini dari Gemini API, setelah menginstal paket yang relevan, dengan menjalankan kode berikut: [disini]("https://aistudio.google.com/prompts/new_chat")

### Set Environment Variable

Edit file `~/.bashrc:`

```
nano ~/.bashrc

```
Tambahkan baris berikut di bagian bawah file:

```
export GEMINI_API_KEY="..."
```
Simpan file (`Ctrl + O`, lalu `Ctrl + X`) dan muat ulang:

```
source ~/.bashrc
```

Verifikasi:

```
echo $GEMINI_API_KEY
```

### Create Virtual Environment

masuk ke folder project

```
cd fastapi-gemini-image-analysis
``

buat environment

```
pytohn3 -m venv .venv
```

aktifkan environment

```
source .venv/bin/activate
```

### Install Depedency


```
pip install -r requirements.txt

```

### Running Project

```
fastapi run main.py
```
