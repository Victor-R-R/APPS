const qrCodeDiv = document.getElementById('qr-code');
socket.on('qr_code', function(qrCode) {
    qrCodeDiv.innerHTML = 'Código QR detectado: ' + qrCode;
});

document.addEventListener('DOMContentLoaded', function() {
    socket.emit('qr_code');
});