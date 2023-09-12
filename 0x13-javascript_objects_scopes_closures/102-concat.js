#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const contentFile1 = fs.readFileSync(file1, 'utf8');
const contentFile2 = fs.readFileSync(file2, 'utf8');
const ContentFile3 = `${contentFile1}${contentFile2}`;
fs.writeFileSync(file3, ContentFile3);
