var SP = require('./sharepoint.js');
var prettyjson = require('prettyjson');

var client = new SP.RestService('https://laureatena.sharepoint.com/sites/psid-ueld/');

client.signin(
	'email@laureate.net', 'password',
	(err, data) => client.list('ActivityInventory').get(console.log)
);
