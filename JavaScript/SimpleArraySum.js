process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function simpleArraySum(n, ar) {
    // Complete this function
    // create a placeholder of total
    var totalValue = 0;
    // n will be the # of items in the array
    // loop through the array of n
    for (i = 0; i < n; i++) {
    // get the sum of each element by adding each
      totalValue += ar[i];
    }
    // return the placeholder
    return totalValue;
}

function main() {
    var n = parseInt(readLine());
    ar = readLine().split(' ');
    ar = ar.map(Number);
    var result = simpleArraySum(n, ar);
    process.stdout.write("" + result + "\n");

}
