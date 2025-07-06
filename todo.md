# ✅ Base64API - ToDo List

## 🧑‍💻 Authentication
- [x] Implement Discord OAuth2 login
- [x] On successful login:
  - [x] Check if user exists in DB
  - [x] If not, generate API key and save user
  - [x] If yes, fetch existing API key

## 🔐 API Key Management
- [x] Generate secure, random API key
- [x] Store user ID ↔ API key mapping in MongoDB
- [x] Allow key regeneration
- [x] Provide copy-to-clipboard button

## 🌐 Web Dashboard
- [x] Show generated API key
- [x] Display:
  - [x] Key status (active/inactive)
- [x] Add “Regenerate Key” button
- [x] Add “Copy Key” button

## 🧪 Preview Panel
- [x] Add test input field (e.g., for raw text)
- [x] Show API endpoint (copyable)
- [x] Display example output after calling endpoint

