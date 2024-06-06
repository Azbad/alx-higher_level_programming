#!/usr/bin/node

/* how to pass arguments */
if (ProcessingInstruction.argv.length === 2) {
    console.log('No argument');
} else if (ProcessingInstruction.argv.length === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
