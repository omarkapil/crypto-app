const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');
const processBtn = document.getElementById('process-btn');
const statusMessage = document.getElementById('status-message');

let currentMethod = '';
const API_BASE_URL = '/api/process/'; // مسار API في Flask

// دالة فتح النافذة المنبثقة
function openModal(method) {
    currentMethod = method;
    modalTitle.textContent = method + ' المعالجة باستخدام';
    inputText.value = '';
    outputText.value = '';
    statusMessage.textContent = '';
    statusMessage.className = 'status-message';
    modal.style.display = 'block';
}

// دالة إغلاق النافذة المنبثقة
function closeModal() {
    modal.style.display = 'none';
}

// استدعاء الـAPI عند الضغط على زر "تنفيذ العملية"
processBtn.onclick = async () => {
    const textToProcess = inputText.value;

    if (!textToProcess) {
        alert('الرجاء إدخال النص أولاً.');
        return;
    }
    
    // تفعيل حالة التحميل
    statusMessage.textContent = 'جاري التنفيذ...';
    statusMessage.className = 'status-message loading';
    processBtn.disabled = true;

    // اسم نقطة النهاية (استبدال المسافات بشرطات وتحويل للحروف الصغيرة)
    const methodName = currentMethod.toLowerCase().replace(/\s+/g, '-');
    const endpoint = API_BASE_URL + encodeURIComponent(methodName);
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: textToProcess })
        });

        const data = await response.json();

        if (response.ok) {
            // نجاح العملية
            outputText.value = data.output;
            statusMessage.textContent = `${currentMethod} تم التشفير/الهاش بنجاح!`;
            statusMessage.className = 'status-message success';
        } else {
            // فشل العملية (سواء خطأ في C++ أو خطأ في Backend)
            const errorMessage = data.error || 'حدث خطأ غير معروف في الخادم.';
            outputText.value = '';
            statusMessage.textContent = `خطأ: ${errorMessage}`;
            statusMessage.className = 'status-message error';
        }

    } catch (error) {
        // فشل اتصال الشبكة
        outputText.value = '';
        statusMessage.textContent = `خطأ في الاتصال: تأكد من أن الخادم يعمل. (${error.message})`;
        statusMessage.className = 'status-message error';
    } finally {
        processBtn.disabled = false;
    }
};

// إغلاق الـModal عند الضغط خارجها
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}