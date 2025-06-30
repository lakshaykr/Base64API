# ✅ Base64API - ToDo List

## 🧑‍💻 Authentication
- [ ] Implement Discord OAuth2 login
- [ ] On successful login:
  - [ ] Check if user exists in DB
  - [ ] If not, generate API key and save user
  - [ ] If yes, fetch existing API key

## 🔐 API Key Management
- [ ] Generate secure, random API key (hidden by default)
- [ ] Store user ID ↔ API key mapping in MongoDB
- [ ] Allow key regeneration with confirmation
- [ ] Provide copy-to-clipboard button

## 📊 Key Usage Tracking
- [ ] Store:
  - [ ] `last_used` timestamp
  - [ ] `use_count` increment on each request
- [ ] Middleware to validate and track key usage

## ⛔ Inactive Key Handling
- [ ] Run scheduled check (daily/weekly)
- [ ] Mark keys inactive or delete if `last_used > X days`

## 🌐 Web Dashboard
- [ ] Show hidden/generated API key
- [ ] Display:
  - [ ] Key status (active/inactive)
  - [ ] Last used timestamp
  - [ ] Total usage count
- [ ] Add “Regenerate Key” button
- [ ] Add “Copy Key” button

## 🧪 Preview Panel
- [ ] Add test input field (e.g., for raw text)
- [ ] Show API endpoint (copyable)
- [ ] Display example output after calling endpoint

