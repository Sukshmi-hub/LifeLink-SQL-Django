# Database & Admin Module – LifeLink

## Overview
This module contains the database design and admin-related documentation
for the LifeLink project. The implementation is design-focused and aligns
with the project SRS and SDS.

## Technologies Considered
- MongoDB: Used for structured and persistent application data
- Firebase Firestore: Used for real-time alerts and communication

## MongoDB Design
The MongoDB schema design includes the following collections:
- Users
- Donors
- Hospitals
- Patients
- Requests
- Transactions
- TributeWall

These schemas are defined in `mongo_schemas.py` using Python-style
annotations for clarity and documentation purposes.

## Firebase Design
Firebase Firestore is used to handle real-time features such as:
- Emergency red alerts
- Live chat between donors and hospitals
- Real-time request status updates

The Firebase structure is documented in `firebase_structure.md`.

## Demo Data
Sample JSON data is provided in the `demo_data` folder to demonstrate
how MongoDB and Firebase documents are structured.

## Admin Handling
Admin-level operations such as verification of hospitals and donors,
request monitoring, and transaction oversight are handled conceptually
through controlled access and validation workflows.

## Contributor
**Member 3 – Database & Admin**
