# Data Wrangling and Baseline Visualization Assignment

## Introduction

Once upon a time, there was a bank offering services to its customers. The services included managing of accounts, offering loans, etc.

The bank wanted to improve its services but the bank managers had only vague idea of who was a good customer (whom to offer some additional services) and who was a bad customer (whom to watch carefully to minimize the bank loses). Fortunately, the bank stored data about its clients, the accounts (transactions within several months), the loans already granted, the credit cards issued. The bank managers hoped to improve their understanding of customers and seek specific actions to improve services, however, they failed.

Your job is to prepare and analyze this data and use it to help guide the operations of a new bank that the startup you just joined as a Data Scientst is going to open.

## The Data

The data for all of the bank's operations was contained in an application that used a relational database for data storage, and the data was exported from their system into separate `CSV` files. This is a snaphot dataset, meaning it shows the values that were current at the time of the dataset export. 

The data is contained in the `data.zip` file included in this repository. **You must unzip the file**, which will create a `data/` directory inside this repository as well, and this directory is ignored by git. 

There are eight files in the `data/` and below is a description of the contents of each file. You will practice reading in data, cleaning and rearranging the data, making the data tidy, and joining datasets for the purposes of creating a dataset that is ready to be visualized.

--

`accounts.csv` contains information about the bank's accounts.

| Field Name | Description |
|------------|-------------|
| `id`| Unique record identifier |
| `district_id` | Branch location |
| `date` | Date of account opening | 
| `statement_frequency` | The frequency that statements are generated for the account

--

`clients.csv` contains information about the bank's customers. A client (customer) can have several accounts.

| Field Name | Description |
|------------|-------------|
| `id`| Unique record identifier |
| `gender` | Client's gender |
| `birth_date` | Client's birthday | 
| `district_id` | Client's location|

--

`links.csv` contains information that links customers to accounts, and wether a customer is the owner or a user in a given account.

| Field Name | Description |
|------------|-------------|
| `id`| Unique record identifier |
| `client_id` | Client identifier |
| `account_id` | Account identifier | 
| `type` | Owner or User |

--

`transactions.csv` contains all of the bank's transactions.

| Field Name | Description |
|------------|-------------|
| `id`| Unique record identifier |
| `account_id` | Account identifier | 
| `date` | Transaction date |
| `type` | Debit or Credit |
| `amount` | Amount of transaction |
| `balance` | Account balance after the transaction is excuted
| `bank` | The two letter code of the other bank if the transaction is a bank transfer | `account` | The account number of the other bank if the transaction is a bank transfer |
| `method` | Method of transaction: can be bank transfer, cash, or credit card | 
| `category` | What the transaction was for |

--

`payment_orders.csv` contains information about orders for payments to other banks via bank transfers. A customer issues an order for payment and the bank executes the payment. These payments should also be reflected in the `transactions.csv` data as debits.

| Field Name | Description |
|------------|-------------|
| `id`| Unique record identifier |
| `account_id` | Account identifier | 
| `recipient_bank` | The two letter code of the bank where the payment is going |
| `recipient_account` | The account number of at the bank where the payment is going to |
| `amount` | Amount of transaction |
| `payment_reason` | What the transaction was for |

--

`cards.csv` contains information about credit cards issued to clients. Accounts can have more than one credit card.

| Field Name | Description |
|------------|-------------|
| `id`| Unique record identifier |
| `link_id` | Entry that maps a client to an account |
| `type` | Credit Card product name (Junior, Classic or Gold) | 
| `issue_date` | Date the credit card was issued |

--

`loans.csv` contains information about loans associated with accounts. Only one loan is allowed per account.

| Field Name | Description |
|------------|-------------|
| `id` | Unique record identifier |
| `date` | The date the loan was granted |
| `amount` | The amount of the loan |
| `payments` | The monthly payment of the loan |
| `24_A`, `12_B`, etc | These fields contain information about the term of the loan, in months, wether a loan is current or expired, and the payment status of the loan. _Expired_ means that the contract is completed, wether or not the loan was paid in full or not. _Current_ means that customers are currently making payments (or not). <br/> `A` stands for an expired loan that was paid in full<br/> `B` stands for an expired loan that was not paid in full (it was in default)<br/> `C` stands for a current loan where all payments are being made<br/> `D` stands for a current loan in default due to not all payments being made

--

`districts.csv` contains demographic information and characteristics about the districts where customers and branches are located. 

| Field Name | Description |
|------------|-------------|
| `id` | Uniquie district identifier |
| `name` | District name |
| `region` | Region name |
| `population` | Number of inhabitants |
| `num_cities` | Number of cities |
| `urban_ratio` | Ratio of urban population |
| `avg_salary` | Average salary |
| `entrepreneur_1000` | Number of entrepreneurs per 1,000 inhabitants |
| `municipality_info` | An array with the number of municipalities with the following attributes:<br/>* Population < 500<br/>* Population 500-1999<br/>* Population 2000-9999<br/>* Population >= 10000 | 
| `unemployment_rate` | An array with the unemployment rate for '95 and '96 respectively | 
| `commited_crimes` | An array with the number of commited crimes for '95 and '96 respectively | 


## Tasks

### Part 1: Data Wrangling

You need to perform the tasks below in **both** `R` and `Python`. For each task, you need to write two scripts an `.R` script and a `.py` script. **Jupyter notebooks (`.ipynb`) are not allowed.** Your scripts must follow these rules and must run on professor/TA machines without any modification:

- No hard coded paths, only relative paths
- Output files must be saved within the same directory
- There should be as many comments as possible

We recommend you use any of the `tidyverse` set of packages in `R` and `pandas` in `Python`.

1. Make the `loans.csv` data tidy. You must account for **all** the information contained in each record (row) and that should be in their own field. Remember, for a dataset to be considered tidy, it must meet the following criteria:
	* Each variable must have its own column
	* Each observation must have its own row
	* Each type of observational unit forms a table

	The scripts that perform this task are called `loans.R` and `loans.py`. The scripts will produce `CSV` files called `loans_r.csv` and `loans_py.csv`.

1. Make the `district.csv` data tidy. You must account for all the information contained in each record (row).

	The scripts that perform this task are called `district.R` and `district.py`. The scripts will produce `CSV` files called `district_r.csv` and `district_py.csv`.

1. Build an _analytical dataset_ by combining (joining) the data from the different tables as you see fit, which will be used for the purposes of exploratory data analysis, visualization and reporting. The unit of analysis is the _account_. This dataset must contain the following information for each _account_ using the following field names:
	- `account_id`: Account number
	- `district_name`: Name of the district where the account is
	- `open_date`: Date when account was opened
	- `statement_frequency`: The frequency that statements are generated for the account
	- `num_customers`: The total number of clients associated with the account (owner and users)
	- `credit_cards`: Number of credit cards for an account or zero if none
	- `loan`: T/F if the account has a loan
	- `loan_amount`: The amount of the loan if there is one, `NA` if none
	- `loan_payments`: The amount of the loan payment if there is one, `NA` if none
	- `loan_term`: The duration of loan in months, `NA` if none
	- `loan_status`: The status of the loan (current or expired), `NA` if none 
	- `loan_default`: T/F if the loan is in default, or `NA` if none
	- `max_withdrawal`: Maximum amount withdrawn for the account 
	- `min_withdrawal`: Minimum amount withdrawn for the account 
	- `cc_payments`: Count of credit payments for the account for all cards
	- `max_balance`: Maximum balance in the account
	- `min_balance`: Minimum balance in the account


	The scripts that perform this task are called `analytical.R` and `analytical.py`. The scripts will produce `CSV` files called `analytical_r.csv` and `analytical_py.csv`.

### Part 2: Baseline Data Visualization

1. Using the _analytical dataset_ created in Part 1 as your dataset, frame a question you would like to answer using a visualization. State your question clearly and state why you think it can be answered visually. 

	Provide the answer to the question in a **plain text** file called `visualization-question.txt`.

1. Write an `R` script called `hw1-viz.R` **or** a `Python` script called `hw1-viz.py` to build the visualization that you think will answer the question above using whichever package(s) you are familiar with. Give it your best shot. We want to see how you approach a visualization problem to set a baseline for you and then see how you progress throughout the course. Try to use any visualization and degisn best practice(s) you may be familiar with. The script must:

	* Read in the `analytical_r.csv` or `analytical_py.csv`
	* Create and format the approprate visualization
	* Export the visualization as a `.png` into a file called `base-visualization.png`

### Submitting the Assignment

Make sure you commit **only the files requested above**, and push your repository to GitHub!

The files to be committed and pushed to the repository for this assignment are:

* 12 files for Part 1: `loans.R`, `loans.py`, `loans_r.csv`, `loans_py.csv`,`district.R`, `district.py`, `district_r.csv`, `district_py.csv`, `analytical.R`, `analytical.py`, `analytical_r.csv`, `analytical_py.csv`.
* 3 files for Part 2: `visualization-question.txt`, `hw1-viz.R` or `hw1-viz.py`, and `base-visualization.png`


