const readLine = require("readline");

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
});

directions = [];

function takeInput(param){
    return new Promise((resolve, reject) => {
        return rl.question(param, value => resolve(value), err => reject(err))
    });
}

       
takeInput('Enter direction: ')
.then((value) =>{ 
    directions = value.split(',');
    pos = [0, 0];
    positionChanged = false;
    for(let i in directions){
        switch(directions[i]){
            case 'n':
                pos[0] +=  1;
                break;
            case 's':
                pos[0] -=  1;
                break;
            case 'e':
                pos[1] +=  1;
                break;
            case 'w':
                pos[1] -=  1;
                break;
            default:
                console.log("Invalid direction entered");
        }
    }
    for (let i in pos){
        if(pos[i] != 0){
            positionChanged = true;
        }
    }

    if (positionChanged){
        console.log('Change in posistion..');
    } else {
        console.log('No change');
    }
})
        

