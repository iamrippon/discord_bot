const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
  console.log('Bot is online!');
});

const token = 'MTEzMTYxNTcwMDAyNTM1MjMwMg.G0VV1V.2jh8Bthjhaqs51dPWYGsPSrFV1vZF31G7HrSRw';
client.login(token);

