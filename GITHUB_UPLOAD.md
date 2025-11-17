# كيفية رفع التحديثات على GitHub

## الخطوات:

### 1. إضافة جميع الملفات
```bash
git add .
```

### 2. عمل Commit للتحديثات
```bash
git commit -m "Update: Add user guide, flowchart, and improved UI"
```

### 3. إضافة Remote Repository (إذا لم يكن موجود)
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```
**ملاحظة:** استبدل `YOUR_USERNAME` و `YOUR_REPO_NAME` بمعلومات repository الخاص بك

### 4. رفع التحديثات
```bash
git push -u origin master
```

أو إذا كنت تستخدم branch اسمه `main`:
```bash
git push -u origin main
```

---

## إذا كان Repository موجود بالفعل:

### 1. التحقق من Remote
```bash
git remote -v
```

### 2. إضافة الملفات
```bash
git add .
```

### 3. Commit
```bash
git commit -m "Update: Add user guide, flowchart, and improved UI"
```

### 4. رفع التحديثات
```bash
git push
```

---

## الأوامر الكاملة (نسخ ولصق):

```bash
cd "d:\the pero project\crypto-app-main"
git add .
git commit -m "Update: Add user guide, flowchart, improved UI with English interface"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin master
```

**تأكد من:**
- استبدال `YOUR_USERNAME` و `YOUR_REPO_NAME` بمعلوماتك
- إذا كان repository موجود بالفعل، استخدم `git push` فقط

