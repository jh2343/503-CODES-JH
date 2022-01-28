

#SPECIFY EXAMPLE TYPE TO RUN
# example="function"
# example="for-loop"
# example="double-for-loop"
example="while-loop"
# example="ls"

# example="data-types"
# example="vectors"
# example="matrices"
# example="dataframes"
# example="lists"
# example="factors"


#-------------------------------
if (example=="function") 
{
	print(c("EXAMPLE:",example))
	new.function <- function(a) 
	{
      b <- a^3+sin(a^2)+exp(-(a-10)/2.0)
      print(b)
	}
	new.function(4) #CALL FUNCTION
}
#-------------------------------


#-------------------------------
if (example=="for-loop") 
{
	print(c("EXAMPLE:",example))
	N <- 10
	for(i in 1:N)
	{
	  b <- i^2
	  print(c("i=",i,b))
	}
}
#-------------------------------


#-------------------------------
if (example=="double-for-loop") 
{
	print(c("EXAMPLE:",example))
	N <- 10
	for(i in 1:N)
	{
		for(j in 1:N)
		{
			b <- i*j
			print(c("i,j=",i,j,"b=i*j:",b))
	   }
	}
}
#-------------------------------


#-------------------------------
if (example=="while-loop") 
{
	print(c("EXAMPLE:",example))
	i <- 1
	while (i <= 10) 
	{
		print(i)
		i = i+1
	}
}
#-------------------------------


#-------------------------------
#RETURN A VECTOR OF CHARACTER STRINGS GIVING THE NAMES OF 
#THE OBJECTS IN THE SPECIFIED ENVIRONMENT
#name=environment (default=current)
#NOTE: ls() and objects() are identical 
if (example=="ls") 
{
	print(c("EXAMPLE:",example))
	i <- 1; a <- 5
	print(ls())
}
#-------------------------------


#-------------------------------
#BASIC DATA TYPES
#-------------------------------
#https://swcarpentry.github.io/r-novice-inflammation/13-supp-data-structures/

# class() - what kind of object is it (high-level)?
# typeof() - what is the object’s data type (low-level)?
# length() - how long is it? What about two dimensional objects?
# attributes() - does it have any metadata?

if (example=="data-types") 
{

	print(c("EXAMPLE:",example))

	#FUNCTION TO GET INFO ABOUT DATATYPES
	report <- function(x) 
	{
		print("-----------------")
		print(x)
		print(c("class=",class(x)))
		print(c("typeof=",typeof(x)))
		print(c("length=",length(x)))
		print(c("is.atomic=",is.atomic(x)))
		print(c("list=",is.list(x)))
		print(c("vector=",is.vector(x)))
		print(c("matrix=",is.matrix(x)))

		if(is.matrix(x))
		{
		print(c("shape=",dim(x)))		#similar to .shape in numpy 
		}

		#VERY USEFUL FUNCTION TO SUMMARIZE INFO ABOUT OBJECT
		print("str=")
		print(str(x))
		print("-----------------")
	}

	#VARIOUS DATA TYPES
	x="test"; 						 			report(x)
	x=FALSE;  						 			report(x)
	x=3.14;   						 			report(x)
	x = as.integer(x);	       			report(x)

	#VECTORS
	x <-c(10,15,20,25,30,35.);  			report(x)
	x <-c("one","two","three"); 			report(x)

	#MATRIX
	x <- matrix(1:20, nrow=5,ncol=4);   report(x)
	
	#DATA FRAME
	d <- c(10,20,30,40)
	e <- c("red", "white", "red", NA)
	f <- c(TRUE,TRUE,TRUE,FALSE)
	x <- data.frame(d,e,f);					report(x)
}


# ----------
# VECTORS
# ----------
#https://www.statmethods.net/input/datatypes.html

if (example=="vectors") 
{

	print(c("EXAMPLE:",example))


	x <- c(10,15,20,25,30,35.) # numeric vector
	str(x)

	# #ACCESS ENTRIES #START A 1
	print("MANIPULATE VECTOR")
	print(x[1])
	print(x[length(x)]) 
	print(is.na(x[length(x)]))
	print(is.na(x[length(x)+3]))
	print(x[1:3])
	print(x[1:length(x)])
	print(x[c(2,4)]) 		# 2nd and 4th elements of vector
	print(x[-2]) 			# delete entry use x <- to overwrite
	print(x[-1:-3]) 		# delete entry 
	print(x <- x[-2]) 	# use x <- to overwrite
	str(x)

	print("VECTOR OPERATIONS")
	print(c("x",x))
	print(c("x-2x",x-2*x))
	print(c("x*x*x",x*x*x))
	print(c("x/x",x/x))
	print(c("x^2",x^2))
	print(c("sin(x)",sin(x)))

	x <- c("one","two","three") # character vector
	str(x)

	x <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) #logical vector
	str(x)
	print(as.numeric(x))  #typecast
}


#----------
#MATRICS
#----------
#ALL COLUMNS IN A MATRIX MUST HAVE THE SAME 
#MODE(NUMERIC, CHARACTER, ETC.) AND THE SAME LENGTH. 

#THE GENERAL FORMAT IS

# MYMATRIX <- MATRIX(VECTOR, NROW=R, NCOL=C, BYROW=FALSE,
#    DIMNAMES=LIST(CHAR_VECTOR_ROWNAMES, CHAR_VECTOR_COLNAMES))

if (example=="matrices") 
{

	print(c("EXAMPLE:",example))
	
	# # generates 5 x 4 numeric matrix
	x <- matrix(1:20, nrow=5,ncol=4)
	str(x); #quit()

	print("MANIPULATE MATRIX")

	# #ACCESS ENTRIES #START A 1
	print(x[,4]) # 4th column of matrix
	print(x[3,]) # 3rd row of matrix
	print(x[1:4,1:3]) # rows 2,3,4 of columns 1,2,3
	print(x[1:4,2]); 
	print(x[length(x)])
	print(x[7])		#unwrapps (opposite of np) (i.e. down rows first)
	print(x[-2]) #delete entry use x <- to overwrite
	print(x[-1:-3]) #delete entry 
	print(x[,-1]) #delete first column 
	print(x[-1,]) #delete first row 

}	


#----------
#ARRAYS --> SIMILAR TO MATRICES BUT CAN HAVE MORE THAN TWO DIMENSIONS (LIKE NP ARRAYS)
# 	-BASICALLY TENSORS
#----------


#----------
#DATA FRAMES 
#----------
# A DATA FRAME IS MORE GENERAL THAN A MATRIX, IN THAT DIFFERENT COLUMNS
# CAN HAVE DIFFERENT MODES (NUMERIC, CHARACTER, FACTOR, ETC.)


if (example=="dataframes") 
{

	print(c("EXAMPLE:",example))

	d <- c(10,20,30,40)
	e <- c("red", "white", "red", NA)
	f <- c(TRUE,TRUE,TRUE,FALSE)
	x <- data.frame(d,e,f)
	str(x)

	#ACCESSING
	print(x[1:2]) # columns of data frame
	names(x) <- c("ID","Color","Passed") # variable names
	print("-----")
	x[c("ID","Passed")] # columns ID and Age from data frame
	x <- x$Color # variable x1 in the data frame
	str(x)
}

#----------
# LISTS
#----------
# AN ORDERED COLLECTION OF OBJECTS (COMPONENTS).  
# ALLOWS YOU TO GATHER A VARIETY OF (POSSIBLY UNRELATED) OBJECTS 
# UNDER ONE NAME.

if (example=="lists") 
{

	print(c("EXAMPLE:",example))

	# example of a list with 4 components -
	# a string, a numeric vector, a matrix, and a scaler
	x <- list(name="Fred", c(1,2,3), age=5.3)
	str(x)

	print(x[[1]]) 			# 1st component of the list
	print(x[["name"]]) 	# component named mynumbers in list

	print(x[[2]]) 			# 2nd component of the list
	print(x[1:3])
	# print(x)
}

#----------
# FACTORS 
#----------
# --> TELL R That a variable is nominal by making it a factor. The factor 
#stores the nominal values as a vector of integers in the range [ 1... k ] 
#(where k is the number of unique values in the nominal variable), and an
# internal vector of character strings (the original values) mapped to these
# integers.
if (example=="factors") 
{

	print(c("EXAMPLE:",example))


	gender <- c(rep("male",20), rep("female", 30))
	str(gender)
	gender <- factor(gender)
	# stores gender as 20 1s and 30 2s and associates
	# 1=female, 2=male internally (alphabetically)
	# R now treats gender as a nominal variable
	summary(gender)

} 


#---------------------------
#XTRA
#---------------------------
# is.atomic(logical())
# is.atomic(integer())
# is.atomic(numeric())
# is.atomic(complex())
# is.atomic(character())
# is.atomic(raw())
# is.atomic(NULL)
# is.atomic(list())        # is.vector==TRUE
# is.atomic(expression())  # is.vector==TRUE
# is.atomic(pairlist())    # potential "gotcha": pairlist() returns NULL
# is.atomic(pairlist(1))   # is.vector==FALSE

#----------- 
#Useful Functions
#----------- 

#https://www.statmethods.net/input/datatypes.html

# length(object) # number of elements or components
# str(object)    # structure of an object
# class(object)  # class or type of an object
# names(object)  # names

# c(object,object,...)       # combine objects into a vector
# cbind(object, object, ...) # combine objects as columns
# rbind(object, object, ...) # combine objects as rows

# object     # prints the object

# ls()       # list current objects
# rm(object) # delete an object from enviroment 

# newobject <- edit(object) # edit copy and save as newobject
# fix(object)               # edit in place


# #---------------------------
# #ASSIGNMENT OPERATORS 
# #---------------------------

# # The difference in assignment operators is clearer when you use them
# # to set an argument value in a function call. For example:

# median(x = 1:10)
# x   
# # ## Error: object 'x' not found
# # In this case, x is declared within the scope of the function, 
# #so it does not exist in the user workspace.

# median(x <- 1:10)
# x    
# # ## [1]  1  2  3  4  5  6  7  8  9 10
# # In this case, x is declared in the user workspace, so you can 
# #use it after the function call has been completed.

# quit()



