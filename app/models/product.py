from pydantic import BaseModel, Field            # Basisklasse für Pydantic-Modelle
from typing import Optional                 # Für optionale Felder

class ProductCreate(BaseModel):             # Modell für Erstellen
    name: str                               # Pflichtfeld: Name des Produkts
    price: float = Field(..., ge=0, description="Preis muss ≥ 0 sein")
    description: Optional[str] = None

class ProductUpdate(BaseModel):             # Modell für Update (alle Felder optional)
    name: Optional[str] = None              # Optional: Name (wenn aktualisiert)
    price: Optional[float] = None           # Optional: Preis (wenn aktualisiert)
    description: Optional[str] = None

class Product(ProductCreate):               # Modell für Rückgabe – inkl. ID
    id: str                                 # ID als String (z. B. MongoDB _id)

    