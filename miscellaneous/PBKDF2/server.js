// IMPORTS
const express = require('express');
const spawn = require('child_process').spawnSync;


// APP
const app = express();
app.get('/', (req, res) => {
    if (!req.query.password || typeof req.query.password !== 'string') {
        return res.send('No password provided! Try /?password=yourpasswordhere');
    }

    console.log('Password: ' + req.query.password);

    if (req.query.password === 'isnt-byuctf-one-of-your-most-favorite-ctfs-even-though-this-is-only-our-second-year-3HF4z') {
        return res.send('Psssssssh like I\'m just gonna let you use the password I provided? Nice try :)')
    }
    
    // this is NOT a web challenge, it's misc on purpose
    var output = spawn('7z', ['e','flag.zip', '-o/tmp', '-p'+req.query.password]).stdout.toString();

    if (output.includes('Everything is Ok')) {
        var flag = spawn('cat', ['/tmp/flag.txt']).stdout;
        spawn('rm', ['/tmp/flag.txt']); // remove flag
        res.set('Content-Type', 'text/plain');
        return res.send(flag);
    }
    else {
        spawn('rm', ['/tmp/flag.txt']); // remove empty file
        return res.send('Incorrect password');
    }
});


// SERVER
app.listen(8080, () => {
    console.log(`Running on http://0.0.0.0:8080`);
});