const mineflayer = require('mineflayer');

function nickRnd() {
    const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_';
    let result = '';
    for (let i = 0; i < 12; i++) {
        result += chars[Math.floor(Math.random() * chars.length)];
    }
    return result;
}

function createBot(host, port, version) {
    const username = nickRnd();
    const password = "discord.gg/astralix";

    const bot = mineflayer.createBot({
        host: host,
        port: port,
        username: username,
        version: version
    });

    bot.on('spawn', () => {
        setTimeout(() => {
            bot.chat(`/register ${password} ${password}`);
            setTimeout(() => {
                bot.chat(`/login ${password}`);
            }, 2000);
        }, 1000);
    });

    bot.on('error', (err) => {
        console.log(`Error con bot ${username}: ${err}`);
    });

    bot.on('kicked', (reason) => {
        console.log(`Bot ${username} fue expulsado: ${reason}`);
    });

    return bot;
}

function main() {
    const args = process.argv.slice(2);

    if (args.length !== 4) {
        console.log('Uso: node bot.js <numero_de_bots> <ip> <puerto> <version>');
        process.exit(1);
    }

    const [numBots, ip, port, version] = args;
    const bots = [];
    let spamIntervals = [];

    console.log(`Iniciando ${numBots} bots...`);

    for (let i = 0; i < numBots; i++) {
        setTimeout(() => {
            const bot = createBot(ip, parseInt(port), version);
            bots.push(bot);
        }, i * 5000);
    }

    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.on('line', (input) => {
        const commandArgs = input.trim().split(' ');

        if (commandArgs[0] === '.spam' && commandArgs.length === 3) {
            const message = commandArgs[1];
            const delay = parseInt(commandArgs[2]);

            if (isNaN(delay)) {
                console.log('El valor de delay no es un número válido.');
                return;
            }

            bots.forEach((bot) => {
                const interval = setInterval(() => {
                    bot.chat(message);
                }, delay);
                spamIntervals.push(interval);
            });
        }

        if (input === '.stop') {
            console.log('Deteniendo el spam de todos los bots');
            spamIntervals.forEach(clearInterval);
            spamIntervals = [];
        }

        if (commandArgs[0] === '.add' && commandArgs.length === 2) {
            const numToAdd = parseInt(commandArgs[1]);

            if (isNaN(numToAdd) || numToAdd <= 0) {
                console.log('El número de bots a agregar no es válido.');
                return;
            }

            console.log(`Agregando ${numToAdd} bots...`);

            for (let i = 0; i < numToAdd; i++) {
                setTimeout(() => {
                    const bot = createBot(ip, parseInt(port), version);
                    bots.push(bot);
                    console.log(`Bot agregado. Total de bots: ${bots.length}`);
                }, i * 5000);
            }
        }

        if (input === '.help') {
            console.log('Comandos disponibles:');
            console.log('[#] .spam <mensaje> <delay> - Hacer spam con el mensaje ingresado');
            console.log('[#] .stop - Detener el spam');
            console.log('[#] .add <numero> - Agregar más bots');
            console.log('[#] .bots - Ver todos los bots que has conectado');
            console.log('[#] .remove <nombre> <opcional> - Eliminar un bot por nombre, si no se especifica se eliminara uno aleatorio');
            console.log('[#] .message <nombre_bot> <mensaje> - Enviar un mensaje desde un bot específico');
            console.log('[#] .restart - Reinicia todo los bots');
            console.log('[#] .clear - Limpiar la consola');
            console.log('[#] .help - Mostrar este mensaje de ayuda');
        }

        if (input === '.bots') {
            if (bots.length === 0) {
                console.log('No has conectado bots.');
            } else {
                console.log('Tus bots conectados:');
                bots.forEach((bot, index) => {
                    console.log(`Bot ${index + 1}: ${bot.username}`);
                });
            }
        }

        if (commandArgs[0] === '.remove') {
            if (commandArgs.length === 1) {
                const botToRemove = bots.pop();
                console.log(`Bot ${botToRemove.username} eliminado`);
                botToRemove.quit();
            } else if (commandArgs.length === 2) {
                const botName = commandArgs[1];
                const botIndex = bots.findIndex(bot => bot.username === botName);
                if (botIndex !== -1) {
                    const removedBot = bots.splice(botIndex, 1)[0];
                    console.log(`Bot ${removedBot.username} eliminado`);
                    removedBot.quit();
                } else {
                    console.log('No se encontró un bot con ese nombre.');
                }
            }
        }

        if (input === '.restart') {
            console.log('Reiniciando bots...');
            bots.forEach(bot => {
                bot.quit();
            });
            bots.length = 0;
            setTimeout(() => {
                console.log('Reiniciando los bots...');
                for (let i = 0; i < numBots; i++) {
                    setTimeout(() => {
                        const bot = createBot(ip, parseInt(port), version);
                        bots.push(bot);
                    }, i * 5000);
                }
            }, 2000);
        }

        if (commandArgs[0] === '.message' && commandArgs.length >= 3) {
            const botName = commandArgs[1];
            const message = commandArgs.slice(2).join(' ');

            const bot = bots.find(b => b.username === botName);

            if (!bot) {
                console.log(`No se encontró un bot con el nombre ${botName}`);
                return;
            }

            console.log(`Enviando mensaje desde el bot ${bot.username}: "${message}"`);
            bot.chat(message);
        }

        if (input === '.clear') {
            console.clear();
            console.log('Consola limpiada.');
        }
    });
}

main();
