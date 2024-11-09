import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_questions.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store the questions and answers

cursor.execute('''
CREATE TABLE IF NOT EXISTS DS3841 (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

ds3850questions = [
    ("What is the output of the following code? print('Hello' + ' World')", "Hello World", "HelloWorld", "Error", "None", "A"),
    ("Which of the following is used to define a function in Python?", "function", "def", "method", "define", "B"),
    ("What keyword is used to create a loop in Python?", "repeat", "while", "loop", "foreach", "B"),
    ("Which of the following data types is immutable?", "list", "dict", "set", "tuple", "D"),
    ("How do you start a comment in Python?", "#", "//", "/*", "--", "A"),
    ("What will be the output of the following code? print(bool(''))", "True", "False", "None", "Error", "B"),
    ("Which of the following is the correct way to create a dictionary?", "dict = []", "dict = {}", "dict = ()", "dict = ''", "B"),
    ("What function is used to read input from the user?", "input()", "read()", "scan()", "get()", "A"),
    ("What does the range() function do?", "Creates a list of numbers", "Creates a tuple of numbers", "Generates a sequence of numbers", "None of the above", "C"),
    ("Which operator is used to check if two values are equal?", "==", "=", "equals", "===", "A")
]

ds3860questions = [
    ("In MySQL, which SQL statement is used to retrieve data from a database?", 
     "SELECT", "GET", "RETRIEVE", "FETCH", "A"),
    
    ("What does ERD stand for in database design?", 
     "Entity Relationship Diagram", "Entity Record Diagram", "Entity Relation Design", "Entity Relationship Data", "A"),
    
    ("Which of the following is a primary goal of normalization?", 
     "To increase redundancy", "To improve data retrieval speed", "To minimize data redundancy", "To increase table size", "C"),
    
    ("What is the purpose of a primary key in a database table?", 
     "To link two tables", "To uniquely identify each record", "To store foreign keys", "To organize data alphabetically", "B"),
    
    ("In an ERD, what does a rectangle represent?", 
     "An entity", "A relationship", "An attribute", "A foreign key", "A"),
    
    ("Which SQL keyword is used to sort query results?", 
     "SORT", "ORDER BY", "GROUP BY", "ARRANGE", "B"),
    
    ("What is the purpose of the 'JOIN' clause in SQL?", 
     "To select data from multiple tables", 
     "To create a new table", 
     "To delete records from a table", 
     "To update records", "A"),
    
    ("In an ERD, what symbol represents a one-to-many relationship?", 
     "A line with a crow's foot", "A dashed line", "A double line", "An arrow", "A"),
    
    ("In SQL, which keyword is used to remove a table?", 
     "DELETE", "DROP", "REMOVE", "TRUNCATE", "B"),
    
    ("In SQL, which statement is used to create a new table?", 
     "INSERT TABLE", "NEW TABLE", "CREATE TABLE", "ADD TABLE", "C"),
]

ds4210questions = [
    ("Which chart type is best for showing the relationship between two numerical variables in Tableau?", 
     "Bar Chart", "Scatter Plot", "Pie Chart", "Line Chart", "B"),
    
    ("What is the purpose of a 'Dashboard' in Tableau?", 
     "To create calculated fields", "To visualize a single chart", "To combine multiple sheets and views", "To import data sources", "C"),
    
    ("Which of the following is not an aggregate function in Tableau?", 
     "SUM", "COUNT", "GROUP", "AVG", "C"),
    
    ("What feature in Tableau enables the user to quickly swap between different views on the dashboard?", 
     "Filter", "Parameter", "Calculated Field", "Set", "B"),
    
    ("In Tableau, which feature allows you to group multiple values into a single category?", 
     "Hierarchy", "Group", "Filter", "Set", "B"),
    
    ("Which chart type is best for showing the percentage distribution of a categorical variable?", 
     "Bar Chart", "Pie Chart", "Scatter Plot", "Heat Map", "B"),
    
    ("In Tableau, what is the 'Pages' shelf used for?", 
     "Creating calculated fields", "Animating data changes over time", "Applying filters", "Grouping data", "B"),
    
    ("What is a 'Story' in Tableau?", 
     "A collection of dashboards and sheets that tells a data narrative", 
     "A single worksheet", 
     "An extension to import new data sources", 
     "A data extraction method", "A"),
    
    ("Which Tableau file type is a standalone file that contains data and all dependencies for sharing?", 
     ".tde", ".twb", ".twbx", ".tbm", "C"),
    
    ("Which Tableau function allows you to show data changes over a continuous range, such as time?", 
     "Trend Analysis", "Forecasting", "Pages Shelf", "Parameter", "C")
]

ds4220questions = [
    ("Which function in R is used to calculate the mean of a numeric vector?", 
     "sum()", "mean()", "avg()", "average()", "B"),
    
    ("What is the purpose of the 'lm()' function in R?", 
     "To calculate the mean", "To perform a t-test", "To fit a linear model", "To calculate the median", "C"),
    
    ("Which R function would you use to create a histogram?", 
     "histogram()", "barplot()", "hist()", "plot_hist()", "C"),
    
    ("What function in R provides the structure of an object, such as the data type and length?", 
     "summary()", "structure()", "str()", "typeof()", "C"),
    
    ("In R, what does the 'head()' function do?", 
     "Calculates the mean", "Displays the first few rows of a data frame", "Shows summary statistics", "Deletes the first row", "B"),
    
    ("What is the output of the R code 'seq(1, 10, by = 2)'?", 
     "A sequence of numbers from 1 to 10 with step size of 2", 
     "A sequence from 1 to 5", 
     "A random sequence", 
     "A sequence of 2s from 1 to 10", "A"),
    
    ("Which function in R would you use to perform a t-test?", 
     "t.test()", "ttest()", "t_test()", "tt()", "A"),
    
    ("Which command in R would you use to read a CSV file into a data frame?", 
     "import_csv()", "read.csv()", "csv_read()", "load_csv()", "B"),

    ("What is the purpose of the 'mutate()' function in the dplyr package?", 
     "To modify a data frame by adding or transforming variables", 
     "To delete rows", 
     "To summarize data", 
     "To merge data frames", "A"),

    ("What does the function 'install.packages()' do in R?", 
     "Loads a package into the session", 
     "Installs a package from CRAN", 
     "Updates a package", 
     "Lists all available packages", "B"),
]

questions = [    
    ("Which component is NOT part of an Information System?", 
     "Hardware", 
     "Software", 
     "Users", 
     "Construction", "D"),
    
    ("What is business intelligence (BI) primarily used for?", 
     "To support real-time decision-making by analyzing data", 
     "To handle customer service requests", 
     "To increase employee productivity", 
     "To manage payroll processes", "A"),
    
    ("Which of the following best describes 'cloud computing'?", 
     "A physical data center owned by a single company", 
     "Using local servers for data processing", 
     "The delivery of computing services over the internet", 
     "A process to speed up network connections", "C"),
    
    ("What is 'data mining'?", 
     "The process of storing large datasets in a database", 
     "The process of analyzing large datasets to find patterns", 
     "The process of cleaning raw data", 
     "The process of transmitting data securely", "B"),
    
    ("In an information system, what is the primary function of a database?", 
     "To store and organize data", 
     "To process payments", 
     "To manage human resources", 
     "To design business models", "A"),
    
    ("What is an advantage of using cloud-based MIS solutions?", 
     "Lower data security", 
     "High upfront costs", 
     "Increased accessibility and scalability", 
     "Limited data storage", "C"),
    
    ("What does the acronym 'SaaS' stand for?", 
     "Software as a Solution", 
     "Software as a Service", 
     "Software and Analytics Services", 
     "System Analysis Software", "B"),
    
    ("In MIS, what is 'data warehousing'?", 
     "A method of storing transaction data for a short time", 
     "A technology for storing and analyzing large amounts of historical data", 
     "A technology that replaces traditional databases", 
     "A way to manage customer data only", "B"),
    
    ("Which of the following is a potential risk of using information systems?", 
     "Improved data management", 
     "Enhanced communication", 
     "Data breaches and loss of privacy", 
     "Increased productivity", "C"),
    
    ("Which of the following is a characteristic of structured data?", 
     "It has no defined format or organization", 
     "It is organized in a fixed format like rows and columns", 
     "It includes images and videos", 
     "It cannot be stored in a database", "B")
]

# Insert questions into the database
cursor.executemany('''
INSERT INTO DS3841 (question, option_a, option_b, option_c, option_d, answer)
VALUES (?, ?, ?, ?, ?, ?)
''', questions)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and questions inserted successfully.")
