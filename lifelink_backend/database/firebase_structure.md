# Firebase Firestore Structure – LifeLink

## Purpose of Firebase
Firebase Firestore is used in LifeLink for real-time operations where
instant updates are critical, such as emergency alerts and chat.

The main backend database remains MongoDB, while Firebase handles
real-time communication.

---

## 1. Red Alert Collection

### Collection Name: alerts

Stores emergency blood or organ requests.

Fields:
- alert_id (string)
- request_type (blood / organ)
- blood_group / organ_type
- hospital_id
- urgency_level
- message
- timestamp
- status (active / resolved)

Usage:
- Instantly notify nearby donors
- Push emergency alerts in real time

---

## 2. Live Chat Collection

### Collection Name: chats

Stores messages between donors, hospitals, and patients.

Fields:
- chat_id
- sender_id
- receiver_id
- message
- timestamp
- read_status

Usage:
- Enables real-time communication
- Improves response speed during emergencies

---

## 3. Live Request Status

### Collection Name: live_requests

Tracks the real-time status of donation requests.

Fields:
- request_id
- current_status
- last_updated

Usage:
- Allows hospitals and donors to see live updates
- Syncs with MongoDB request records

---

## Summary
Firebase Firestore is integrated to handle real-time features such as
alerts, chat, and live request updates, ensuring faster response and
better coordination in critical situations.
