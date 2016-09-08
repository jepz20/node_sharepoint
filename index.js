var SP = require('./sharepoint.js');
var prettyjson = require('prettyjson');
var util = require("util");
var fs = require('fs');

var client = new SP.RestService('https://laureatena.sharepoint.com/sites/psid-ueld/');

client.signin(
	'User', 'Password' /*change for real user and password*/,
	(err, data) =>  {

		client.list('CourseInventory').get((err, courses) => {
			fs.writeFile(`jsons/courses.json`, JSON.stringify(courses))
		})

		client.list('ModuleInventory').get((err, modules) => {
			modules.results.forEach((module, index) => {
				uri = module.Course.__deferred.uri
				courses_uri = uri.slice(uri.indexOf('.svc/') + 5)
				client.list(courses_uri).get((err2, cour) => {
					module.CoursesDetail = cour.results
					fs.writeFile(`jsons/modules.json`, JSON.stringify(modules))
				})
			})
		});

		client.list('UnitInventory').get((err, units) => {
			fs.writeFile(`jsons/units.json`, JSON.stringify(units))
		});

		client.list('ActivityInventory').get((err, activities) => {
			fs.writeFile(`jsons/activities.json`, JSON.stringify(activities))
		});

		client.list('ResourcesInventory').get((err, resources) => {
			fs.writeFile(`jsons/resources.json`, JSON.stringify(resources))
		});
		// client.list('CourseInventory(1)/Attachments').get((err, data) => {
		// 	fs.writeFile("ci2.json", JSON.stringify(data))
		// })
	}
);


