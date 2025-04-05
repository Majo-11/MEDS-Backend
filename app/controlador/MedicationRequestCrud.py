# app/controlador/MedicationRequestCrud.py

from pymongo import MongoClient
from bson import ObjectId
import os

client = MongoClient(os.getenv("MONGO_URL", "mongodb://localhost:27017"))
db = client["fhir"]
collection = db["medication_request"]

def WriteMedicationRequest(data: dict):
    try:
        result = collection.insert_one(data)
        return "success", str(result.inserted_id)
    except Exception as e:
        return str(e), None

def GetMedicationRequestById(req_id: str):
    try:
        med_req = collection.find_one({"_id": ObjectId(req_id)})
        if not med_req:
            return "notFound", None
        med_req["_id"] = str(med_req["_id"])
        return "success", med_req
    except Exception as e:
        return str(e), None
