#!/usr/bin/node
const fs = require('fs');
const first_file = fs.readFileSync(process.argv[2], 'utf8');
const second_file = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], first_file + second_file);
