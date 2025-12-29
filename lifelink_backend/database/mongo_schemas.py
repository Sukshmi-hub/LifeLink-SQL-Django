"""
MongoDB Schema Design for LifeLink
---------------------------------
Design-only schema definitions.
No database connection is implemented.

Member 3: Database + Admin
"""

# =========================
# User Collection
# =========================
class User:
    user_id: str
    name: str
    role: str          # admin / donor / patient / hospital / ngo
    phone: str
    email: str
    verified: bool
    created_at: str


# =========================
# Donor Collection
# =========================
class Donor:
    donor_id: str
    user_id: str
    donation_type: str     # blood / organ
    blood_group: str
    organ_type: str        # nullable
    consent_document: str
    availability: str
    verified: bool


# =========================
# Hospital Collection
# =========================
class Hospital:
    hospital_id: str
    user_id: str
    hospital_name: str
    location: str
    contact_number: str
    verified: bool


# =========================
# Patient Collection
# =========================
class Patient:
    patient_id: str
    user_id: str
    hospital_id: str
    age: int
    blood_group: str
    organ_needed: str


# =========================
# Request Collection
# =========================
class Request:
    request_id: str
    request_type: str      # blood / organ
    patient_id: str
    hospital_id: str
    urgency_level: str
    status: str            # open / matched / completed
    created_at: str


# =========================
# Transaction Collection
# =========================
class Transaction:
    transaction_id: str
    patient_id: str
    amount: float
    payment_type: str      # donation / micro-loan
    status: str
    created_at: str


# =========================
# Tribute Wall Collection
# =========================
class TributeWall:
    tribute_id: str
    donor_id: str
    story: str
    created_at: str
