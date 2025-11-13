// Wait for DOM to be ready
let modal, modalTitle, inputText, outputText, processBtn, statusMessage, modalContent;
let currentMethod = '';
const API_BASE_URL = '/api/process/'; // مسار API في Flask

// Make functions globally accessible for HTML onclick
window.openModal = function(method) {
    if (!modal || !modalContent) {
        // Elements not loaded yet, wait a bit
        setTimeout(() => window.openModal(method), 100);
        return;
    }
    
    currentMethod = method;
    if (modalTitle) modalTitle.textContent = method + ' working ';
    if (inputText) inputText.value = '';
    if (outputText) outputText.value = '';
    if (statusMessage) {
        statusMessage.textContent = '';
        statusMessage.className = 'status-message';
    }
    
    // Add smooth animation
    modal.style.display = 'block';
    modal.style.opacity = '0';
    modalContent.style.transform = 'scale(0.8) translateY(-50px)';
    modalContent.style.opacity = '0';
    
    // Animate in
    requestAnimationFrame(() => {
        modal.style.transition = 'opacity 0.3s ease-out';
        modal.style.opacity = '1';
        modalContent.style.transition = 'all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        modalContent.style.transform = 'scale(1) translateY(0)';
        modalContent.style.opacity = '1';
    });
    
    // Focus input after animation
    setTimeout(() => {
        if (inputText) inputText.focus();
    }, 400);
};

window.closeModal = function() {
    if (!modal || !modalContent) return;
    
    modalContent.style.transition = 'all 0.3s ease-in';
    modalContent.style.transform = 'scale(0.8) translateY(-50px)';
    modalContent.style.opacity = '0';
    modal.style.transition = 'opacity 0.3s ease-in';
    modal.style.opacity = '0';
    
    setTimeout(() => {
        modal.style.display = 'none';
    }, 300);
};

document.addEventListener('DOMContentLoaded', function() {
    modal = document.getElementById('modal');
    modalTitle = document.getElementById('modal-title');
    inputText = document.getElementById('input-text');
    outputText = document.getElementById('output-text');
    processBtn = document.getElementById('process-btn');
    statusMessage = document.getElementById('status-message');
    modalContent = document.querySelector('.modal-content');
    
    // Initialize other features
    initializeFeatures();
});

// Add ripple effect to buttons
function createRipple(event, button) {
    const ripple = document.createElement('span');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');
    
    button.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

// Add ripple effect CSS dynamically
const style = document.createElement('style');
style.textContent = `
    .method-btn, #process-btn {
        position: relative;
        overflow: hidden;
    }
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Initialize all features
function initializeFeatures() {
    // Add ripple to all method buttons
    const methodButtons = document.querySelectorAll('.method-btn');
    methodButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            createRipple(e, this);
        });
        
        // Add hover effect
        button.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        });
    });
    
    // Set up process button click handler
    processBtn.addEventListener('click', function(e) {
        if (!this.disabled) {
            createRipple(e, this);
            handleProcess();
        }
    });
    
    // Add stagger animation to buttons
    const buttons = document.querySelectorAll('.method-btn');
    buttons.forEach((btn, index) => {
        btn.style.animationDelay = `${index * 0.1}s`;
        btn.setAttribute('data-index', index);
    });
    
    // Add touch gesture support for mobile
    let touchStartY = 0;
    let touchEndY = 0;
    
    if (modalContent) {
        modalContent.addEventListener('touchstart', function(e) {
            touchStartY = e.changedTouches[0].screenY;
        });
        
        modalContent.addEventListener('touchend', function(e) {
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        });
    }
    
    function handleSwipe() {
        const swipeThreshold = 50;
        const swipeDistance = touchStartY - touchEndY;
        
        // Swipe down to close (on mobile)
        if (swipeDistance < -swipeThreshold && window.innerWidth < 768) {
            closeModal();
        }
    }
    
    // Add keyboard navigation for textareas
    if (inputText) {
        inputText.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                processBtn.click();
            }
        });
    }
}


// استدعاء الـAPI عند الضغط على زر "تنفيذ العملية"
async function handleProcess() {
    if (!inputText || !processBtn || !statusMessage || !outputText) return;
    
    const textToProcess = inputText.value;

    if (!textToProcess) {
        alert('الرجاء إدخال النص أولاً.');
        return;
    }
    
    // Add pulsing effect
    processBtn.style.animation = 'scaleBounce 1s ease infinite';
    
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
            // Scroll to result
            setTimeout(scrollToResult, 100);
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
        // Remove pulsing after processing
        processBtn.style.animation = '';
    }
}


// إغلاق الـModal عند الضغط خارجها
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && modal.style.display === 'block') {
        closeModal();
    }
});

// Add smooth scroll to output when result appears
function scrollToResult() {
    const resultArea = document.getElementById('result-area');
    if (resultArea) {
        resultArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

