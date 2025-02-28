const mineflayer = require('mineflayer');
const fs = require('fs');
const moment = require('moment');
const readline = require('readline');

const GRAY = '\x1b[37m';
const RED = '\x1b[31m';
const GREEN = '\x1b[32m';
const WHITE = '\x1b[97m';

const args = process.argv.slice(2);
if (args.length < 4) {
    console.log('Uso: node Bot.js (nick) (ip) (puerto) (version)');
    process.exit(1);
}

const [nick, ip, puerto, version] = args;

const logDir = 'pass_nick';
if (!fs.existsSync(logDir)) {
    console.log(`❌ La carpeta ${logDir} no existe. ¡Créala antes de ejecutar el bot!`);
    process.exit(1);
}

const passFile = `${logDir}/${ip}.json`;

const playersJoined = new Set();

function registrarJugador(player) {
    const timestamp = moment().format('YYYY-MM-DD HH:mm:ss');
    const logEntry = {
        username: player.username,
        ip: ip,
        timestamp: timestamp
    };

    let data = [];
    if (fs.existsSync(passFile)) {
        try {
            data = JSON.parse(fs.readFileSync(passFile, 'utf8'));
        } catch (error) {
            console.log('⚠️ Error al leer el archivo JSON, reiniciando el archivo.');
            data = [];
        }
    }

    if (data.some(entry => entry.username === player.username)) {
        return;
    }

    data.push(logEntry);

    fs.writeFileSync(passFile, JSON.stringify(data, null, 2), 'utf8');

    console.log('');
    console.log(`${GRAY}[${RED}#${GRAY}]${GRAY} ${WHITE}${player.username} ${GRAY}-${GREEN} ${ip} ${GRAY}-${WHITE} ${timestamp}${GRAY}`);
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function showHelp() {
    console.log('');
    console.log(`${GRAY}[${RED}#${GRAY}] .help - Muestra este mensaje de ayuda`);
    console.log(`${GRAY}[${RED}#${GRAY}] .kick - El bot se desconecta`);
    console.log(`${GRAY}[${RED}#${GRAY}] .restart - El bot se desconecta y luego vuelve a entrar`);
    console.log(`${GRAY}[${RED}#${GRAY}] .pass - Muestra todos los jugadores que han entrado`);
    console.log(`${GRAY}[${RED}#${GRAY}] .clear - Limpia la consola`);
}

function kickBot() {
    console.log('🔴 El bot se desconectará ahora...');
    bot.end();
}

function restartBot() {
    console.log('🔄 El bot se desconectará y volverá a entrar...');
    bot.end();
}

function showPass() {
    if (fs.existsSync(passFile)) {
        const logContent = JSON.parse(fs.readFileSync(passFile, 'utf8'));
        console.log('Jugadores que han entrado:');
        logContent.forEach(entry => {
            console.log(`${entry.username} - ${entry.timestamp}`);
        });
    } else {
        console.log('No hay registros aún.');
    }
}

function clearConsole() {
    console.clear();
    console.log('Consola limpia!');
}

function reconnectBot() {
    console.log('🔄 Reconectando bot...');
    setTimeout(() => {
        require('child_process').spawn('node', process.argv, { stdio: 'inherit' });
    }, 5000);
}

rl.on('line', (input) => {
    const command = input.trim();
    if (command === '.help') {
        showHelp();
    } else if (command === '.kick') {
        kickBot();
    } else if (command === '.restart') {
        restartBot();
    } else if (command === '.pass') {
        showPass();
    } else if (command === '.clear') {
        clearConsole();
    } else {
        bot.chat(command);
    }
});

const bot = mineflayer.createBot({
    host: ip,
    port: parseInt(puerto),
    username: nick,
    version: version
});

bot.on('message', (message) => {
    if (message.toString().includes("Ignoring block entities")) {
        return;
    }

    console.log(message.toString());
});

bot.on('playerJoined', (player) => {
    if (!playersJoined.has(player.username)) {
        playersJoined.add(player.username);
        registrarJugador(player);
    }
});

bot.on('playerLeft', (player) => {
    if (playersJoined.has(player.username)) {
        playersJoined.delete(player.username);
    }
});

bot.on('login', () => {
    console.log(`✅ Bot conectado como ${nick} en ${ip}:${puerto}`);
});

bot.on('chat', (username, message) => {
    if (username === nick) return;
    console.log(`<${username}> ${message}`);
});

bot.on('end', () => {
    console.log('🔌 Bot desconectado.');
    reconnectBot();
});

bot.on('error', (err) => console.log(`❌ Error: ${err.message}`));
