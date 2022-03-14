

// RUN FROM COMMAND LINE --> node index.js
// cntl+L --> clear consol


// MODIFIED FROM 
    // https://www.youtube.com/watch?v=W6NZfCO5SIk
    // https://www.w3schools.com/js/js_loop_for.asp

// DECLARE VARIABLES 
// use meaningful names, no space/hypens, use camel case,
// case sensitive, can't be reserved JS keywords 

 
//------------------- 
//DATA TYPES 
//-------------------

// PRIMITIVE TYPES
// string,number,boolean, unidentified, null

// OLD WAY
var MyVar1="test1";

//dynamic types
// text=typeof MyVar1
console.log(typeof MyVar1);
MyVar1=4
console.log(typeof MyVar1);

// RECOMMENDED  (vars )
let my_var2="test2";

// statement (action)
console.log("Hello world --> ",MyVar1,my_var2);

//CONTSANTS  (CANT CHANGE, WILL THROW ERROR)
const my_cnst=4.0;
console.log("my_cnst",my_cnst);
// my_cnst=5.

//ARRAY-1
let userColors = ['red','green']
console.log(userColors)
console.log(userColors[0])
userColors[2]='blue'  //add values to end 
console.log(userColors)




//FUNCTINOS
function myFunction(a, b) 
{
    // Jargon
    // a=parameter of function
    // a=3 --> 3 is an argument of function

    // scope of a and b is only inside function

  console.log(a,b);

  return a * b;             // Function returns the product of a and b
}

let x = myFunction(4, 3);   // Function is called, return value will end up in x
console.log(x);



//ARRAY-2
var my_array=[];
my_array[0]=10;
my_array[1]=20;
my_array[2]=30;
console.log(my_array)
console.log("length =",my_array.length)




//OBJECT (similar to a python dictionary)
let person = {
    name : "james"
}

//ADD NEW ATTRIBUTE 
person['age']=10

console.log(person)

// // OVERWRITE ATTRIBUTE
person.name="jack"

let selection='name'
console.log("name-1:",person.name)
console.log("name-2:",person[selection])
console.log("name-3:",person['name'])


//------------------- 
//LOOPS
//-------------------

//FOR LOOP EXAMPLE-1
var my_array=[];
my_array[0]='X';
my_array[1]='Y';
my_array[2]='Z';

for (let i = 0; i < my_array.length; i++) 
{
  console.log(i,my_array[i])
}

// for/in - loops through the properties of an object
for (const j in my_array) 
{
  console.log("j : ",j,my_array[j]);
}

// FOR/OF - LOOPS THROUGH THE VALUES OF AN ITERABLE OBJECT
for (var j of my_array) 
{
  console.log("j = ",j);
}

//FOR LOOP EXAMPLE-2
for (let i = 0; i < 5; i++) 
{
  text = "The number is " + i ;
  console.log(text)

}

//FOR IN LOOP EXAMPLE-1
const object = { a: 1, b: 2, c: 3 };

for (const property in object) 
{
  console.log(`${property}: ${object[property]}`);
}


// WHILE LOOP
let i=1
while ( i < 10) {
  console.log("The number is " , i)
  i++;
}

 // DO WHILE LOOP: 
 // VARIANT OF THE WHILE LOOP. THIS LOOP WILL 
 // EXECUTE THE CODE BLOCK ONCE, BEFORE CHECKING IF THE CONDITION 
 // IS TRUE, THEN IT WILL REPEAT THE LOOP AS LONG AS THE CONDITION IS TRUE.

i=1
do {
  text = "NUMBER= " + i;
  console.log(text)
  i++;
}
while (i < 10);









// function myFunc(theObject) {
//   theObject.make = 'Toyota';
// }

// var mycar = {make: 'Honda', model: 'Accord', year: 1998};
// var x, y;

// x = mycar.make; // x gets the value "Honda"

// myFunc(mycar);
// y = mycar.make; // y gets the value "Toyota"
//                 // (the make property was changed by the function)





