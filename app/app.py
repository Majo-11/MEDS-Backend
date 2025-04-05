from fastapi import FastAPI, HTTPException, Request
import uvicorn
from app.controlador.PatientCrud import GetPatientById,WritePatient,GetPatientByIdentifier
from fastapi.middleware.cors import CORSMiddleware
from app.controlador.MedicationRequestCrud import WriteMedicationRequest, GetMedicationRequestById


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solo este dominio
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)



@app.post("/medication-request", response_model=dict)
async def create_medication_request(request: Request):
    med_req = dict(await request.json())
    status, req_id = WriteMedicationRequest(med_req)
    if status == 'success':
        return {"_id": req_id}
    else:
        raise HTTPException(status_code=500, detail=f"Error: {status}")

@app.get("/medication-request/{req_id}", response_model=dict)
async def get_medication_request(req_id: str):
    status, data = GetMedicationRequestById(req_id)
    if status == 'success':
        return data
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="MedicationRequest not found")
    else:
        raise HTTPException(status_code=500, detail=f"Error: {status}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
