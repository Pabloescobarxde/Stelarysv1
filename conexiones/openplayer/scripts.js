const mineflayer = require('mineflayer');
const { WebhookClient } = require('discord.js');
const chalk = require('chalk');
const axios = require('axios');

if (process.argv.length !== 7) {
    console.log('Uso: node script.js [Nick] [ip/dominio] [puerto] [version] [webhook]');
    process.exit(1);
}

const [,, nick, host, port, version, webhookUrl] = process.argv;
const webhook = new WebhookClient({ url: webhookUrl });

const bot = mineflayer.createBot({
    host: host,
    port: parseInt(port),
    username: nick,
    version: version
});

let previousPlayers = new Set();
let hasScanned = false;

async function checkPremium(username) {
    try {
        const response = await axios.get(`https://api.mojang.com/users/profiles/minecraft/${username}`);
        return response.status === 200 ? response.data : null;
    } catch (error) {
        return null;
    }
}

function formatUUID(uuid) {
    if (!uuid || uuid.length !== 32) return uuid;
    return `${uuid.slice(0, 8)}-${uuid.slice(8, 12)}-${uuid.slice(12, 16)}-${uuid.slice(16, 20)}-${uuid.slice(20)}`;
}

async function getPlayerInfo() {
    const players = [];
    for (const name of Object.keys(bot.players)) {
        if (!name) continue;

        const premiumData = await checkPremium(name);
        players.push({
            name,
            uuid: formatUUID(premiumData ? premiumData.id : bot.players[name].uuid),
            isPremium: !!premiumData
        });
    }
    return players;
}

function formatConsoleOutput(players) {
    const borderColor = chalk.magenta.bold;
    const headerColor = chalk.magenta.bold;
    const indexColor = chalk.green;
    const nameColor = chalk.white;
    const uuidColor = chalk.green;

    const border = borderColor('╭' + '─'.repeat(72) + '╮');
    const bottomBorder = borderColor('╰' + '─'.repeat(72) + '╯');
    const header = borderColor('│') + 
                  headerColor(' Astralix '.padStart(41).padEnd(72)) +
                  borderColor('│');
    const separator = borderColor('├' + '─'.repeat(72) + '┤');

    let output = '\n' + border + '\n' + header + '\n' + separator + '\n';

    const columnHeader = borderColor('│') +
                        headerColor(' ID │      NOMBRE       │                UUID                  │ PREMIUM') +
                        borderColor('│');
    output += columnHeader + '\n' + separator + '\n';
    players.forEach((player, index) => {
        const premiumStatus = player.isPremium ? chalk.green('Premium') : chalk.red('Cracked');
        const line = borderColor('│') +
                     `${indexColor(String(index + 1).padStart(2, '0'))} ${borderColor(' │')}  ` +
                     `${nameColor(player.name.padEnd(16))}${borderColor(' │')} ` +
                     `${uuidColor(player.uuid.padEnd(18))}${borderColor(' │')} ` +
                     `${premiumStatus}` +
                     borderColor('│');
        output += line + '\n';
    });  
    output += separator + '\n';
    const statsLine = borderColor('│') +
                     chalk.white(` Total de jugadores: ${chalk.white(players.length)}`) +
                     ' '.repeat(42) +
                     borderColor('       │');
    output += statsLine + '\n' + bottomBorder;
    return output;
}

async function sendUpdate(players) {
    const playerCount = players.length;
    const premiumPlayers = players.filter(player => player.isPremium).length;
    const crackedPlayers = playerCount - premiumPlayers;

    const embed = {
        color: 0x9B4DE3,
        title: '📊 Connect',
        fields: [
            {
                name: '📈 Stats',
                value: `👥 Players: ${playerCount}\n💎 Premium: ${premiumPlayers}\n🎮 No Premium: ${crackedPlayers}`,
                inline: false
            },
            {
                name: 'Jugadores Conectados:',
                value: players.slice(0, 5).map((player, index) => {
                    return `${index + 1}. ${player.name} \n╰ UUID: ${player.uuid}\n╰ Premium: ${player.isPremium ? '`✅`' : '`❌`'}`;
                }).join('\n\n'),
                inline: false
            }
        ],
        footer: {
            text: 'Astralix',
        },
        timestamp: new Date()
    };

    try {
        await webhook.send({
            embeds: [embed],
            username: 'astralix'
        });
    } catch (error) {
        console.error('Error al enviar webhook:', error);
    }
}

async function checkPlayerChanges() {
    if (hasScanned) return;
    
    const currentPlayers = await getPlayerInfo();
    console.log(formatConsoleOutput(currentPlayers));
    await sendUpdate(currentPlayers);
    hasScanned = true;
    
    setTimeout(() => {
        process.exit(0);
    }, 2000);
}

async function authenticate() {
    try {
        await new Promise(resolve => setTimeout(resolve, 2000));
        bot.chat('/register password123 password123');
        await new Promise(resolve => setTimeout(resolve, 1000));
        bot.chat('/login password123');
        await new Promise(resolve => setTimeout(resolve, 1000));
    } catch (error) {
        console.error('Error en la autenticación:', error);
        process.exit(1);
    }
}

bot.on('spawn', async () => {
    console.log('Bot conectado al servidor');
    await authenticate();
    checkPlayerChanges();
});

bot.on('error', (err) => {
    console.error('Error del bot:', err);
    process.exit(1);
});

bot.on('kicked', (reason) => {
    console.log('Bot kickeado del servidor:', reason);
    process.exit(1);
});
