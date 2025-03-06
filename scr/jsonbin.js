const JSONBIN_API_URL = 'https://api.jsonbin.io/v3/b';
const X_MASTER_KEY = '$2a$10$je6p73nh/fBxNl4uthJQ4OEWss4ePbdu4hoyq.QejgaSIIuUyw7Ia';
const X_ACCESS_KEY = '$2a$10$lDiIBwW/oSWbuxbNXHK1zOGCo4pzKQdFb7auAlfVimp7yQhD2kfGi';
const COLLECTION_ID = '67c8e9aae41b4d34e4a17c63';

async function saveToJsonBin(data) {
    try {
        const response = await fetch(JSONBIN_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Master-Key': X_MASTER_KEY,
                'X-Access-Key': X_ACCESS_KEY,
                'X-Collection-Id': COLLECTION_ID
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        return result.metadata.id;
    } catch (error) {
        console.error('Erro ao salvar no JSONBin:', error);
        throw error;
    }
}

async function getFromJsonBin(recordId) {
    try {
        const response = await fetch(`${JSONBIN_API_URL}/${recordId}`, {
            headers: {
                'X-Master-Key': X_MASTER_KEY,
                'X-Access-Key': X_ACCESS_KEY
            }
        });

        const result = await response.json();
        return result.record;
    } catch (error) {
        console.error('Erro ao recuperar do JSONBin:', error);
        throw error;
    }
}