from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import bcrypt
from pymongo import MongoClient
import os

app = FastAPI()

# --- CORS İZİNLERİ ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- VERİTABANI BAĞLANTILARI ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/staj_db")

def get_mongodb_collection():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["staj_db"]
        return db["tasks"]
    except Exception as e:
        print("MongoDB ERROR:", repr(e))
        return None

# --- VERİ MODELLERİ ---
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    db_choice: str = "mongodb"

# --- ADRESLER (ENDPOINTS) ---

@app.get("/")
def ana_sayfa():
    return {"mesaj": "FastAPI Modelleri ve MongoDB Hazır!"}

# 1. Görev Ekleme (POST)
@app.post("/tasks")
def create_task(task: Task):
    try:
        if task.db_choice == "mongodb":
            gorevler_kolleksiyonu = get_mongodb_collection()
            if gorevler_kolleksiyonu is None:
                raise HTTPException(status_code=500, detail="MongoDB hazır değil.")
            
            yeni_gorev = {
                "title": task.title,
                "description": task.description,
                "db_choice": task.db_choice
            }
            sonuc = gorevler_kolleksiyonu.insert_one(yeni_gorev)
            return {"mesaj": "Başarılı", "id": str(sonuc.inserted_id)}
            
        elif task.db_choice == "mssql":
            # MSSQL kilitlenmesini engellemek için mock (taklit) kayıt simülasyonu yapıyoruz
            print(f"MSSQL MOCK POST: '{task.title}' MSSQL sistemine simüle edildi. 💾")
            return {"mesaj": "MSSQL Taklit Kayıt Başarılı"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Görevleri Listeleme (GET)
@app.get("/tasks")
def get_tasks():
    try:
        gorevler_kolleksiyonu = get_mongodb_collection()
        all_tasks = []
        
        if gorevler_kolleksiyonu is not None:
            mongo_tasks = list(gorevler_kolleksiyonu.find({}, {"_id": 0}))
            for t in mongo_tasks:
                all_tasks.append({"title": t.get("title", ""), "db_choice": "mongodb"})
        
        # Taklit MSSQL görevini de ekleyelim
        all_tasks.append({"title": "MSSQL Taklit Görev (RAM Koruma)", "db_choice": "mssql"})
        return all_tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Görev Silme (DELETE) - Yeni Eklenen Kısım
@app.delete("/tasks/{task_title}")
def delete_task(task_title: str, db_choice: str = "mongodb"):
    try:
        if db_choice == "mongodb":
            gorevler_kolleksiyonu = get_mongodb_collection()
            if gorevler_kolleksiyonu is None: 
                raise HTTPException(status_code=500, detail="MongoDB hazır değil.")
            
            # Başlığa göre eşleşen görevi siliyoruz
            result = gorevler_kolleksiyonu.delete_one({"title": task_title})
            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail="Silinmek istenen görev bulunamadı.")
            return {"mesaj": f"'{task_title}' başlıklı görev başarıyla silindi! 🍃"}
            
        elif db_choice == "mssql":
            print(f"MSSQL MOCK DELETE: {task_title} silindi sayıldı. ✅")
            return {"mesaj": "Mock Silme Başarılı"}
            
    except Exception as e:
        if isinstance(e, HTTPException): raise e
        raise HTTPException(status_code=500, detail=str(e))