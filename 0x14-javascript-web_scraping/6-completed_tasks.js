#!/usr/bin/node
// prrinting task done by each user in an api

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const tasksData = JSON.parse(body);

      if (tasksData.length > 0) {
        const completedTasks = tasksData.filter(task => task.completed);

        const completedTasksByUser = {};
        completedTasks.forEach(task => {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        });

	    console.log(JSON.stringify(completedTasksByUser, null, 2));
      }
    }
  });
