![image](https://github.com/user-attachments/assets/f2167ffa-b892-4ec8-b763-ce2667afa6e0)# Modul-1
## 1. API publik dengan endpoint /health
Penggunaan python untuk membuat Flask-based API untuk menampilkan nama, nrp, status, timestamp, uptime 
![image](https://github.com/user-attachments/assets/d6337285-aeb8-486f-9539-a0a997d5ead9)

## 2. Deployment API ke VPS (Railway)
<b>Saya melakukan deployment ke VPS secara manual untuk pertama kali<b>
1. Masuk ke laman https://railway.com/dashboard
   ![image](https://github.com/user-attachments/assets/e6d182ab-351b-410e-863a-4a60456fac79)

2. Klik + New pada kanan atas lalu klik Deploy from GitHub Repo
   ![image](https://github.com/user-attachments/assets/2f067eb0-9490-40f1-8e9a-a5f679d72cba)

3. Klik pada repo yang ingin digunakan
   Pada kasus ini saya menggunakan repo Modul-1
   ![image](https://github.com/user-attachments/assets/a2ceac0e-45ce-4eae-9d4d-74fabf93334c)
   
5. Rename project
   Saya melakukan rename project dengan menggantinya melalui project settings yang ada di kanan atas. Saya rename menjadi ci-cd-implementation
   ![image](https://github.com/user-attachments/assets/d8db9845-63ca-41a7-9798-b70e1e059168)

6. Tunggu hingga deployment selesai
   Deployment akan dilakukan railway secara otomatis. Apabila sudah selesai buatkan domain agar bisa diakses secara publik. Jangan lupa tambahkan endpoint /health. <br>Ini link milik saya http://modul-1-production.up.railway.app/health
   ![image](https://github.com/user-attachments/assets/8420368f-f583-4b07-b017-a07bfebb1bbe)

## 3. CI/CD dengan GitHub Actions
File untuk GitHub Actions terletak pada .github/workflows/
Dengan nama main.yml

Di dalamnya terdapat kode seperti berikut:
```
 deploy:
    name: Deploy to Railway
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Install Railway CLI
        run: npm install -g @railway/cli

      - name: Deploy with Railway
        run: railway up --service Modul-1
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```
Potongan kode di atas digunakan untuk mendeploy tiap kali ada perubahan di dalam repository ini.
